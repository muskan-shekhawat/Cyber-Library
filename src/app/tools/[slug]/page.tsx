import React from "react";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, ExternalLink, Terminal } from "lucide-react";
import { ALL_TOOLS, getToolBySlug } from "@/data/tools";
import { getBookBySlug } from "@/data/books";
import HorizontalScroller from "@/components/library/HorizontalScroller";

interface Props {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return ALL_TOOLS.map((tool) => ({
    slug: tool.slug,
  }));
}

export default async function ToolDetailPage({ params }: Props) {
  const { slug } = await params;
  const tool = getToolBySlug(slug);

  if (!tool) {
    notFound();
  }

  const relatedBooks = tool.relatedBookSlugs
    .map((s) => getBookBySlug(s))
    .filter((b): b is NonNullable<typeof b> => b !== undefined);

  return (
    <div className="w-full pb-24">
      <div className="max-w-6xl mx-auto px-6 sm:px-10 pt-8 pb-4">
        <Link
          href="/tools"
          className="inline-flex items-center space-x-2 text-[11px] text-[#858585] hover:text-[#222222] transition-colors uppercase tracking-[0.16em]"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Back to Tools</span>
        </Link>
      </div>

      <section className="max-w-6xl mx-auto px-6 sm:px-10 pt-4 pb-12 border-b border-[#E8E6E1]">
        <div className="flex flex-col md:flex-row md:items-start justify-between gap-6">
          <div className="max-w-2xl">
            <div className="text-[11px] uppercase tracking-[0.16em] text-[#858585]">
              {tool.category}
            </div>
            <h1 className="text-3xl font-semibold tracking-[-0.02em] text-[#222222] mt-2">
              {tool.name}
            </h1>
            <p className="text-sm text-[#858585] mt-3 leading-relaxed">
              {tool.purpose}
            </p>
          </div>

          <div className="flex flex-wrap gap-2 shrink-0">
            <a
              href={tool.officialWebsite}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center space-x-2 px-4 py-2 bg-white border border-[#E8E6E1] hover:border-[#222222] rounded-[2px] text-[11px] font-medium text-[#222222] uppercase tracking-[0.14em] transition-colors"
            >
              <span>Website</span>
              <ExternalLink className="w-3 h-3 text-[#858585]" />
            </a>

            <a
              href={tool.officialDocs}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center space-x-2 px-4 py-2 bg-[#222222] text-white hover:bg-black rounded-[2px] text-[11px] font-medium uppercase tracking-[0.14em] transition-colors"
            >
              <span>Documentation</span>
              <ExternalLink className="w-3 h-3 text-white/80" />
            </a>
          </div>
        </div>

        <div className="mt-8 p-4 bg-white border border-[#E8E6E1] rounded-[2px]">
          <span className="text-[10px] uppercase tracking-[0.16em] text-[#858585] block mb-1">
            Usage
          </span>
          <code className="text-xs font-medium text-[#222222] font-sans">
            {tool.basicUsage}
          </code>
        </div>
      </section>

      <section className="max-w-6xl mx-auto px-6 sm:px-10 py-10 border-b border-[#E8E6E1]">
        <h2 className="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#858585] mb-5">
          Installation
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {tool.installation.linux && (
            <div className="p-4 bg-white border border-[#E8E6E1] rounded-[2px]">
              <span className="text-xs font-semibold text-[#222222] block mb-2">
                Linux
              </span>
              <pre className="p-3 bg-[#F8F7F4] text-[#222222] text-xs rounded-[2px] overflow-x-auto font-sans">
                <code>{tool.installation.linux}</code>
              </pre>
            </div>
          )}

          {tool.installation.macos && (
            <div className="p-4 bg-white border border-[#E8E6E1] rounded-[2px]">
              <span className="text-xs font-semibold text-[#222222] block mb-2">
                macOS
              </span>
              <pre className="p-3 bg-[#F8F7F4] text-[#222222] text-xs rounded-[2px] overflow-x-auto font-sans">
                <code>{tool.installation.macos}</code>
              </pre>
            </div>
          )}

          {tool.installation.windows && (
            <div className="p-4 bg-white border border-[#E8E6E1] rounded-[2px]">
              <span className="text-xs font-semibold text-[#222222] block mb-2">
                Windows
              </span>
              <pre className="p-3 bg-[#F8F7F4] text-[#222222] text-xs rounded-[2px] overflow-x-auto font-sans">
                <code>{tool.installation.windows}</code>
              </pre>
            </div>
          )}
        </div>
      </section>

      <section className="max-w-6xl mx-auto px-6 sm:px-10 py-10 border-b border-[#E8E6E1]">
        <h2 className="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#858585] mb-5">
          Practical Examples
        </h2>
        <div className="space-y-5">
          {tool.safeExamples.map((ex, i) => (
            <div key={i} className="border border-[#E8E6E1] rounded-[2px] bg-white overflow-hidden">
              <div className="px-4 py-2.5 bg-[#F8F7F4] border-b border-[#E8E6E1] flex items-center space-x-2 text-xs font-medium text-[#222222]">
                <Terminal className="w-3.5 h-3.5 text-[#858585]" />
                <span>{ex.title}</span>
              </div>
              <div className="p-4">
                <p className="text-xs text-[#858585] mb-3 leading-relaxed">
                  {ex.description}
                </p>
                <pre className="p-3 bg-[#F8F7F4] text-[#222222] text-xs rounded-[2px] overflow-x-auto font-sans">
                  <code>{ex.command}</code>
                </pre>
                {ex.expectedOutput && (
                  <pre className="mt-3 p-3 bg-white border border-[#E8E6E1] text-[#858585] text-[11px] rounded-[2px] overflow-x-auto font-sans">
                    <code>{ex.expectedOutput}</code>
                  </pre>
                )}
              </div>
            </div>
          ))}
        </div>
      </section>

      {relatedBooks.length > 0 && (
        <section className="pt-12">
          <div className="max-w-6xl mx-auto px-6 sm:px-10 mb-2">
            <h2 className="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#858585]">
              Related Volumes
            </h2>
          </div>
          <HorizontalScroller books={relatedBooks} rowId={`tool-${tool.slug}`} />
        </section>
      )}
    </div>
  );
}
