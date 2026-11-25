"use client";

import React, { useRef } from "react";
import Link from "next/link";
import { Book } from "@/types";
import BookCover from "./BookCover";

interface BookCardProps {
  book: Book;
  priority?: boolean;
  enterDelay?: number;
}

export default function BookCard({ book, priority = false, enterDelay = 0 }: BookCardProps) {
  const cardRef = useRef<HTMLAnchorElement>(null);

  const handleMouseMove = (e: React.MouseEvent<HTMLAnchorElement>) => {
    const card = cardRef.current;
    if (!card) return;
    const rect = card.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width - 0.5;  // -0.5 to 0.5
    const y = (e.clientY - rect.top) / rect.height - 0.5;
    // Subtle tilt: max 8 degrees
    card.style.transform = `perspective(900px) rotateY(${x * 8}deg) rotateX(${-y * 6}deg) translateY(-10px) scale(1.03)`;
  };

  const handleMouseLeave = () => {
    const card = cardRef.current;
    if (!card) return;
    card.style.transform = "";
    card.style.transition = "transform 0.5s cubic-bezier(0.22, 1, 0.36, 1)";
    setTimeout(() => {
      if (cardRef.current) cardRef.current.style.transition = "";
    }, 500);
  };

  const delayClass = [
    "", "book-enter-1", "book-enter-2", "book-enter-3",
    "book-enter-4", "book-enter-5", "book-enter-6", "book-enter-7", "book-enter-8"
  ][Math.min(enterDelay, 8)];

  return (
    <Link
      ref={cardRef}
      href={`/books/${book.slug}`}
      className={`group block shrink-0 cursor-pointer focus:outline-none book-enter ${delayClass}`}
      style={{ willChange: "transform", transition: "transform 0.18s cubic-bezier(0.22, 1, 0.36, 1)" }}
      draggable={false}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
    >
      <BookCover book={book} size="md" priority={priority} />
    </Link>
  );
}
