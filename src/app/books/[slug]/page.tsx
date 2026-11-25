import React from "react";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, Check, ChevronRight } from "lucide-react";
import { ALL_BOOKS, getBookBySlug } from "@/data/books";
import BookCover from "@/components/library/BookCover";
import HorizontalScroller from "@/components/library/HorizontalScroller";

interface Props {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return ALL_BOOKS.map((book) => ({
    slug: book.slug,
  }));
}

export default async function BookDetailPage({ params }: Props) {
  const { slug } = await params;
  const book = getBookBySlug(slug);

  if (!book) {
    notFound();
  }

  const relatedBooks = book.relatedBookSlugs
    .map((s) => getBookBySlug(s))
    .filter((b): b is NonNullable<typeof b> => b !== undefined);

  const firstChapterSlug = book.chapters[0]?.slug || "";

  return (
    <div className="w-full pb-24">
      {/* Quiet Top Breadcrumb */}
      <div className="max-w-6xl mx-auto px-6 sm:px-10 pt-8 pb-4">
        <Link
          href="/"
          className="inline-flex items-center space-x-2 text-[11px] text-[#858585] hover:text-[#222222] transition-colors uppercase tracking-[0.16em]"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Back to Library</span>
        </Link>
      </div>

      {/* Main Editorial Hero */}
      <section className="max-w-6xl mx-auto px-6 sm:px-10 pt-6 pb-16 border-b border-[#E8E6E1]">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">
          {/* Left: Clean Large Book Cover */}
          <div className="lg:col-span-5 flex justify-center lg:justify-start">
            <div className="group">
              <BookCover book={book} size="lg" priority />
            </div>
          </div>

          {/* Right: Editorial Book Details */}
          <div className="lg:col-span-7">
            <div className="flex items-center space-x-3 text-[11px] uppercase tracking-[0.16em] text-[#858585]">
              <span>{book.category}</span>
              <span>·</span>
              <span>{book.difficulty}</span>
              <span>·</span>
              <span>{book.chaptersCount} Chapters</span>
              <span>·</span>
              <span>{book.estimatedHours} Hours</span>
            </div>

            <h1 className="text-3xl sm:text-4xl font-semibold tracking-[-0.02em] text-[#222222] mt-4 leading-[1.12]">
              {book.title}
            </h1>

            <p className="text-sm sm:text-base text-[#858585] mt-3 leading-relaxed max-w-xl">
              {book.shortDescription}
            </p>

            {/* Primary Actions */}
            <div className="flex flex-wrap items-center gap-3 mt-8">
              <Link
                href={`/books/${book.slug}/${firstChapterSlug}`}
                className="inline-flex items-center justify-center bg-[#222222] text-white hover:bg-black px-6 py-3 rounded-[2px] text-[11px] font-medium tracking-[0.16em] uppercase transition-colors"
              >
                Read Book
              </Link>

              <a
                href="#chapters"
                className="inline-flex items-center justify-center bg-white text-[#222222] border border-[#E8E6E1] hover:border-[#222222] px-6 py-3 rounded-[2px] text-[11px] font-medium tracking-[0.16em] uppercase transition-colors"
              >
                Explore Chapters
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Learning Objectives & Tools */}
      <section className="max-w-6xl mx-auto px-6 sm:px-10 py-14 border-b border-[#E8E6E1]">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12">
          <div className="lg:col-span-7">
            <h2 className="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#858585] mb-5">
              Learning Objectives
            </h2>
            <ul className="space-y-3">
              {book.learningObjectives.map((obj, i) => (
                <li key={i} className="flex items-start space-x-3 text-sm text-[#222222]">
                  <Check className="w-4 h-4 text-[#B5A184] shrink-0 mt-0.5" />
                  <span className="leading-relaxed">{obj}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="lg:col-span-5">
            <h2 className="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#858585] mb-5">
              Tools Covered
            </h2>
            <div className="flex flex-wrap gap-2">
              {book.toolsCovered.map((tool) => (
                <Link
                  key={tool}
                  href="/tools"
                  className="px-3 py-1.5 bg-white border border-[#E8E6E1] hover:border-[#222222] rounded-[2px] text-xs text-[#222222] transition-colors"
                >
                  {tool}
                </Link>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Chapter Index */}
      <section id="chapters" className="max-w-6xl mx-auto px-6 sm:px-10 py-14 border-b border-[#E8E6E1]">
        <h2 className="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#858585] mb-6">
          Chapters ({book.chapters.length})
        </h2>

        <div className="divide-y divide-[#E8E6E1] border-t border-b border-[#E8E6E1]">
          {book.chapters.map((ch) => (
            <Link
              key={ch.slug}
              href={`/books/${book.slug}/${ch.slug}`}
              className="py-4 flex items-center justify-between gap-4 hover:bg-white/60 px-2 transition-colors group"
            >
              <div className="flex items-baseline space-x-4 min-w-0">
                <span className="text-xs text-[#858585] tabular-nums shrink-0">
                  {String(ch.chapterNumber).padStart(2, "0")}
                </span>
                <div className="min-w-0">
                  <h3 className="text-sm font-medium text-[#222222] group-hover:text-black truncate">
                    {ch.title}
                  </h3>
                  <p className="text-xs text-[#858585] mt-0.5 truncate">
                    {ch.summary}
                  </p>
                </div>
              </div>

              <ChevronRight className="w-4 h-4 text-[#858585] group-hover:text-[#222222] group-hover:translate-x-0.5 transition-all shrink-0" />
            </Link>
          ))}
        </div>
      </section>

      {/* Related Volumes */}
      {relatedBooks.length > 0 && (
        <section className="pt-14">
          <div className="max-w-6xl mx-auto px-6 sm:px-10 mb-2">
            <h2 className="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#858585]">
              Related Volumes
            </h2>
          </div>
          <HorizontalScroller books={relatedBooks} rowId={`related-${book.slug}`} />
        </section>
      )}
    </div>
  );
}
