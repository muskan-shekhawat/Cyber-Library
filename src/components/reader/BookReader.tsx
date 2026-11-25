"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import {
  ArrowLeft,
  Bookmark,
  CheckCircle,
  Copy,
  Check,
  ChevronLeft,
  ChevronRight,
  ShieldCheck,
  AlertTriangle,
  ExternalLink,
  Terminal,
  Menu,
  X,
} from "lucide-react";
import { Book, Chapter } from "@/types";
import BookCover from "@/components/library/BookCover";

interface BookReaderProps {
  book: Book;
  chapter: Chapter;
}

export default function BookReader({ book, chapter }: BookReaderProps) {
  const [scrollProgress, setScrollProgress] = useState(0);
  const [copiedIndex, setCopiedIndex] = useState<number | null>(null);
  const [isBookmarked, setIsBookmarked] = useState(false);
  const [isCompleted, setIsCompleted] = useState(false);
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const storageKeyBookmark = `null_lib_bookmark_${book.slug}_${chapter.slug}`;
  const storageKeyCompleted = `null_lib_completed_${book.slug}_${chapter.slug}`;

  useEffect(() => {
    const handleScroll = () => {
      const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
      if (totalHeight > 0) {
        const currentProgress = (window.scrollY / totalHeight) * 100;
        setScrollProgress(Math.min(100, Math.max(0, currentProgress)));
      }
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  useEffect(() => {
    try {
      setIsBookmarked(localStorage.getItem(storageKeyBookmark) === "true");
      setIsCompleted(localStorage.getItem(storageKeyCompleted) === "true");
    } catch {}
  }, [storageKeyBookmark, storageKeyCompleted]);

  const toggleBookmark = () => {
    const next = !isBookmarked;
    setIsBookmarked(next);
    try {
      localStorage.setItem(storageKeyBookmark, String(next));
    } catch {}
  };

  const toggleCompleted = () => {
    const next = !isCompleted;
    setIsCompleted(next);
    try {
      localStorage.setItem(storageKeyCompleted, String(next));
    } catch {}
  };

  const handleCopyCode = (code: string, index: number) => {
    navigator.clipboard.writeText(code);
    setCopiedIndex(index);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  const currentChapterIndex = book.chapters.findIndex((c) => c.slug === chapter.slug);
  const prevChapter = currentChapterIndex > 0 ? book.chapters[currentChapterIndex - 1] : null;
  const nextChapter =
    currentChapterIndex < book.chapters.length - 1 ? book.chapters[currentChapterIndex + 1] : null;

  return (
    <div className="w-full min-h-screen bg-white text-[#222222] font-sans">
      {/* Top Progress Line */}
      <div className="fixed top-0 left-0 right-0 h-[2px] bg-[#E8E6E1] z-50">
        <div
          className="h-full bg-[#222222] transition-all duration-150"
          style={{ width: `${scrollProgress}%` }}
        />
      </div>

      {/* Sub-header */}
      <div className="sticky top-14 z-30 bg-white border-b border-[#E8E6E1] px-4 sm:px-8 py-3 flex items-center justify-between text-xs">
        <div className="flex items-center space-x-3">
          <button
            type="button"
            onClick={() => setIsSidebarOpen(!isSidebarOpen)}
            className="lg:hidden p-1 text-[#858585] hover:text-[#222222]"
            aria-label="Toggle chapters navigation"
          >
            {isSidebarOpen ? <X className="w-4 h-4" /> : <Menu className="w-4 h-4" />}
          </button>

          <Link
            href={`/books/${book.slug}`}
            className="flex items-center space-x-1.5 text-[#858585] hover:text-[#222222] font-medium uppercase tracking-[0.12em] transition-colors text-[11px]"
          >
            <ArrowLeft className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">Volume</span>
          </Link>
          <span className="text-[#E8E6E1] hidden sm:inline">/</span>
          <span className="text-[#858585] uppercase tracking-[0.12em] text-[11px] truncate max-w-[200px] sm:max-w-xs">
            {book.title}
          </span>
        </div>

        <div className="flex items-center space-x-2.5">
          <button
            type="button"
            onClick={toggleBookmark}
            className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-[2px] border text-[11px] uppercase tracking-wider transition-colors cursor-pointer ${
              isBookmarked
                ? "bg-[#222222] text-white border-[#222222]"
                : "bg-white text-[#858585] border-[#E8E6E1] hover:text-[#222222]"
            }`}
          >
            <Bookmark className="w-3 h-3" />
            <span className="hidden sm:inline">{isBookmarked ? "Bookmarked" : "Bookmark"}</span>
          </button>

          <button
            type="button"
            onClick={toggleCompleted}
            className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-[2px] border text-[11px] uppercase tracking-wider transition-colors cursor-pointer ${
              isCompleted
                ? "bg-[#222222] text-white border-[#222222]"
                : "bg-white text-[#858585] border-[#E8E6E1] hover:text-[#222222]"
            }`}
          >
            <CheckCircle className="w-3 h-3" />
            <span className="hidden sm:inline">{isCompleted ? "Completed" : "Mark Complete"}</span>
          </button>
        </div>
      </div>

      {/* 3-Column Editorial Reader */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
        {/* Left Sidebar */}
        <aside
          className={`lg:col-span-3 fixed lg:sticky top-28 left-0 z-20 w-72 lg:w-full h-[calc(100vh-7rem)] bg-white lg:bg-transparent border-r lg:border-r-0 border-[#E8E6E1] p-5 lg:p-0 overflow-y-auto no-scrollbar transition-transform lg:translate-x-0 ${
            isSidebarOpen ? "translate-x-0 shadow-xl" : "-translate-x-full lg:translate-x-0"
          }`}
        >
          <div className="p-3 bg-[#F8F7F4] border border-[#E8E6E1] rounded-[2px] mb-6 flex items-center space-x-3">
            <div className="w-11 shrink-0">
              <BookCover book={book} size="sm" showOverlay={false} />
            </div>
            <div className="min-w-0">
              <span className="text-[10px] uppercase tracking-[0.14em] text-[#858585] block">
                {book.volumeNumber}
              </span>
              <h4 className="text-xs font-semibold truncate text-[#222222]">
                {book.title}
              </h4>
            </div>
          </div>

          <div className="text-[10px] font-semibold uppercase tracking-[0.16em] text-[#858585] mb-3">
            Chapters
          </div>

          <nav className="space-y-1">
            {book.chapters.map((ch) => {
              const isActive = ch.slug === chapter.slug;
              return (
                <Link
                  key={ch.slug}
                  href={`/books/${book.slug}/${ch.slug}`}
                  onClick={() => setIsSidebarOpen(false)}
                  className={`block px-3 py-2 rounded-[2px] text-xs transition-colors ${
                    isActive
                      ? "bg-[#222222] text-white font-medium"
                      : "text-[#222222]/80 hover:bg-[#F8F7F4] hover:text-black"
                  }`}
                >
                  <div className="flex items-center space-x-2.5">
                    <span className="tabular-nums opacity-60 text-[11px]">
                      {String(ch.chapterNumber).padStart(2, "0")}
                    </span>
                    <span className="truncate">{ch.title}</span>
                  </div>
                </Link>
              );
            })}
          </nav>
        </aside>

        {/* Center Content */}
        <article className="lg:col-span-6 min-w-0 pb-16">
          <header className="mb-10 pb-6 border-b border-[#E8E6E1]">
            <div className="text-[11px] uppercase tracking-[0.16em] text-[#858585]">
              Chapter {chapter.chapterNumber} · {book.category}
            </div>
            <h1 className="text-2xl sm:text-3xl font-semibold tracking-[-0.02em] text-[#222222] mt-3 leading-tight">
              {chapter.title}
            </h1>
            <p className="text-sm text-[#858585] mt-2 leading-relaxed">
              {chapter.summary}
            </p>
          </header>

          <section id="introduction" className="mb-10">
            <h2 className="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#858585] mb-3">
              01 · Introduction
            </h2>
            <p className="text-sm text-[#222222] leading-relaxed">{chapter.introduction}</p>
          </section>

          <section id="detailed-explanation" className="mb-10">
            <h2 className="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#858585] mb-3">
              02 · Technical Breakdown
            </h2>
            <p className="text-sm text-[#222222] leading-relaxed">
              {chapter.detailedExplanation}
            </p>
          </section>

          <section id="key-concepts" className="mb-10">
            <h2 className="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#858585] mb-4">
              03 · Key Concepts
            </h2>
            <div className="space-y-3">
              {chapter.keyConcepts.map((concept, idx) => (
                <div
                  key={idx}
                  className="p-4 bg-[#F8F7F4] border border-[#E8E6E1] rounded-[2px]"
                >
                  <span className="text-xs font-semibold text-[#222222] block">
                    {concept.term}
                  </span>
                  <span className="text-xs text-[#858585] mt-1 block leading-relaxed">
                    {concept.definition}
                  </span>
                </div>
              ))}
            </div>
          </section>

          <section id="code-implementation" className="mb-10">
            <h2 className="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#858585] mb-4">
              04 · Commands & Examples
            </h2>
            <div className="space-y-5">
              {chapter.commandsOrCode.map((block, idx) => (
                <div
                  key={idx}
                  className="border border-[#E8E6E1] rounded-[2px] overflow-hidden bg-white"
                >
                  <div className="px-4 py-2.5 bg-[#F8F7F4] border-b border-[#E8E6E1] flex items-center justify-between text-xs">
                    <div className="flex items-center space-x-2 text-[#222222] font-medium">
                      <Terminal className="w-3.5 h-3.5 text-[#858585]" />
                      <span>{block.title}</span>
                    </div>
                    <button
                      type="button"
                      onClick={() => handleCopyCode(block.code, idx)}
                      className="flex items-center space-x-1 text-[#858585] hover:text-[#222222] transition-colors cursor-pointer"
                    >
                      {copiedIndex === idx ? (
                        <>
                          <Check className="w-3.5 h-3.5 text-[#222222]" />
                          <span className="text-[11px] text-[#222222]">Copied</span>
                        </>
                      ) : (
                        <>
                          <Copy className="w-3.5 h-3.5" />
                          <span className="text-[11px]">Copy</span>
                        </>
                      )}
                    </button>
                  </div>

                  <pre className="p-4 bg-[#F8F7F4]/40 text-[#222222] text-xs overflow-x-auto leading-relaxed font-sans">
                    <code>{block.code}</code>
                  </pre>

                  <div className="px-4 py-2.5 bg-white border-t border-[#E8E6E1] text-xs text-[#858585]">
                    {block.explanation}
                  </div>
                </div>
              ))}
            </div>
          </section>

          <section id="practical-exercise" className="mb-10">
            <h2 className="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#858585] mb-4">
              05 · Practical Lab Exercise
            </h2>
            <div className="border border-[#E8E6E1] rounded-[2px] p-5 bg-[#F8F7F4]">
              <div className="text-xs font-semibold text-[#222222] mb-2 flex items-center space-x-2">
                <ShieldCheck className="w-4 h-4 text-[#B5A184]" />
                <span>{chapter.practicalExercise.title}</span>
              </div>
              <p className="text-xs text-[#858585] leading-relaxed mb-4">
                {chapter.practicalExercise.scenario}
              </p>

              <ol className="list-decimal list-inside space-y-2 text-xs text-[#222222] mb-4 leading-relaxed">
                {chapter.practicalExercise.steps.map((step, sIdx) => (
                  <li key={sIdx}>{step}</li>
                ))}
              </ol>

              <div className="text-xs text-[#222222] bg-white p-3 border border-[#E8E6E1] rounded-[2px]">
                <span className="text-[#858585] font-medium">Expected Outcome: </span>
                {chapter.practicalExercise.expectedOutcome}
              </div>
            </div>
          </section>

          <section id="best-practices" className="mb-10 grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div className="p-4 border border-[#E8E6E1] rounded-[2px] bg-white">
              <div className="flex items-center space-x-1.5 text-[11px] font-semibold text-[#222222] uppercase tracking-wider mb-3">
                <AlertTriangle className="w-3.5 h-3.5 text-[#858585]" />
                <span>Common Mistakes</span>
              </div>
              <ul className="space-y-2 text-xs text-[#858585] leading-relaxed list-disc list-inside">
                {chapter.commonMistakes.map((mistake, mIdx) => (
                  <li key={mIdx}>{mistake}</li>
                ))}
              </ul>
            </div>

            <div className="p-4 border border-[#E8E6E1] rounded-[2px] bg-white">
              <div className="flex items-center space-x-1.5 text-[11px] font-semibold text-[#222222] uppercase tracking-wider mb-3">
                <ShieldCheck className="w-3.5 h-3.5 text-[#B5A184]" />
                <span>Security Best Practices</span>
              </div>
              <ul className="space-y-2 text-xs text-[#858585] leading-relaxed list-disc list-inside">
                {chapter.bestPractices.map((bp, bIdx) => (
                  <li key={bIdx}>{bp}</li>
                ))}
              </ul>
            </div>
          </section>

          <section id="references" className="mb-12 pt-6 border-t border-[#E8E6E1]">
            <h2 className="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#858585] mb-3">
              06 · References
            </h2>
            <div className="space-y-2">
              {chapter.references.map((ref, rIdx) => (
                <a
                  key={rIdx}
                  href={ref.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center justify-between p-3 bg-[#F8F7F4] hover:bg-white border border-[#E8E6E1] rounded-[2px] text-xs text-[#222222] transition-colors"
                >
                  <span className="truncate">{ref.title}</span>
                  <ExternalLink className="w-3.5 h-3.5 text-[#858585] shrink-0 ml-2" />
                </a>
              ))}
            </div>
          </section>

          {/* Bottom Pagination */}
          <div className="pt-8 border-t border-[#E8E6E1] flex items-center justify-between gap-4">
            {prevChapter ? (
              <Link
                href={`/books/${book.slug}/${prevChapter.slug}`}
                className="flex items-center space-x-2 text-xs font-medium text-[#222222] hover:opacity-70 transition-opacity"
              >
                <ChevronLeft className="w-4 h-4" />
                <div>
                  <span className="text-[10px] text-[#858585] uppercase tracking-wider block">
                    Previous
                  </span>
                  <span className="truncate max-w-[160px] sm:max-w-xs block">
                    {prevChapter.title}
                  </span>
                </div>
              </Link>
            ) : (
              <div />
            )}

            {nextChapter && (
              <Link
                href={`/books/${book.slug}/${nextChapter.slug}`}
                className="flex items-center space-x-2 text-xs font-medium text-[#222222] hover:opacity-70 transition-opacity text-right"
              >
                <div>
                  <span className="text-[10px] text-[#858585] uppercase tracking-wider block">
                    Next
                  </span>
                  <span className="truncate max-w-[160px] sm:max-w-xs block">
                    {nextChapter.title}
                  </span>
                </div>
                <ChevronRight className="w-4 h-4" />
              </Link>
            )}
          </div>
        </article>

        {/* Right Column: On This Page */}
        <aside className="hidden lg:block lg:col-span-3 sticky top-28 space-y-4">
          <div className="p-4 border border-[#E8E6E1] rounded-[2px] bg-[#F8F7F4]">
            <span className="text-[10px] font-semibold uppercase tracking-[0.16em] text-[#858585] block mb-3">
              On This Page
            </span>
            <ul className="space-y-2 text-xs text-[#858585]">
              <li>
                <a href="#introduction" className="hover:text-[#222222] transition-colors block">
                  01 · Introduction
                </a>
              </li>
              <li>
                <a href="#detailed-explanation" className="hover:text-[#222222] transition-colors block">
                  02 · Technical Breakdown
                </a>
              </li>
              <li>
                <a href="#key-concepts" className="hover:text-[#222222] transition-colors block">
                  03 · Key Concepts
                </a>
              </li>
              <li>
                <a href="#code-implementation" className="hover:text-[#222222] transition-colors block">
                  04 · Commands & Examples
                </a>
              </li>
              <li>
                <a href="#practical-exercise" className="hover:text-[#222222] transition-colors block">
                  05 · Practical Lab
                </a>
              </li>
              <li>
                <a href="#best-practices" className="hover:text-[#222222] transition-colors block">
                  06 · Best Practices
                </a>
              </li>
              <li>
                <a href="#references" className="hover:text-[#222222] transition-colors block">
                  07 · References
                </a>
              </li>
            </ul>
          </div>

          <div className="p-4 border border-[#E8E6E1] rounded-[2px] bg-white text-xs text-[#858585]">
            <span className="uppercase text-[10px] tracking-[0.14em] block mb-1">Progress</span>
            <span className="text-base font-semibold text-[#222222] tabular-nums">
              {Math.round(scrollProgress)}%
            </span>
          </div>
        </aside>
      </div>
    </div>
  );
}
