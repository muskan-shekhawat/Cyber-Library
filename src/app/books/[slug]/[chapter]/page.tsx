import React from "react";
import { notFound } from "next/navigation";
import { ALL_BOOKS, getChapterBySlug } from "@/data/books";
import BookReader from "@/components/reader/BookReader";

interface Props {
  params: Promise<{
    slug: string;
    chapter: string;
  }>;
}

export async function generateStaticParams() {
  const params: { slug: string; chapter: string }[] = [];
  for (const book of ALL_BOOKS) {
    for (const ch of book.chapters) {
      params.push({
        slug: book.slug,
        chapter: ch.slug,
      });
    }
  }
  return params;
}

export default async function ChapterPage({ params }: Props) {
  const { slug, chapter: chapterSlug } = await params;
  const result = getChapterBySlug(slug, chapterSlug);

  if (!result) {
    notFound();
  }

  const { book, chapter } = result;

  return <BookReader book={book} chapter={chapter} />;
}
