"use client";

import React from "react";
import Image from "next/image";
import { Book } from "@/types";

interface BookCoverProps {
  book: Book;
  size?: "sm" | "md" | "lg";
  showOverlay?: boolean;
  priority?: boolean;
}

const DARK_COVERS = new Set([
  "advanced-networking",
  "kali-linux",
  "linux-administration",
  "penetration-testing",
  "python-cybersecurity",
  "bash-scripting",
  "cryptography",
  "malware-analysis",
  "soc-analyst",
]);

export default function BookCover({
  book,
  size = "md",
  showOverlay = true,
  priority = false,
}: BookCoverProps) {
  const isDarkCover = DARK_COVERS.has(book.slug);

  const sizeClasses = {
    sm: "w-[140px] h-[210px]",
    md: "w-[220px] sm:w-[250px] h-[330px] sm:h-[375px]",
    lg: "w-[280px] sm:w-[340px] h-[420px] sm:h-[510px]",
  }[size];

  const titleClasses = {
    sm: "text-[11px] leading-[1.2]",
    md: "text-[15px] sm:text-[17px] leading-[1.18]",
    lg: "text-[20px] sm:text-[22px] leading-[1.16]",
  }[size];

  const metaClasses = {
    sm: "text-[8px]",
    md: "text-[10px]",
    lg: "text-[11px]",
  }[size];

  return (
    <div
      className={`relative ${sizeClasses} select-none overflow-hidden rounded-[2px] transition-shadow duration-500 ease-out book-shadow group-hover:book-shadow-hover`}
      style={{
        aspectRatio: "2 / 3",
        transform: "translateZ(0)",
      }}
    >
      {/* Full-Bleed Editorial Artwork */}
      <Image
        src={book.coverImage}
        alt={book.title}
        fill
        sizes="(max-width: 640px) 220px, (max-width: 1024px) 280px, 360px"
        priority={priority}
        draggable={false}
        className="object-cover select-none pointer-events-none"
      />

      {/* Realistic Book Spine Hinge & Edge Depth */}
      <div className="absolute inset-y-0 left-0 w-3 z-10 pointer-events-none bg-gradient-to-r from-black/20 via-black/5 to-transparent" />
      <div className="absolute inset-y-0 left-[9px] w-[1px] z-10 pointer-events-none bg-white/15" />
      <div className="absolute inset-y-0 right-0 w-[1px] z-10 pointer-events-none bg-black/10" />

      {/* Clean Editorial Typography in Top Negative Space */}
      {showOverlay && (
        <div
          className={`relative z-20 w-full px-5 sm:px-6 pt-5 sm:pt-6 pointer-events-none ${
            isDarkCover ? "text-white" : "text-[#222222]"
          }`}
        >
          <div className="flex items-center justify-between mb-2">
            <span
              className={`${metaClasses} uppercase tracking-[0.16em] font-medium ${
                isDarkCover ? "text-white/70" : "text-[#858585]"
              }`}
            >
              {book.category}
            </span>
            <span
              className={`${metaClasses} tabular-nums tracking-[0.12em] font-medium ${
                isDarkCover ? "text-white/60" : "text-[#858585]"
              }`}
            >
              {book.volumeNumber.replace("VOL. ", "")}
            </span>
          </div>

          <h3
            className={`${titleClasses} font-semibold tracking-[-0.02em] line-clamp-3`}
          >
            {book.title}
          </h3>
        </div>
      )}
    </div>
  );
}
