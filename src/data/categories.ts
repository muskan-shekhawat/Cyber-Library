import { BookRowCategory } from "@/types";

export const BOOK_ROW_CATEGORIES: BookRowCategory[] = [
  {
    id: "networking",
    number: "ROW 01",
    title: "NETWORKING",
    subtitle: "Architecture, packet dynamics, routing protocols & telemetry",
    bookSlugs: [
      "computer-networking",
      "advanced-networking",
      "wireshark",
      "nmap",
    ],
  },
  {
    id: "linux-kali",
    number: "ROW 02",
    title: "LINUX & KALI",
    subtitle: "Kernel architecture, system management, automated pipelines & offensive distributions",
    bookSlugs: [
      "linux-fundamentals",
      "kali-linux",
      "linux-administration",
      "bash-scripting",
    ],
  },
  {
    id: "ethical-hacking",
    number: "ROW 03",
    title: "ETHICAL HACKING",
    subtitle: "Assessment methodology, authorized penetration testing, open source intelligence & wireless protocols",
    bookSlugs: [
      "ethical-hacking",
      "penetration-testing",
      "osint-guide",
      "wireless-security",
    ],
  },
  {
    id: "web-security",
    number: "ROW 04",
    title: "WEB SECURITY",
    subtitle: "HTTP mechanics, modern web architectures, API vulnerability vectors & mobile application defenses",
    bookSlugs: [
      "web-security",
      "owasp-top10",
      "api-security",
      "mobile-security",
    ],
  },
  {
    id: "forensics-crypto",
    number: "ROW 05",
    title: "DIGITAL FORENSICS & INCIDENT RESPONSE",
    subtitle: "Evidence integrity, mathematical cryptosystems, reverse engineering & rapid breach containment",
    bookSlugs: [
      "digital-forensics",
      "cryptography",
      "malware-analysis",
      "incident-response",
    ],
  },
  {
    id: "operations-cloud",
    number: "ROW 06",
    title: "SECURITY TOOLS & OPERATIONS",
    subtitle: "Automated scripting, Active Directory enterprise security, SIEM detection engineering & cloud perimeters",
    bookSlugs: [
      "python-cybersecurity",
      "windows-security",
      "soc-analyst",
      "cloud-security",
    ],
  },
];
