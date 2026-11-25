"use client";

import React, { useState } from "react";
import Link from "next/link";
import { Search, ArrowRight } from "lucide-react";
import { ALL_TOOLS } from "@/data/tools";

const CATEGORIES = [
  "All",
  "Networking",
  "Kali Linux",
  "Linux",
  "OSINT",
  "Digital Forensics",
  "Malware Analysis",
  "SOC",
  "Python",
] as const;

export default function ToolsPage() {
  const [selectedCategory, setSelectedCategory] = useState<string>("All");
  const [searchQuery, setSearchQuery] = useState("");

  const filteredTools = ALL_TOOLS.filter((tool) => {
    const matchesCategory =
      selectedCategory === "All" ||
      tool.category.toLowerCase() === selectedCategory.toLowerCase();
    const matchesQuery =
      !searchQuery.trim() ||
      tool.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      tool.purpose.toLowerCase().includes(searchQuery.toLowerCase()) ||
      tool.category.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesQuery;
  });

  return (
    <div className="w-full pb-24">
      <div className="max-w-7xl mx-auto px-6 sm:px-10 pt-10 sm:pt-14 pb-8 border-b border-[#E8E6E1]">
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-6">
          <div>
            <h1 className="text-xs font-semibold tracking-[0.22em] text-[#222222] uppercase">
              Cybersecurity Tools
            </h1>
            <p className="text-xs text-[#858585] tracking-[0.14em] uppercase mt-1.5">
              Diagnostics, scanners & analysis utilities
            </p>
          </div>

          <div className="relative w-full md:w-64">
            <Search className="w-3.5 h-3.5 text-[#858585] absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Filter tools..."
              className="w-full pl-9 pr-3 py-2 bg-white border border-[#E8E6E1] text-xs text-[#222222] placeholder-[#858585] rounded-[2px] focus:outline-none focus:border-[#222222]"
            />
          </div>
        </div>

        <div className="flex items-center space-x-5 overflow-x-auto no-scrollbar pt-6 text-[11px] uppercase tracking-[0.14em]">
          {CATEGORIES.map((cat) => {
            const isActive = selectedCategory === cat;
            return (
              <button
                key={cat}
                type="button"
                onClick={() => setSelectedCategory(cat)}
                className={`shrink-0 transition-colors cursor-pointer ${
                  isActive
                    ? "text-[#222222] font-semibold"
                    : "text-[#858585] hover:text-[#222222]"
                }`}
              >
                {cat}
              </button>
            );
          })}
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-6 sm:px-10 py-10">
        {filteredTools.length === 0 ? (
          <div className="py-16 text-center text-xs text-[#858585]">
            No tools match your filter.
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredTools.map((tool) => (
              <Link
                key={tool.slug}
                href={`/tools/${tool.slug}`}
                className="group p-6 bg-white border border-[#E8E6E1] hover:border-[#222222] rounded-[2px] transition-colors flex flex-col justify-between"
              >
                <div>
                  <div className="text-[10px] text-[#858585] uppercase tracking-[0.16em] mb-2">
                    {tool.category}
                  </div>
                  <h2 className="text-base font-semibold text-[#222222] tracking-tight">
                    {tool.name}
                  </h2>
                  <p className="text-xs text-[#858585] mt-2 line-clamp-3 leading-relaxed">
                    {tool.purpose}
                  </p>
                </div>

                <div className="mt-6 pt-3 border-t border-[#E8E6E1]/70 flex items-center justify-between text-[11px]">
                  <span className="text-[#858585] truncate max-w-[200px]">
                    {tool.basicUsage}
                  </span>
                  <ArrowRight className="w-3.5 h-3.5 text-[#858585] group-hover:text-[#222222] group-hover:translate-x-0.5 transition-all shrink-0" />
                </div>
              </Link>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
