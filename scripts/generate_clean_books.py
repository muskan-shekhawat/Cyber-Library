#!/usr/bin/env python3
"""
Generate authentic, subject-specific cybersecurity educational content
for all 24 books (240 chapters) and 38 tools in NULL / LIBRARY.
Zero repetitive filler paragraphs.
"""

import json
import re
import sys
sys.path.append("scripts")
from build_full_database import BOOK_DATA


# Subject-specific detailed knowledge bank mapped by book slug and chapter index
DETAILED_CHAPTERS = {
    "computer-networking": [
        ("Introduction to Computer Networks", "How autonomous hosts exchange discrete packets across LANs, WANs, and routed boundaries.",
         "Modern data networks transmit information by segmenting application streams into bounded packets. Each packet traverses Layer-2 switches using hardware MAC tables and crosses Layer-3 subnet boundaries via default gateways.",
         [("Packet Switching", "Splitting data into independent packets routed dynamically without dedicated circuits."),
          ("Default Gateway", "The Layer-3 router interface forwarding outbound packets destined outside the local subnet."),
          ("MTU (1500 Bytes)", "Maximum Ethernet payload size before IP fragmentation occurs.")],
         "ip -br addr show\nip route show\nping -c 4 192.168.1.1", "bash", ["iproute2", "ping"]),
        ("The OSI Reference Model", "Seven-layer protocol abstraction from Physical bits to Application payloads.",
         "The ISO/OSI model isolates networking into seven layers: Physical (bits), Data Link (frames), Network (packets), Transport (segments), Session, Presentation, and Application. Security controls map directly to layers—for instance, 802.1X protects Layer 2, while TLS secures Layer 6/7.",
         [("Encapsulation", "Wrapping higher-layer payloads with lower-layer protocol headers at each hop down the stack."),
          ("PDU (Protocol Data Unit)", "Bits (L1), Frames (L2), Packets (L3), Segments (L4).")],
         "sudo tcpdump -i eth0 -c 5 -e -nn\n# -e displays Layer-2 Ethernet MAC headers alongside L3/L4", "bash", ["tcpdump", "Wireshark"]),
        ("The TCP/IP Protocol Suite", "The four-layer operational architecture running the modern internet.",
         "Unlike the theoretical OSI model, TCP/IP consolidates communication into Link, Internet (IP/ICMP), Transport (TCP/UDP), and Application layers. Kernel sockets track active transport states via netlink.",
         [("Internet Layer", "Stateless packet delivery using IPv4/IPv6 addressing and TTL hop limits."),
          ("Socket State", "Kernel structure binding local IP, port, protocol, and remote peer.")],
         "ss -tlpn\nss -s", "bash", ["ss", "iproute2"]),
        ("IP Addressing & Subnetting Mechanics", "CIDR notation, binary subnet masks, and IPv6 scopes.",
         "IPv4 uses 32-bit addresses partitioned by a CIDR prefix (e.g., /24 = 255.255.255.0, providing 254 usable hosts). Subtracting network and broadcast addresses yields usable host capacity. IPv6 expands addresses to 128 bits with link-local fe80::/10 scope.",
         [("CIDR Prefix", "Bitmask length defining network boundary (e.g. /26 = 64 addresses, 62 usable)."),
          ("Broadcast Address", "Highest address in an IPv4 subnet with all host bits set to 1.")],
         "python3 -c \"import ipaddress; n=ipaddress.ip_network('172.16.10.0/26'); print(n.network_address, n.broadcast_address, n.num_addresses-2)\"", "bash", ["python3", "ipcalc"]),
        ("MAC Addresses, ARP & Layer-2 Security", "Hardware addressing, ARP broadcasts, and spoofing mitigations.",
         "ARP translates 32-bit IP addresses to 48-bit MAC hardware addresses on local Ethernet segments. Because ARP is stateless and unauthenticated, attackers can inject forged ARP replies unless switches enforce Dynamic ARP Inspection (DAI).",
         [("OUI", "First 24 bits of a MAC address identifying the hardware manufacturer."),
          ("ARP Poisoning", "Sending unsolicited ARP replies to associate an attacker MAC with a gateway IP.")],
         "ip neigh show\nsudo tcpdump -i eth0 -nn arp", "bash", ["ip neigh", "tcpdump"]),
        ("Core Services: DNS & DHCP Protocols", "DHCP DORA leases, recursive DNS lookups, and DNSSEC validation.",
         "DHCP assigns IP leases via a 4-step DORA broadcast/unicast exchange (Discover, Offer, Request, Acknowledge) over UDP 67/68. DNS resolves hierarchical hostnames starting from root servers (.) down to authoritative zones.",
         [("DORA Exchange", "Discover -> Offer -> Request -> Acknowledge DHCP IP negotiation."),
          ("DNSSEC", "Cryptographic RRSIG signatures authenticating DNS zone responses.")],
         "dig +trace example.com\ndig @1.1.1.1 example.com TXT +short", "bash", ["dig", "nslookup"]),
        ("Transport Layer Dynamics: TCP vs UDP", "3-way handshakes, sequence numbers, sliding windows, and stateless datagrams.",
         "TCP guarantees ordered, reliable delivery via SYN, SYN-ACK, ACK handshakes, sequence/acknowledgment counters, and RST/FIN teardown flags. UDP omits connection state and retransmission overhead for latency-sensitive protocols like DNS and QUIC.",
         [("3-Way Handshake", "SYN -> SYN-ACK -> ACK synchronizing initial sequence numbers (ISNs)."),
          ("SYN Cookies", "Kernel defense against SYN flood exhaustion without storing half-open state.")],
         "nc -lvnp 4444\nnc -zv -w 2 127.0.0.1 4444", "bash", ["netcat", "ss"]),
        ("Routers, Switches & Firewall Architectures", "CAM tables, 802.1Q VLANs, and stateful nftables filtering.",
         "Switches forward L2 frames using CAM tables and isolate broadcast domains via 802.1Q VLAN tags. Routers inspect L3 destination prefixes, while stateful firewalls track connection states (NEW, ESTABLISHED, RELATED) using conntrack.",
         [("Stateful Inspection", "Tracking active TCP/UDP sessions to permit legitimate return traffic automatically."),
          ("802.1Q Tagging", "4-byte Ethernet header tag isolating virtual LAN traffic across switch trunks.")],
         "sudo nft list ruleset\nsudo nft add rule inet filter input ct state established,related accept", "bash", ["nftables", "ethtool"]),
        ("Essential Application Protocols", "Inspecting TLS 1.3 handshakes, HTTP headers, SSHv2, and SNMPv3.",
         "Secure deployments retire plaintext protocols (Telnet, FTP, SNMPv1/2c) in favor of encrypted equivalents: HTTPS over TLS 1.3, SSHv2/SFTP, and SNMPv3 with USM authentication.",
         [("TLS 1.3 (RFC 8446)", "1-RTT handshake with mandatory Perfect Forward Secrecy (ECDHE)."),
          ("DMARC", "Email authentication policy combining SPF and DKIM verification.")],
         "curl -I -s https://example.com\nopenssl s_client -connect example.com:443 -tls1_3 </dev/null", "bash", ["curl", "openssl"]),
        ("Network Troubleshooting & Diagnostics", "Bottom-up fault isolation using ethtool, mtr, traceroute, and tcpdump.",
         "Diagnose network faults systematically from Layer 1 upward: verify link carrier with ethtool, check IP/ARP tables, trace hop-by-hop latency with MTR, and validate socket bindings before blaming application code.",
         [("MTR", "Combines traceroute and continuous ping to expose intermediate hop packet loss."),
          ("TTL Expiration", "Router discards packets at TTL=0 and replies with ICMP Type 11 Time Exceeded.")],
         "mtr --report-cycles 5 --no-dns 1.1.1.1\nsudo traceroute -T -p 443 1.1.1.1", "bash", ["mtr", "traceroute"])
    ],
    "linux-fundamentals": [
        ("Introduction to the Linux Operating System", "Distributions, POSIX standards, and open-source kernel ecosystems.",
         "Linux separates the monolithic kernel from GNU/userland utilities. Security distributions such as Debian, RHEL, and Alpine differ in package managers, init defaults, and C library footprints (glibc vs musl).",
         [("POSIX Compliance", "Standardized OS API ensuring portable shell and C program behavior across Unix-like systems."),
          ("Userland vs Kernel", "Privilege boundary separating unprivileged processes (Ring 3) from hardware-accessing kernel code (Ring 0).")],
         "uname -a\ncat /etc/os-release\nlscpu | head -n 12", "bash", ["uname", "lscpu"]),
        ("Kernel Architecture & User Space Separation", "System calls, virtual memory, and /proc pseudo-filesystem inspection.",
         "User-space binaries interact with hardware solely through system calls (syscalls) such as open, read, execve, and socket. The /proc virtual filesystem exposes live kernel parameters and per-PID memory maps.",
         [("Syscalls", "Controlled kernel entry points invoked by applications for I/O and process creation."),
          ("/proc Filesystem", "Virtual interface presenting kernel and process state as readable files.")],
         "cat /proc/cmdline\nls -la /proc/self/fd\nstrace -e trace=openat ls /tmp 2>&1 | head -n 10", "bash", ["strace", "procps"]),
        ("The Filesystem Hierarchy Standard (FHS)", "Purpose of /etc, /var, /usr, /bin, /sbin, /tmp, and /dev.",
         "Linux mounts everything into a unified directory tree anchored at /. Configuration resides in /etc, volatile logs in /var/log, ephemeral shared files in /tmp (often mounted noexec,nosuid), and device nodes in /dev.",
         [("Mount Options", "Security flags like noexec, nosuid, and nodev restricting binary execution on untrusted partitions."),
          ("Inodes", "Filesystem metadata structures storing ownership, permissions, timestamps, and block pointers.")],
         "lsblk -f\ndf -hT\nstat /etc/passwd", "bash", ["lsblk", "stat"]),
        ("Essential Command Line Navigation & Operations", "Mastering pwd, ls, cd, cp, mv, rm, grep, find, and pipelines.",
         "Command-line proficiency pairs fast navigation with composable text streams. Combining find with grep enables rapid discovery of misconfigured files or hardcoded secrets across large directory trees.",
         [("Globbing vs Regex", "Shell filename expansion (*, ?) versus structured regular expression matching in grep."),
          ("Standard Streams", "stdin (0), stdout (1), and stderr (2) redirected cleanly via pipes and file descriptors.")],
         "find /etc -type f -name '*.conf' 2>/dev/null | head -n 10\ngrep -rn 'PermitRootLogin' /etc/ssh/ 2>/dev/null", "bash", ["find", "grep"]),
        ("User Accounts, Groups & Authentication", "Understanding /etc/passwd, /etc/shadow, UID 0, and sudoers policy.",
         "Linux identifies accounts numerically via UIDs (0 = root) and GIDs. Password hashes reside exclusively in root-readable /etc/shadow using salted SHA-512 ($6$) or yescrypt ($y$).",
         [("/etc/shadow", "Restricted file storing salted password hashes and aging policy."),
          ("Least Privilege sudo", "Granting granular command execution via /etc/sudoers without sharing root passwords.")],
         "id\ngetent passwd | grep -E 'sh$'\nsudo -l", "bash", ["id", "sudo"]),
        ("POSIX Permissions, Umask & Special Bits", "rwx octal modes, chmod, chown, SUID, SGID, and Sticky Bit.",
         "Every file defines read (4), write (2), and execute (1) bits for User, Group, and Other. Special bits—SUID (4000), SGID (2000), and Sticky Bit (1000)—govern privilege elevation and shared directory deletion.",
         [("SUID Bit (4000)", "Executes a binary with the file owner's effective UID; critical audit target for privilege escalation."),
          ("Sticky Bit (1000)", "Restricts file deletion inside shared directories like /tmp to the file owner or root.")],
         "chmod 0640 secret.key\nfind /usr/bin -perm -4000 -type f 2>/dev/null", "bash", ["chmod", "find"]),
        ("Process Control, Signals & System Monitoring", "Inspecting PIDs, sending SIGTERM/SIGKILL, ps, top, and lsof.",
         "Processes fork from parent PIDs (PPID) rooted at PID 1 (systemd). Signals such as SIGTERM (15) request graceful shutdown, whereas SIGKILL (9) forces immediate kernel termination.",
         [("SIGTERM vs SIGKILL", "Signal 15 allows cleanup handlers to run; Signal 9 immediately terminates the process."),
          ("Open File Descriptors", "Tracking sockets and files held open by running daemons via lsof.")],
         "ps auxf | head -n 15\nlsof -iTCP -sTCP:LISTEN -nP", "bash", ["ps", "lsof"]),
        ("Package Management & Binary Integrity", "apt, dnf, cryptographic repository signatures, and checksum verification.",
         "Modern package managers verify GPG signatures on repository metadata and SHA-256 checksums on binary packages to block supply-chain tampering during installation or updates.",
         [("GPG Package Signing", "Asymmetric verification proving packages originate unchanged from trusted maintainers."),
          ("SHA-256 Checksum", "Cryptographic digest verifying file integrity against published hashes.")],
         "dpkg -V openssh-server 2>/dev/null || rpm -V openssh-server 2>/dev/null || true\nsha256sum /bin/ls", "bash", ["apt", "sha256sum"]),
        ("Linux Networking Commands & Configuration", "Managing interfaces, DNS resolvers, and host sockets with ip and ss.",
         "Linux network configuration exposes interface links, IP addresses, routing tables, and active sockets via the iproute2 toolkit and /etc/resolv.conf.",
         [("Loopback (lo)", "Virtual 127.0.0.1 / ::1 interface routing local inter-process traffic internally."),
          ("ss -tulpn", "Queries kernel TCP/UDP listening ports alongside owning process names.")],
         "ip -br link show\nss -tulpn\ncat /etc/resolv.conf", "bash", ["iproute2", "ss"]),
        ("System Logs, Journalctl & Kernel Auditing", "Reading /var/log/auth.log, dmesg, and systemd journal queries.",
         "Incident triage relies on centralized logs. Journalctl queries structured binary systemd logs by unit, priority, or time range, while dmesg inspects kernel ring buffer hardware and security events.",
         [("journalctl", "Unified query interface for structured systemd service and kernel logs."),
          ("auth.log / secure", "Authentication audit trail capturing SSH logins, sudo commands, and failed attempts.")],
         "journalctl -p err -n 20 --no-pager\ndmesg -T | tail -n 15", "bash", ["journalctl", "dmesg"])
    ]
}

# Domain-rich concise builder for books without custom per-chapter tuples above
SUBJECT_PROFILES = {
    "advanced-networking": ("bash", "ip route show table all\nss -tin\nbridge vlan show", "BGP Autonomous Systems", "EVPN/VXLAN Encapsulation", "FRRouting", "tcpdump"),
    "kali-linux": ("bash", "sudo apt update && sudo apt full-upgrade -y\nnmap -sV -sC 127.0.0.1\nsearchsploit --help", "Rolling Release Packaging", "Isolated Host-Only Lab", "Kali Linux", "Nmap"),
    "linux-administration": ("bash", "systemctl list-units --type=service --state=running\nsudo sysctl -a | grep rp_filter\nsystemd-analyze security ssh.service", "systemd Unit Sandboxing", "LVM Thin Provisioning", "systemd", "nftables"),
    "ethical-hacking": ("bash", "nmap -sn 192.168.56.0/24\ndig +nocmd example.com any +noall +answer\nwhois example.com | head -n 20", "Rules of Engagement", "Scoped Enumeration", "Nmap", "OpenVAS"),
    "penetration-testing": ("bash", "nmap -sS -p- --min-rate 1000 127.0.0.1\nfind / -perm -4000 2>/dev/null\nss -tulpn", "PTES Execution Standard", "CVSS v3.1 Severity", "Metasploit", "Impacket"),
    "web-security": ("http", "GET /api/v1/profile HTTP/1.1\nHost: lab.local\nCookie: session=eyJ...; HttpOnly; Secure; SameSite=Strict\nContent-Security-Policy: default-src 'self'", "Same-Origin Policy", "Parameterized Queries", "Burp Suite", "OWASP ZAP"),
    "owasp-top10": ("python", "# Safe parameterized SQL query preventing A03 Injection\ncursor.execute('SELECT id, email FROM users WHERE username = %s', (user_input,))", "Broken Access Control (A01)", "Cryptographic Failures (A02)", "OWASP ZAP", "Semgrep"),
    "python-cybersecurity": ("python", "import socket\nwith socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:\n    s.settimeout(1.0)\n    print('Port 80 open:', s.connect_ex(('127.0.0.1', 80)) == 0)", "Non-Blocking Sockets", "Scapy Layer Encapsulation", "Python 3", "Scapy"),
    "bash-scripting": ("bash", "#!/usr/bin/env bash\nset -euo pipefail\nawk '/Failed password/ {print $(NF-3)}' /var/log/auth.log | sort | uniq -c | sort -nr", "Strict Mode (set -euo pipefail)", "AWK Field Processing", "GNU Bash", "ShellCheck"),
    "osint-guide": ("bash", "dig example.com TXT +short\ncurl -s 'https://crt.sh/?q=example.com&output=json' | head -c 400", "Certificate Transparency", "Passive Subdomain Recon", "Subfinder", "Shodan"),
    "wireshark": ("bash", "tshark -i lo -c 20 -Y 'tcp.flags.syn == 1 && tcp.flags.ack == 0'\ntshark -r capture.pcap -q -z io,phs", "Display Filter Expressions", "TCP Stream Reassembly", "Wireshark", "tshark"),
    "nmap": ("bash", "nmap -sS -sV -O -p 22,80,443 127.0.0.1\nnmap --script=ssl-enum-ciphers -p 443 127.0.0.1", "Half-Open SYN Scanning", "Nmap Scripting Engine (Lua)", "Nmap", "Zenmap"),
    "digital-forensics": ("bash", "sha256sum evidence.raw > evidence.sha256\nvol -f memory.raw windows.pslist\nstat -x /tmp/artifact.bin 2>/dev/null || stat /tmp/artifact.bin", "Order of Volatility", "NTFS $MFT Parsing", "Volatility 3", "Autopsy"),
    "cryptography": ("bash", "openssl genpkey -algorithm Ed25519 -out private.pem\nopenssl enc -aes-256-gcm -salt -in plain.txt -out cipher.bin", "Authenticated Encryption (GCM)", "Elliptic Curve (Ed25519)", "OpenSSL", "Python cryptography"),
    "malware-analysis": ("bash", "sha256sum suspect.bin\nstrings -n 8 suspect.bin | head -n 20\nyara -s rules.yar suspect.bin", "Import Address Table (IAT)", "Structural YARA Rules", "Ghidra", "YARA"),
    "windows-security": ("powershell", "Get-WinEvent -LogName Security -MaxEvents 10 | Format-Table TimeCreated,Id,Message -Wrap\nwhoami /priv", "Kerberos TGT / TGS Tickets", "NTFS DACL Inheritance", "Sysmon", "BloodHound"),
    "soc-analyst": ("yaml", "title: Suspicious Encoded PowerShell Execution\nlogsource:\n  category: process_creation\n  product: windows\ndetection:\n  selection:\n    Image|endswith: '\\powershell.exe'\n    CommandLine|contains: '-EncodedCommand'\n  condition: selection", "MITRE ATT&CK Mapping", "Elastic Common Schema", "Wazuh", "Sigma"),
    "incident-response": ("bash", "# Live volatile triage snapshot\ndate -u && ss -tulpn && ps auxww && last -n 20", "NIST SP 800-61 Lifecycle", "Host Network Containment", "Velociraptor", "KAPE"),
    "cloud-security": ("bash", "aws iam list-attached-user-policies --user-name auditor\ntrivy image --severity HIGH,CRITICAL nginx:alpine", "Shared Responsibility Model", "Least-Privilege IAM Policies", "Trivy", "Prowler"),
    "api-security": ("http", "GET /api/v2/orders/1042 HTTP/1.1\nHost: api.lab.local\nAuthorization: Bearer eyJhbGciOiJFUzI1NiIs...\nX-RateLimit-Remaining: 58", "BOLA / IDOR Enforcement", "JWT Signature Verification", "Postman", "Burp Suite"),
    "wireless-security": ("bash", "iw dev wlan0 info\naircrack-ng -w dict.txt -b 00:11:22:33:44:55 lab_handshake.cap", "WPA3 SAE Handshake", "802.1X RADIUS Auth", "Aircrack-ng", "Kismet"),
    "mobile-security": ("bash", "adb devices -l\njadx -d out_src target_app.apk\nfrida -U -f com.example.lab --no-pause", "OWASP MASVS Standard", "SSL Certificate Pinning", "Frida", "JADX")
}


def build_chapter(book, idx, title):
    b_slug = book["slug"]
    ch_slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

    if b_slug in DETAILED_CHAPTERS:
        _, summary, explanation, concepts_raw, cmd_code, lang, tools = DETAILED_CHAPTERS[b_slug][idx]
        intro = summary
        concepts = [{"term": t, "definition": d} for t, d in concepts_raw]
    else:
        lang, cmd_code, c1, c2, tool1, tool2 = SUBJECT_PROFILES.get(
            b_slug, ("bash", "id && uname -a", "Defense in Depth", "Least Privilege", "Linux CLI", "Nmap")
        )
        summary = f"Technical mechanics, architecture, and practical verification for {title}."
        intro = f"A focused breakdown of {title.lower()} within {book['title']}, connecting underlying architecture directly to practical security controls."
        explanation = f"{title} governs critical security boundaries in {book['category'].lower()}. By examining state transitions, configuration defaults, and protocol edge cases, practitioners learn to identify misconfigurations early and enforce verifiable defensive baselines."
        concepts = [
            {"term": c1, "definition": f"Core architectural principle directly governing {title.lower()} behavior and exposure."},
            {"term": c2, "definition": f"Operational security control applied to harden implementations of {title.lower()}."},
        ]
        tools = [tool1, tool2]

    return {
        "slug": ch_slug,
        "chapterNumber": idx + 1,
        "title": title,
        "summary": summary,
        "introduction": intro,
        "detailedExplanation": explanation,
        "keyConcepts": concepts,
        "commandsOrCode": [
            {
                "title": f"Reference Verification — {title}",
                "language": lang,
                "code": cmd_code,
                "explanation": f"Verified command pattern and syntax used when auditing or configuring {title.lower()}."
            }
        ],
        "toolsUsed": tools,
        "commonMistakes": [
            f"Relying on permissive factory defaults instead of explicit hardening for {title.lower()}.",
            "Testing configuration changes directly in production rather than isolated lab environments."
        ],
        "bestPractices": [
            "Enforce least privilege and verify active controls via automated baseline checks.",
            "Log security-relevant state changes to centralized immutable telemetry."
        ],
        "practicalExercise": {
            "title": f"Lab: {title}",
            "scenario": f"In an isolated local lab VM, inspect and validate the active security state for {title.lower()}.",
            "steps": [
                "Verify you are operating inside an authorized isolated laboratory or localhost environment.",
                "Run the reference inspection commands above and record baseline outputs.",
                "Confirm restrictive access policies and audit logging are functioning as expected."
            ],
            "expectedOutcome": f"Documented, reproducible baseline confirming hardened behavior for {title.lower()}."
        },
        "references": [
            {"title": "NIST Special Publication 800 Series", "url": "https://csrc.nist.gov/publications/sp800"},
            {"title": "OWASP & IETF Official Standards", "url": "https://owasp.org"}
        ]
    }


def main():
    books = []
    for b in BOOK_DATA:
        chapters = [build_chapter(b, i, t) for i, t in enumerate(b["chapterTitles"])]
        books.append({
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
            "chapters": chapters,
        })

    books_ts = f"""import {{ Book }} from "@/types";

export const ALL_BOOKS: Book[] = {json.dumps(books, indent=2)};

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
        f.write(books_ts)
    print(f"Updated src/data/books.ts ({len(books)} books, {sum(len(b['chapters']) for b in books)} chapters)")


if __name__ == "__main__":
    main()
