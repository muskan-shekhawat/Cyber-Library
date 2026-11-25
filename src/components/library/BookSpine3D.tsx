"use client";

import React, { useState } from "react";
import { Book } from "@/types";
import { BOOK_STYLES } from "@/data/bookStyles";

interface BookSpine3DProps {
  book: Book;
  onClick: () => void;
  priority?: boolean;
}

export default function BookSpine3D({ book, onClick }: BookSpine3DProps) {
  const [isHovered, setIsHovered] = useState(false);

  const style = BOOK_STYLES[book.slug] || {
    height: 360,
    thickness: 42,
    coverWidth: 244,
    spineColor: "#1C1C1C",
    spineGradient: "linear-gradient(180deg, #1C1C1C 0%, #2A2A2A 50%, #111111 100%)",
    foilColor: "#D4AF37",
    textColor: "#FFFFFF",
    author: "Editorial",
    rating: "4.8",
    badge: "VOL",
    theme: "charcoal",
  };

  // Truncate title if extremely long for vertical spine fit
  const displayTitle = book.title.length > 36 ? book.title.slice(0, 34) + "…" : book.title;

  return (
    <div
      onClick={onClick}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      className="relative shrink-0 cursor-pointer select-none group transition-transform duration-300 ease-[cubic-bezier(0.25,1,0.5,1)]"
      style={{
        width: `${style.thickness}px`,
        height: `${style.height}px`,
        transform: isHovered
          ? "translate3d(0, -10px, 18px) scale(1.02)"
          : "translate3d(0, 0, 0)",
        transformStyle: "preserve-3d",
      }}
      title={`${book.title} (Click to open)`}
    >
      {/* ── Top Page Block Edge (reveals book depth when looking slightly down) ── */}
      <div
        className="absolute top-0 left-0 right-0 h-4 origin-bottom pointer-events-none"
        style={{
          transform: "rotateX(-90deg) translateY(-16px)",
          background: "linear-gradient(90deg, #D4CEBE 0%, #F5F1E6 40%, #E8E2D5 100%)",
          borderTop: `1.5px solid ${style.spineColor}`,
          boxShadow: "inset 0 1px 2px rgba(0,0,0,0.15)",
        }}
      />

      {/* ── Realistic Book Spine Body ── */}
      <div
        className="relative w-full h-full rounded-[1px] overflow-hidden flex flex-col justify-between items-center py-4 px-1"
        style={{
          backgroundColor: style.spineColor,
          backgroundImage: style.spineGradient,
          boxShadow: isHovered
            ? "0 18px 30px -4px rgba(0,0,0,0.35), inset 1px 0 2px rgba(255,255,255,0.3), inset -1px 0 2px rgba(0,0,0,0.4)"
            : "0 6px 14px -2px rgba(0,0,0,0.22), inset 1px 0 1.5px rgba(255,255,255,0.2), inset -1px 0 1.5px rgba(0,0,0,0.35)",
        }}
      >
        {/* Cylindrical Spine Curvature Highlight Overlay */}
        <div className="absolute inset-0 pointer-events-none spine-lighting z-10" />

        {/* Top Foil Accents & Volume Number */}
        <div className="relative z-20 flex flex-col items-center w-full px-1">
          {/* Top double foil band */}
          <div className="w-full flex flex-col gap-[2px] mb-2">
            <div
              className="w-full h-[1.5px] opacity-75"
              style={{ backgroundColor: style.foilColor }}
            />
            <div
              className="w-full h-[0.75px] opacity-50"
              style={{ backgroundColor: style.foilColor }}
            />
          </div>

          <span
            className="text-[8px] font-mono font-bold tracking-[0.2em] uppercase opacity-90 text-center"
            style={{ color: style.foilColor }}
          >
            {book.volumeNumber.replace("VOL. ", "V.")}
          </span>
        </div>

        {/* ── Main Vertical Spine Title ── */}
        <div
          className="relative z-20 flex-1 flex items-center justify-center my-3 overflow-hidden"
          style={{
            writingMode: "vertical-rl",
            transform: "rotate(180deg)",
          }}
        >
          <span
            className="text-[11px] font-semibold tracking-[0.14em] uppercase whitespace-nowrap text-center select-none"
            style={{
              color: style.textColor,
              textShadow: "0 1px 2px rgba(0,0,0,0.35)",
              letterSpacing: "0.14em",
            }}
          >
            {displayTitle}
          </span>
        </div>

        {/* Bottom Publisher Mark & Foil Ribs */}
        <div className="relative z-20 flex flex-col items-center w-full px-1">
          <span
            className="text-[7px] font-mono tracking-[0.22em] uppercase opacity-80 mb-2 select-none"
            style={{ color: style.foilColor }}
          >
            NULL
          </span>

          {/* Bottom double foil band */}
          <div className="w-full flex flex-col gap-[2px]">
            <div
              className="w-full h-[0.75px] opacity-50"
              style={{ backgroundColor: style.foilColor }}
            />
            <div
              className="w-full h-[1.5px] opacity-75"
              style={{ backgroundColor: style.foilColor }}
            />
          </div>
        </div>
      </div>

      {/* ── Physical Contact Shadow on the Shelf Baseline ── */}
      <div
        className="absolute -bottom-2 left-1/2 -translate-x-1/2 h-3 pointer-events-none rounded-full transition-opacity duration-300"
        style={{
          width: `${style.thickness + 8}px`,
          background: "radial-gradient(ellipse at center, rgba(0,0,0,0.45) 0%, rgba(0,0,0,0.12) 60%, transparent 80%)",
          opacity: isHovered ? 0.9 : 0.65,
          filter: "blur(1.5px)",
        }}
      />
    </div>
  );
}
