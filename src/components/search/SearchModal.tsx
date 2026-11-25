"use client";

import React, { useState, useEffect, useRef } from "react";
import { useRouter } from "next/navigation";
import { Search, X, BookOpen, Wrench, FileText, ArrowRight } from "lucide-react";
import { ALL_BOOKS, searchBooksAndChapters } from "@/data/books";
import { ALL_TOOLS, searchTools } from "@/data/tools";

interface SearchModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function SearchModal({ isOpen, onClose }: SearchModalProps) {
  const [query, setQuery] = useState("");
  const [selectedIndex, setSelectedIndex] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);
  const router = useRouter();

  useEffect(() => {
    if (isOpen) {
      setTimeout(() => inputRef.current?.focus(), 40);
      setQuery("");
      setSelectedIndex(0);
    }
  }, [isOpen]);

  const bookResults = query.trim()
    ? searchBooksAndChapters(query).books.slice(0, 4)
    : ALL_BOOKS.slice(0, 3);
  const chapterResults = query.trim()
    ? searchBooksAndChapters(query).chapters.slice(0, 4)
    : [];
  const toolResults = query.trim()
    ? searchTools(query).slice(0, 4)
    : ALL_TOOLS.slice(0, 3);

  const items = [
    ...bookResults.map((b) => ({
      id: `book-${b.slug}`,
      type: "book" as const,
      title: b.title,
      subtitle: `${b.volumeNumber} · ${b.category}`,
      url: `/books/${b.slug}`,
    })),
    ...chapterResults.map((c) => ({
      id: `ch-${c.bookSlug}-${c.chapterSlug}`,
      type: "chapter" as const,
      title: `Ch. ${c.chapterNumber}: ${c.title}`,
      subtitle: c.bookTitle,
      url: `/books/${c.bookSlug}/${c.chapterSlug}`,
    })),
    ...toolResults.map((t) => ({
      id: `tool-${t.slug}`,
      type: "tool" as const,
      title: t.name,
      subtitle: t.category,
      url: `/tools/${t.slug}`,
    })),
  ];

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!isOpen) return;
      if (e.key === "Escape") {
        onClose();
      } else if (e.key === "ArrowDown") {
        e.preventDefault();
        setSelectedIndex((prev) => (prev + 1 < items.length ? prev + 1 : 0));
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        setSelectedIndex((prev) => (prev - 1 >= 0 ? prev - 1 : items.length - 1));
      } else if (e.key === "Enter" && items[selectedIndex]) {
        e.preventDefault();
        router.push(items[selectedIndex].url);
        onClose();
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, selectedIndex, items, router, onClose]);

  if (!isOpen) return null;

  return (
    <div
      className="fixed inset-0 z-50 flex items-start justify-center pt-16 sm:pt-24 px-4 bg-[#222222]/25"
      onClick={onClose}
    >
      <div
        className="w-full max-w-xl bg-white border border-[#E8E6E1] shadow-xl rounded-[2px] overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center px-4 py-3.5 border-b border-[#E8E6E1]">
          <Search className="w-4 h-4 text-[#858585] mr-3 shrink-0" />
          <input
            ref={inputRef}
            type="text"
            value={query}
            onChange={(e) => {
              setQuery(e.target.value);
              setSelectedIndex(0);
            }}
            placeholder="Search volumes, chapters, tools or concepts..."
            className="w-full bg-transparent text-[#222222] placeholder-[#858585] text-sm focus:outline-none"
          />
          <button
            type="button"
            onClick={onClose}
            className="text-[#858585] hover:text-[#222222] p-1 transition-colors cursor-pointer"
            aria-label="Close search"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        <div className="max-h-[55vh] overflow-y-auto divide-y divide-[#E8E6E1]/60 p-1.5">
          {items.length === 0 ? (
            <div className="py-10 text-center text-xs text-[#858585]">
              No matching volumes, chapters, or tools.
            </div>
          ) : (
            items.map((item, index) => {
              const isSelected = index === selectedIndex;
              return (
                <div
                  key={item.id}
                  onClick={() => {
                    router.push(item.url);
                    onClose();
                  }}
                  onMouseEnter={() => setSelectedIndex(index)}
                  className={`flex items-center justify-between px-3 py-2.5 cursor-pointer rounded-[2px] transition-colors text-xs ${
                    isSelected ? "bg-[#F8F7F4]" : "hover:bg-[#F8F7F4]/60"
                  }`}
                >
                  <div className="flex items-center min-w-0 mr-3">
                    <span className="mr-3 text-[#858585] shrink-0">
                      {item.type === "book" && <BookOpen className="w-3.5 h-3.5" />}
                      {item.type === "chapter" && <FileText className="w-3.5 h-3.5" />}
                      {item.type === "tool" && <Wrench className="w-3.5 h-3.5" />}
                    </span>
                    <div className="truncate">
                      <div className="font-medium text-[#222222] truncate">{item.title}</div>
                      <div className="text-[11px] text-[#858585] truncate">{item.subtitle}</div>
                    </div>
                  </div>
                  <ArrowRight
                    className={`w-3.5 h-3.5 shrink-0 transition-opacity ${
                      isSelected ? "opacity-100 text-[#222222]" : "opacity-0"
                    }`}
                  />
                </div>
              );
            })
          )}
        </div>

        <div className="px-4 py-2 bg-[#F8F7F4] border-t border-[#E8E6E1] flex items-center justify-between text-[10px] text-[#858585] tracking-wider uppercase">
          <span>↑↓ Navigate · ↵ Open · Esc Close</span>
          <span>Search</span>
        </div>
      </div>
    </div>
  );
}
