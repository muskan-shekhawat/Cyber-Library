import type { Metadata } from "next";
import Navbar from "@/components/navigation/Navbar";
import "./globals.css";

export const metadata: Metadata = {
  title: "NULL / LIBRARY — Premium Cybersecurity Digital Library",
  description: "A physical-feel interactive 3D cybersecurity digital library and bookstore of 24 foundational textbooks and reference guides.",
  icons: {
    icon: "/favicon.ico",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="h-full antialiased">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Space+Grotesk:wght@500;600;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="min-h-full flex flex-col bg-[#F7F6F2] text-[#1C1C1C] selection:bg-[#E4E1DA]">
        <Navbar />
        <main className="flex-1 w-full">
          {children}
        </main>
      </body>
    </html>
  );
}
