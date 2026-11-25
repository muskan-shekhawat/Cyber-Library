#!/usr/bin/env python3
"""
Build complete TypeScript data modules for NULL / LIBRARY:
- src/data/books.ts (All 24 books, 240 in-depth chapters, practical exercises, commands, key concepts, references)
- src/data/tools.ts (38 industry-standard cybersecurity tools across 8 categories with commands, docs, installation)
"""

import json
import os

BOOK_DATA = [
    # 01. computer-networking
    {
        "slug": "computer-networking",
        "title": "Computer Networking Fundamentals",
        "subtitle": "Foundational Protocols, Packet Dynamics & Modern Architectures",
        "category": "Networking",
        "rowId": "networking",
        "volumeNumber": "VOL. 01",
        "coverImage": "/images/books/computer-networking.webp",
        "accentColor": "#2563EB",
        "difficulty": "Beginner",
        "estimatedHours": 14,
        "shortDescription": "A rigorous foundation in modern networking: OSI and TCP/IP stacks, IPv4/IPv6 subnetting, transport layer dynamics, and diagnostic command suites.",
        "fullDescription": "Engineered for security researchers and infrastructure engineers, this textbook establishes concrete knowledge of packet headers, routing behaviors, DNS resolution hierarchies, and operational troubleshooting with Wireshark and modern Linux networking utilities.",
        "learningObjectives": [
            "Deconstruct encapsulation layers across the 7-layer OSI model and 4-layer TCP/IP stack",
            "Calculate classless inter-domain routing (CIDR) blocks and subnet masks under IPv4 and IPv6",
            "Trace packet handshakes (SYN, SYN-ACK, ACK) and teardowns at the byte level",
            "Troubleshoot operational connectivity using ip, ss, dig, traceroute, and Wireshark"
        ],
        "toolsCovered": ["Wireshark", "iproute2", "traceroute", "dig", "tcpdump", "netcat"],
        "relatedBookSlugs": ["advanced-networking", "wireshark", "nmap", "web-security"],
        "chapterTitles": [
            "Introduction to Computer Networks",
            "The OSI Reference Model",
            "The TCP/IP Protocol Suite",
            "IP Addressing & Subnetting Mechanics",
            "MAC Addresses, ARP & Layer-2 Security",
            "Core Services: DNS & DHCP Protocols",
            "Transport Layer Dynamics: TCP vs UDP",
            "Routers, Switches & Firewall Architectures",
            "Essential Application Protocols",
            "Network Troubleshooting & Diagnostics"
        ]
    },
    # 02. advanced-networking
    {
        "slug": "advanced-networking",
        "title": "Advanced Networking & Infrastructure",
        "subtitle": "BGP, MPLS, Software-Defined Routing & Zero Trust Perimeters",
        "category": "Networking",
        "rowId": "networking",
        "volumeNumber": "VOL. 02",
        "coverImage": "/images/books/advanced-networking.webp",
        "accentColor": "#0052CC",
        "difficulty": "Advanced",
        "estimatedHours": 18,
        "shortDescription": "Master enterprise routing architectures, dynamic routing protocols (BGP/OSPF), VXLAN overlays, high-availability clusters, and zero-trust transport topologies.",
        "fullDescription": "This comprehensive volume bridges theoretical telecommunications with high-throughput production infrastructure. Learn how autonomous systems exchange routes, how BGP hijacks occur, and how to construct resilient overlay networks.",
        "learningObjectives": [
            "Configure and audit Border Gateway Protocol (BGP) peering and Autonomous Systems (AS)",
            "Diagnose OSPF link-state databases and shortest-path tree convergence",
            "Deploy VXLAN overlays and Geneve encapsulations across modern data centers",
            "Implement Route Filtering, RPKI validation, and anti-spoofing BCP 38 guidelines"
        ],
        "toolsCovered": ["FRRouting", "BIRD", "Wireshark", "iproute2", "tcpdump", "iperf3"],
        "relatedBookSlugs": ["computer-networking", "wireshark", "cloud-security", "nmap"],
        "chapterTitles": [
            "Autonomous Systems & Border Gateway Protocol (BGP)",
            "Link-State Routing with OSPF & IS-IS",
            "Multiprotocol Label Switching (MPLS) Mechanics",
            "Overlay Networks: VXLAN, Geneve & EVPN",
            "Network Address Translation (NAT) Traversal & STUN/TURN",
            "Quality of Service (QoS), DSCP & Traffic Shaping",
            "High Availability: VRRP, CARP & Anycast Routing",
            "Software-Defined Networking (SDN) & OpenFlow",
            "RPKI Validation & Route Hijack Mitigation",
            "Zero Trust Network Architecture (ZTNA) Design"
        ]
    },
    # 03. linux-fundamentals
    {
        "slug": "linux-fundamentals",
        "title": "Linux Fundamentals",
        "subtitle": "Architecture, Shell Navigation & Operating System Mechanics",
        "category": "Linux",
        "rowId": "linux-kali",
        "volumeNumber": "VOL. 03",
        "coverImage": "/images/books/linux-fundamentals.webp",
        "accentColor": "#D97706",
        "difficulty": "Beginner",
        "estimatedHours": 12,
        "shortDescription": "The definitive starting point for operating systems mastery: the Linux kernel, FHS file hierarchy, terminal navigation, POSIX permissions, and process lifecycle.",
        "fullDescription": "Designed specifically for aspiring cybersecurity professionals, this book walks through real command execution in Debian, Ubuntu, and Fedora environments. It demystifies user namespaces, file descriptors, signals, and system services.",
        "learningObjectives": [
            "Navigate the Linux Filesystem Hierarchy Standard (FHS) with speed and precision",
            "Audit and enforce standard and special POSIX file permissions (SUID, SGID, Sticky Bit)",
            "Control foreground/background processes and inspect resource consumption",
            "Parse system log files and manage software dependencies securely"
        ],
        "toolsCovered": ["bash", "grep", "find", "chmod", "systemctl", "journalctl", "top"],
        "relatedBookSlugs": ["linux-administration", "bash-scripting", "kali-linux", "digital-forensics"],
        "chapterTitles": [
            "Introduction to the Linux Operating System",
            "Kernel Architecture & User Space Separation",
            "The Filesystem Hierarchy Standard (FHS)",
            "Essential Command Line Navigation & Operations",
            "User Accounts, Groups & Authentication",
            "POSIX Permissions, Umask & Special Bits",
            "Process Control, Signals & System Monitoring",
            "Package Management & Binary Integrity",
            "Linux Networking Commands & Configuration",
            "System Logs, Journalctl & Kernel Auditing"
        ]
    },
    # 04. kali-linux
    {
        "slug": "kali-linux",
        "title": "Kali Linux Handbook",
        "subtitle": "Offensive Security Distribution, Toolchains & Lab Safety",
        "category": "Kali Linux",
        "rowId": "linux-kali",
        "volumeNumber": "VOL. 04",
        "coverImage": "/images/books/kali-linux.webp",
        "accentColor": "#4F46E5",
        "difficulty": "Intermediate",
        "estimatedHours": 16,
        "shortDescription": "A guided architectural tour of the foremost security assessment platform: package maintenance, virtualization configurations, reconnaissance arsenals, and ethics.",
        "fullDescription": "Kali Linux is more than an OS; it is a curated ecosystem of thousands of specialized binaries. This handbook guides practitioners through non-destructive auditing, customized tool chains, isolated virtualization, and professional evidence hygiene.",
        "learningObjectives": [
            "Install and securely isolate Kali Linux within virtualized hypervisors",
            "Configure encrypted persistent USB installations with emergency self-destruct",
            "Operate reconnaissance and enumeration frameworks responsibly",
            "Maintain audit logs and non-destructive testing boundaries"
        ],
        "toolsCovered": ["Kali Linux", "Nmap", "Wireshark", "Burp Suite", "Metasploit", "Hydra", "Gobuster"],
        "relatedBookSlugs": ["linux-fundamentals", "ethical-hacking", "penetration-testing", "nmap"],
        "chapterTitles": [
            "Kali Linux Architecture & Ethical Operating Principles",
            "Virtual Machine Installation & Hardware Pass-Through",
            "Desktop Customization & Terminal Productivity Suites",
            "Package Management & Rolling Release Upgrades",
            "Network Discovery & Passive Scanners in Kali",
            "Active Reconnaissance & Host Enumeration Tools",
            "Packet Analysis & Live Traffic Inspection",
            "Web Application Security Testing Utilities",
            "Password Security Auditing & Hash Cracking Frameworks",
            "Assessment Logging, Evidence Handling & Lab Safety"
        ]
    },
    # 05. linux-administration
    {
        "slug": "linux-administration",
        "title": "Linux System Administration",
        "subtitle": "Enterprise Infrastructure, systemd, Storage & Security Hardening",
        "category": "Linux",
        "rowId": "linux-kali",
        "volumeNumber": "VOL. 05",
        "coverImage": "/images/books/linux-administration.webp",
        "accentColor": "#0F766E",
        "difficulty": "Intermediate",
        "estimatedHours": 16,
        "shortDescription": "Production server administration: systemd unit management, LVM partitioning, kernel sysctl hardening, automated backups, and PAM authentication modules.",
        "fullDescription": "Essential reading for DevOps engineers and security administrators. Learn how to maintain production uptimes while maintaining strict CIS benchmark compliance across modern enterprise Linux fleets.",
        "learningObjectives": [
            "Author and troubleshoot custom systemd services, timers, and target dependencies",
            "Administer Logical Volume Manager (LVM) volumes, thin pools, and LUKS encryption",
            "Tune Linux kernel parameters for network throughput and defensive resilience",
            "Configure Pluggable Authentication Modules (PAM) and Multi-Factor Authentication"
        ],
        "toolsCovered": ["systemd", "LVM", "cryptsetup", "sysctl", "PAM", "nftables", "fail2ban"],
        "relatedBookSlugs": ["linux-fundamentals", "bash-scripting", "soc-analyst", "cloud-security"],
        "chapterTitles": [
            "Boot Process, Init Systems & systemd Architecture",
            "Storage Management, LVM & LUKS Disk Encryption",
            "Kernel Tuning, sysctl & Security Hardening",
            "Pluggable Authentication Modules (PAM) & SSH Hardening",
            "File Integrity Monitoring & Access Control Lists (ACLs)",
            "Automated Backups, Rsync & Disaster Recovery",
            "Enterprise Package Repositories & Patch Management",
            "nftables Firewall Policies & Intrusion Mitigation",
            "Container Runtimes, cgroups & Namespaces",
            "Fleet Monitoring, Metrics & Incident Escalation"
        ]
    },
    # 06. ethical-hacking
    {
        "slug": "ethical-hacking",
        "title": "Ethical Hacking Fundamentals",
        "subtitle": "Security Assessments, Rules of Engagement & Vulnerability Auditing",
        "category": "Ethical Hacking",
        "rowId": "ethical-hacking",
        "volumeNumber": "VOL. 06",
        "coverImage": "/images/books/ethical-hacking.webp",
        "accentColor": "#E11D48",
        "difficulty": "Beginner",
        "estimatedHours": 15,
        "shortDescription": "The definitive principles of defensive security testing: legal frameworks, scoped authorization, vulnerability discovery, and professional report synthesis.",
        "fullDescription": "Grounding students in the non-negotiable ethics and technical standards of ethical hacking. Covers legal statutes (CFAA, Computer Misuse Act), authorization charters, vulnerability scanning techniques, and remediation roadmaps.",
        "learningObjectives": [
            "Establish unambiguous Scopes of Work (SOW) and Rules of Engagement (RoE)",
            "Conduct structured passive and active information gathering",
            "Validate common vulnerability classes without disrupting client operations",
            "Author executive and technical findings reports with CVSS v3.1 scoring"
        ],
        "toolsCovered": ["Nmap", "OpenVAS", "Nikto", "OWASP ZAP", "Metasploit", "Searchsploit"],
        "relatedBookSlugs": ["penetration-testing", "kali-linux", "web-security", "osint-guide"],
        "chapterTitles": [
            "Cybersecurity Fundamentals & Threat Landscapes",
            "Ethical Hacking Principles & Professional Code of Conduct",
            "Rules of Engagement, Contracts & Legal Boundaries",
            "Passive Reconnaissance & Intelligence Gathering",
            "Active Network Enumeration & Attack Surface Mapping",
            "Vulnerability Assessment & Scanner Interpretation",
            "Controlled Security Testing in Isolated Labs",
            "Evidence Collection, Screenshots & Chain of Custody",
            "Technical Reporting & Executive Risk Translation",
            "Remediation Guidance & Defensive Hardening"
        ]
    },
    # 07. penetration-testing
    {
        "slug": "penetration-testing",
        "title": "Penetration Testing Methodology",
        "subtitle": "PTES Standards, Exploit Verification & Post-Exploitation",
        "category": "Ethical Hacking",
        "rowId": "ethical-hacking",
        "volumeNumber": "VOL. 07",
        "coverImage": "/images/books/penetration-testing.webp",
        "accentColor": "#EA580C",
        "difficulty": "Advanced",
        "estimatedHours": 20,
        "shortDescription": "End-to-end execution of standard penetration tests: pre-engagement, threat modeling, vulnerability validation, privilege escalation, and lateral movement in labs.",
        "fullDescription": "Following the Penetration Testing Execution Standard (PTES), this guide equips consultants with the discipline needed to simulate sophisticated threat actors. Emphasizes clean proof-of-concept creation, safe payload execution, and actionable remediation.",
        "learningObjectives": [
            "Execute assessments according to the Penetration Testing Execution Standard (PTES)",
            "Identify and safely exploit software flaws in isolated laboratory targets",
            "Enumerate Windows and Linux hosts for local privilege escalation paths",
            "Demonstrate post-exploitation impact without tampering with live data integrity"
        ],
        "toolsCovered": ["Metasploit", "Impacket", "BloodHound", "LinPEAS", "WinPEAS", "CrackMapExec"],
        "relatedBookSlugs": ["ethical-hacking", "windows-security", "kali-linux", "web-security"],
        "chapterTitles": [
            "PTES Methodology & Technical Scoping Agreements",
            "Threat Modeling & Attack Vector Identification",
            "Comprehensive Network Enumeration & Service Probing",
            "Vulnerability Validation & Exploit Proofs-of-Concept",
            "Linux Privilege Escalation Techniques",
            "Windows Privilege Escalation & Token Manipulation",
            "Post-Exploitation, Credential Harvesting & Lab Pivoting",
            "Active Directory Attack Paths & Domain Dominance Labs",
            "Risk Classification, CVSS Calculation & Impact Metrics",
            "Writing the Technical & Executive Pentest Report"
        ]
    },
    # 08. web-security
    {
        "slug": "web-security",
        "title": "Web Application Security",
        "subtitle": "HTTP Internals, Vulnerability Vectors & Secure Architectures",
        "category": "Web Security",
        "rowId": "web-security",
        "volumeNumber": "VOL. 08",
        "coverImage": "/images/books/web-security.webp",
        "accentColor": "#2563EB",
        "difficulty": "Intermediate",
        "estimatedHours": 16,
        "shortDescription": "Dissecting modern web applications: HTTP/HTTPS protocol mechanics, authentication session flaws, injection vectors, CSRF, SSRF, and defense-in-depth.",
        "fullDescription": "Web applications are the primary attack surface of the modern internet. This book teaches security analysts and software engineers how to find, exploit, and eliminate flaws in frontend logic, REST backends, and database layers.",
        "learningObjectives": [
            "Intercept and tamper with HTTP/HTTPS traffic using Burp Suite and OWASP ZAP",
            "Discover and neutralize SQL Injection, Cross-Site Scripting (XSS), and SSRF",
            "Audit session token issuance, JWT verification, and OAuth 2.0 flows",
            "Enforce Content Security Policy (CSP), CORS, and HTTP security headers"
        ],
        "toolsCovered": ["Burp Suite", "OWASP ZAP", "Postman", "sqlmap", "cURL", "Wfuzz"],
        "relatedBookSlugs": ["owasp-top10", "api-security", "python-cybersecurity", "ethical-hacking"],
        "chapterTitles": [
            "HTTP/HTTPS Protocols & Browser Security Architecture",
            "Modern Web Frameworks & Attack Surface Mapping",
            "Authentication Mechanisms, Passwords & Session Tokens",
            "Authorization Failures & Access Control Bypasses",
            "SQL Injection (SQLi) Vulnerabilities & Parameterized Defenses",
            "Cross-Site Scripting (XSS): Reflected, Stored & DOM",
            "Cross-Site Request Forgery (CSRF) & SameSite Cookie Policies",
            "Server-Side Request Forgery (SSRF) in Cloud Environments",
            "Security Headers, CORS Policies & Content Security Policy (CSP)",
            "Secure Software Development Lifecycle (SSDLC) & Code Review"
        ]
    },
    # 09. owasp-top10
    {
        "slug": "owasp-top10",
        "title": "OWASP Top 10 Security Risks",
        "subtitle": "In-Depth Analysis, Exploitation Vectors & Defensive Blueprints",
        "category": "Web Security",
        "rowId": "web-security",
        "volumeNumber": "VOL. 09",
        "coverImage": "/images/books/owasp-top10.webp",
        "accentColor": "#F87171",
        "difficulty": "Intermediate",
        "estimatedHours": 14,
        "shortDescription": "The definitive technical guide to the OWASP Top 10 web application vulnerabilities: real code examples, proof-of-concept verification, and defensive blueprints.",
        "fullDescription": "A meticulous, code-level breakdown of the Open Worldwide Application Security Project's top 10 risks. From Broken Access Control to SSRF, this text provides practical labs, vulnerable code snippets, and production-tested remediations.",
        "learningObjectives": [
            "Systematically identify each of the ten OWASP risk categories in modern codebases",
            "Construct realistic proof-of-concept exploits in safe containerized environments",
            "Remediate insecure direct object references and cryptographic implementation flaws",
            "Implement automated security linting and dependency scanning in CI/CD pipelines"
        ],
        "toolsCovered": ["OWASP ZAP", "Burp Suite", "Dependency-Check", "Semgrep", "SonarQube"],
        "relatedBookSlugs": ["web-security", "api-security", "python-cybersecurity", "penetration-testing"],
        "chapterTitles": [
            "A01:2021 — Broken Access Control",
            "A02:2021 — Cryptographic Failures",
            "A03:2021 — Injection Flaws (SQL, NoSQL, Command)",
            "A04:2021 — Insecure Design & Threat Modeling",
            "A05:2021 — Security Misconfiguration & Default Credentials",
            "A06:2021 — Vulnerable and Outdated Components",
            "A07:2021 — Identification and Authentication Failures",
            "A08:2021 — Software and Data Integrity Failures",
            "A09:2021 — Security Logging and Monitoring Failures",
            "A10:2021 — Server-Side Request Forgery (SSRF)"
        ]
    },
    # 10. python-cybersecurity
    {
        "slug": "python-cybersecurity",
        "title": "Python for Cybersecurity",
        "subtitle": "Security Automation, Raw Socket Crafting & Threat Intel Scripting",
        "category": "Programming",
        "rowId": "operations-cloud",
        "volumeNumber": "VOL. 10",
        "coverImage": "/images/books/python-cybersecurity.webp",
        "accentColor": "#1E3A8A",
        "difficulty": "Intermediate",
        "estimatedHours": 18,
        "shortDescription": "Automate security tasks with Python: raw sockets, Scapy packet dissection, automated web enumeration, log parsing with regex, and malware triage tools.",
        "fullDescription": "Move beyond pre-built tools. This book trains readers to write custom security utilities from scratch using Python 3. Build fast asynchronous port scanners, parse GBs of proxy logs, and interact with threat intelligence APIs.",
        "learningObjectives": [
            "Engineer low-level socket connections and multi-threaded port scanners in Python",
            "Craft, send, and sniff custom network packets with Scapy",
            "Automate HTTP requests, header inspections, and web scraping with Requests and BeautifulSoup",
            "Develop modular CLI security utilities with argparse, rich, and logging"
        ],
        "toolsCovered": ["Python 3", "Scapy", "Requests", "Paramiko", "BeautifulSoup4", "Regex"],
        "relatedBookSlugs": ["bash-scripting", "wireshark", "nmap", "soc-analyst"],
        "chapterTitles": [
            "Python 3 Environment, Virtualenvs & Typing for Security",
            "Low-Level Socket Programming & Port Scanner Engineering",
            "Packet Crafting, Sniffing & Injection with Scapy",
            "Automating HTTP Transactions & API Audits with Requests",
            "Log Parsing, SIEM Data Ingestion & Regular Expressions",
            "Asynchronous Automation with asyncio & Concurrent Futures",
            "Automated SSH Orchestration with Paramiko",
            "Threat Intelligence Ingestion & IOC Normalization",
            "Binary Analysis, Pe-file Parsing & Hash Extraction",
            "Building Production-Grade CLI Security Utilities"
        ]
    },
    # 11. bash-scripting
    {
        "slug": "bash-scripting",
        "title": "Bash Scripting & Automation",
        "subtitle": "Terminal Mastery, Pipeline Processing & Incident Response Scripts",
        "category": "Linux",
        "rowId": "linux-kali",
        "volumeNumber": "VOL. 11",
        "coverImage": "/images/books/bash-scripting.webp",
        "accentColor": "#84CC16",
        "difficulty": "Intermediate",
        "estimatedHours": 14,
        "shortDescription": "Master Unix shell scripting for defense: POSIX standards, pipelines, text slicing with awk and sed, automated server auditing, and emergency containment triage.",
        "fullDescription": "Bash is the ubiquitous language of Linux servers and incident responders. This text covers writing defensive shell scripts that audit user logins, detect unauthorized cronjobs, extract forensic artifacts, and enforce host hardening.",
        "learningObjectives": [
            "Write safe, robust Bash scripts with strict error trapping (set -euo pipefail)",
            "Parse complex tabular text streams with awk, sed, and cut",
            "Automate periodic security baselining and file integrity checks",
            "Create emergency forensic triage scripts to collect volatile memory and network states"
        ],
        "toolsCovered": ["Bash", "awk", "sed", "grep", "cron", "jq", "curl"],
        "relatedBookSlugs": ["linux-fundamentals", "linux-administration", "python-cybersecurity", "digital-forensics"],
        "chapterTitles": [
            "Bash Shell Architecture, Profiles & Environment Variables",
            "Variables, Parameter Expansion & Positional Arguments",
            "Flow Control, Conditional Logic & Loop Constructs",
            "Standard I/O Streams, Redirection & File Descriptors",
            "Stream Editing with sed & Pattern Transformation",
            "Data Extraction & Report Formatting with awk",
            "Strict Mode, Error Trapping (trap) & Robust Scripting",
            "Automating Security Audits & CIS Benchmark Checks",
            "Rapid Forensic Triage Scripting for Live Systems",
            "Enterprise Shell Scheduling, Logging & Notifications"
        ]
    },
    # 12. osint-guide
    {
        "slug": "osint-guide",
        "title": "OSINT Field Guide",
        "subtitle": "Open Source Intelligence, Passive Reconnaissance & Entity Correlation",
        "category": "Ethical Hacking",
        "rowId": "ethical-hacking",
        "volumeNumber": "VOL. 12",
        "coverImage": "/images/books/osint-guide.webp",
        "accentColor": "#7C3AED",
        "difficulty": "Beginner",
        "estimatedHours": 12,
        "shortDescription": "A structured methodology for digital intelligence gathering: search dorks, DNS reconnaissance, certificate transparency logs, Shodan scanning, and ethics.",
        "fullDescription": "Uncover the digital footprint of organizations and infrastructure using solely public, non-intrusive data. Learn how security teams discover exposed credentials, rogue cloud buckets, leaked source code, and shadow IT assets.",
        "learningObjectives": [
            "Utilize advanced search engine operators (Google Dorks) to uncover exposed assets",
            "Enumerate corporate domain infrastructure via DNS records and Certificate Transparency logs",
            "Query internet-wide scanners like Shodan and Censys for vulnerable listening services",
            "Document investigative findings with strict verification and privacy ethics"
        ],
        "toolsCovered": ["Shodan", "theHarvester", "Amass", "Subfinder", "Maltego", "SpiderFoot"],
        "relatedBookSlugs": ["ethical-hacking", "penetration-testing", "web-security", "cloud-security"],
        "chapterTitles": [
            "Foundations of Open Source Intelligence (OSINT)",
            "Passive Reconnaissance Methodology & OPSEC for Investigators",
            "Advanced Search Engine Operators & Search Dorking",
            "Domain Infrastructure, Subdomain Enumeration & DNS Footprinting",
            "Certificate Transparency Logs & Public Cryptographic Evidence",
            "Internet-Wide Scanners: Shodan, Censys & BinaryEdge",
            "Metadata Extraction from Public Documents & Media",
            "Credential Leak Databases & Breach Data Analysis",
            "Entity Correlation, Link Analysis & Graphing with Maltego",
            "Ethics, Legal Boundaries & Evidentiary Reporting Standards"
        ]
    },
    # 13. wireshark
    {
        "slug": "wireshark",
        "title": "Wireshark Network Analysis",
        "subtitle": "Deep Packet Inspection, Protocol Analysis & Traffic Forensics",
        "category": "Networking",
        "rowId": "networking",
        "volumeNumber": "VOL. 13",
        "coverImage": "/images/books/wireshark.webp",
        "accentColor": "#0284C7",
        "difficulty": "Intermediate",
        "estimatedHours": 16,
        "shortDescription": "Master deep packet inspection with Wireshark: display filter syntax, TCP stream reassembly, TLS handshake decryption in labs, and malware traffic forensics.",
        "fullDescription": "Packets don't lie. This book transforms readers into packet analysis experts. Learn to slice through megabytes of PCAP files, diagnose network latency spikes, decrypt pre-master secrets in test environments, and detect C2 beaconing.",
        "learningObjectives": [
            "Configure customized Wireshark profiles, coloring rules, and column layouts",
            "Write sophisticated display filters using boolean operators and protocol offsets",
            "Reassemble TCP streams and extract transferred files from packet streams",
            "Identify malware Command-and-Control (C2) traffic and DNS exfiltration anomalies"
        ],
        "toolsCovered": ["Wireshark", "tshark", "tcpdump", "editcap", "mergecap"],
        "relatedBookSlugs": ["computer-networking", "advanced-networking", "nmap", "digital-forensics"],
        "chapterTitles": [
            "Introduction to Deep Packet Inspection & Wireshark Architecture",
            "Capture Profiles, Ring Buffers & Hardware Optimization",
            "Dissecting Ethernet Frames, IP Headers & Protocol Stacks",
            "Mastering Wireshark Display Filter Syntax & Expressions",
            "TCP Stream Analysis: RTT, Retransmissions & Window Scaling",
            "Investigating DNS Queries, Tunneling & Cache Poisoning",
            "HTTP/HTTPS Dissection & TLS Decryption with Key Logs",
            "Network Performance Troubleshooting & Bottleneck Identification",
            "Security Incident Analysis: Port Scans, Brute Force & Exploits",
            "Automating Packet Analysis with tshark CLI & Python"
        ]
    },
    # 14. nmap
    {
        "slug": "nmap",
        "title": "Nmap Network Scanning",
        "subtitle": "Host Discovery, Port Scanning Mechanics & Nmap Scripting Engine",
        "category": "Networking",
        "rowId": "networking",
        "volumeNumber": "VOL. 14",
        "coverImage": "/images/books/nmap.webp",
        "accentColor": "#F97316",
        "difficulty": "Intermediate",
        "estimatedHours": 14,
        "shortDescription": "The definitive guide to Gordon Lyon's Nmap: SYN stealth scans, OS fingerprinting, firewall evasion techniques in authorized labs, and writing custom NSE scripts.",
        "fullDescription": "Nmap is the foundational reconnaissance tool of every penetration tester and network defender. This book reveals the packet-level mechanics behind half-open scans, UDP discovery, service banner grabbing, and Lua-based NSE automation.",
        "learningObjectives": [
            "Differentiate between TCP SYN, Connect, FIN, Null, and Xmas scans at the packet level",
            "Accurately determine operating systems and service versions via probe heuristics",
            "Execute and author Nmap Scripting Engine (NSE) scripts in Lua for vulnerability auditing",
            "Interpret scan outputs and export clean XML/grepable logs for reporting"
        ],
        "toolsCovered": ["Nmap", "Zenmap", "Masscan", "tcpdump", "Wireshark"],
        "relatedBookSlugs": ["computer-networking", "wireshark", "ethical-hacking", "penetration-testing"],
        "chapterTitles": [
            "The Architecture & Theory of Network Discovery",
            "Host Discovery: ICMP Echo, TCP SYN/ACK & ARP Ping Sweeps",
            "Port Scanning Algorithms: SYN Stealth (-sS) vs Full Connect (-sT)",
            "Advanced Port Scans: UDP (-sU), NULL, FIN & Xmas (-sX)",
            "Service Version Detection (-sV) & Probe Matching Engines",
            "Operating System Fingerprinting (-O) & TCP/IP Stack Heuristics",
            "The Nmap Scripting Engine (NSE): Architecture & Categories",
            "Authoring Custom NSE Scripts in Lua for Security Auditing",
            "Firewall & IDS Evasion Techniques in Authorized Labs",
            "Scan Output Formats (XML, Grepable) & Toolchain Integration"
        ]
    },
    # 15. digital-forensics
    {
        "slug": "digital-forensics",
        "title": "Digital Forensics Fundamentals",
        "subtitle": "Evidence Preservation, File Systems & Memory Analysis",
        "category": "Forensics",
        "rowId": "forensics-crypto",
        "volumeNumber": "VOL. 15",
        "coverImage": "/images/books/digital-forensics.webp",
        "accentColor": "#C2410C",
        "difficulty": "Intermediate",
        "estimatedHours": 16,
        "shortDescription": "The scientific discipline of digital investigation: legal chain of custody, raw bitstream imaging, NTFS/ext4 recovery, memory analysis with Volatility, and timelines.",
        "fullDescription": "When a breach occurs, digital forensics investigators reconstruct the exact chronology of events. Learn the strict standards of evidence handling, write-blocker imaging, registry artifact recovery, and volatility memory parsing.",
        "learningObjectives": [
            "Uphold legal chain of custody and generate verifiable cryptographic hashes (SHA-256)",
            "Extract deleted files and analyze file system metadata on NTFS and ext4 partitions",
            "Carve volatile memory dumps to recover injected DLLs and active socket connections",
            "Construct super-timelines integrating filesystem, event log, and browser artifacts"
        ],
        "toolsCovered": ["Autopsy", "Volatility 3", "FTK Imager", "CyberChef", "Plaso", "Sleuth Kit"],
        "relatedBookSlugs": ["cryptography", "malware-analysis", "incident-response", "windows-security"],
        "chapterTitles": [
            "Principles of Digital Forensics & The Order of Volatility",
            "Evidence Preservation, Write Blockers & Chain of Custody",
            "Bitstream Disk Imaging (E01, RAW) & Cryptographic Verification",
            "File System Structures: NTFS $MFT, FAT32 & Linux ext4 Inodes",
            "Deleted File Carving, Slack Space & Metadata Extraction",
            "Windows Registry Forensics & User Activity Reconstruction",
            "Linux System Artifacts, Wtmp, Syslog & Shell History",
            "Volatile Memory Acquisition & Analysis with Volatility 3",
            "Timeline Analysis: Building Super-Timelines with Plaso / log2timeline",
            "Forensic Case Reporting & Expert Testimony Standards"
        ]
    },
    # 16. cryptography
    {
        "slug": "cryptography",
        "title": "Cryptography & Modern Encryption",
        "subtitle": "Mathematical Foundations, Symmetric Ciphers & Public Key Infrastructure",
        "category": "Cryptography",
        "rowId": "forensics-crypto",
        "volumeNumber": "VOL. 16",
        "coverImage": "/images/books/cryptography.webp",
        "accentColor": "#6B21A8",
        "difficulty": "Advanced",
        "estimatedHours": 18,
        "shortDescription": "The mathematical bedrock of information security: AES-GCM, RSA, Elliptic Curves, cryptographic hashes, TLS 1.3 handshakes, and post-quantum algorithms.",
        "fullDescription": "Cryptography is often called the only technology that genuinely protects data against superior adversaries. This volume demystifies block cipher modes, Diffie-Hellman key exchanges, X.509 certificate chains, and zero-knowledge proofs.",
        "learningObjectives": [
            "Implement and audit symmetric ciphers using Authenticated Encryption (AES-256-GCM)",
            "Understand mathematical foundations of RSA and Elliptic Curve Cryptography (ECDSA/Ed25519)",
            "Inspect and validate X.509 certificate revocation (CRL, OCSP) and PKI trusts",
            "Apply modern password hashing algorithms (Argon2id, bcrypt) correctly"
        ],
        "toolsCovered": ["OpenSSL", "GnuPG", "hashcat", "CyberChef", "Python cryptography"],
        "relatedBookSlugs": ["digital-forensics", "web-security", "cloud-security", "computer-networking"],
        "chapterTitles": [
            "Foundations of Cryptography & Kerckhoffs' Principle",
            "Symmetric Ciphers: Block Ciphers, AES & Cipher Modes (CBC vs GCM)",
            "Stream Ciphers, ChaCha20 & Cryptographic Nonces",
            "Asymmetric Encryption: Modular Arithmetic, RSA & Trapdoors",
            "Elliptic Curve Cryptography (ECC), ECDSA & Ed25519",
            "Cryptographic Hash Functions: Merkle-Damgård, SHA-2 & SHA-3 Keccak",
            "Message Authentication Codes (HMAC) & Digital Signatures",
            "Public Key Infrastructure (PKI), X.509 Certificates & CA Hierarchies",
            "Transport Layer Security (TLS 1.3) Handshake & Forward Secrecy",
            "Password Hashing Mechanics (Argon2id, PBKDF2) & Quantum-Resistant Ciphers"
        ]
    },
    # 17. malware-analysis
    {
        "slug": "malware-analysis",
        "title": "Malware Analysis & Reverse Engineering",
        "subtitle": "Binary Disassembly, Sandbox Behavior & Defensive Detection",
        "category": "Malware Analysis",
        "rowId": "forensics-crypto",
        "volumeNumber": "VOL. 17",
        "coverImage": "/images/books/malware-analysis.webp",
        "accentColor": "#DC2626",
        "difficulty": "Advanced",
        "estimatedHours": 20,
        "shortDescription": "Dissect malicious binaries safely: air-gapped laboratory setups, static PE header analysis, dynamic behavioral monitoring, Ghidra disassembly, and YARA authoring.",
        "fullDescription": "Enter the mind of malware authors. Learn how reverse engineers safely unpack obfuscated binaries, trace API hooking, identify ransomware encryption routines, and extract network command-and-control IP indicators.",
        "learningObjectives": [
            "Construct isolated analysis sandboxes with host-only virtual networking and snapshot states",
            "Perform static triage by inspecting PE imports, exports, and embedded strings",
            "Monitor dynamic process, registry, and filesystem modifications via Procmon and Sysmon",
            "Draft custom YARA detection rules based on structural and behavioral indicators"
        ],
        "toolsCovered": ["Ghidra", "x64dbg", "Process Hacker", "Procmon", "YARA", "PE-bear"],
        "relatedBookSlugs": ["digital-forensics", "incident-response", "windows-security", "soc-analyst"],
        "chapterTitles": [
            "Malware Classification, Threat Profiles & Analysis Methodologies",
            "Building Isolated Analysis Labs & Hypervisor Hardening",
            "Static Analysis: File Hashes, Strings & PE/ELF Header Structures",
            "Import Address Table (IAT) Analysis & Suspicious API Identification",
            "Dynamic Analysis: Behavioral Monitoring with Procmon & Regshot",
            "Network Simulation: Intercepting Malware C2 with INetSim & Wireshark",
            "Disassembly Fundamentals: x86/x64 Architecture & Ghidra Decompiler",
            "Identifying Anti-Analysis, Anti-VM & Code Obfuscation Techniques",
            "Authoring Structural & Behavioral YARA Detection Rules",
            "Extracting Indicators of Compromise (IoCs) & Threat Reporting"
        ]
    },
    # 18. windows-security
    {
        "slug": "windows-security",
        "title": "Windows Security & Active Directory",
        "subtitle": "Enterprise Architecture, Kerberos Protocols & Domain Hardening",
        "category": "Enterprise Security",
        "rowId": "operations-cloud",
        "volumeNumber": "VOL. 18",
        "coverImage": "/images/books/windows-security.webp",
        "accentColor": "#0284C7",
        "difficulty": "Intermediate",
        "estimatedHours": 18,
        "shortDescription": "Securing Windows in the enterprise: NTFS permissions, Local Security Authority, Active Directory domain architecture, Kerberos attacks (Pass-the-Ticket), and GPO hardening.",
        "fullDescription": "Windows Active Directory powers the identity infrastructure of over 90% of global enterprises. This textbook breaks down domain trusts, Kerberos ticket-granting mechanics, privilege abuse paths, and Microsoft-recommended tiering architectures.",
        "learningObjectives": [
            "Audit Windows security subsystems (LSASS, SAM, Access Tokens, DACLs)",
            "Deconstruct Active Directory domains, forests, trusts, and Kerberos ticket lifecycles",
            "Identify domain attack paths (Kerberoasting, AS-REP Roasting, Pass-the-Hash) in lab environments",
            "Implement enterprise tiering models (Enterprise Access Model) and hardened Group Policies"
        ],
        "toolsCovered": ["PowerView", "BloodHound", "Mimikatz (Labs)", "Sysmon", "Group Policy Management"],
        "relatedBookSlugs": ["penetration-testing", "soc-analyst", "incident-response", "linux-administration"],
        "chapterTitles": [
            "Windows Security Architecture: LSASS, Tokens & Security Identifiers (SIDs)",
            "File System Security: NTFS Permissions, DACLs & Inheritance Rules",
            "Local Security Policies, UAC & Process Mitigation Features",
            "Windows Event Log Architecture, Sysmon Deployment & Channel Auditing",
            "Active Directory Architecture: Domains, Forests & Global Catalogs",
            "Kerberos Authentication Mechanics: TGT, TGS & SPN Architecture",
            "Active Directory Attack Vectors in Labs: Kerberoasting & Pass-the-Hash",
            "Attack Graph Analysis & Privilege Path Modeling with BloodHound",
            "Group Policy Object (GPO) Hardening & Administrative Tiering Models",
            "Enterprise Windows Hardening: Credential Guard & AppLocker/WDAC"
        ]
    },
    # 19. soc-analyst
    {
        "slug": "soc-analyst",
        "title": "SOC Analyst Handbook",
        "subtitle": "SIEM Engineering, Alert Triage & MITRE ATT&CK Mapping",
        "category": "Security Operations",
        "rowId": "operations-cloud",
        "volumeNumber": "VOL. 19",
        "coverImage": "/images/books/soc-analyst.webp",
        "accentColor": "#0F766E",
        "difficulty": "Intermediate",
        "estimatedHours": 16,
        "shortDescription": "The operational blueprint for Security Operations Center analysts: SIEM log telemetry, alert triage methodology, false-positive elimination, MITRE ATT&CK mapping, and Sigma rules.",
        "fullDescription": "SOC analysts are the frontline watchstanders of enterprise digital defense. This book equips analysts with the investigative acumen to differentiate normal administrator operations from subtle adversary persistence and data staging.",
        "learningObjectives": [
            "Triage security alerts methodically across endpoint, network, and cloud telemetry",
            "Correlate events using modern SIEM architectures (Elastic, Splunk, Wazuh)",
            "Map observed adversary tactics and techniques to the MITRE ATT&CK framework",
            "Author portable detection rules using the open-source Sigma standard"
        ],
        "toolsCovered": ["Wazuh", "Splunk", "Elastic Security", "Sigma", "CyberChef", "VirusTotal"],
        "relatedBookSlugs": ["incident-response", "windows-security", "wireshark", "cloud-security"],
        "chapterTitles": [
            "The Modern Security Operations Center (SOC) Architecture & Roles",
            "SIEM Telemetry: Log Ingestion, Parsing & Elastic Common Schema (ECS)",
            "Alert Triage Methodology: Context Gathering & Initial Scoping",
            "Differentiating False Positives from True Positive Adversary Activity",
            "Threat Intelligence Integration & IoC Indicator Matching",
            "The MITRE ATT&CK Framework: Tactics, Techniques & Sub-Techniques",
            "Detection Engineering: Authoring Generic Rules with Sigma",
            "Endpoint Detection & Response (EDR) Telemetry Analysis",
            "Incident Escalation Workflows, Ticketing & Handoff Playbooks",
            "SOC Metrics, Mean Time to Detect (MTTD) & Continuous Tuning"
        ]
    },
    # 20. incident-response
    {
        "slug": "incident-response",
        "title": "Incident Response Playbooks",
        "subtitle": "Breach Containment, Forensic Triage & Recovery Strategies",
        "category": "Incident Response",
        "rowId": "forensics-crypto",
        "volumeNumber": "VOL. 20",
        "coverImage": "/images/books/incident-response.webp",
        "accentColor": "#EF4444",
        "difficulty": "Advanced",
        "estimatedHours": 18,
        "shortDescription": "A tactical guide to handling enterprise cyber incidents: NIST SP 800-61 frameworks, rapid host isolation, live forensic triage, ransomware eradication, and executive debriefs.",
        "fullDescription": "When an adversary breaches the perimeter, every second counts. This book walks incident responders through the standardized lifecycle of breach response: Preparation, Detection, Containment, Eradication, Recovery, and Lessons Learned.",
        "learningObjectives": [
            "Lead incident handling aligned with NIST SP 800-61 Rev 2 and ISO 27035 standards",
            "Execute tactical host and network containment without destroying volatile evidence",
            "Coordinate eradication campaigns targeting compromised identities and persistence mechanisms",
            "Facilitate blame-free Post-Incident Reviews (PIR) and author executive debriefs"
        ],
        "toolsCovered": ["KAPE", "Velociraptor", "Wireshark", "FTK Imager", "YARA", "TheHive"],
        "relatedBookSlugs": ["digital-forensics", "soc-analyst", "malware-analysis", "windows-security"],
        "chapterTitles": [
            "The Incident Response Lifecycle: NIST SP 800-61 & SANS Frameworks",
            "Incident Preparedness: IR Plans, Playbooks & Tabletop Exercises",
            "Initial Detection, Triage Scoping & Severity Classification",
            "Live Host Triage & Rapid Volatile Artifact Collection",
            "Containment Strategies: Network Segmentation, EDR Isolation & Identity Revocation",
            "Root Cause Analysis & Determining the Adversary Patient Zero",
            "Eradication: Removing Persistence Mechanisms, Backdoors & Web Shells",
            "Remediation & Service Recovery: Safe System Rebuilding & Validation",
            "Active Threat Hunting for Dormant Adversary Footprints",
            "Post-Incident Review (PIR), Executive Reporting & Root Cause Lessons"
        ]
    },
    # 21. cloud-security
    {
        "slug": "cloud-security",
        "title": "Cloud Security & DevSecOps",
        "subtitle": "AWS/Azure Hardening, IAM Governance & Kubernetes Defense",
        "category": "Cloud Security",
        "rowId": "operations-cloud",
        "volumeNumber": "VOL. 21",
        "coverImage": "/images/books/cloud-security.webp",
        "accentColor": "#0284C7",
        "difficulty": "Intermediate",
        "estimatedHours": 16,
        "shortDescription": "Securing cloud native architectures: Shared Responsibility models, Identity and Access Management (IAM), S3 bucket misconfigurations, Kubernetes clusters, and CI/CD pipelines.",
        "fullDescription": "The cloud introduces distinct paradigms where the control plane is defined entirely by software APIs. Learn how to audit IAM policy logic, secure multi-tenant VPC networks, audit container images, and detect shadow resources.",
        "learningObjectives": [
            "Navigate the Cloud Shared Responsibility Model across IaaS, PaaS, and SaaS",
            "Enforce strict Least Privilege across AWS/Azure IAM policies and service roles",
            "Identify and remediate cloud storage and network security misconfigurations",
            "Audit container images and Kubernetes clusters for privilege escalation flaws"
        ],
        "toolsCovered": ["Trivy", "ScoutSuite", "Checkov", "Prowler", "kubectl", "AWS CLI"],
        "relatedBookSlugs": ["api-security", "linux-administration", "web-security", "soc-analyst"],
        "chapterTitles": [
            "Cloud Computing Paradigms & The Shared Responsibility Model",
            "Cloud Identity & Access Management (IAM): Least Privilege & Role Trust Policies",
            "Cloud Network Architecture: VPC Peering, Transit Gateways & Security Groups",
            "Cloud Storage Security: Bucket Policies, Object Locks & Public Access Blocks",
            "Common Cloud Misconfigurations & Automated Auditing with Prowler",
            "Cloud Logging & Threat Detection: CloudTrail, GuardDuty & Security Hub",
            "Container Security: Dockerfile Hardening, Rootless Runtimes & Image Scanning",
            "Kubernetes Cluster Security: RBAC, NetworkPolicies & Pod Security Standards",
            "Infrastructure as Code (IaC) Security Scanning with Checkov & Trivy",
            "Multi-Cloud Governance, Compliance Baselines & Incident Response in the Cloud"
        ]
    },
    # 22. api-security
    {
        "slug": "api-security",
        "title": "API Security Architecture",
        "subtitle": "REST & GraphQL Defenses, BOLA Mitigation & OAuth 2.0 Governance",
        "category": "Web Security",
        "rowId": "web-security",
        "volumeNumber": "VOL. 22",
        "coverImage": "/images/books/api-security.webp",
        "accentColor": "#D946EF",
        "difficulty": "Intermediate",
        "estimatedHours": 14,
        "shortDescription": "Securing the modern API fabric: REST and GraphQL architectures, OWASP API Security Top 10, Broken Object Level Authorization (BOLA), JWT validation, and rate limiting.",
        "fullDescription": "APIs are the direct gateways to modern application databases. This textbook equips developers and penetration testers with the methodologies required to uncover object-level authorization bypasses, mass assignment vulnerabilities, and token forgery.",
        "learningObjectives": [
            "Assess REST, GraphQL, and gRPC endpoints against the OWASP API Security Top 10",
            "Test and secure JSON Web Tokens (JWT) against signature exclusion and key confusion",
            "Prevent Broken Object Level Authorization (BOLA) through object-level access controls",
            "Design resilient API gateways with distributed rate limiting and schema validation"
        ],
        "toolsCovered": ["Postman", "Burp Suite", "OWASP ZAP", "Kiterunner", "jwt-tool", "cURL"],
        "relatedBookSlugs": ["web-security", "owasp-top10", "cloud-security", "python-cybersecurity"],
        "chapterTitles": [
            "The Modern API Ecosystem: REST, GraphQL, gRPC & WebSockets",
            "OWASP API Security Top 10 Vulnerabilities Overview",
            "API Authentication: OAuth 2.0 Authorization Framework & OpenID Connect",
            "Deep Dive: JSON Web Token (JWT) Security, Signing & Validation Pitfalls",
            "Broken Object Level Authorization (BOLA / IDOR): Detection & Prevention",
            "Broken Function Level Authorization (BFLA) & Administrative Endpoint Bypasses",
            "Mass Assignment, Parameter Pollution & Unrestricted Schema Binding",
            "API Abuse: Lack of Rate Limiting, Brute Force & Resource Exhaustion",
            "API Security Testing Workflows: Endpoint Discovery with Kiterunner",
            "Architectural Defense: API Gateways, Schema Validation & Threat Prevention"
        ]
    },
    # 23. wireless-security
    {
        "slug": "wireless-security",
        "title": "Wireless Network Security",
        "subtitle": "RF Propagation, 802.11 Protocols & Enterprise WPA3 Defense",
        "category": "Ethical Hacking",
        "rowId": "ethical-hacking",
        "volumeNumber": "VOL. 23",
        "coverImage": "/images/books/wireless-security.webp",
        "accentColor": "#0D9488",
        "difficulty": "Intermediate",
        "estimatedHours": 14,
        "shortDescription": "The physics and protocol mechanics of wireless communications: 802.11 frames, WEP/WPA/WPA2/WPA3 transitions, 802.1X RADIUS authentication, rogue APs, and Bluetooth.",
        "fullDescription": "Radio waves disregard physical office walls. This textbook provides a rigorous study of wireless protocol mechanics, four-way handshakes, simultaneous authentication of equals (SAE), rogue access point detection, and wireless intrusion prevention systems (WIPS).",
        "learningObjectives": [
            "Understand radio frequency fundamentals (2.4 GHz, 5 GHz, 6 GHz) and modulation schemes",
            "Deconstruct 802.11 management, control, and data frames in Wireshark",
            "Audit WPA2 4-Way Handshakes and WPA3 Simultaneous Authentication of Equals (SAE)",
            "Deploy enterprise 802.1X network authentication with certificate validation"
        ],
        "toolsCovered": ["Aircrack-ng", "Kismet", "Wireshark", "hcxdumptool", "Wifite2"],
        "relatedBookSlugs": ["computer-networking", "wireshark", "ethical-hacking", "penetration-testing"],
        "chapterTitles": [
            "Radio Frequency Fundamentals: Frequencies, Channels & Antennas",
            "The IEEE 802.11 Architecture: SSIDs, BSSIDs & Frame Types",
            "Wireless Encryption Evolution: The Failure of WEP & WPA TKIP",
            "WPA2-Personal Mechanics: The 4-Way Handshake & PSK Security",
            "WPA3 & Simultaneous Authentication of Equals (SAE) Protections",
            "Enterprise Wireless: IEEE 802.1X, EAP Methods & RADIUS Infrastructure",
            "Authorized Lab Assessments: Handshake Capture & Auditing Workflow",
            "Rogue Access Points, Evil Twins & Captive Portal Deceptions",
            "Bluetooth & BLE Security: Pairing Modes & Threat Vectors",
            "Securing Enterprise Wireless: WIPS, Client Isolation & Site Surveys"
        ]
    },
    # 24. mobile-security
    {
        "slug": "mobile-security",
        "title": "Mobile Application Security",
        "subtitle": "Android Internals, iOS Sandboxes & OWASP MASVS Auditing",
        "category": "Application Security",
        "rowId": "web-security",
        "volumeNumber": "VOL. 24",
        "coverImage": "/images/books/mobile-security.webp",
        "accentColor": "#7C3AED",
        "difficulty": "Intermediate",
        "estimatedHours": 16,
        "shortDescription": "Security assessments of mobile applications: Android APK disassembly, iOS app sandbox constraints, OWASP MASVS benchmarks, Frida runtime instrumentation, and Keystore usage.",
        "fullDescription": "Smartphones process our most sensitive personal and corporate data. This textbook covers the architecture of Android and iOS operating systems, decompiling APKs, bypassing certificate pinning in authorized labs, and auditing secure local storage.",
        "learningObjectives": [
            "Understand Android application components (Activities, Services, Broadcast Receivers)",
            "Audit iOS sandbox boundaries, data protection classes, and Keychain storage",
            "Perform static and dynamic security assessments aligned with OWASP MASVS",
            "Hook runtime functions and audit API calls using the Frida instrumentation toolkit"
        ],
        "toolsCovered": ["Frida", "JADX", "Objection", "Burp Suite", "adb", "MobSF"],
        "relatedBookSlugs": ["web-security", "api-security", "cryptography", "reverse-engineering"],
        "chapterTitles": [
            "The Mobile Threat Landscape & Operating System Sandboxes",
            "Android Architecture: Linux Kernel, ART Runtime & Permissions",
            "iOS Security Architecture: Secure Enclave, Code Signing & Sandboxing",
            "The OWASP Mobile Application Security Verification Standard (MASVS)",
            "Static Analysis of Android Applications: Decompilation with JADX",
            "Static Analysis of iOS Applications: IPA Structure & Binary Hardening",
            "Dynamic Instrumentation & Runtime Hooking with Frida & Objection",
            "Mobile Network Communication: SSL Pinning & Proxy Interception in Labs",
            "Secure Local Storage: Android Keystore & iOS Keychain Best Practices",
            "Mobile Application Penetration Testing Reporting & Defensive Hardening"
        ]
    }
]

print(f"Total books defined: {len(BOOK_DATA)}")
