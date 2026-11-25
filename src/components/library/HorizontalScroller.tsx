"use client";

import React, { useRef, useState, useEffect, useCallback } from "react";
import gsap from "gsap";
import { Book } from "@/types";
import BookCard from "./BookCard";

interface HorizontalScrollerProps {
  books: Book[];
  rowId: string;
  showProgress?: boolean;
}

export default function HorizontalScroller({
  books,
  rowId,
  showProgress = false,
}: HorizontalScrollerProps) {
  const viewportRef = useRef<HTMLDivElement>(null);
  const trackRef = useRef<HTMLDivElement>(null);
  const progressBarRef = useRef<HTMLDivElement>(null);

  const [isOverflowing, setIsOverflowing] = useState(false);

  const stateRef = useRef({
    currentX: 0,
    targetX: 0,
    maxScroll: 0,
    isDragging: false,
    startX: 0,
    startTargetX: 0,
    lastPointerX: 0,
    lastTime: 0,
    velocity: 0,
    hasMoved: false,
    reducedMotion: false,
  });

  const measureBounds = useCallback(() => {
    const viewport = viewportRef.current;
    const track = trackRef.current;
    if (!viewport || !track) return;
    const maxScroll = Math.max(0, track.scrollWidth - viewport.clientWidth);
    stateRef.current.maxScroll = maxScroll;
    setIsOverflowing(maxScroll > 4);
    stateRef.current.targetX = Math.max(-maxScroll, Math.min(0, stateRef.current.targetX));
    stateRef.current.currentX = Math.max(-maxScroll, Math.min(0, stateRef.current.currentX));
  }, []);

  useEffect(() => {
    stateRef.current.targetX = 0;
    stateRef.current.currentX = 0;
    if (trackRef.current) gsap.set(trackRef.current, { x: 0, force3D: true });
    measureBounds();
  }, [books, rowId, measureBounds]);

  useEffect(() => {
    const viewport = viewportRef.current;
    const track = trackRef.current;
    if (!viewport || !track) return;

    stateRef.current.reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    measureBounds();

    const ro = new ResizeObserver(measureBounds);
    ro.observe(viewport);
    ro.observe(track);

    const tick = () => {
      const s = stateRef.current;
      const ratio = gsap.ticker.deltaRatio(60);

      // Silkier lerp — 0.078 factor = very smooth momentum feel
      const factor = s.reducedMotion
        ? 1
        : s.isDragging
        ? 1 - Math.pow(0.30, ratio)   // snappy follow while dragging
        : 1 - Math.pow(0.88, ratio);  // gentle glide after release

      const diff = s.targetX - s.currentX;
      if (Math.abs(diff) > 0.05) {
        s.currentX += diff * factor;
      } else {
        s.currentX = s.targetX;
      }

      gsap.set(track, { x: s.currentX, force3D: true });

      if (progressBarRef.current && s.maxScroll > 0) {
        const pct = Math.min(1, Math.max(0, Math.abs(s.currentX) / s.maxScroll));
        gsap.set(progressBarRef.current, {
          scaleX: 0.08 + pct * 0.92,
          transformOrigin: "left center",
          force3D: true,
        });
      }
    };

    gsap.ticker.add(tick);

    const handleWheel = (e: WheelEvent) => {
      const s = stateRef.current;
      if (s.maxScroll <= 0) return;

      const multiplier = e.deltaMode === 1 ? 32 : e.deltaMode === 2 ? 400 : 1;
      const dx = e.deltaX * multiplier;
      const dy = e.deltaY * multiplier;
      const rawDelta = Math.abs(dx) > Math.abs(dy) ? dx : dy;
      if (Math.abs(rawDelta) < 0.5) return;

      const atStart = s.targetX >= -0.5 && rawDelta < 0;
      const atEnd = s.targetX <= -s.maxScroll + 0.5 && rawDelta > 0;
      if (Math.abs(dy) > Math.abs(dx) && (atStart || atEnd)) return;

      e.preventDefault();
      // Slightly more sensitive — 1.4x multiplier
      s.targetX = Math.max(-s.maxScroll, Math.min(0, s.targetX - rawDelta * 1.4));
    };

    viewport.addEventListener("wheel", handleWheel, { passive: false });

    return () => {
      gsap.ticker.remove(tick);
      viewport.removeEventListener("wheel", handleWheel);
      ro.disconnect();
    };
  }, [measureBounds]);

  // Pointer drag with momentum throw
  const onPointerDown = (e: React.PointerEvent<HTMLDivElement>) => {
    if (e.pointerType === "mouse" && e.button !== 0) return;
    const s = stateRef.current;
    if (s.maxScroll <= 0) return;
    s.isDragging = true;
    s.hasMoved = false;
    s.startX = e.clientX;
    s.startTargetX = s.targetX;
    s.lastPointerX = e.clientX;
    s.lastTime = performance.now();
    s.velocity = 0;
    if (viewportRef.current) viewportRef.current.style.cursor = "grabbing";
    (e.currentTarget as HTMLDivElement).setPointerCapture(e.pointerId);
  };

  const onPointerMove = (e: React.PointerEvent<HTMLDivElement>) => {
    const s = stateRef.current;
    if (!s.isDragging) return;
    const totalDx = e.clientX - s.startX;
    if (Math.abs(totalDx) > 5) s.hasMoved = true;
    s.targetX = Math.max(-s.maxScroll, Math.min(0, s.startTargetX + totalDx));
    const now = performance.now();
    const dt = Math.max(now - s.lastTime, 4);
    s.velocity = s.velocity * 0.35 + ((e.clientX - s.lastPointerX) / dt) * 0.65;
    s.lastPointerX = e.clientX;
    s.lastTime = now;
  };

  const onPointerUp = () => {
    const s = stateRef.current;
    if (!s.isDragging) return;
    s.isDragging = false;
    if (viewportRef.current) viewportRef.current.style.cursor = "grab";
    // Momentum throw — generous multiplier for natural feel
    if (Math.abs(s.velocity) > 0.08) {
      const momentum = s.velocity * 320;
      s.targetX = Math.max(-s.maxScroll, Math.min(0, s.targetX + momentum));
    }
    setTimeout(() => { stateRef.current.hasMoved = false; }, 60);
  };

  return (
    <div className="relative w-full">
      {/* GPU Viewport */}
      <div
        ref={viewportRef}
        onPointerDown={onPointerDown}
        onPointerMove={onPointerMove}
        onPointerUp={onPointerUp}
        onPointerCancel={onPointerUp}
        onClickCapture={(e) => {
          if (stateRef.current.hasMoved) {
            e.preventDefault();
            e.stopPropagation();
          }
        }}
        className="w-full overflow-hidden py-8 sm:py-10 cursor-grab select-none touch-pan-y"
      >
        <div
          ref={trackRef}
          className="flex items-end gap-5 sm:gap-7 px-6 sm:px-12 lg:px-20 w-max will-change-transform"
        >
          {books.map((book, index) => (
            <BookCard
              key={book.slug}
              book={book}
              priority={index < 6}
              enterDelay={Math.min(index, 7)}
            />
          ))}
        </div>
      </div>

      {/* Hairline progress bar */}
      {showProgress && isOverflowing && (
        <div className="px-6 sm:px-12 lg:px-20 mt-1 pb-1">
          <div className="w-full h-[1px] bg-[#E8E6E1] overflow-hidden">
            <div
              ref={progressBarRef}
              className="w-full h-full bg-[#B5A184] origin-left"
              style={{ transform: "scaleX(0.08)" }}
            />
          </div>
        </div>
      )}
    </div>
  );
}
