"use client";

import React, { useState } from "react";
import { Book } from "@/types";
import { BOOK_STYLES } from "@/data/bookStyles";
import EditorialCoverArt from "./EditorialCoverArt";

interface BookFrontCover3DProps {
  book: Book;
  onOpen: () => void;
  priority?: boolean;
}

export default function BookFrontCover3D({
  book,
  onOpen,
  priority = true,
}: BookFrontCover3DProps) {
  const [isHovered, setIsHovered] = useState(false);

  const style = BOOK_STYLES[book.slug] || {
    height: 366,
    thickness: 44,
    coverWidth: 248,
    spineColor: "#1C1C1C",
    author: "Editorial",
  };

  return (
    <div
      onClick={onOpen}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      className="relative shrink-0 cursor-pointer select-none group transition-all duration-500 ease-[cubic-bezier(0.22,1,0.36,1)]"
      style={{
        width: `${style.coverWidth}px`,
        height: `${style.height}px`,
        transform: isHovered
          ? "translate3d(0, -8px, 24px) scale(1.025)"
          : "translate3d(0, 0, 10px)",
        transformStyle: "preserve-3d",
      }}
      title={`Open ${book.title}`}
    >
      {/* ── Top Page Block Edge (reveals top paper depth) ── */}
      <div
        className="absolute top-0 left-0 right-0 h-4 origin-bottom pointer-events-none"
        style={{
          transform: "rotateX(-90deg) translateY(-16px)",
          background: "linear-gradient(90deg, #D6D0C2 0%, #FAF7F0 30%, #E6E0D2 100%)",
          borderTop: `2px solid ${style.spineColor}`,
          boxShadow: "inset 0 1px 2px rgba(0,0,0,0.15)",
        }}
      />

      {/* ── Right Page Block Edge (reveals side paper thickness) ── */}
      <div
        className="absolute top-0 right-0 bottom-0 w-3 origin-left pointer-events-none"
        style={{
          transform: "rotateY(90deg) translateX(0px)",
          background: "repeating-linear-gradient(180deg, #E6E0D2 0px, #E6E0D2 2px, #FAF7F0 2px, #FAF7F0 4px)",
          borderRight: `1.5px solid ${style.spineColor}`,
          boxShadow: "inset -1px 0 2px rgba(0,0,0,0.15)",
        }}
      />

      {/* ── Main Hardcover Front Face ── */}
      <div
        className="relative w-full h-full rounded-[2px] overflow-hidden shadow-2xl transition-shadow duration-500"
        style={{
          boxShadow: isHovered
            ? "0 28px 56px -10px rgba(0,0,0,0.38), 0 12px 24px -6px rgba(0,0,0,0.22)"
            : "0 20px 40px -8px rgba(0,0,0,0.28), 0 8px 16px -4px rgba(0,0,0,0.15)",
        }}
      >
        <EditorialCoverArt book={book} priority={priority} />

        {/* Left Spine Joint Hinge Crease */}
        <div className="absolute inset-y-0 left-0 w-4 pointer-events-none bg-gradient-to-r from-black/40 via-black/10 to-transparent z-20" />
        <div className="absolute inset-y-0 left-[11px] w-[1px] pointer-events-none bg-white/20 z-20" />

        {/* ── Prominent Cobalt Blue Circular "OPEN" Button (matches Reference Image 2) ── */}
        <div className="absolute inset-0 z-30 flex items-center justify-center pointer-events-none">
          <div
            className={`w-14 h-14 rounded-full bg-[#2455FF] text-white flex items-center justify-center shadow-lg transition-all duration-300 ${
              isHovered
                ? "scale-110 shadow-2xl bg-[#1B42D6]"
                : "scale-100 shadow-md opacity-95"
            }`}
            style={{
              boxShadow: isHovered
                ? "0 12px 28px -4px rgba(36, 85, 255, 0.55), 0 4px 10px rgba(0,0,0,0.2)"
                : "0 8px 18px -4px rgba(36, 85, 255, 0.45)",
            }}
          >
            <span className="text-[11px] font-bold tracking-[0.16em] uppercase select-none">
              OPEN
            </span>
          </div>
        </div>
      </div>

      {/* ── Physical Contact Baseline Shadow ── */}
      <div
        className="absolute -bottom-3 left-1/2 -translate-x-1/2 h-4 pointer-events-none rounded-full transition-opacity duration-300"
        style={{
          width: `${style.coverWidth + 24}px`,
          background: "radial-gradient(ellipse at center, rgba(0,0,0,0.50) 0%, rgba(0,0,0,0.18) 55%, transparent 75%)",
          opacity: isHovered ? 0.95 : 0.75,
          filter: "blur(2.5px)",
        }}
      />
    </div>
  );
}
