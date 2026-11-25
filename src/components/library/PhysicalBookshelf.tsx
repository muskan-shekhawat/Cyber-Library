"use client";

import React, { useState, useRef, useEffect, useCallback, useMemo } from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { Book } from "@/types";
import { BOOK_ROW_CATEGORIES } from "@/data/categories";
import Mawise3DBook, { BookInteractionState } from "./Mawise3DBook";
import BookDetailModal from "./BookDetailModal";

interface PhysicalBookshelfProps {
  books: Book[];
}

export default function PhysicalBookshelf({ books }: PhysicalBookshelfProps) {
  const [activeCategory, setActiveCategory] = useState<string>("all");
  const [selectedSlug, setSelectedSlug] = useState<string | null>(books[0]?.slug || null);
  const [isModalOpen, setIsModalOpen] = useState<boolean>(false);

  const containerRef = useRef<HTMLDivElement>(null);
  const shelfTrackRef = useRef<HTMLDivElement>(null);
  const wheelAccumulatorRef = useRef<number>(0);
  const wheelTimeoutRef = useRef<NodeJS.Timeout | null>(null);

  // Filter books according to category
  const filteredBooks = useMemo(() => {
    if (activeCategory === "all") return books;
    return books.filter((b) => b.rowId === activeCategory);
  }, [books, activeCategory]);

  useEffect(() => {
    if (filteredBooks.length > 0) {
      setSelectedSlug(filteredBooks[0].slug);
    } else {
      setSelectedSlug(null);
    }
  }, [activeCategory, filteredBooks]);

  const selectedIndex = useMemo(() => {
    if (!selectedSlug) return 0;
    const idx = filteredBooks.findIndex((b) => b.slug === selectedSlug);
    return idx >= 0 ? idx : 0;
  }, [filteredBooks, selectedSlug]);

  const selectedBook = filteredBooks[selectedIndex] || null;

  // Center selected book smoothly in shelf viewport
  const centerSelectedBook = useCallback((slug: string | null) => {
    if (!slug) return;
    const container = containerRef.current;
    const track = shelfTrackRef.current;
    if (!container || !track) return;

    const idx = filteredBooks.findIndex((b) => b.slug === slug);
    if (idx < 0) return;

    const bookElements = track.children;
    const targetBook = bookElements[idx] as HTMLElement;
    if (!targetBook) return;

    const containerWidth = container.clientWidth;
    const bookLeft = targetBook.offsetLeft;
    const bookWidth = targetBook.offsetWidth;
    const targetScrollLeft = bookLeft - containerWidth / 2 + bookWidth / 2;

    container.scrollTo({
      left: Math.max(0, targetScrollLeft),
      behavior: "smooth",
    });
  }, [filteredBooks]);

  useEffect(() => {
    const timer = setTimeout(() => {
      centerSelectedBook(selectedSlug);
    }, 50);
    return () => clearTimeout(timer);
  }, [selectedSlug, centerSelectedBook]);

  // Keyboard navigation (← / → to browse books)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (isModalOpen) return;
      if (e.key === "ArrowLeft") {
        e.preventDefault();
        if (selectedIndex > 0) {
          setSelectedSlug(filteredBooks[selectedIndex - 1].slug);
        }
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        if (selectedIndex < filteredBooks.length - 1) {
          setSelectedSlug(filteredBooks[selectedIndex + 1].slug);
        }
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [selectedIndex, filteredBooks, isModalOpen]);

  // Smooth wheel & trackpad scrolling: cycles through books smoothly without moving the fixed shelf
  const handleWheel = (e: React.WheelEvent) => {
    e.preventDefault();
    const delta = Math.abs(e.deltaX) > Math.abs(e.deltaY) ? e.deltaX : e.deltaY;
    wheelAccumulatorRef.current += delta;

    if (wheelTimeoutRef.current) clearTimeout(wheelTimeoutRef.current);
    wheelTimeoutRef.current = setTimeout(() => {
      wheelAccumulatorRef.current = 0;
    }, 180);

    const threshold = 35; // smooth threshold for changing books
    if (wheelAccumulatorRef.current > threshold) {
      wheelAccumulatorRef.current = 0;
      if (selectedIndex < filteredBooks.length - 1) {
        setSelectedSlug(filteredBooks[selectedIndex + 1].slug);
      }
    } else if (wheelAccumulatorRef.current < -threshold) {
      wheelAccumulatorRef.current = 0;
      if (selectedIndex > 0) {
        setSelectedSlug(filteredBooks[selectedIndex - 1].slug);
      }
    }
  };

  return (
    <div className="w-full flex flex-col items-center select-none overflow-hidden">
      {/* ── Category Filters (Matching Reference Images 1 & 2) ── */}
      <div className="w-full max-w-5xl mx-auto px-6 mb-3 sm:mb-4 flex items-center justify-center">
        <div className="flex items-center gap-1.5 sm:gap-2 overflow-x-auto no-scrollbar py-1 text-[11px] tracking-[0.16em] uppercase">
          <button
            type="button"
            onClick={() => setActiveCategory("all")}
            className={`px-3.5 py-1.5 rounded-full transition-all cursor-pointer font-semibold ${
              activeCategory === "all"
                ? "bg-[#2455FF] text-white shadow-sm"
                : "text-[#77736E] hover:text-[#1C1C1C] hover:bg-[#E4E1DA]/40"
            }`}
          >
            All
          </button>

          {BOOK_ROW_CATEGORIES.map((cat) => (
            <button
              key={cat.id}
              type="button"
              onClick={() => setActiveCategory(cat.id)}
              className={`px-3.5 py-1.5 rounded-full transition-all cursor-pointer font-semibold whitespace-nowrap ${
                activeCategory === cat.id
                  ? "bg-[#2455FF] text-white shadow-sm"
                  : "text-[#77736E] hover:text-[#1C1C1C] hover:bg-[#E4E1DA]/40"
              }`}
            >
              {cat.title}
            </button>
          ))}
        </div>
      </div>

      {/* ── 3D Bookshelf Stage (Firmly Fixed in Place) ── */}
      <div className="relative w-full max-w-6xl mx-auto px-4 sm:px-8 py-2 bookshelf-stage">
        {/* Navigation Arrows on Shelf Sides */}
        {selectedIndex > 0 && (
          <button
            type="button"
            onClick={() => {
              setSelectedSlug(filteredBooks[selectedIndex - 1].slug);
            }}
            className="absolute left-2 sm:left-4 top-[55%] -translate-y-1/2 z-30 w-10 h-10 rounded-full bg-white text-[#1C1C1C] border border-[#E4E1DA] shadow-xl flex items-center justify-center hover:scale-110 hover:border-[#1C1C1C] transition-all cursor-pointer"
            aria-label="Previous book"
          >
            <ChevronLeft className="w-5 h-5" />
          </button>
        )}

        {selectedIndex < filteredBooks.length - 1 && (
          <button
            type="button"
            onClick={() => {
              setSelectedSlug(filteredBooks[selectedIndex + 1].slug);
            }}
            className="absolute right-2 sm:right-4 top-[55%] -translate-y-1/2 z-30 w-10 h-10 rounded-full bg-white text-[#1C1C1C] border border-[#E4E1DA] shadow-xl flex items-center justify-center hover:scale-110 hover:border-[#1C1C1C] transition-all cursor-pointer"
            aria-label="Next book"
          >
            <ChevronRight className="w-5 h-5" />
          </button>
        )}

        {/* ── Books Track (Glides Smoothly Across the Fixed Shelf) ── */}
        <div
          ref={containerRef}
          onWheel={handleWheel}
          className="w-full overflow-x-hidden no-scrollbar scroll-smooth px-12 sm:px-32 lg:px-48"
          style={{ touchAction: "pan-x" }}
        >
          <div
            ref={shelfTrackRef}
            className="flex items-end justify-center min-w-max pb-0 pt-16 gap-1 sm:gap-1.5 preserve-3d"
            style={{
              minHeight: "420px",
            }}
          >
            {filteredBooks.map((book, index) => {
              const isSelected = book.slug === selectedSlug;
              const state: BookInteractionState = isSelected ? "front" : "resting";

              return (
                <Mawise3DBook
                  key={book.slug}
                  book={book}
                  state={state}
                  isOpenModal={isModalOpen && isSelected}
                  onSelect={() => {
                    setSelectedSlug(book.slug);
                  }}
                  onFlip={() => {}}
                  onReturn={() => {
                    setSelectedSlug(null);
                  }}
                  onOpenModal={() => setIsModalOpen(true)}
                  priority={Math.abs(index - selectedIndex) < 4}
                />
              );
            })}
          </div>
        </div>

        {/* ── Fixed 3D Terracotta Physical Shelf Plank (Firmly Anchored at Base) ── */}
        <div className="w-full relative preserve-3d -mt-[2px] pointer-events-none">
          <div className="shelf3D">
            <div className="shelfFace shelfTop" />
            <div className="shelfFace shelfFront" />
            <div className="shelfFace shelfLeft" />
            <div className="shelfFace shelfRight" />
            <div className="shelfFace shelfBottom" />
          </div>
          <div className="shelfCastShadow" />
        </div>

        {/* ── Minimal Selected Book Title Below Shelf (Matching Reference Images 1 & 2) ── */}
        {selectedBook && (
          <div className="w-full text-center mt-7 sm:mt-9 animate-in fade-in duration-300 pointer-events-none">
            <h3 className="text-xl sm:text-2xl font-serif font-bold text-[#1C1C1C] tracking-tight">
              {selectedBook.title}
            </h3>
            <p className="text-[10px] font-mono tracking-[0.24em] uppercase text-[#77736E] mt-1.5">
              {selectedBook.volumeNumber} · {selectedBook.category}
            </p>
          </div>
        )}
      </div>

      {/* ── Full Split Book Detail Reader Modal (Opens on Clicking the Book) ── */}
      <BookDetailModal
        book={selectedBook}
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onPrev={() => {
          if (selectedIndex > 0) {
            setSelectedSlug(filteredBooks[selectedIndex - 1].slug);
          }
        }}
        onNext={() => {
          if (selectedIndex < filteredBooks.length - 1) {
            setSelectedSlug(filteredBooks[selectedIndex + 1].slug);
          }
        }}
        hasPrev={selectedIndex > 0}
        hasNext={selectedIndex < filteredBooks.length - 1}
      />
    </div>
  );
}
