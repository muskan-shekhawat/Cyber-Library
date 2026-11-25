import React from "react";
import { ALL_BOOKS } from "@/data/books";
import PhysicalBookshelf from "@/components/library/PhysicalBookshelf";

export default function LibraryPage() {
  return (
    <div className="w-full min-h-[calc(100vh-3.5rem)] flex flex-col justify-between overflow-x-hidden">
      <div className="w-full max-w-7xl mx-auto px-6 sm:px-10 pt-6 sm:pt-8 pb-2 text-center">
        <h1 className="text-[11px] sm:text-xs font-mono font-bold tracking-[0.28em] text-[#1C1C1C] uppercase">
          Curated Catalog
        </h1>
        <p className="text-[10px] tracking-[0.2em] text-[#77736E] uppercase mt-1 font-mono">
          Interactive Hardcover Bookshelf &nbsp;·&nbsp; 6 Subject Categories
        </p>
      </div>

      <div className="my-auto w-full">
        <PhysicalBookshelf books={ALL_BOOKS} />
      </div>

      <footer className="pb-4 text-center">
        <p className="text-[9px] font-mono tracking-[0.25em] text-[#77736E]/60 uppercase">
          Select any volume to inspect chapters and technical curriculum
        </p>
      </footer>
    </div>
  );
}
