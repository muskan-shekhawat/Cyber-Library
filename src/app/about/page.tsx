import React from "react";
import Link from "next/link";
import { ArrowRight } from "lucide-react";

export default function AboutPage() {
  const audiences = [
    "Cybersecurity students",
    "Ethical hacking learners",
    "Network engineers",
    "Linux enthusiasts",
    "Security researchers",
    "Beginners exploring information security",
  ];

  return (
    <div className="w-full pb-24">
      <div className="max-w-3xl mx-auto px-6 sm:px-10 pt-14 sm:pt-20 pb-12 border-b border-[#E8E6E1]">
        <div className="text-[11px] uppercase tracking-[0.18em] text-[#858585] mb-4">
          About NULL / LIBRARY
        </div>
        <h1 className="text-3xl sm:text-4xl font-semibold tracking-[-0.02em] text-[#222222] uppercase leading-[1.15]">
          Knowledge for the Digital World.
        </h1>
        <p className="text-sm sm:text-base text-[#858585] leading-relaxed mt-6">
          NULL / LIBRARY is a curated cybersecurity digital library combining editorial book design with structured, hands-on technical curricula across networking, Linux, ethical hacking, web security, and digital forensics.
        </p>
      </div>

      <section className="max-w-3xl mx-auto px-6 sm:px-10 py-12 border-b border-[#E8E6E1]">
        <div className="text-[11px] font-semibold uppercase tracking-[0.18em] text-[#858585] mb-6">
          Intended For
        </div>

        <ul className="grid grid-cols-1 sm:grid-cols-2 gap-y-3 gap-x-8 text-sm text-[#222222]">
          {audiences.map((aud) => (
            <li key={aud} className="py-2 border-b border-[#E8E6E1]/70">
              {aud}
            </li>
          ))}
        </ul>
      </section>

      <section className="max-w-3xl mx-auto px-6 sm:px-10 pt-12">
        <Link
          href="/"
          className="inline-flex items-center space-x-2 bg-[#222222] text-white hover:bg-black px-6 py-3 rounded-[2px] text-[11px] font-medium tracking-[0.16em] uppercase transition-colors"
        >
          <span>Browse Collection</span>
          <ArrowRight className="w-3.5 h-3.5" />
        </Link>
      </section>
    </div>
  );
}
