"use client";

import React from "react";
import Image from "next/image";
import { Book } from "@/types";
import { BOOK_STYLES } from "@/data/bookStyles";

interface EditorialCoverArtProps {
  book: Book;
  className?: string;
  priority?: boolean;
}

export default function EditorialCoverArt({ book, className = "", priority = false }: EditorialCoverArtProps) {
  const style = BOOK_STYLES[book.slug] || {
    spineColor: "#1C1C1C",
    textColor: "#FFFFFF",
    foilColor: "#D4AF37",
    author: "Cybersecurity Editorial Board",
    badge: "MONOGRAPH",
  };

  // If there is an existing cover image and it's not a broken placeholder, we can display it
  const hasImage = Boolean(book.coverImage);

  return (
    <div
      className={`relative w-full h-full overflow-hidden select-none ${className}`}
      style={{
        backgroundColor: style.spineColor,
      }}
    >
      {hasImage ? (
        <Image
          src={book.coverImage}
          alt={book.title}
          fill
          sizes="(max-width: 640px) 240px, (max-width: 1024px) 280px, 340px"
          priority={priority}
          draggable={false}
          className="object-cover select-none pointer-events-none"
        />
      ) : (
        /* Swiss Minimal / Technical Editorial Cover */
        <div className="absolute inset-0 p-6 flex flex-col justify-between text-white bg-gradient-to-br from-black/20 via-transparent to-black/40">
          <div>
            <div className="flex items-center justify-between text-[10px] tracking-[0.24em] uppercase font-mono opacity-70 mb-4">
              <span>{book.volumeNumber}</span>
              <span>{book.category}</span>
            </div>
            <h2 className="text-xl font-bold tracking-tight leading-snug">
              {book.title}
            </h2>
            <p className="text-xs opacity-75 mt-2 line-clamp-2">
              {book.subtitle}
            </p>
          </div>

          <div>
            <div className="w-12 h-[2px] bg-white/40 mb-4" />
            <p className="text-[11px] tracking-wider uppercase opacity-80 font-mono">
              {style.author}
            </p>
            <p className="text-[9px] tracking-[0.2em] uppercase opacity-50 font-mono mt-1">
              NULL / LIBRARY PRESS
            </p>
          </div>
        </div>
      )}

      {/* Realistic Hardcover Book Texture & Lighting Overlays */}
      <div className="absolute inset-y-0 left-0 w-4 pointer-events-none bg-gradient-to-r from-black/35 via-black/10 to-transparent z-10" />
      <div className="absolute inset-y-0 left-[11px] w-[1px] pointer-events-none bg-white/20 z-10" />
      <div className="absolute inset-y-0 right-0 w-2 pointer-events-none bg-gradient-to-l from-black/25 to-transparent z-10" />
      <div className="absolute inset-0 pointer-events-none border border-black/10 rounded-[1px] z-10" />
      <div className="absolute inset-0 pointer-events-none bg-gradient-to-tr from-white/[0.04] via-transparent to-black/[0.06] z-10" />
    </div>
  );
}
