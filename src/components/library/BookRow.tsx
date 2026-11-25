"use client";

import React from "react";
import { BookRowCategory, Book } from "@/types";
import HorizontalScroller from "./HorizontalScroller";

interface BookRowProps {
  category: BookRowCategory;
  books: Book[];
}

export default function BookRow({ category, books }: BookRowProps) {
  if (books.length === 0) return null;

  return (
    <section className="py-5 sm:py-6 border-b border-[#ECEAE6] last:border-b-0">
      {/* Row header */}
      <div className="max-w-7xl mx-auto px-6 sm:px-10 lg:px-16 mb-1 flex items-baseline gap-3">
        <span
          className="text-[9px] tracking-[0.28em] uppercase text-[#C8C4BC]"
          style={{ fontWeight: 600 }}
        >
          {category.number}
        </span>
        <span className="text-[9px] text-[#D8D4CE]">—</span>
        <span
          className="text-[11px] tracking-[0.18em] uppercase text-[#222222]"
          style={{ fontWeight: 700 }}
        >
          {category.title}
        </span>
        <span className="ml-auto text-[9px] tracking-[0.14em] text-[#BBBBBB] uppercase" style={{ fontWeight: 500 }}>
          {books.length} {books.length === 1 ? "book" : "books"}
        </span>
      </div>

      <HorizontalScroller books={books} rowId={category.id} />
    </section>
  );
}
