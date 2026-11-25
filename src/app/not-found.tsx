import Link from "next/link";

export default function NotFound() {
  return (
    <div className="min-h-[70vh] flex flex-col items-center justify-center px-4 text-center">
      <p className="text-xs font-mono tracking-[0.25em] text-[#D95A2B] uppercase mb-2">
        NULL / 404
      </p>
      <h2 className="text-3xl sm:text-4xl font-serif font-bold text-[#1C1C1C] mb-4">
        Volume Not Found
      </h2>
      <p className="text-sm text-[#77736E] max-w-md mb-8">
        The requested cybersecurity volume, monograph, or chapter does not exist in the NULL / LIBRARY catalog.
      </p>
      <Link
        href="/"
        className="px-6 py-2.5 rounded-full bg-[#1C1C1C] text-white text-xs font-mono uppercase tracking-wider hover:bg-[#2455FF] transition-colors"
      >
        Return to Bookshelf
      </Link>
    </div>
  );
}
