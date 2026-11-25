"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { Search } from "lucide-react";
import SearchModal from "@/components/search/SearchModal";

export default function Navbar() {
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [isMac, setIsMac] = useState(true);
  const pathname = usePathname();

  useEffect(() => {
    setIsMac(navigator.platform.toUpperCase().indexOf("MAC") >= 0);

    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setIsSearchOpen((prev) => !prev);
      }
    };

    const handleScroll = () => setScrolled(window.scrollY > 12);

    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  const navLink = (href: string, label: string) => {
    const active =
      href === "/"
        ? pathname === "/"
        : href === "/library"
        ? pathname === "/" || pathname === "/library" || pathname?.startsWith("/books")
        : pathname?.startsWith(href);

    return (
      <Link
        href={href}
        className={`text-[11px] tracking-[0.18em] uppercase transition-all duration-200 ${
          active
            ? "text-[#222222] font-700"
            : "text-[#999999] hover:text-[#222222]"
        }`}
        style={{ fontWeight: active ? 700 : 500 }}
      >
        {label}
      </Link>
    );
  };

  return (
    <>
      <header
        className="sticky top-0 z-40 w-full transition-all duration-300"
        style={{
          background: scrolled ? "rgba(248,247,244,0.92)" : "#F8F7F4",
          borderBottom: "1px solid #E8E6E1",
          backdropFilter: scrolled ? "blur(12px)" : "none",
          WebkitBackdropFilter: scrolled ? "blur(12px)" : "none",
        }}
      >
        <div className="max-w-7xl mx-auto px-6 sm:px-10 lg:px-16 h-14 flex items-center justify-between">
          {/* Brand */}
          <Link
            href="/"
            className="flex items-center gap-2 group"
          >
            <span
              className="text-[13px] tracking-[0.22em] uppercase text-[#222222] group-hover:opacity-70 transition-opacity"
              style={{ fontWeight: 700 }}
            >
              NULL
            </span>
            <span className="text-[#D0CCCA] text-[13px] font-light">/</span>
            <span
              className="text-[13px] tracking-[0.22em] uppercase text-[#858585] group-hover:text-[#222222] transition-colors"
              style={{ fontWeight: 500 }}
            >
              LIBRARY
            </span>
          </Link>

          {/* Nav */}
          <nav className="flex items-center gap-6 sm:gap-8">
            {navLink("/library", "Library")}
            {navLink("/tools", "Tools")}
            {navLink("/about", "About")}

            <button
              type="button"
              onClick={() => setIsSearchOpen(true)}
              className="flex items-center gap-1.5 text-[#999999] hover:text-[#222222] transition-colors cursor-pointer"
              title="Search Library"
            >
              <Search className="w-3.5 h-3.5" />
              <span className="hidden sm:inline text-[10px] tracking-[0.1em] text-[#BBBBBB] font-medium">
                {isMac ? "⌘K" : "Ctrl+K"}
              </span>
            </button>
          </nav>
        </div>
      </header>

      <SearchModal isOpen={isSearchOpen} onClose={() => setIsSearchOpen(false)} />
    </>
  );
}
