import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "#F7F6F2",
        surface: "#FFFFFF",
        primary: "#1C1C1C",
        secondary: "#77736E",
        border: "#E4E1DA",
        accent: "#2455FF",
        "accent-gold": "#B5A184",
      },
      fontFamily: {
        sans: ["Montserrat", "-apple-system", "BlinkMacSystemFont", "Segoe UI", "Roboto", "sans-serif"],
        serif: ["'Cormorant Garamond'", "Georgia", "serif"],
        display: ["'Space Grotesk'", "sans-serif"],
      },
      boxShadow: {
        'shelf-contact': '0 12px 24px -6px rgba(0, 0, 0, 0.12), 0 4px 8px -2px rgba(0, 0, 0, 0.08)',
        'book-active': '0 20px 48px -10px rgba(0, 0, 0, 0.22), 0 8px 16px -4px rgba(0, 0, 0, 0.10)',
        'spine-lift': '0 14px 28px -4px rgba(0, 0, 0, 0.18)',
      }
    },
  },
  plugins: [],
};
export default config;
