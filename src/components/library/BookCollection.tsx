"use client";

import React, { useState } from "react";
import { BOOK_ROW_CATEGORIES } from "@/data/categories";
import { ALL_BOOKS } from "@/data/books";
import HorizontalScroller from "./HorizontalScroller";
import BookRow from "./BookRow";

export default function BookCollection({ initialView = "shelf" }: { initialView?: "shelf" | "rows" }) {
  const [activeFilter, setActiveFilter] = useState<string>("all");
  const [viewMode, setViewMode] = useState<"shelf" | "rows">(initialView);

  const visibleBooks =
    activeFilter === "all"
      ? ALL_BOOKS
      : ALL_BOOKS.filter((b) => b.rowId === activeFilter);

  return (
    <div className="w-full">
      {/* ── Slim Filter Bar ── */}
      <div className="max-w-7xl mx-auto px-6 sm:px-10 lg:px-16 pt-5 pb-3 flex flex-wrap items-center justify-between gap-3">
        {/* Category filters */}
        <div className="flex items-center gap-4 sm:gap-5 overflow-x-auto no-scrollbar">
          <button
            type="button"
            onClick={() => { setActiveFilter("all"); setViewMode("shelf"); }}
            className={`shrink-0 text-[10px] tracking-[0.2em] uppercase font-600 transition-colors cursor-pointer pb-0.5 border-b ${
              viewMode === "shelf" && activeFilter === "all"
                ? "text-[#222222] border-[#222222]"
                : "text-[#BBBBBB] border-transparent hover:text-[#222222] hover:border-[#222222]"
            }`}
            style={{ fontWeight: viewMode === "shelf" && activeFilter === "all" ? 700 : 500 }}
          >
            All
          </button>

          {BOOK_ROW_CATEGORIES.map((cat) => (
            <button
              key={cat.id}
              type="button"
              onClick={() => { setActiveFilter(cat.id); setViewMode("shelf"); }}
              className={`shrink-0 text-[10px] tracking-[0.2em] uppercase transition-colors cursor-pointer pb-0.5 border-b ${
                viewMode === "shelf" && activeFilter === cat.id
                  ? "text-[#222222] border-[#222222] font-700"
                  : "text-[#BBBBBB] border-transparent hover:text-[#222222] hover:border-[#222222]"
              }`}
              style={{
                fontWeight: viewMode === "shelf" && activeFilter === cat.id ? 700 : 500,
              }}
            >
              {cat.title}
            </button>
          ))}
        </div>

        {/* View toggle */}
        <div className="flex items-center gap-2 text-[10px] tracking-[0.2em] uppercase shrink-0">
          <button
            type="button"
            onClick={() => setViewMode("shelf")}
            className={`cursor-pointer transition-colors pb-0.5 border-b ${
              viewMode === "shelf"
                ? "text-[#222222] border-[#222222]"
                : "text-[#CCCCCC] border-transparent hover:text-[#222222]"
            }`}
            style={{ fontWeight: viewMode === "shelf" ? 700 : 400 }}
          >
            Shelf
          </button>
          <span className="text-[#DDDDDD]">·</span>
          <button
            type="button"
            onClick={() => setViewMode("rows")}
            className={`cursor-pointer transition-colors pb-0.5 border-b ${
              viewMode === "rows"
                ? "text-[#222222] border-[#222222]"
                : "text-[#CCCCCC] border-transparent hover:text-[#222222]"
            }`}
            style={{ fontWeight: viewMode === "rows" ? 700 : 400 }}
          >
            Rows
          </button>
        </div>
      </div>

      {/* ── Collection ── */}
      {viewMode === "shelf" ? (
        <div className="pb-4">
          <HorizontalScroller
            books={visibleBooks}
            rowId={activeFilter}
            showProgress={true}
          />
        </div>
      ) : (
        <div className="w-full pt-2">
          {BOOK_ROW_CATEGORIES.map((category) => {
            const rowBooks = category.bookSlugs
              .map((slug) => ALL_BOOKS.find((b) => b.slug === slug))
              .filter((b): b is NonNullable<typeof b> => b !== undefined);
            return (
              <BookRow key={category.id} category={category} books={rowBooks} />
            );
          })}
        </div>
      )}
    </div>
  );
}
