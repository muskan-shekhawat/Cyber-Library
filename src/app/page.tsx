import React from "react";
import { ALL_BOOKS } from "@/data/books";
import PhysicalBookshelf from "@/components/library/PhysicalBookshelf";

export default function HomePage() {
  return (
    <div className="w-full min-h-[calc(100vh-3.5rem)] flex flex-col justify-between overflow-x-hidden bg-[#F7F6F2]">
      {/* ── Editorial Header (Matching "Design Shelf of Timeless Classics") ── */}
      <div className="w-full max-w-7xl mx-auto px-6 sm:px-10 lg:px-16 pt-8 sm:pt-10 pb-2">
        <div className="max-w-2xl">
          <p className="text-[10px] font-mono font-bold tracking-[0.28em] text-[#D95A2B] uppercase mb-2">
            NULL / LIBRARY ARCHIVE
          </p>
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-serif font-bold text-[#1C1C1C] tracking-tight leading-[1.08]">
            Cybersecurity Shelf<br />
            of Timeless<br />
            Classics
          </h1>
          <p className="text-xs sm:text-sm text-[#77736E] mt-3 leading-relaxed max-w-lg">
            A curated collection of 25 foundational textbooks, operational manuals, and security monographs that shaped digital defense history.
          </p>
        </div>
      </div>

      {/* ── 3D Floating Physical Shelf Stage ── */}
      <div className="my-auto w-full py-4 pb-8">
        <PhysicalBookshelf books={ALL_BOOKS} />
      </div>
    </div>
  );
}
