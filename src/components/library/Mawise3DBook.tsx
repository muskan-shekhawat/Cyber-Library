"use client";

/**
 * 3D Animated Physical Book Component
 * 
 * Inspired by and adapted from the MIT-licensed project:
 * mawise/bookshelf (https://github.com/mawise/bookshelf)
 * Original 3D CSS book concept by Sébastien Castiel (https://scastiel.dev/3dbook)
 * 
 * MIT License - Copyright (c) 2021 mawise
 */

import React, { useState, useEffect } from "react";
import Image from "next/image";
import Link from "next/link";
import { ArrowRight, BookOpen } from "lucide-react";
import { Book } from "@/types";
import { BOOK_STYLES } from "@/data/bookStyles";

export type BookInteractionState = "resting" | "front" | "back";

interface Mawise3DBookProps {
  book: Book;
  state: BookInteractionState;
  isOpenModal?: boolean;
  onSelect: () => void;
  onFlip: () => void;
  onReturn: () => void;
  onOpenModal: () => void;
  priority?: boolean;
}

export default function Mawise3DBook({
  book,
  state,
  isOpenModal = false,
  onSelect,
  onFlip,
  onReturn,
  onOpenModal,
  priority = false,
}: Mawise3DBookProps) {
  const [isHovered, setIsHovered] = useState(false);
  const [isOpening, setIsOpening] = useState(false);

  const style = BOOK_STYLES[book.slug] || {
    height: 366,
    thickness: 60,
    coverWidth: 350,
    spineColor: "#1C1C1C",
    spineGradient: "linear-gradient(180deg, #1C1C1C 0%, #2A2A2A 50%, #111111 100%)",
    foilColor: "#D4AF37",
    textColor: "#FFFFFF",
    author: "Cybersecurity Editorial Board",
    rating: "4.9",
    badge: "MONOGRAPH",
    theme: "charcoal",
  };

  const height = style.height;
  const width = style.coverWidth;
  const depth = style.thickness;

  // Reset opening animation when state returns to resting or modal closes
  useEffect(() => {
    if (state === "resting" || !isOpenModal) {
      setIsOpening(false);
    }
  }, [state, isOpenModal]);

  // Transform calculation based on interaction states:
  // - resting: stowed on shelf, rotated 90deg so spine faces viewer!
  // - resting + hover: slides forward slightly along Z
  // - front: pulled out towards viewer onto front shelf surface and rotated to 0deg (facing camera flat)
  // - back: flipped 180deg to display back cover!
  let bookTransform = "rotateY(90deg) translateZ(40px)";
  if (state === "resting") {
    bookTransform = isHovered
      ? "rotateY(90deg) translateZ(75px) translateY(-8px)"
      : "rotateY(90deg) translateZ(40px)";
  } else if (state === "front") {
    bookTransform = "translateZ(160px) translateY(-12px) rotateY(0deg)";
  } else if (state === "back") {
    bookTransform = "translateZ(160px) translateY(-12px) rotateY(180deg)";
  }

  // Handle click on the book:
  // If resting: select book to pull it forward.
  // If front-facing: animate book opening first, then trigger reader modal!
  const handleClick = (e: React.MouseEvent) => {
    e.stopPropagation();
    if (state === "resting") {
      onSelect();
    } else {
      setIsOpening(true);
      setTimeout(() => {
        onOpenModal();
      }, 550);
    }
  };

  const firstChapterSlug = book.chapters?.[0]?.slug || "";

  return (
    <div
      className="relative shrink-0 select-none preserve-3d transition-all duration-700 ease-[cubic-bezier(0.25,1,0.35,1)]"
      style={{
        // Allocated horizontal space on the shelf:
        // When resting: spine thickness + small gap
        // When selected: full cover width + margin
        width: state === "resting" ? `${depth + 6}px` : `${width + 24}px`,
        height: `${height}px`,
      }}
    >
      {/* ── 3D Physical Book Rig ── */}
      <div
        onClick={handleClick}
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
        className="absolute bottom-0 left-1/2 preserve-3d cursor-pointer transition-transform duration-700 ease-[cubic-bezier(0.25,1,0.35,1)]"
        style={{
          width: `${width}px`,
          height: `${height}px`,
          marginLeft: `-${width / 2}px`,
          transform: bookTransform,
          transformOrigin: "center center",
        }}
      >
        {/* ── 1. FRONT COVER ASSEMBLY (Physical Door Hinge Open Animation) ── */}
        <div
          className="absolute inset-0 rounded-[2px] preserve-3d transition-transform duration-700 ease-[cubic-bezier(0.2,0.85,0.25,1)]"
          style={{
            transformOrigin: "left center",
            transform: isOpening
              ? `translateZ(${depth / 2}px) rotateY(-150deg)`
              : `translateZ(${depth / 2}px) rotateY(0deg)`,
            zIndex: isOpening ? 30 : 20,
          }}
          title={state === "front" ? `Click to open ${book.title}` : undefined}
        >
          {/* Front Cover Artwork Face */}
          <div
            className="absolute inset-0 rounded-[2px] overflow-hidden backface-hidden shadow-2xl"
            style={{
              backgroundColor: style.spineColor,
            }}
          >
            <Image
              src={book.coverImage}
              alt={book.title}
              fill
              sizes="500px"
              priority={priority}
              draggable={false}
              className="object-contain p-0.5 pointer-events-none select-none"
            />

            {/* Hardcover bevel, spine joint hinge crease, and physical lighting */}
            <div className="absolute inset-y-0 left-0 w-4 pointer-events-none bg-gradient-to-r from-black/40 via-black/10 to-transparent z-10" />
            <div className="absolute inset-y-0 left-[11px] w-[1px] pointer-events-none bg-white/30 z-10" />
            <div className="absolute inset-0 pointer-events-none border border-black/15 rounded-[2px] z-10" />
          </div>

          {/* Front Cover Inside (Endpaper revealed as cover swings open) */}
          <div
            className="absolute inset-0 rounded-[2px] p-6 flex flex-col justify-between overflow-hidden shadow-2xl"
            style={{
              transform: "rotateY(180deg)",
              backfaceVisibility: "hidden",
              backgroundColor: "#161616",
              backgroundImage: "radial-gradient(ellipse at 50% 50%, #262626 0%, #0F0F0F 100%)",
              color: "#FFFFFF",
              border: "1px solid rgba(255,255,255,0.12)",
            }}
          >
            <div className="flex items-center justify-between border-b border-white/10 pb-3">
              <span className="text-[9px] font-mono tracking-[0.25em] uppercase text-white/60">
                {book.volumeNumber}
              </span>
              <span className="text-[9px] font-mono tracking-[0.25em] uppercase text-[#2455FF] font-semibold">
                ENDPAPER
              </span>
            </div>

            <div className="flex flex-col items-center justify-center my-auto text-center px-4">
              <div className="w-12 h-12 rounded-full border border-white/20 flex items-center justify-center mb-3 shadow-inner">
                <span className="text-xs font-mono font-bold tracking-widest text-white/90">NULL</span>
              </div>
              <p className="text-xs font-serif italic text-white/80">
                Cybersecurity Library Collection
              </p>
              <p className="text-[9px] font-mono text-white/40 uppercase tracking-widest mt-1">
                Official Monograph Edition
              </p>
            </div>

            <div className="text-[8px] font-mono tracking-wider text-white/40 border-t border-white/10 pt-2 text-center uppercase">
              EX LIBRIS · 24 VOLUMES ARCHIVE
            </div>
          </div>
        </div>

        {/* ── 1.5 FIRST INSIDE TITLE PAGE (Revealed as cover swings open) ── */}
        <div
          className="absolute inset-0 rounded-[2px] p-6 flex flex-col justify-between bg-[#FAF7F0] text-[#1C1C1C] border border-[#E8E2D5] shadow-inner"
          style={{
            transform: `translateZ(${depth / 2 - 2}px)`,
            zIndex: 10,
          }}
        >
          {/* Spine valley shadow at left hinge */}
          <div className="absolute inset-y-0 left-0 w-8 pointer-events-none bg-gradient-to-r from-black/25 via-black/05 to-transparent z-10" />

          <div className="relative z-10">
            <div className="flex items-center justify-between text-[9px] font-mono tracking-[0.22em] uppercase text-[#77736E] mb-3 pb-2 border-b border-[#E8E2D5]">
              <span>{book.volumeNumber}</span>
              <span className="text-[#2455FF] font-bold">{book.category}</span>
            </div>

            <h2 className="text-lg font-serif font-bold tracking-tight leading-snug mb-2 text-[#1C1C1C]">
              {book.title}
            </h2>

            <p className="text-[11px] font-medium text-[#77736E] mb-3">
              by <span className="text-[#1C1C1C] font-semibold">{style.author}</span>
            </p>

            <div className="w-10 h-[1.5px] bg-[#2455FF] mb-3" />

            <p className="text-[10px] text-[#77736E] leading-relaxed line-clamp-4">
              {book.shortDescription}
            </p>
          </div>

          <div className="relative z-10 pt-3 border-t border-[#E8E2D5] flex items-center justify-between">
            <div className="text-[9px] font-mono text-[#77736E]">
              {book.chaptersCount} Chapters · {book.estimatedHours}h Study
            </div>
            <span className="inline-flex items-center gap-1 text-[10px] font-bold uppercase tracking-wider text-[#2455FF]">
              Opening Reader <ArrowRight className="w-3 h-3 animate-pulse" />
            </span>
          </div>
        </div>

        {/* ── 2. BACK COVER (face-back) ── */}
        <div
          className="absolute inset-0 rounded-[2px] p-6 flex flex-col justify-between preserve-3d shadow-2xl"
          style={{
            transform: `rotateY(180deg) translateZ(${depth / 2}px)`,
            backgroundColor: style.spineColor,
            color: style.textColor,
          }}
        >
          {/* Subtle cloth texture overlay */}
          <div className="absolute inset-0 bg-gradient-to-tr from-black/25 via-transparent to-white/10 pointer-events-none" />

          <div className="relative z-10">
            <div className="flex items-center justify-between text-[10px] font-mono tracking-[0.2em] uppercase opacity-80 mb-3 border-b pb-2" style={{ borderColor: style.foilColor + "40" }}>
              <span>{book.volumeNumber}</span>
              <span className="font-bold">{book.category}</span>
            </div>

            <h3 className="text-base font-serif font-bold tracking-tight leading-snug mb-2">
              {book.title}
            </h3>

            <p className="text-[11px] opacity-85 leading-relaxed line-clamp-5 mb-4">
              {book.shortDescription}
            </p>

            <div className="text-[10px] font-mono opacity-80 space-y-1">
              <p>Difficulty: <span className="font-semibold">{book.difficulty}</span></p>
              <p>Curriculum: {book.chaptersCount} Detailed Chapters</p>
              <p>Estimated Study: {book.estimatedHours} Hours</p>
            </div>
          </div>

          {/* Back Cover Actions */}
          <div className="relative z-10 pt-4 border-t" style={{ borderColor: style.foilColor + "40" }}>
            <div className="flex items-center justify-between">
              {firstChapterSlug ? (
                <Link
                  href={`/books/${book.slug}/${firstChapterSlug}`}
                  className="inline-flex items-center gap-1.5 px-3 py-1.5 bg-[#2455FF] text-white text-[10px] font-bold tracking-wider uppercase rounded shadow hover:bg-[#1B42D6] transition-colors"
                >
                  <span>Read Chapter 1</span>
                  <ArrowRight className="w-3 h-3" />
                </Link>
              ) : null}

              <button
                type="button"
                onClick={(e) => {
                  e.stopPropagation();
                  onFlip();
                }}
                className="text-[10px] font-mono uppercase tracking-wider underline opacity-80 hover:opacity-100 cursor-pointer"
              >
                ← Front
              </button>
            </div>
          </div>
        </div>

        {/* ── 3. BOOK SPINE (face-spine, visible when resting on shelf) ── */}
        <div
          className="absolute top-0 bottom-0 flex flex-col justify-between items-center py-4 px-1 rounded-[1px] preserve-3d"
          style={{
            width: `${depth}px`,
            left: `-${depth / 2}px`,
            transform: `rotateY(-90deg) translateZ(0px)`,
            backgroundColor: style.spineColor,
            backgroundImage: style.spineGradient,
            boxShadow: "inset 1px 0 2px rgba(255,255,255,0.25), inset -1px 0 2px rgba(0,0,0,0.35)",
          }}
        >
          {/* Spine Cylindrical Lighting */}
          <div className="absolute inset-0 pointer-events-none spine-lighting z-10" />

          {/* Top Foil Band & Volume Badge */}
          <div className="relative z-20 flex flex-col items-center w-full px-1">
            <div className="w-full h-[1.5px] opacity-75 mb-1" style={{ backgroundColor: style.foilColor }} />
            <span
              className="text-[8px] font-mono font-bold tracking-[0.18em] uppercase"
              style={{ color: style.foilColor }}
            >
              {book.volumeNumber.replace("VOL. ", "V.")}
            </span>
          </div>

          {/* ── Vertical Spine Title (Clean, crisp, readable) ── */}
          <div
            className="relative z-20 flex-1 flex items-center justify-center my-2 overflow-hidden"
            style={{
              writingMode: "vertical-rl",
              transform: "rotate(180deg)",
            }}
          >
            <span
              className="text-[11px] font-semibold tracking-[0.14em] uppercase whitespace-nowrap text-center select-none"
              style={{
                color: style.textColor,
                textShadow: "0 1px 2px rgba(0,0,0,0.3)",
              }}
            >
              {book.title.length > 34 ? book.title.slice(0, 32) + "…" : book.title}
            </span>
          </div>

          {/* Bottom Colophon & Foil Band */}
          <div className="relative z-20 flex flex-col items-center w-full px-1">
            <span
              className="text-[7px] font-mono tracking-[0.2em] uppercase opacity-75 mb-1"
              style={{ color: style.foilColor }}
            >
              NULL
            </span>
            <div className="w-full h-[1.5px] opacity-75" style={{ backgroundColor: style.foilColor }} />
          </div>
        </div>

        {/* ── 4. RIGHT PAGE BLOCK EDGE (face-pages, thick physical paper block) ── */}
        <div
          className="absolute top-1 bottom-1 pointer-events-none preserve-3d"
          style={{
            width: `${depth - 5}px`,
            right: `-${(depth - 5) / 2}px`,
            transform: `rotateY(90deg) translateZ(0px)`,
            background: "repeating-linear-gradient(180deg, #FAF7F0 0px, #FAF7F0 2px, #E6DFCE 2px, #FAF7F0 4px)",
            boxShadow: "inset 0 0 5px rgba(0,0,0,0.22)",
          }}
        />

        {/* ── 5. TOP PAGE BLOCK EDGE (face-top) ── */}
        <div
          className="absolute left-3 right-1 pointer-events-none preserve-3d"
          style={{
            height: `${depth - 5}px`,
            top: `-${(depth - 5) / 2}px`,
            transform: `rotateX(90deg) translateZ(0px)`,
            background: "linear-gradient(90deg, #D6CFC0 0%, #FAF7F0 40%, #E8E2D5 100%)",
            boxShadow: "inset 0 0 4px rgba(0,0,0,0.18)",
          }}
        />
      </div>

      {/* ── Dynamic Shelf Contact Shadow ── */}
      <div
        className="absolute -bottom-2 left-1/2 -translate-x-1/2 h-3 pointer-events-none rounded-full transition-all duration-700"
        style={{
          width: state === "resting" ? `${depth + 10}px` : `${width * 0.85}px`,
          background: "radial-gradient(ellipse at center, rgba(0,0,0,0.45) 0%, rgba(0,0,0,0.12) 60%, transparent 80%)",
          opacity: state === "resting" ? (isHovered ? 0.9 : 0.65) : 0.85,
          filter: state === "resting" ? "blur(1.5px)" : "blur(4px)",
        }}
      />
    </div>
  );
}
