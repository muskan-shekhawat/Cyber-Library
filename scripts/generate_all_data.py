#!/usr/bin/env python3
"""
Complete database compiler for NULL / LIBRARY:
Generates src/data/books.ts and src/data/tools.ts
"""

import json
import re

# Load base book metadata
from build_full_database import BOOK_DATA

CHAPTER_CONTENT_TEMPLATES = {
    # We generate rich domain-specific technical details for every book and chapter
}

def generate_chapter_details(book, ch_idx, ch_title):
    slug_part = re.sub(r'[^a-z0-9]+', '-', ch_title.lower()).strip('-')
    
    # Specific practical commands and exercises tailored by subject
    cat = book["category"]
    b_slug = book["slug"]
    
    # Provide tailored technical concepts and commands per subject
    if "Networking" in cat or "wireshark" in b_slug or "nmap" in b_slug:
        code_lang = "bash"
        sample_code = f"# Diagnostic inspection for {ch_title}\n# 1. Interface telemetry\nip -s link show dev eth0\n\n# 2. Capture specific traffic flow\nsudo tcpdump -ni any 'tcp port 443 or udp port 53' -c 10 -v\n\n# 3. Kernel socket buffer inspect\nss -tulpn state established"
        term1 = "Packet Encapsulation" if ch_idx < 3 else "Buffer Congestion"
        def1 = "The layering process where each protocol wraps payload data with its metadata headers." if ch_idx < 3 else "Packet queue overflow resulting in dropped segments and latency spikes."
        term2 = "Path MTU" if ch_idx < 6 else "SYN Backlog"
        def2 = "Maximum transmission unit permissible along the complete network path without fragmentation." if ch_idx < 6 else "The kernel queue holding half-open TCP connections awaiting final ACK."
        tool1, tool2 = "Wireshark", "iproute2"
        ref_title = "IETF RFC Standards & Linux Network Documentation"
        ref_url = "https://www.ietf.org"
    elif "Linux" in cat or "Kali" in cat:
        code_lang = "bash"
        sample_code = f"# System administration commands for {ch_title}\n# 1. Inspect unit status and journal telemetry\nsudo systemctl status sshd.service --no-pager\njournalctl -u sshd.service -n 20 --no-pager\n\n# 2. Audit file permissions and POSIX ACLs\nls -la /etc/security/\ngetfacl /var/log/audit/audit.log 2>/dev/null || true"
        term1 = "POSIX Permissions" if ch_idx < 4 else "cgroups (Control Groups)"
        def1 = "Standard read, write, execute permissions allocated across user, group, and other classes." if ch_idx < 4 else "Linux kernel feature that limits, accounts for, and isolates resource usage of process groups."
        term2 = "System Call Interface" if ch_idx < 7 else "Inodes & Superblocks"
        def2 = "The fundamental programmatic boundary between user space applications and kernel space services." if ch_idx < 7 else "Data structures holding metadata about files and filesystem layout."
        tool1, tool2 = "systemd", "auditd"
        ref_title = "Linux Kernel Documentation & Man Pages"
        ref_url = "https://man7.org/linux/man-pages/"
    elif "Web" in cat or "OWASP" in book["title"] or "API" in book["title"] or "Mobile" in book["title"]:
        code_lang = "http" if ch_idx % 2 == 0 else "python"
        sample_code = f"POST /api/v1/auth/verify HTTP/1.1\nHost: target.local\nAuthorization: Bearer eyJhbGciOiJSUzI1NiIsIn...\nContent-Type: application/json\nX-Requested-With: XMLHttpRequest\n\n{{\n  \"account_id\": \"usr_892102\",\n  \"role\": \"standard_auditor\",\n  \"session_nonce\": \"a4f9b2c8\"\n}}" if code_lang == "http" else f"import requests\n\ndef test_endpoint_security(base_url, token):\n    headers = {{\n        'Authorization': f'Bearer {{token}}',\n        'Accept': 'application/json',\n        'User-Agent': 'SecurityAuditor/2.0'\n    }}\n    response = requests.get(f'{{base_url}}/api/v1/user/profile', headers=headers, timeout=5)\n    print(f'Status: {{response.status_code}}, Length: {{len(response.text)}}')\n    return response.headers.get('Content-Security-Policy')"
        term1 = "Same-Origin Policy (SOP)" if ch_idx < 5 else "Broken Object Level Authorization (BOLA)"
        def1 = "A critical browser security mechanism that restricts how a document or script loaded by one origin can interact with a resource from another origin." if ch_idx < 5 else "An access control flaw where user-supplied input is directly used to access an object without server-side validation."
        term2 = "Content Security Policy (CSP)" if ch_idx < 8 else "JWT Signing Key Confusion"
        def2 = "An HTTP response header allowing site administrators to declare approved sources of executable scripts, stylesheets, and frames." if ch_idx < 8 else "A cryptographic vulnerability where public verification keys are mistakenly treated as symmetric HMAC secrets."
        tool1, tool2 = "Burp Suite", "OWASP ZAP"
        ref_title = "OWASP Foundation Verification Standards"
        ref_url = "https://owasp.org"
    elif "Forensics" in cat or "Crypto" in cat or "Malware" in cat or "Incident" in cat:
        code_lang = "bash" if ch_idx % 2 == 0 else "python"
        sample_code = f"# Forensic artifact extraction & verification\n# 1. Compute cryptographic hashes\nsha256sum forensic_evidence.raw > evidence.sha256\n\n# 2. Inspect volatile memory or PE headers\nvol -f memory.dmp windows.pslist\n\n# 3. YARA rule pattern match\nyara -w -s rule_detect.yar /mnt/analysis/sample.bin" if code_lang == "bash" else f"import hashlib\n\ndef compute_hashes(filepath):\n    sha256 = hashlib.sha256()\n    with open(filepath, 'rb') as f:\n        while chunk := f.read(65536):\n            sha256.update(chunk)\n    return sha256.hexdigest()\n\nprint('Evidence SHA-256:', compute_hashes('disk_image.dd'))"
        term1 = "Order of Volatility" if ch_idx < 5 else "Merkle-Damgård Construction"
        def1 = "The sequence in which digital evidence must be acquired, prioritizing CPU registers and RAM before persistent disk storage." if ch_idx < 5 else "A mathematical design principle used in hash functions like SHA-2 to process arbitrary-length messages into fixed outputs."
        term2 = "Master File Table ($MFT)" if ch_idx < 8 else "Dynamic Link Library Injection"
        def2 = "The database in an NTFS filesystem where information about every file and directory is stored as structured records." if ch_idx < 8 else "A stealth technique where malicious code forces another running process to load a DLL and execute malicious instructions."
        tool1, tool2 = "Volatility 3", "Autopsy"
        ref_title = "NIST SP 800-86 Guide to Integrating Forensic Techniques into Incident Response"
        ref_url = "https://csrc.nist.gov"
    elif "Programming" in cat or "Scripting" in cat:
        code_lang = "python" if "python" in b_slug else "bash"
        sample_code = f"import socket\n\ndef scan_target_port(host: str, port: int, timeout: float = 1.0) -> bool:\n    \"\"\"Perform non-blocking TCP connect audit on a single port.\"\"\"\n    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:\n        sock.settimeout(timeout)\n        result = sock.connect_ex((host, port))\n        return result == 0\n\nif __name__ == '__main__':\n    is_open = scan_target_port('127.0.0.1', 80)\n    print(f'Port 80 reachable: {{is_open}}')" if code_lang == "python" else f"#!/usr/bin/env bash\nset -euo pipefail\n\nTARGET_IP=\"127.0.0.1\"\nTIMESTAMP=$(date +\"%Y%m%d_%H%M%S\")\nLOG_FILE=\"/var/log/audit_${{TIMESTAMP}}.log\"\n\necho \"[INFO] Beginning automated security audit on ${{TARGET_IP}}\" | tee -a \"${{LOG_FILE}}\"\nss -tulnp | grep LISTEN >> \"${{LOG_FILE}}\"\necho \"[INFO] Audit complete. Output saved to ${{LOG_FILE}}\""
        term1 = "Non-blocking Socket I/O" if ch_idx < 5 else "Subprocess Pipe Sanitization"
        def1 = "Asynchronous network socket communication permitting multiple concurrent queries without thread locking." if ch_idx < 5 else "Ensuring shell commands executed from code do not permit command injection via untrusted inputs."
        term2 = "Regex ReDoS Vulnerability" if ch_idx < 8 else "Memory Buffer Safety"
        def2 = "Regular Expression Denial of Service caused by exponential backtracking on ambiguous string patterns." if ch_idx < 8 else "Managing memory allocations to prevent buffer overflows or use-after-free conditions."
        tool1, tool2 = "Python 3", "ShellCheck"
        ref_title = "Python Software Foundation Security Guidelines"
        ref_url = "https://docs.python.org/3/"
    else:
        code_lang = "bash"
        sample_code = f"# Assessment and auditing command suite for {ch_title}\n# 1. Scoped service probe\nnmap -sV -sC -Pn --open -p 22,80,443 192.168.1.100\n\n# 2. Passive OSINT verification\nwhois target-domain.local\ndig +nocmd target-domain.local any +multiline +noall +answer"
        term1 = "Attack Surface Reduction" if ch_idx < 5 else "Least Privilege Principle"
        def1 = "The defensive practice of disabling unnecessary open ports, services, and protocol daemons to minimize breach opportunities." if ch_idx < 5 else "Granting user accounts and service daemons only the minimum permissions necessary to complete assigned duties."
        term2 = "Threat Modeling" if ch_idx < 8 else "Defense in Depth"
        def2 = "A structured process for identifying, quantifying, and addressing the security risks associated with an application or system." if ch_idx < 8 else "Layering multiple independent security controls so that the failure of any single measure does not lead to complete system compromise."
        tool1, tool2 = "Nmap", "Metasploit Framework"
        ref_title = "MITRE ATT&CK Framework Enterprise Matrix"
        ref_url = "https://attack.mitre.org"

    return {
        "slug": slug_part,
        "chapterNumber": ch_idx + 1,
        "title": ch_title,
        "summary": f"In-depth analysis of {ch_title.lower()} covering foundational mechanics, enterprise threat modeling, defensive controls, and hands-on exercises.",
        "introduction": f"Chapter {ch_idx + 1} investigates the theoretical mechanics and operational implementation of {ch_title}. In modern cybersecurity architecture, mastering this subject is essential for eliminating single points of failure, verifying defense posture, and executing safe, authorized evaluations.",
        "detailedExplanation": f"A comprehensive examination of {ch_title} requires understanding both low-level protocol behavior and high-level architectural policies. When operating in production or authorized laboratory settings, security practitioners must analyze system telemetry, anticipate edge-case failure modes, and apply rigorous verification baselines. This chapter explores common architectural paradigms, analyzes protocol state machines, and provides battle-tested CLI commands and configuration patterns.",
        "keyConcepts": [
            {"term": term1, "definition": def1},
            {"term": term2, "definition": def2},
            {"term": "Audit Verification Trail", "definition": "A tamper-evident, chronological record of system events providing documented evidence of operational transactions and security states."}
        ],
        "commandsOrCode": [
            {
                "title": f"Production Implementation & Inspection for {ch_title}",
                "language": code_lang,
                "code": sample_code,
                "explanation": f"This code snippet illustrates standard, verified syntax used by security analysts and system architects when examining or configuring {ch_title}."
            }
        ],
        "toolsUsed": [tool1, tool2, "Linux CLI"],
        "commonMistakes": [
            f"Overlooking boundary constraints and default fallback behaviors when configuring {ch_title.lower()}.",
            "Executing offensive testing procedures without an authorized, signed scope of engagement.",
            "Failing to review timestamp synchronizations across distributed log sources."
        ],
        "bestPractices": [
            "Enforce strict least privilege access controls across all service roles and administrative interfaces.",
            "Automate configuration drift detection and execute regression verifications after every major update.",
            "Maintain comprehensive runbooks and verifiable cryptographic hashes for all evidence and deployment artifacts."
        ],
        "practicalExercise": {
            "title": f"Hands-on Lab: Verifying {ch_title}",
            "scenario": f"Within an isolated local virtual laboratory, verify the configuration and security baseline of the target service associated with {ch_title}.",
            "steps": [
                f"Initialize the local laboratory target environment with host-only networking enabled.",
                f"Execute the primary diagnostic commands demonstrated in this chapter to collect baseline telemetry.",
                f"Verify that all defensive controls are active, logging is enabled, and unauthorized probes are safely rejected.",
                f"Document all findings in a structured Markdown report accompanied by SHA-256 hashes of test outputs."
            ],
            "expectedOutcome": f"Successful verification of the target system baseline with complete audit logs and zero disruption to external networks."
        },
        "references": [
            {"title": ref_title, "url": ref_url},
            {"title": "National Institute of Standards and Technology (NIST) Special Publications", "url": "https://csrc.nist.gov/publications/sp800"}
        ]
    }

def build_all_books():
    books = []
    for b in BOOK_DATA:
        chapters = []
        for i, ch_title in enumerate(b["chapterTitles"]):
            chapters.append(generate_chapter_details(b, i, ch_title))
        
        book_obj = {
            "slug": b["slug"],
            "title": b["title"],
            "subtitle": b["subtitle"],
            "category": b["category"],
            "rowId": b["rowId"],
            "volumeNumber": b["volumeNumber"],
            "coverImage": b["coverImage"],
            "accentColor": b["accentColor"],
            "difficulty": b["difficulty"],
            "estimatedHours": b["estimatedHours"],
            "chaptersCount": len(chapters),
            "shortDescription": b["shortDescription"],
            "fullDescription": b["fullDescription"],
            "learningObjectives": b["learningObjectives"],
            "toolsCovered": b["toolsCovered"],
            "relatedBookSlugs": b["relatedBookSlugs"],
            "chapters": chapters
        }
        books.append(book_obj)
    return books

# Write src/data/books.ts
all_books = build_all_books()

books_ts_content = f"""import {{ Book }} from "@/types";

export const ALL_BOOKS: Book[] = {json.dumps(all_books, indent=2)};

export function getAllBooks(): Book[] {{
  return ALL_BOOKS;
}}

export function getBookBySlug(slug: string): Book | undefined {{
  return ALL_BOOKS.find((b) => b.slug === slug);
}}

export function getBooksByRowId(rowId: string): Book[] {{
  return ALL_BOOKS.filter((b) => b.rowId === rowId);
}}

export function getChapterBySlug(bookSlug: string, chapterSlug: string) {{
  const book = getBookBySlug(bookSlug);
  if (!book) return undefined;
  const chapter = book.chapters.find((c) => c.slug === chapterSlug);
  return chapter ? {{ book, chapter }} : undefined;
}}

export function searchBooksAndChapters(query: string) {{
  const q = query.toLowerCase().trim();
  if (!q) return {{ books: [], chapters: [] }};

  const matchedBooks = ALL_BOOKS.filter(
    (b) =>
      b.title.toLowerCase().includes(q) ||
      b.subtitle.toLowerCase().includes(q) ||
      b.category.toLowerCase().includes(q) ||
      b.shortDescription.toLowerCase().includes(q) ||
      b.toolsCovered.some((t) => t.toLowerCase().includes(q))
  );

  const matchedChapters: {{
    bookSlug: string;
    bookTitle: string;
    chapterNumber: number;
    chapterSlug: string;
    title: string;
    summary: string;
  }}[] = [];

  for (const book of ALL_BOOKS) {{
    for (const ch of book.chapters) {{
      if (
        ch.title.toLowerCase().includes(q) ||
        ch.summary.toLowerCase().includes(q) ||
        ch.detailedExplanation.toLowerCase().includes(q) ||
        ch.toolsUsed.some((t) => t.toLowerCase().includes(q)) ||
        ch.keyConcepts.some((c) => c.term.toLowerCase().includes(q))
      ) {{
        matchedChapters.push({{
          bookSlug: book.slug,
          bookTitle: book.title,
          chapterNumber: ch.chapterNumber,
          chapterSlug: ch.slug,
          title: ch.title,
          summary: ch.summary,
        }});
      }}
    }}
  }}

  return {{ books: matchedBooks, chapters: matchedChapters }};
}}
"""

with open("src/data/books.ts", "w") as f:
    f.write(books_ts_content)

print(f"Generated src/data/books.ts with {len(all_books)} books and {sum(len(b['chapters']) for b in all_books)} chapters!")

# Now build src/data/tools.ts
TOOLS_DATA = [
    # NETWORKING
    {
        "slug": "wireshark",
        "name": "Wireshark",
        "category": "Networking",
        "officialWebsite": "https://www.wireshark.org",
        "officialDocs": "https://www.wireshark.org/docs/",
        "purpose": "The world's foremost and widely-used network protocol analyzer, providing deep packet inspection, live capture, and microscopic stream analysis.",
        "installation": {
            "linux": "sudo apt install wireshark tshark",
            "macos": "brew install --cask wireshark",
            "windows": "winget install WiresharkFoundation.Wireshark"
        },
        "basicUsage": "wireshark [options] [capture file]",
        "safeExamples": [
            {
                "title": "Capture 100 packets on local loopback interface",
                "command": "tshark -i lo -c 100 -w /tmp/local_loop.pcap",
                "description": "Uses the CLI tshark utility to capture local network communication safely into a standardized pcap file.",
                "expectedOutput": "Capturing on 'lo'\n100 packets captured"
            },
            {
                "title": "Filter HTTP GET requests from captured pcap",
                "command": "tshark -r /tmp/local_loop.pcap -Y 'http.request.method == \"GET\"' -T fields -e http.host -e http.request.uri",
                "description": "Applies a display filter to extract host headers and target URIs without modifying any network state."
            }
        ],
        "relatedBookSlugs": ["wireshark", "computer-networking", "advanced-networking"]
    },
    {
        "slug": "nmap",
        "name": "Nmap",
        "category": "Networking",
        "officialWebsite": "https://nmap.org",
        "officialDocs": "https://nmap.org/book/",
        "purpose": "Network exploration tool and security/port scanner designed to rapidly audit large networks and determine available hosts, services, and OS types.",
        "installation": {
            "linux": "sudo apt install nmap",
            "macos": "brew install nmap",
            "windows": "winget install Insecure.Nmap"
        },
        "basicUsage": "nmap [Scan Type(s)] [Options] {target specification}",
        "safeExamples": [
            {
                "title": "Localhost Safe Service Audit",
                "command": "nmap -sV -sC 127.0.0.1 -p 22,80,443",
                "description": "Runs default safe detection scripts and version detection strictly on the local loopback interface.",
                "expectedOutput": "PORT    STATE SERVICE VERSION\n22/tcp  open  ssh     OpenSSH 8.9p1\n80/tcp  open  http    nginx 1.18.0"
            }
        ],
        "relatedBookSlugs": ["nmap", "computer-networking", "ethical-hacking"]
    },
    {
        "slug": "tcpdump",
        "name": "tcpdump",
        "category": "Networking",
        "officialWebsite": "https://www.tcpdump.org",
        "officialDocs": "https://www.tcpdump.org/manpages/tcpdump.1.html",
        "purpose": "A powerful command-line packet analyzer that captures and displays TCP/IP and other packets being transmitted or received over a network.",
        "installation": {
            "linux": "sudo apt install tcpdump",
            "macos": "brew install tcpdump",
            "windows": "Pre-installed or available via WSL"
        },
        "basicUsage": "tcpdump [ -AbdDefhHIJKlLnNOpqStuUvxX# ] [ -c count ] [ -F file ] [ -i interface ] [ expression ]",
        "safeExamples": [
            {
                "title": "Inspect DNS query traffic on local interface",
                "command": "sudo tcpdump -i eth0 -n -c 5 'udp port 53'",
                "description": "Sniffs five UDP packets directed to or originating from DNS resolvers with numeric IP formatting.",
                "expectedOutput": "IP 192.168.1.10.53421 > 1.1.1.1.53: 1243+ A? example.com. (29)"
            }
        ],
        "relatedBookSlugs": ["computer-networking", "wireshark", "advanced-networking"]
    },
    {
        "slug": "zeek",
        "name": "Zeek Network Security Monitor",
        "category": "Networking",
        "officialWebsite": "https://zeek.org",
        "officialDocs": "https://docs.zeek.org",
        "purpose": "A passive, open-source network traffic analyzer that converts raw packet streams into structured high-level behavioral logs (conn.log, http.log, ssl.log).",
        "installation": {
            "linux": "sudo apt install zeek",
            "macos": "brew install zeek",
            "windows": "Use via Docker or WSL2"
        },
        "basicUsage": "zeek [options] [file/interface]",
        "safeExamples": [
            {
                "title": "Process an offline PCAP into structured forensic logs",
                "command": "zeek -r capture.pcap",
                "description": "Parses an existing packet capture and generates formatted TSV log files in the current working directory."
            }
        ],
        "relatedBookSlugs": ["wireshark", "soc-analyst", "incident-response"]
    },
    {
        "slug": "netcat",
        "name": "Netcat (nc)",
        "category": "Networking",
        "officialWebsite": "https://nc110.sourceforge.io",
        "officialDocs": "https://man7.org/linux/man-pages/man1/nc.1.html",
        "purpose": "The premier network utility for reading and writing data across network connections using TCP or UDP protocols.",
        "installation": {
            "linux": "sudo apt install netcat-openbsd",
            "macos": "Pre-installed in macOS (/usr/bin/nc)",
            "windows": "Available via ncat in Nmap suite"
        },
        "basicUsage": "nc [-options] hostname port[s] [ports]",
        "safeExamples": [
            {
                "title": "Test local TCP port availability with timeout",
                "command": "nc -zv -w 2 127.0.0.1 22",
                "description": "Verifies whether port 22 is listening locally without transmitting any payload.",
                "expectedOutput": "Connection to 127.0.0.1 22 port [tcp/ssh] succeeded!"
            }
        ],
        "relatedBookSlugs": ["computer-networking", "bash-scripting", "penetration-testing"]
    },
    # KALI LINUX
    {
        "slug": "metasploit",
        "name": "Metasploit Framework",
        "category": "Kali Linux",
        "officialWebsite": "https://www.metasploit.com",
        "officialDocs": "https://docs.metasploit.com",
        "purpose": "The world's most used penetration testing framework, providing verified exploit databases, auxiliary scanning modules, and post-exploitation payloads.",
        "installation": {
            "linux": "sudo apt install metasploit-framework",
            "macos": "brew install metasploit",
            "windows": "Rapid7 Metasploit Installer"
        },
        "basicUsage": "msfconsole [options]",
        "safeExamples": [
            {
                "title": "Start interactive console and verify auxiliary scanner",
                "command": "msfconsole -q -x 'use auxiliary/scanner/portscan/tcp; set RHOSTS 127.0.0.1; set PORTS 22,80; run; exit'",
                "description": "Runs a safe, non-exploitative TCP port scan module strictly against the localhost.",
                "expectedOutput": "[+] 127.0.0.1:22 - TCP OPEN\n[*] Scanned 1 of 1 hosts (100% complete)"
            }
        ],
        "relatedBookSlugs": ["kali-linux", "ethical-hacking", "penetration-testing"]
    },
    {
        "slug": "burp-suite",
        "name": "Burp Suite",
        "category": "Kali Linux",
        "officialWebsite": "https://portswigger.net/burp",
        "officialDocs": "https://portswigger.net/burp/documentation",
        "purpose": "An integrated platform for performing security testing of web applications, featuring an intercepting proxy, repeater, and scanner.",
        "installation": {
            "linux": "sudo apt install burpsuite",
            "macos": "brew install --cask burp-suite",
            "windows": "PortSwigger Community Installer"
        },
        "basicUsage": "burpsuite [options]",
        "safeExamples": [
            {
                "title": "Launch Burp Suite in headless mode for lab test",
                "command": "burpsuite --project-file=/tmp/lab_test.burp &",
                "description": "Starts Burp Suite proxy listener on 127.0.0.1:8080 for intercepting local browser HTTP requests."
            }
        ],
        "relatedBookSlugs": ["web-security", "owasp-top10", "api-security"]
    },
    {
        "slug": "owasp-zap",
        "name": "OWASP ZAP (Zed Attack Proxy)",
        "category": "Kali Linux",
        "officialWebsite": "https://www.zaproxy.org",
        "officialDocs": "https://www.zaproxy.org/docs/",
        "purpose": "Open-source web application security scanner designed for automated vulnerability discovery in development and CI/CD pipelines.",
        "installation": {
            "linux": "sudo apt install zaproxy",
            "macos": "brew install --cask zap",
            "windows": "winget install OWASP.ZAP"
        },
        "basicUsage": "zap.sh [options]",
        "safeExamples": [
            {
                "title": "Execute safe passive scan on local test server",
                "command": "zap-baseline.py -t http://127.0.0.1:3000 -r baseline_report.html",
                "description": "Performs passive analysis on a local web service without injecting offensive payloads."
            }
        ],
        "relatedBookSlugs": ["web-security", "owasp-top10", "api-security"]
    },
    {
        "slug": "gobuster",
        "name": "Gobuster",
        "category": "Kali Linux",
        "officialWebsite": "https://github.com/OJ/gobuster",
        "officialDocs": "https://github.com/OJ/gobuster#readme",
        "purpose": "A high-performance directory and DNS brute-forcing tool written in Go for discovering hidden URIs, vhosts, and S3 buckets.",
        "installation": {
            "linux": "sudo apt install gobuster",
            "macos": "brew install gobuster",
            "windows": "go install github.com/OJ/gobuster/v3@latest"
        },
        "basicUsage": "gobuster [dir|dns|s3|vhost] -u <target> -w <wordlist>",
        "safeExamples": [
            {
                "title": "Enumerate web endpoints on local authorized test lab",
                "command": "gobuster dir -u http://127.0.0.1:8080 -w /usr/share/wordlists/dirb/common.txt -t 10",
                "description": "Probes local endpoints with 10 concurrent threads to map API surface."
            }
        ],
        "relatedBookSlugs": ["web-security", "kali-linux", "ethical-hacking"]
    },
    {
        "slug": "john-the-ripper",
        "name": "John the Ripper",
        "category": "Kali Linux",
        "officialWebsite": "https://www.openwall.com/john/",
        "officialDocs": "https://www.openwall.com/john/doc/",
        "purpose": "A fast password security auditing and hash recovery tool combining dictionary attacks, permutations, and custom rules.",
        "installation": {
            "linux": "sudo apt install john",
            "macos": "brew install john-jumbo",
            "windows": "Pre-compiled jumbo binaries"
        },
        "basicUsage": "john [options] [password-files]",
        "safeExamples": [
            {
                "title": "Audit SHA-256 test hash against common wordlist",
                "command": "echo 'test_hash:5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8' > /tmp/h.txt && john --format=raw-sha256 /tmp/h.txt",
                "description": "Verifies that weak user passwords can be cracked in milliseconds, proving the necessity of Argon2."
            }
        ],
        "relatedBookSlugs": ["cryptography", "kali-linux", "penetration-testing"]
    },
    {
        "slug": "aircrack-ng",
        "name": "Aircrack-ng Suite",
        "category": "Kali Linux",
        "officialWebsite": "https://www.aircrack-ng.org",
        "officialDocs": "https://www.aircrack-ng.org/documentation.html",
        "purpose": "A complete suite of tools to assess Wi-Fi network security, focusing on monitoring, attacking, testing, and cracking 802.11 keys.",
        "installation": {
            "linux": "sudo apt install aircrack-ng",
            "macos": "brew install aircrack-ng",
            "windows": "Aircrack-ng Windows binaries"
        },
        "basicUsage": "aircrack-ng [options] <.cap/.ivs file(s)>",
        "safeExamples": [
            {
                "title": "Audit captured lab WPA2 handshake offline",
                "command": "aircrack-ng -w wordlist.txt -b 00:14:6C:7E:40:80 lab_capture.cap",
                "description": "Performs offline dictionary verification on an authorized lab handshake file."
            }
        ],
        "relatedBookSlugs": ["wireless-security", "kali-linux", "ethical-hacking"]
    },
    # LINUX
    {
        "slug": "bash",
        "name": "GNU Bash",
        "category": "Linux",
        "officialWebsite": "https://www.gnu.org/software/bash/",
        "officialDocs": "https://www.gnu.org/software/bash/manual/",
        "purpose": "The standard Bourne Again SHell providing programmable command execution, scripting, and IPC pipelines.",
        "installation": {
            "linux": "Pre-installed across standard Linux distributions",
            "macos": "brew install bash (for modern Bash 5+)",
            "windows": "Available via Git Bash or WSL"
        },
        "basicUsage": "bash [options] [script-file]",
        "safeExamples": [
            {
                "title": "Execute hardened bash script with error trapping",
                "command": "bash -c 'set -euo pipefail; echo \"Hardened execution active\"'",
                "description": "Demonstrates strict error trapping preventing silent script execution failures."
            }
        ],
        "relatedBookSlugs": ["bash-scripting", "linux-fundamentals", "linux-administration"]
    },
    {
        "slug": "ssh",
        "name": "OpenSSH",
        "category": "Linux",
        "officialWebsite": "https://www.openssh.com",
        "officialDocs": "https://www.openssh.com/manual.html",
        "purpose": "The premier connectivity tool for secure remote login, port forwarding, and cryptographic server administration.",
        "installation": {
            "linux": "sudo apt install openssh-client openssh-server",
            "macos": "Pre-installed (/usr/bin/ssh)",
            "windows": "Built-in Optional Feature: OpenSSH Client"
        },
        "basicUsage": "ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-b bind_address] [user@]hostname [command]",
        "safeExamples": [
            {
                "title": "Generate Ed25519 cryptographic keypair",
                "command": "ssh-keygen -t ed25519 -C 'sec-admin@lab.local' -f /tmp/id_ed25519 -N ''",
                "description": "Creates modern high-security elliptic curve keypair without weak RSA parameters."
            }
        ],
        "relatedBookSlugs": ["linux-administration", "cryptography", "linux-fundamentals"]
    },
    {
        "slug": "lynis",
        "name": "Lynis",
        "category": "Linux",
        "officialWebsite": "https://cisofy.com/lynis/",
        "officialDocs": "https://cisofy.com/documentation/lynis/",
        "purpose": "Battle-tested security auditing and compliance benchmarking tool for systems running Linux, macOS, or Unix-based OS.",
        "installation": {
            "linux": "sudo apt install lynis",
            "macos": "brew install lynis",
            "windows": "Not directly supported (Unix systems)"
        },
        "basicUsage": "lynis audit system",
        "safeExamples": [
            {
                "title": "Perform automated local host security audit",
                "command": "sudo lynis audit system --quick --auditor 'SecTeam'",
                "description": "Scans system configuration against CIS benchmarks and outputs actionable hardening recommendations."
            }
        ],
        "relatedBookSlugs": ["linux-administration", "soc-analyst", "linux-fundamentals"]
    },
    {
        "slug": "fail2ban",
        "name": "Fail2ban",
        "category": "Linux",
        "officialWebsite": "https://www.fail2ban.org",
        "officialDocs": "https://fail2ban.readthedocs.io",
        "purpose": "Intrusion prevention software framework that protects computer servers from brute-force attacks by dynamically updating firewall rules.",
        "installation": {
            "linux": "sudo apt install fail2ban",
            "macos": "brew install fail2ban",
            "windows": "Not supported (Linux firewall specific)"
        },
        "basicUsage": "fail2ban-client [command]",
        "safeExamples": [
            {
                "title": "Check status of SSH jail filter",
                "command": "sudo fail2ban-client status sshd",
                "description": "Reports number of actively monitored logs and currently banned attacking IP addresses."
            }
        ],
        "relatedBookSlugs": ["linux-administration", "soc-analyst", "incident-response"]
    },
    {
        "slug": "systemd",
        "name": "systemd",
        "category": "Linux",
        "officialWebsite": "https://systemd.io",
        "officialDocs": "https://www.freedesktop.org/software/systemd/man/",
        "purpose": "The foundational system and service manager for Linux operating systems, providing daemon management, cgroups sandboxing, and journal logging.",
        "installation": {
            "linux": "Core component of Debian, Ubuntu, Red Hat, Arch, and SUSE",
            "macos": "Not applicable (macOS uses launchd)",
            "windows": "Available inside WSL2"
        },
        "basicUsage": "systemctl [command] [unit]",
        "safeExamples": [
            {
                "title": "Inspect security sandbox status of running system services",
                "command": "systemd-analyze security",
                "description": "Evaluates the sandboxing posture (ProtectSystem, NoNewPrivileges, PrivateTmp) of all active services.",
                "expectedOutput": "UNIT                     EXPOSURE PREDICATE HAPPY\nsshd.service                  5.8 MEDIUM    :-|"
            }
        ],
        "relatedBookSlugs": ["linux-fundamentals", "linux-administration", "soc-analyst"]
    },
    # OSINT
    {
        "slug": "shodan",
        "name": "Shodan CLI",
        "category": "OSINT",
        "officialWebsite": "https://www.shodan.io",
        "officialDocs": "https://cli.shodan.io",
        "purpose": "The search engine for Internet-connected devices, enabling researchers to discover exposed servers, webcams, SCADA, and IoT hardware.",
        "installation": {
            "linux": "pip install shodan",
            "macos": "pip install shodan",
            "windows": "pip install shodan"
        },
        "basicUsage": "shodan [COMMAND] [ARGS]",
        "safeExamples": [
            {
                "title": "Inspect public information for authoritative DNS resolver",
                "command": "shodan host 1.1.1.1",
                "description": "Queries Shodan's indexed database for open ports and banners without actively scanning the target host."
            }
        ],
        "relatedBookSlugs": ["osint-guide", "ethical-hacking", "cloud-security"]
    },
    {
        "slug": "theharvester",
        "name": "theHarvester",
        "category": "OSINT",
        "officialWebsite": "https://github.com/laramies/theHarvester",
        "officialDocs": "https://github.com/laramies/theHarvester/wiki",
        "purpose": "A tool for gathering emails, subdomains, hosts, employee names, open ports, and banners from public sources (Baidu, Bing, Google, LinkedIn).",
        "installation": {
            "linux": "sudo apt install theharvester",
            "macos": "brew install theharvester",
            "windows": "git clone & pip install -r requirements.txt"
        },
        "basicUsage": "theHarvester -d <domain> -b <source>",
        "safeExamples": [
            {
                "title": "Passive domain search via DuckDuckGo",
                "command": "theHarvester -d example.com -b duckduckgo -l 100",
                "description": "Passively aggregates indexed domain references without sending a single packet to the target domain."
            }
        ],
        "relatedBookSlugs": ["osint-guide", "penetration-testing", "ethical-hacking"]
    },
    {
        "slug": "subfinder",
        "name": "Subfinder",
        "category": "OSINT",
        "officialWebsite": "https://github.com/projectdiscovery/subfinder",
        "officialDocs": "https://docs.projectdiscovery.io/tools/subfinder",
        "purpose": "Fast passive subdomain enumeration tool that discovers valid subdomains for websites by querying passive online sources.",
        "installation": {
            "linux": "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
            "macos": "brew install subfinder",
            "windows": "go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"
        },
        "basicUsage": "subfinder -d <target-domain> [flags]",
        "safeExamples": [
            {
                "title": "Enumerate subdomains passively and silently",
                "command": "subfinder -d example.com -silent",
                "description": "Queries multiple passive threat intelligence feeds to discover public subdomains."
            }
        ],
        "relatedBookSlugs": ["osint-guide", "web-security", "ethical-hacking"]
    },
    {
        "slug": "amass",
        "name": "OWASP Amass",
        "category": "OSINT",
        "officialWebsite": "https://owasp.org/www-project-amass/",
        "officialDocs": "https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md",
        "purpose": "In-depth attack surface mapping and network infrastructure analysis using open-source information gathering and active reconnaissance techniques.",
        "installation": {
            "linux": "sudo apt install amass",
            "macos": "brew install amass",
            "windows": "go install -v github.com/owasp-amass/amass/v4/...@master"
        },
        "basicUsage": "amass enum [options] -d <domain>",
        "safeExamples": [
            {
                "title": "Passive attack surface discovery on domain",
                "command": "amass enum -passive -d example.com",
                "description": "Performs reconnaissance strictly relying on third-party public databases and certificate transparency logs."
            }
        ],
        "relatedBookSlugs": ["osint-guide", "web-security", "penetration-testing"]
    },
    {
        "slug": "maltego",
        "name": "Maltego",
        "category": "OSINT",
        "officialWebsite": "https://www.maltego.com",
        "officialDocs": "https://docs.maltego.com",
        "purpose": "Interactive visual data mining tool that queries transform hubs to render relationships between domains, IPs, people, and social accounts.",
        "installation": {
            "linux": "sudo apt install maltego",
            "macos": "brew install --cask maltego",
            "windows": "Maltego Official Community Installer"
        },
        "basicUsage": "maltego &",
        "safeExamples": [
            {
                "title": "Transform domain entity to DNS records",
                "command": "# Executed via Maltego GUI transform hub on target domain entity",
                "description": "Correlates DNS MX, NS, and A records visually in an interconnected node graph."
            }
        ],
        "relatedBookSlugs": ["osint-guide", "ethical-hacking"]
    },
    {
        "slug": "spiderfoot",
        "name": "SpiderFoot",
        "category": "OSINT",
        "officialWebsite": "https://www.spiderfoot.net",
        "officialDocs": "https://spiderfoot.readthedocs.io",
        "purpose": "An open source intelligence (OSINT) automation tool that integrates over 200 data sources to gather intelligence on IP addresses, domain names, and ASNs.",
        "installation": {
            "linux": "pip install spiderfoot",
            "macos": "pip install spiderfoot",
            "windows": "pip install spiderfoot"
        },
        "basicUsage": "sf.py -l 127.0.0.1:5001",
        "safeExamples": [
            {
                "title": "Start local SpiderFoot web interface",
                "command": "python3 -m spiderfoot -l 127.0.0.1:5001 &",
                "description": "Spins up local browser interface for launching scoped OSINT scans."
            }
        ],
        "relatedBookSlugs": ["osint-guide", "ethical-hacking"]
    },
    # DIGITAL FORENSICS
    {
        "slug": "autopsy",
        "name": "Autopsy Digital Forensics",
        "category": "Digital Forensics",
        "officialWebsite": "https://www.autopsy.com",
        "officialDocs": "https://sleuthkit.org/autopsy/docs/user-docs/",
        "purpose": "A premier digital forensics platform and graphical interface to The Sleuth Kit (TSK), used by law enforcement, military, and corporate investigators.",
        "installation": {
            "linux": "sudo apt install autopsy",
            "macos": "Available via Docker or Sleuth Kit CLI",
            "windows": "Autopsy MSI 64-bit installer"
        },
        "basicUsage": "autopsy &",
        "safeExamples": [
            {
                "title": "Ingest disk image for automated timeline parsing",
                "command": "# Within Autopsy, create new case and select disk_image.E01 as DataSource",
                "description": "Parses Master File Table, browser histories, EXIF data, and extracted deleted files into searchable cases."
            }
        ],
        "relatedBookSlugs": ["digital-forensics", "incident-response", "windows-security"]
    },
    {
        "slug": "volatility",
        "name": "Volatility 3",
        "category": "Digital Forensics",
        "officialWebsite": "https://www.volatilityfoundation.org",
        "officialDocs": "https://volatility3.readthedocs.io",
        "purpose": "The world's most widely used memory forensics framework for extracting volatile runtime artifacts from RAM dumps.",
        "installation": {
            "linux": "pip install volatility3",
            "macos": "pip install volatility3",
            "windows": "pip install volatility3"
        },
        "basicUsage": "vol -f <imagepath> <plugin>",
        "safeExamples": [
            {
                "title": "List active processes from a Windows memory image",
                "command": "vol -f /tmp/memdump.raw windows.pslist",
                "description": "Inspects active EPROCESS blocks in RAM to list PIDs, parent PIDs, and creation timestamps.",
                "expectedOutput": "PID     PPID    ImageFileName   CreateTime\n4       0       System          2026-11-20 08:12:01"
            }
        ],
        "relatedBookSlugs": ["digital-forensics", "malware-analysis", "incident-response"]
    },
    {
        "slug": "ftk-imager",
        "name": "FTK Imager",
        "category": "Digital Forensics",
        "officialWebsite": "https://www.exterro.com/ftk-imager",
        "officialDocs": "https://www.exterro.com/digital-forensics-software",
        "purpose": "A data preview and imaging tool that lets forensic examiners create perfect bit-for-bit copies (E01/DD) without modifying original evidence.",
        "installation": {
            "linux": "Available via FTK CLI for Linux",
            "macos": "Use dd/dc3dd or virtualized environment",
            "windows": "Exterro FTK Imager Installer"
        },
        "basicUsage": "ftkimager [source] [destination] [options]",
        "safeExamples": [
            {
                "title": "Create bitstream image with simultaneous SHA-256 verification",
                "command": "ftkimager /dev/sdb /evidence/disk.E01 --e01 --verify",
                "description": "Reads source drive through hardware write-blocker and validates hashes match before and after acquisition."
            }
        ],
        "relatedBookSlugs": ["digital-forensics", "incident-response"]
    },
    {
        "slug": "cyberchef",
        "name": "CyberChef",
        "category": "Digital Forensics",
        "officialWebsite": "https://gchq.github.io/CyberChef/",
        "officialDocs": "https://github.com/gchq/CyberChef/wiki",
        "purpose": "The Cyber Swiss Army Knife — a web app for encryption, encoding, compression and data analysis created by GCHQ.",
        "installation": {
            "linux": "docker run -d -p 8080:80 mpepping/cyberchef",
            "macos": "docker run -d -p 8080:80 mpepping/cyberchef",
            "windows": "Use online or self-hosted in browser"
        },
        "basicUsage": "Open CyberChef in browser, assemble operations in recipe pipeline.",
        "safeExamples": [
            {
                "title": "Decode Base64 string and extract readable strings",
                "command": "# Recipe: From_Base64('A-Za-z0-9+/=',true,false) -> Strings('Single char',4)",
                "description": "Instantly decodes obfuscated payloads retrieved during forensic or malware investigations."
            }
        ],
        "relatedBookSlugs": ["cryptography", "digital-forensics", "malware-analysis"]
    },
    # MALWARE ANALYSIS
    {
        "slug": "ghidra",
        "name": "Ghidra",
        "category": "Malware Analysis",
        "officialWebsite": "https://ghidra-sre.org",
        "officialDocs": "https://htmlpreview.github.io/?https://github.com/NationalSecurityAgency/ghidra/blob/master/Ghidra/RuntimeScripts/Linux/support/index.html",
        "purpose": "A software reverse engineering (SRE) suite developed by the NSA, featuring a comprehensive decompiler, disassembler, and graphing engine.",
        "installation": {
            "linux": "sudo apt install ghidra",
            "macos": "brew install --cask ghidra",
            "windows": "Download Ghidra zip with OpenJDK 17+"
        },
        "basicUsage": "ghidraRun",
        "safeExamples": [
            {
                "title": "Decompile binary in headless mode for symbol analysis",
                "command": "ghidra/support/analyzeHeadless /tmp/ghidra_proj Project1 -import /bin/ls",
                "description": "Parses executable headers and produces C-style pseudo-code of functions without launching the GUI."
            }
        ],
        "relatedBookSlugs": ["malware-analysis", "reverse-engineering", "windows-security"]
    },
    {
        "slug": "yara",
        "name": "YARA",
        "category": "Malware Analysis",
        "officialWebsite": "https://virustotal.github.io/yara/",
        "officialDocs": "https://yara.readthedocs.io",
        "purpose": "The pattern matching swiss army knife for malware researchers, allowing creation of rules based on textual and binary patterns.",
        "installation": {
            "linux": "sudo apt install yara",
            "macos": "brew install yara",
            "windows": "winget install VirusTotal.YARA"
        },
        "basicUsage": "yara [OPTIONS] RULES_FILE TARGET",
        "safeExamples": [
            {
                "title": "Scan directory using custom detection rule",
                "command": "yara -r -s sample_rule.yar /mnt/quarantine/",
                "description": "Scans suspect directory recursively and outputs matching string offsets."
            }
        ],
        "relatedBookSlugs": ["malware-analysis", "soc-analyst", "incident-response"]
    },
    {
        "slug": "remnux",
        "name": "REMnux",
        "category": "Malware Analysis",
        "officialWebsite": "https://remnux.org",
        "officialDocs": "https://docs.remnux.org",
        "purpose": "A Linux toolkit for reverse-engineering and analyzing malicious software, pre-configured with dozens of analysis utilities.",
        "installation": {
            "linux": "remnux install (on clean Ubuntu 20.04/22.04 LTS)",
            "macos": "Import REMnux OVA into UTM or VirtualBox",
            "windows": "Import REMnux OVA into VMware or Hyper-V"
        },
        "basicUsage": "remnux [command]",
        "safeExamples": [
            {
                "title": "Simulate external internet services for isolated malware lab",
                "command": "inetsim &",
                "description": "Spins up fake DNS, HTTP, and SMTP responders to log outbound malware queries safely."
            }
        ],
        "relatedBookSlugs": ["malware-analysis", "digital-forensics"]
    },
    {
        "slug": "gdb",
        "name": "GNU Debugger (GDB)",
        "category": "Malware Analysis",
        "officialWebsite": "https://www.gnu.org/software/gdb/",
        "officialDocs": "https://sourceware.org/gdb/documentation/",
        "purpose": "The standard debugger for the GNU software system, enabling step-by-step execution, memory inspection, and breakpoint control.",
        "installation": {
            "linux": "sudo apt install gdb",
            "macos": "brew install gdb",
            "windows": "Available via MinGW or MSYS2"
        },
        "basicUsage": "gdb [options] [prog|core|pid]",
        "safeExamples": [
            {
                "title": "Disassemble function entry point in Intel syntax",
                "command": "gdb -q -batch -ex 'set disassembly-flavor intel' -ex 'disassemble main' /bin/echo",
                "description": "Disassembles the main routine of /bin/echo without executing the binary."
            }
        ],
        "relatedBookSlugs": ["malware-analysis", "linux-fundamentals"]
    },
    # SOC
    {
        "slug": "wazuh",
        "name": "Wazuh",
        "category": "SOC",
        "officialWebsite": "https://wazuh.com",
        "officialDocs": "https://documentation.wazuh.com",
        "purpose": "Open-source security monitoring, threat detection, integrity monitoring, and incident response platform for endpoints and cloud workloads.",
        "installation": {
            "linux": "curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh && sudo bash wazuh-install.sh -a",
            "macos": "Install Wazuh Agent pkg",
            "windows": "Wazuh Agent MSI installer"
        },
        "basicUsage": "systemctl status wazuh-manager",
        "safeExamples": [
            {
                "title": "Check connected agent status via Wazuh API",
                "command": "curl -k -u wazuh-wui:MySecret -X GET 'https://127.0.0.1:55000/agents?pretty=true'",
                "description": "Queries the local Wazuh manager for the health and sync state of connected endpoint agents."
            }
        ],
        "relatedBookSlugs": ["soc-analyst", "incident-response", "windows-security"]
    },
    {
        "slug": "splunk",
        "name": "Splunk Enterprise",
        "category": "SOC",
        "officialWebsite": "https://www.splunk.com",
        "officialDocs": "https://docs.splunk.com",
        "purpose": "The industry standard platform for searching, monitoring, and analyzing machine-generated big data via a web-style interface.",
        "installation": {
            "linux": "sudo dpkg -i splunk-enterprise.deb",
            "macos": "brew install --cask splunk",
            "windows": "Splunk Enterprise MSI"
        },
        "basicUsage": "splunk [start|stop|restart|status]",
        "safeExamples": [
            {
                "title": "Run SPL search query via CLI",
                "command": "splunk search 'index=_internal sourcetype=splunkd error | head 10'",
                "description": "Queries internal indexing logs to diagnose system performance."
            }
        ],
        "relatedBookSlugs": ["soc-analyst", "incident-response", "cloud-security"]
    },
    {
        "slug": "elastic-security",
        "name": "Elastic Security (ELK)",
        "category": "SOC",
        "officialWebsite": "https://www.elastic.co/security",
        "officialDocs": "https://www.elastic.co/guide/en/security/current/index.html",
        "purpose": "Unified SIEM, endpoint security, and cloud security platform combining Elasticsearch, Logstash, Kibana, and Elastic Agent.",
        "installation": {
            "linux": "sudo apt install elasticsearch kibana",
            "macos": "brew install elastic/tap/elasticsearch-full",
            "windows": "Elastic Cloud or local zip distribution"
        },
        "basicUsage": "systemctl status elasticsearch",
        "safeExamples": [
            {
                "title": "Check health of local Elasticsearch cluster",
                "command": "curl -X GET 'http://localhost:9200/_cluster/health?pretty'",
                "description": "Verifies that shard allocations are green or yellow without writing data."
            }
        ],
        "relatedBookSlugs": ["soc-analyst", "cloud-security", "incident-response"]
    },
    {
        "slug": "sigma",
        "name": "Sigma Rules",
        "category": "SOC",
        "officialWebsite": "https://github.com/SigmaHQ/sigma",
        "officialDocs": "https://sigmahq.github.io",
        "purpose": "Generic and open signature format that allows you to describe relevant log events in a straightforward manner and convert them to any SIEM query.",
        "installation": {
            "linux": "pip install sigmatools pySigma",
            "macos": "pip install sigmatools pySigma",
            "windows": "pip install sigmatools pySigma"
        },
        "basicUsage": "sigma convert -t <backend> <rule.yml>",
        "safeExamples": [
            {
                "title": "Convert Sigma rule to Elastic Lucene query",
                "command": "sigma convert -t elasticsearch -p ecs rules/windows/process_creation/proc_creation_win_mimikatz.yml",
                "description": "Translates a vendor-neutral detection rule into native Elastic Common Schema query."
            }
        ],
        "relatedBookSlugs": ["soc-analyst", "incident-response", "windows-security"]
    },
    # PYTHON
    {
        "slug": "python",
        "name": "Python 3",
        "category": "Python",
        "officialWebsite": "https://www.python.org",
        "officialDocs": "https://docs.python.org/3/",
        "purpose": "The premier programming language for cybersecurity, automation, artificial intelligence, and rapid prototype development.",
        "installation": {
            "linux": "sudo apt install python3 python3-pip python3-venv",
            "macos": "brew install python",
            "windows": "winget install Python.Python.3.12"
        },
        "basicUsage": "python3 [options] [-c cmd | -m mod | file] [arg] ...",
        "safeExamples": [
            {
                "title": "Check Python version and run isolated safe calculation",
                "command": "python3 -c 'import sys, platform; print(f\"Python {sys.version.split()[0]} on {platform.system()}\")'",
                "description": "Queries the active interpreter version and underlying platform metadata."
            }
        ],
        "relatedBookSlugs": ["python-cybersecurity", "bash-scripting"]
    },
    {
        "slug": "scapy",
        "name": "Scapy",
        "category": "Python",
        "officialWebsite": "https://scapy.net",
        "officialDocs": "https://scapy.readthedocs.io",
        "purpose": "A powerful Python-based interactive packet manipulation program and library capable of forging, decoding, and sending packets of a wide number of protocols.",
        "installation": {
            "linux": "pip install scapy",
            "macos": "pip install scapy",
            "windows": "pip install scapy"
        },
        "basicUsage": "from scapy.all import *",
        "safeExamples": [
            {
                "title": "Craft an ICMP packet and print its hex summary",
                "command": "python3 -c 'from scapy.all import IP, ICMP; pkt = IP(dst=\"127.0.0.1\")/ICMP(); pkt.show()'",
                "description": "Demonstrates layer encapsulation (IP layer wrapping ICMP layer) safely in memory."
            }
        ],
        "relatedBookSlugs": ["python-cybersecurity", "computer-networking", "wireshark"]
    },
    {
        "slug": "requests",
        "name": "Python Requests",
        "category": "Python",
        "officialWebsite": "https://requests.readthedocs.io",
        "officialDocs": "https://requests.readthedocs.io/en/latest/",
        "purpose": "An elegant and simple HTTP library for Python, built for human beings, simplifying authenticated API testing and web enumeration.",
        "installation": {
            "linux": "pip install requests",
            "macos": "pip install requests",
            "windows": "pip install requests"
        },
        "basicUsage": "import requests; r = requests.get('https://example.com')",
        "safeExamples": [
            {
                "title": "Inspect HTTP headers of a target server securely",
                "command": "python3 -c 'import requests; r = requests.get(\"https://www.google.com\", timeout=3); print(r.headers.get(\"Server\"))'",
                "description": "Queries public server header with a non-blocking timeout."
            }
        ],
        "relatedBookSlugs": ["python-cybersecurity", "web-security", "api-security"]
    },
    {
        "slug": "paramiko",
        "name": "Paramiko",
        "category": "Python",
        "officialWebsite": "https://www.paramiko.org",
        "officialDocs": "https://docs.paramiko.org",
        "purpose": "A Python (2.7, 3.4+) implementation of the SSHv2 protocol, providing both client and server functionality for automated remote system orchestration.",
        "installation": {
            "linux": "pip install paramiko",
            "macos": "pip install paramiko",
            "windows": "pip install paramiko"
        },
        "basicUsage": "import paramiko; client = paramiko.SSHClient()",
        "safeExamples": [
            {
                "title": "Instantiate SSHClient with auto-add host key policy",
                "command": "python3 -c 'import paramiko; client = paramiko.SSHClient(); client.set_missing_host_key_policy(paramiko.RejectPolicy()); print(\"Paramiko Client Initialized\")'",
                "description": "Verifies Paramiko imports and enforces strict host key verification by default."
            }
        ],
        "relatedBookSlugs": ["python-cybersecurity", "linux-administration"]
    }
]

tools_ts_content = f"""import {{ ToolItem }} from "@/types";

export const ALL_TOOLS: ToolItem[] = {json.dumps(TOOLS_DATA, indent=2)};

export function getAllTools(): ToolItem[] {{
  return ALL_TOOLS;
}}

export function getToolBySlug(slug: string): ToolItem | undefined {{
  return ALL_TOOLS.find((t) => t.slug === slug);
}}

export function getToolsByCategory(category: string): ToolItem[] {{
  return ALL_TOOLS.filter((t) => t.category.toLowerCase() === category.toLowerCase());
}}

export function searchTools(query: string): ToolItem[] {{
  const q = query.toLowerCase().trim();
  if (!q) return ALL_TOOLS;
  return ALL_TOOLS.filter(
    (t) =>
      t.name.toLowerCase().includes(q) ||
      t.category.toLowerCase().includes(q) ||
      t.purpose.toLowerCase().includes(q) ||
      t.safeExamples.some((e) => e.command.toLowerCase().includes(q) || e.title.toLowerCase().includes(q))
  );
}}
"""

with open("src/data/tools.ts", "w") as f:
    f.write(tools_ts_content)

print(f"Generated src/data/tools.ts with {len(TOOLS_DATA)} tools!")
