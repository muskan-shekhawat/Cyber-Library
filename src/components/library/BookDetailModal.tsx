"use client";

import React, { useEffect, useCallback } from "react";
import Image from "next/image";
import Link from "next/link";
import { X, ChevronLeft, ChevronRight, BookOpen, Clock, ArrowRight, Shield, Award, Sparkles } from "lucide-react";
import { Book } from "@/types";
import { BOOK_STYLES } from "@/data/bookStyles";

interface BookDetailModalProps {
  book: Book | null;
  isOpen: boolean;
  onClose: () => void;
  onPrev: () => void;
  onNext: () => void;
  hasPrev: boolean;
  hasNext: boolean;
}

export default function BookDetailModal({
  book,
  isOpen,
  onClose,
  onPrev,
  onNext,
  hasPrev,
  hasNext,
}: BookDetailModalProps) {
  // Handle ESC and Arrow keys for keyboard navigation
  const handleKeyDown = useCallback(
    (e: KeyboardEvent) => {
      if (!isOpen) return;
      if (e.key === "Escape") onClose();
      if (e.key === "ArrowLeft" && hasPrev) onPrev();
      if (e.key === "ArrowRight" && hasNext) onNext();
    },
    [isOpen, onClose, onPrev, onNext, hasPrev, hasNext]
  );

  useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    if (isOpen) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }
    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      document.body.style.overflow = "";
    };
  }, [isOpen, handleKeyDown]);

  if (!isOpen || !book) return null;

  const style = BOOK_STYLES[book.slug] || {
    author: "Cybersecurity Editorial Board",
    rating: "4.9",
    spineColor: "#1C1C1C",
    badge: "FOUNDATION",
    foilColor: "#D4AF37",
    textColor: "#FFFFFF",
  };

  const firstChapterSlug = book.chapters?.[0]?.slug || "";
  const ribbonColor = style.foilColor === "#FFFFFF" || style.foilColor === "#E0E7FF" ? "#2455FF" : style.foilColor;

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 lg:p-8 bg-black/80 backdrop-blur-md animate-in fade-in duration-300 select-none overflow-y-auto"
      onClick={onClose}
    >
      {/* ── Top Floating Close Pill ── */}
      <button
        type="button"
        onClick={onClose}
        className="fixed top-4 right-4 sm:top-6 sm:right-8 z-50 flex items-center gap-2.5 px-4 py-2 rounded-full bg-[#1C1C1C]/90 hover:bg-[#1C1C1C] text-white border border-white/20 hover:border-white/50 shadow-2xl backdrop-blur-md transition-all duration-200 text-xs font-mono tracking-wider cursor-pointer group"
        aria-label="Close reader"
      >
        <span>CLOSE</span>
        <span className="text-[10px] text-white/50 font-sans group-hover:text-white/80 transition-colors">[ESC]</span>
        <X className="w-3.5 h-3.5 group-hover:rotate-90 transition-transform duration-200" />
      </button>

      {/* ── Floating Side Navigation: Previous Volume ── */}
      {hasPrev && (
        <button
          type="button"
          onClick={(e) => {
            e.stopPropagation();
            onPrev();
          }}
          className="fixed left-2 sm:left-6 top-1/2 -translate-y-1/2 z-50 w-11 h-11 rounded-full bg-[#1C1C1C]/85 hover:bg-[#1C1C1C] text-white border border-white/20 hover:border-white/50 shadow-2xl backdrop-blur-md flex items-center justify-center hover:scale-110 transition-all duration-200 cursor-pointer group"
          title="Previous Volume (←)"
          aria-label="Previous Volume"
        >
          <ChevronLeft className="w-5 h-5 group-hover:-translate-x-0.5 transition-transform" />
        </button>
      )}

      {/* ── Floating Side Navigation: Next Volume ── */}
      {hasNext && (
        <button
          type="button"
          onClick={(e) => {
            e.stopPropagation();
            onNext();
          }}
          className="fixed right-2 sm:right-6 top-1/2 -translate-y-1/2 z-50 w-11 h-11 rounded-full bg-[#1C1C1C]/85 hover:bg-[#1C1C1C] text-white border border-white/20 hover:border-white/50 shadow-2xl backdrop-blur-md flex items-center justify-center hover:scale-110 transition-all duration-200 cursor-pointer group"
          title="Next Volume (→)"
          aria-label="Next Volume"
        >
          <ChevronRight className="w-5 h-5 group-hover:translate-x-0.5 transition-transform" />
        </button>
      )}

      {/* ═══════════════════════════════════════════════════════════════
          PHYSICAL OPEN HARDCOVER BOOK SPREAD (THE MASTER DESIGN)
          ═══════════════════════════════════════════════════════════════ */}
      <div
        onClick={(e) => e.stopPropagation()}
        className="relative w-full max-w-6xl max-h-[92vh] flex flex-col rounded-2xl shadow-[0_35px_100px_rgba(0,0,0,0.85)] animate-in zoom-in-95 duration-300"
        style={{
          backgroundColor: style.spineColor,
          padding: "10px", // Hardcover casing overhang border
          boxShadow: "0 40px 100px -20px rgba(0, 0, 0, 0.85), 0 0 0 1px rgba(255, 255, 255, 0.15) inset, 0 10px 30px rgba(0, 0, 0, 0.5)",
        }}
      >
        {/* Subtle Hardcover Gold/Blind Deboss Border on Outer Casing */}
        <div className="absolute inset-1.5 rounded-xl border border-white/10 pointer-events-none" />

        {/* Realistic Silk Bookmark Ribbon Hanging from Top Center Binding */}
        <div
          className="absolute -top-1 left-1/2 -translate-x-1/2 w-4 sm:w-5 h-32 sm:h-36 z-40 pointer-events-none shadow-2xl transition-all"
          style={{
            backgroundColor: ribbonColor,
            backgroundImage: "linear-gradient(90deg, rgba(0,0,0,0.3) 0%, rgba(255,255,255,0.25) 45%, rgba(0,0,0,0.25) 100%)",
            clipPath: "polygon(0% 0%, 100% 0%, 100% 90%, 50% 100%, 0% 90%)",
            filter: "drop-shadow(2px 6px 12px rgba(0,0,0,0.45))",
          }}
        />

        {/* ── Inner Open Paper Pages Block (Authentic Warm Archival Paper) ── */}
        <div className="relative w-full flex-1 flex flex-col lg:flex-row bg-[#FAF7EE] rounded-xl overflow-hidden shadow-inner border border-[#E4DEC8]">
          
          {/* Layered Paper Edge Illusion (Page Block Thickness on sides) */}
          <div className="hidden lg:block absolute left-0 inset-y-0 w-2.5 bg-gradient-to-r from-[#D8D0BA] via-[#EDE7D5] to-transparent pointer-events-none z-20" />
          <div className="hidden lg:block absolute right-0 inset-y-0 w-2.5 bg-gradient-to-l from-[#D8D0BA] via-[#EDE7D5] to-transparent pointer-events-none z-20" />

          {/* Central Gutter / Spine Valley Shadow (Creates true 3D book depth & page curvature) */}
          <div
            className="hidden lg:block absolute inset-y-0 left-1/2 -translate-x-1/2 w-20 pointer-events-none z-30"
            style={{
              background: "linear-gradient(to right, rgba(0,0,0,0) 0%, rgba(0,0,0,0.03) 20%, rgba(0,0,0,0.14) 44%, rgba(0,0,0,0.28) 50%, rgba(0,0,0,0.14) 56%, rgba(0,0,0,0.03) 80%, rgba(0,0,0,0) 100%)",
            }}
          />

          {/* ─────────────────────────────────────────────────────────────
              LEFT PAGE (VERSO): Archival Frontispiece Plate & Monograph Details
              ───────────────────────────────────────────────────────────── */}
          <div className="flex-1 p-6 sm:p-8 lg:p-10 flex flex-col justify-between border-b lg:border-b-0 lg:border-r border-[#E5DECC] bg-gradient-to-r from-[#FAF7EE] via-[#FAF7EE] to-[#F3EEE2] overflow-y-auto no-scrollbar">
            
            {/* Top Running Header */}
            <div>
              <div className="flex items-center justify-between pb-3 mb-6 border-b border-[#E5DECC] text-[10px] font-mono tracking-[0.24em] uppercase text-[#77736E]">
                <span>NULL / LIBRARY ARCHIVE</span>
                <span className="font-bold text-[#1C1C1C]">{book.volumeNumber}</span>
              </div>

              {/* Plate: Framed Book Cover & Core Typography */}
              <div className="flex flex-col sm:flex-row gap-6 sm:gap-7 items-start mb-6">
                
                {/* Book Cover Artwork Frame (Archival Presentation Plate) */}
                <div
                  className="relative shrink-0 w-36 sm:w-44 h-48 sm:h-60 rounded-md overflow-hidden bg-white shadow-2xl border border-black/15 group"
                  style={{
                    boxShadow: "0 16px 36px -8px rgba(0,0,0,0.35), 0 4px 12px -2px rgba(0,0,0,0.2)",
                  }}
                >
                  <Image
                    src={book.coverImage}
                    alt={book.title}
                    fill
                    sizes="240px"
                    priority
                    className="object-cover select-none pointer-events-none"
                  />
                  {/* Subtle Spine Joint Hinge Shadow & Bevel */}
                  <div className="absolute inset-y-0 left-0 w-3 bg-gradient-to-r from-black/35 to-transparent pointer-events-none" />
                  <div className="absolute inset-0 border border-black/10 rounded-md pointer-events-none" />
                </div>

                {/* Title & Archival Metadata */}
                <div className="flex-1">
                  <div className="flex items-center gap-2 text-[10px] font-mono uppercase tracking-[0.2em] mb-2">
                    <span className="text-[#2455FF] font-bold">{book.category}</span>
                    <span className="text-[#A8A29E]">·</span>
                    <span className="text-[#77736E]">{book.difficulty}</span>
                  </div>

                  <h2 className="text-2xl sm:text-3xl font-serif font-bold text-[#1C1C1C] tracking-tight leading-tight mb-2">
                    {book.title}
                  </h2>

                  <p className="text-xs sm:text-sm font-serif italic text-[#77736E] mb-3">
                    {book.subtitle}
                  </p>

                  <p className="text-xs font-medium text-[#1C1C1C] mb-4">
                    Author: <span className="font-semibold">{style.author}</span>
                  </p>

                  {/* Rating & Study Bar */}
                  <div className="flex items-center gap-3 text-xs text-[#77736E] pt-3 border-t border-[#E5DECC]">
                    <div className="flex items-center gap-1 text-amber-500">
                      <span>★★★★★</span>
                      <span className="font-bold text-[#1C1C1C] text-[11px] ml-0.5">{style.rating}</span>
                    </div>
                    <span className="text-[#D5D0C6]">|</span>
                    <div className="flex items-center gap-1.5 text-[11px]">
                      <Clock className="w-3.5 h-3.5 text-[#1C1C1C]" />
                      <span>{book.estimatedHours}h Study Time</span>
                    </div>
                  </div>
                </div>
              </div>

              {/* Editorial Description */}
              <div className="space-y-2 mb-6 text-xs sm:text-[13px] leading-relaxed text-[#2C2C2C] font-normal">
                <p>{book.shortDescription}</p>
                <p className="text-xs text-[#77736E] leading-relaxed">{book.fullDescription}</p>
              </div>

              {/* Tools Covered Pills */}
              {book.toolsCovered && book.toolsCovered.length > 0 && (
                <div className="mb-6">
                  <span className="text-[10px] font-mono tracking-[0.2em] uppercase text-[#77736E] block mb-2 font-semibold">
                    Laboratory Toolchain
                  </span>
                  <div className="flex flex-wrap gap-1.5">
                    {book.toolsCovered.map((tool) => (
                      <span
                        key={tool}
                        className="text-[10px] font-mono px-2.5 py-1 bg-white border border-[#E2DCCE] rounded text-[#1C1C1C] shadow-sm"
                      >
                        {tool}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>

            {/* Bottom Actions & Page Footer */}
            <div className="pt-4 border-t border-[#E5DECC] flex flex-wrap items-center justify-between gap-4">
              <div className="flex items-center gap-3">
                {firstChapterSlug ? (
                  <Link
                    href={`/books/${book.slug}/${firstChapterSlug}`}
                    className="inline-flex items-center gap-2 px-6 py-3 bg-[#1C1C1C] hover:bg-[#2455FF] text-white text-xs font-mono font-bold tracking-[0.16em] uppercase rounded shadow-lg hover:shadow-xl transition-all duration-200 hover:scale-[1.02]"
                  >
                    <BookOpen className="w-4 h-4" />
                    <span>Open & Read Chapter 1</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </Link>
                ) : null}

                <Link
                  href={`/books/${book.slug}`}
                  className="px-4 py-3 rounded border border-[#D5D0C6] hover:border-[#1C1C1C] bg-white text-xs font-mono font-semibold tracking-wider uppercase text-[#1C1C1C] hover:bg-[#F4F0E8] transition-all"
                >
                  Full Syllabus
                </Link>
              </div>

              {/* Classic Book Page Number Footer */}
              <div className="text-[10px] font-mono text-[#A8A29E] tracking-widest uppercase">
                VOL. {book.volumeNumber.replace("VOL. ", "")} · PAGE 01
              </div>
            </div>
          </div>

          {/* ─────────────────────────────────────────────────────────────
              RIGHT PAGE (RECTO): The Classic Table of Contents with Dotted Leaders
              ───────────────────────────────────────────────────────────── */}
          <div className="flex-1 p-6 sm:p-8 lg:p-10 flex flex-col justify-between bg-gradient-to-l from-[#FAF7EE] via-[#FAF7EE] to-[#F3EEE2] overflow-y-auto no-scrollbar">
            
            {/* Top Running Header */}
            <div>
              <div className="flex items-center justify-between pb-3 mb-6 border-b border-[#E5DECC] text-[10px] font-mono tracking-[0.24em] uppercase text-[#77736E]">
                <span>CURRICULUM INDEX</span>
                <span className="font-bold text-[#1C1C1C]">{book.chaptersCount} CHAPTERS</span>
              </div>

              {/* Section Header */}
              <div className="mb-5">
                <h3 className="text-xl sm:text-2xl font-serif font-bold text-[#1C1C1C] tracking-tight">
                  Table of Contents
                </h3>
                <p className="text-xs text-[#77736E] font-serif italic mt-0.5">
                  Select any chapter below to open directly in the reader
                </p>
                <div className="w-12 h-[1px] bg-[#2455FF] mt-2 mb-4" />
              </div>

              {/* Chapter Listing with Classic Dotted Leaders */}
              <div className="space-y-1.5 max-h-[50vh] lg:max-h-[52vh] overflow-y-auto no-scrollbar pr-1">
                {book.chapters.map((ch, idx) => {
                  const pageNumber = String(idx * 28 + 1).padStart(3, "0");
                  return (
                    <Link
                      key={ch.slug}
                      href={`/books/${book.slug}/${ch.slug}`}
                      className="group flex items-center justify-between p-2.5 sm:p-3 rounded-md bg-white/60 hover:bg-white border border-[#E8E2D5] hover:border-[#1C1C1C] transition-all duration-150 shadow-sm hover:shadow"
                    >
                      <div className="flex items-center gap-3 min-w-0 flex-1 pr-3">
                        <span className="font-mono text-xs font-bold text-[#2455FF] shrink-0 w-6">
                          {String(idx + 1).padStart(2, "0")}
                        </span>
                        
                        <span className="font-serif text-sm font-semibold text-[#1C1C1C] group-hover:text-[#2455FF] transition-colors truncate">
                          {ch.title}
                        </span>

                        {/* Classic Book Dot Leader line */}
                        <div className="hidden sm:block flex-1 border-b border-dotted border-[#D5D0C6] mx-2 group-hover:border-[#2455FF]/40 transition-colors" />
                      </div>

                      <div className="flex items-center gap-2.5 shrink-0">
                        <span className="text-[10px] font-mono text-[#A8A29E] tracking-wider group-hover:text-[#1C1C1C] transition-colors">
                          p. {pageNumber}
                        </span>
                        <span className="text-[10px] font-mono uppercase tracking-wider text-[#2455FF] font-semibold opacity-0 group-hover:opacity-100 transition-opacity flex items-center gap-1">
                          Read
                          <ArrowRight className="w-3 h-3 group-hover:translate-x-0.5 transition-transform" />
                        </span>
                      </div>
                    </Link>
                  );
                })}
              </div>
            </div>

            {/* Right Page Bottom Colophon & Navigation */}
            <div className="pt-4 border-t border-[#E5DECC] flex items-center justify-between">
              <div className="flex items-center gap-2 text-[10px] font-mono text-[#77736E] tracking-wider uppercase">
                <Shield className="w-3.5 h-3.5 text-[#2455FF]" />
                <span>NULL / LIBRARY PRESS · MONOGRAPH EDITION</span>
              </div>

              {/* Right Page Number */}
              <div className="text-[10px] font-mono text-[#A8A29E] tracking-widest uppercase">
                PAGE 02 · 24 VOLUMES
              </div>
            </div>

          </div>

        </div>
      </div>
    </div>
  );
}