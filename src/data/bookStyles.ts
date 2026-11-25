export interface BookVisualProfile {
  slug: string;
  volumeNumber: string;
  height: number;
  thickness: number;
  coverWidth: number;
  spineColor: string;    // base color of the hardcover cloth
  spineGradient: string; // realistic cylindrical lighting
  foilColor: string;     // embossed foil color
  textColor: string;     // spine text color
  author: string;
  rating: string;
  badge?: string;
  theme: "yellow" | "blue" | "green" | "burgundy" | "navy" | "orange" | "purple" | "teal" | "charcoal" | "cream" | "pink";
}

export const BOOK_STYLES: Record<string, BookVisualProfile> = {
  // ── ROW 1 ──
  "computer-networking": {
    slug: "computer-networking",
    volumeNumber: "VOL. 01",
    height: 366,
    thickness: 62,
    coverWidth: 272,
    spineColor: "#EEE1D1", // Cream
    spineGradient: "linear-gradient(180deg, #E0D3C3 0%, #EEE1D1 50%, #D4C7B7 100%)",
    foilColor: "#C2410C", // Orange
    textColor: "#1C1C1C",
    author: "Andrew S. Tanenbaum & Nick Feamster",
    rating: "4.9",
    badge: "FOUNDATION",
    theme: "cream",
  },
  "advanced-networking": {
    slug: "advanced-networking",
    volumeNumber: "VOL. 02",
    height: 380,
    thickness: 66,
    coverWidth: 283,
    spineColor: "#152F62", // Deep Royal Blue
    spineGradient: "linear-gradient(180deg, #0D2045 0%, #152F62 50%, #0A1733 100%)",
    foilColor: "#E0E7FF",
    textColor: "#FFFFFF",
    author: "David Wetherall & Radia Perlman",
    rating: "5.0",
    badge: "INFRASTRUCTURE",
    theme: "blue",
  },
  "linux-fundamentals": {
    slug: "linux-fundamentals",
    volumeNumber: "VOL. 03",
    height: 344,
    thickness: 58,
    coverWidth: 256,
    spineColor: "#F2E2D2", // Warm Cream
    spineGradient: "linear-gradient(180deg, #E5D5C5 0%, #F2E2D2 50%, #D9C9B9 100%)",
    foilColor: "#CA8A04", // Yellow/Gold
    textColor: "#1C1C1C",
    author: "Dan Nanni",
    rating: "4.9",
    badge: "ESSENTIAL",
    theme: "cream",
  },
  "kali-linux": {
    slug: "kali-linux",
    volumeNumber: "VOL. 04",
    height: 372,
    thickness: 62,
    coverWidth: 277,
    spineColor: "#151412", // Obsidian Black
    spineGradient: "linear-gradient(180deg, #0A0A09 0%, #151412 50%, #050505 100%)",
    foilColor: "#EF4444", // Silver
    textColor: "#FFFFFF",
    author: "Offensive Security Team",
    rating: "4.9",
    badge: "OFFSEC",
    theme: "charcoal",
  },
  "linux-administration": {
    slug: "linux-administration",
    volumeNumber: "VOL. 05",
    height: 384,
    thickness: 66,
    coverWidth: 286,
    spineColor: "#053328", // Dark Forest Green
    spineGradient: "linear-gradient(180deg, #03211A 0%, #053328 50%, #021712 100%)",
    foilColor: "#FDE047", // Gold
    textColor: "#FFFFFF",
    author: "Evi Nemeth & Garth Snyder",
    rating: "5.0",
    badge: "HANDBOOK 5TH ED",
    theme: "green",
  },
  "ethical-hacking": {
    slug: "ethical-hacking",
    volumeNumber: "VOL. 06",
    height: 360,
    thickness: 62,
    coverWidth: 268,
    spineColor: "#EFE2D2", // Cream
    spineGradient: "linear-gradient(180deg, #E2D5C5 0%, #EFE2D2 50%, #D5C8B8 100%)",
    foilColor: "#991B1B", // Red
    textColor: "#1C1C1C",
    author: "Michael T. Simpson & Kent Backman",
    rating: "4.9",
    badge: "ASSESSMENT",
    theme: "cream",
  },

  // ── ROW 2 ──
  "web-security": {
    slug: "web-security",
    volumeNumber: "VOL. 07",
    height: 368,
    thickness: 62,
    coverWidth: 274,
    spineColor: "#2F163E", // Deep Purple
    spineGradient: "linear-gradient(180deg, #1F0D2B 0%, #2F163E 50%, #160820 100%)",
    foilColor: "#C084FC",
    textColor: "#FFFFFF",
    author: "Andrew Hoffman",
    rating: "4.9",
    badge: "APP SEC",
    theme: "purple",
  },
  "digital-forensics": {
    slug: "digital-forensics",
    volumeNumber: "VOL. 15",
    height: 374,
    thickness: 62,
    coverWidth: 278,
    spineColor: "#F8E6D2", // Oatmeal Cream
    spineGradient: "linear-gradient(180deg, #E9D7C3 0%, #F8E6D2 50%, #DCCAB6 100%)",
    foilColor: "#EA580C",
    textColor: "#1C1C1C",
    author: "Bill Nelson, Amelia Phillips & Chris Steuart",
    rating: "4.9",
    badge: "INVESTIGATION",
    theme: "cream",
  },
  "soc-analyst": {
    slug: "soc-analyst",
    volumeNumber: "VOL. 19",
    height: 358,
    thickness: 58,
    coverWidth: 266,
    spineColor: "#F8EADF", // Burnt Orange
    spineGradient: "linear-gradient(180deg, #E9DACF 0%, #F8EADF 50%, #DACCC1 100%)",
    foilColor: "#A855F7",
    textColor: "#1C1C1C",
    author: "Tyler Wall & Jarrett Rodrick",
    rating: "4.9",
    badge: "OPERATIONS",
    theme: "cream",
  },
  "security-tools": {
    slug: "security-tools",
    volumeNumber: "VOL. 09",
    height: 358,
    thickness: 58,
    coverWidth: 266,
    spineColor: "#C65102",
    spineGradient: "linear-gradient(180deg, #9C3F02 0%, #C65102 50%, #783001 100%)",
    foilColor: "#FEF08A",
    textColor: "#FFFFFF",
    author: "Tyler Wall & Jarrett Rodrick",
    rating: "4.9",
    badge: "OPERATIONS",
    theme: "orange",
  },
  "nmap": {
    slug: "nmap",
    volumeNumber: "VOL. 14",
    height: 362,
    thickness: 62,
    coverWidth: 269,
    spineColor: "#012A1A", // Deep Navy
    spineGradient: "linear-gradient(180deg, #001A10 0%, #012A1A 50%, #000E08 100%)",
    foilColor: "#34D399",
    textColor: "#FFFFFF",
    author: "Gordon \"Fyodor\" Lyon",
    rating: "5.0",
    badge: "PORT SCAN",
    theme: "green",
  },
  "wireless-security": {
    slug: "wireless-security",
    volumeNumber: "VOL. 23",
    height: 350,
    thickness: 58,
    coverWidth: 260,
    spineColor: "#112F0D", // Sand
    spineGradient: "linear-gradient(180deg, #0A1F08 0%, #112F0D 50%, #051304 100%)",
    foilColor: "#84CC16",
    textColor: "#FFFFFF",
    author: "Yi Qian, Feng Ye & Hsiao-Hwa Chen",
    rating: "4.8",
    badge: "802.11 RADIO",
    theme: "green",
  },
  "cloud-security": {
    slug: "cloud-security",
    volumeNumber: "VOL. 21",
    height: 370,
    thickness: 62,
    coverWidth: 275,
    spineColor: "#051A2F", // Cloud Slate Blue
    spineGradient: "linear-gradient(180deg, #03101E 0%, #051A2F 50%, #020B15 100%)",
    foilColor: "#38BDF8",
    textColor: "#FFFFFF",
    author: "Eyal Estrin",
    rating: "4.8",
    badge: "AWS · AZURE · GCP",
    theme: "navy",
  },

  // ── ROW 3 ──
  "python-cybersecurity": {
    slug: "python-cybersecurity",
    volumeNumber: "VOL. 13",
    height: 356,
    thickness: 58,
    coverWidth: 265,
    spineColor: "#091734", // Mustard Yellow
    spineGradient: "linear-gradient(180deg, #050E20 0%, #091734 50%, #030814 100%)",
    foilColor: "#38BDF8",
    textColor: "#FFFFFF",
    author: "Nishant Krishna",
    rating: "4.8",
    badge: "COOKBOOK",
    theme: "blue",
  },
  "windows-security": {
    slug: "windows-security",
    volumeNumber: "VOL. 18",
    height: 378,
    thickness: 66,
    coverWidth: 281,
    spineColor: "#5D030C", // Dark Teal
    spineGradient: "linear-gradient(180deg, #3D0208 0%, #5D030C 50%, #260105 100%)",
    foilColor: "#F87171",
    textColor: "#FFFFFF",
    author: "Dishan Francis",
    rating: "4.9",
    badge: "ACTIVE DIRECTORY",
    theme: "burgundy",
  },
  "incident-response": {
    slug: "incident-response",
    volumeNumber: "VOL. 20",
    height: 348,
    thickness: 58,
    coverWidth: 259,
    spineColor: "#371561", // Alabaster
    spineGradient: "linear-gradient(180deg, #230D3E 0%, #371561 50%, #170829 100%)",
    foilColor: "#F97316", // Red Siren
    textColor: "#FFFFFF",
    author: "Gerard Johansen & Jason T. Luttgens",
    rating: "4.9",
    badge: "BREACH LAB",
    theme: "purple",
  },
  "malware-analysis": {
    slug: "malware-analysis",
    volumeNumber: "VOL. 17",
    height: 372,
    thickness: 62,
    coverWidth: 277,
    spineColor: "#FCECDC", // Cobalt Navy
    spineGradient: "linear-gradient(180deg, #ECDCСC 0%, #FCECDC 50%, #DDD0C0 100%)",
    foilColor: "#D97706",
    textColor: "#1C1C1C",
    author: "Alexey Kleymenov & Amr Thabet",
    rating: "4.9",
    badge: "REVERSE LAB",
    theme: "cream",
  },
  "cryptography": {
    slug: "cryptography",
    volumeNumber: "VOL. 16",
    height: 364,
    thickness: 62,
    coverWidth: 271,
    spineColor: "#00142F", // Classic Cream
    spineGradient: "linear-gradient(180deg, #000B1A 0%, #00142F 50%, #00060E 100%)",
    foilColor: "#60A5FA",
    textColor: "#FFFFFF",
    author: "Keith Martin",
    rating: "5.0",
    badge: "CIPHERS",
    theme: "navy",
  },
  "owasp-top10": {
    slug: "owasp-top10",
    volumeNumber: "VOL. 18",
    height: 376,
    thickness: 66,
    coverWidth: 280,
    spineColor: "#131416", // Crimson Wine
    spineGradient: "linear-gradient(180deg, #0B0B0D 0%, #131416 50%, #060607 100%)",
    foilColor: "#84CC16",
    textColor: "#FFFFFF",
    author: "OWASP Threat Intelligence Group",
    rating: "5.0",
    badge: "INTEL RADAR",
    theme: "charcoal",
  },

  // ── ROW 4 ──
  "osint-guide": {
    slug: "osint-guide",
    volumeNumber: "VOL. 12",
    height: 362,
    thickness: 62,
    coverWidth: 269,
    spineColor: "#052151", // Pure Ivory
    spineGradient: "linear-gradient(180deg, #031433 0%, #052151 50%, #020C1F 100%)",
    foilColor: "#38BDF8",
    textColor: "#FFFFFF",
    author: "Michael Bazzell & DevSecOps Guild",
    rating: "5.0",
    badge: "PIPELINES",
    theme: "blue",
  },
  "container-security": {
    slug: "container-security",
    volumeNumber: "VOL. 20",
    height: 368,
    thickness: 62,
    coverWidth: 274,
    spineColor: "#5B21B6", // Electric Violet
    spineGradient: "linear-gradient(180deg, #3E167D 0%, #5B21B6 50%, #2C0F59 100%)",
    foilColor: "#E9D5FF",
    textColor: "#FFFFFF",
    author: "Liz Rice & Container Security Authors",
    rating: "4.9",
    badge: "DOCKER & K8S",
    theme: "purple",
  },
  "api-security": {
    slug: "api-security",
    volumeNumber: "VOL. 22",
    height: 366,
    thickness: 62,
    coverWidth: 272,
    spineColor: "#FDEDE0", // Charcoal Slate
    spineGradient: "linear-gradient(180deg, #EEDECF 0%, #FDEDE0 50%, #DFD0C2 100%)",
    foilColor: "#2563EB", // Cyan
    textColor: "#1C1C1C",
    author: "Neil Madden & Corey Ball",
    rating: "4.8",
    badge: "SDLC",
    theme: "cream",
  },
  "mobile-security": {
    slug: "mobile-security",
    volumeNumber: "VOL. 24",
    height: 342,
    thickness: 58,
    coverWidth: 254,
    spineColor: "#F8EADF", // Warm Linen
    spineGradient: "linear-gradient(180deg, #E9DACF 0%, #F8EADF 50%, #DACCC1 100%)",
    foilColor: "#DC2626",
    textColor: "#1C1C1C",
    author: "Deya Eldeen & Hardware Authors",
    rating: "4.8",
    badge: "CONNECTED",
    theme: "cream",
  },
  "penetration-testing": {
    slug: "penetration-testing",
    volumeNumber: "VOL. 23",
    height: 374,
    thickness: 62,
    coverWidth: 278,
    spineColor: "#2F163E", // Dark Olive Green
    spineGradient: "linear-gradient(180deg, #1F0D2B 0%, #2F163E 50%, #160820 100%)",
    foilColor: "#C084FC",
    textColor: "#FFFFFF",
    author: "Eldad Eilam & Reverse Engineers",
    rating: "4.9",
    badge: "BINARY RE",
    theme: "purple",
  },
  "bash-scripting": {
    slug: "bash-scripting",
    volumeNumber: "VOL. 11",
    height: 352,
    thickness: 58,
    coverWidth: 262,
    spineColor: "#F5E5D5", // Wheat Cream
    spineGradient: "linear-gradient(180deg, #E6D6C6 0%, #F5E5D5 50%, #DACAC0 100%)",
    foilColor: "#EF4444",
    textColor: "#1C1C1C",
    author: "Michael Basler",
    rating: "4.8",
    badge: "NET ADMIN",
    theme: "cream",
  },
  "wireshark": {
    slug: "wireshark",
    volumeNumber: "VOL. 13",
    height: 354,
    thickness: 58,
    coverWidth: 263,
    spineColor: "#360107",
    spineGradient: "linear-gradient(180deg, #220004 0%, #360107 50%, #150002 100%)",
    foilColor: "#F87171",
    textColor: "#FFFFFF",
    author: "Michael Basler & Laura Chappell",
    rating: "4.9",
    badge: "PACKET LAB",
    theme: "burgundy",
  },

  // ── ROW 5 (WIDE VOLUME) ──
  "red-blue-team": {
    slug: "red-blue-team",
    volumeNumber: "VOL. 25",
    height: 366,
    thickness: 62,
    coverWidth: 272,
    spineColor: "#143622", // British Racing Green
    spineGradient: "linear-gradient(180deg, #0C2114 0%, #143622 50%, #07140C 100%)",
    foilColor: "#FDE047", // Gold
    textColor: "#FFFFFF",
    author: "Ben Clark & Nick Downer",
    rating: "5.0",
    badge: "PLAYBOOK SPECIAL",
    theme: "green",
  },
};
