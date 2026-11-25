#!/usr/bin/env python3
"""
Generate comprehensive, technically accurate cybersecurity educational books and chapters
for all 24 volumes in NULL / LIBRARY.
"""

import json
import os

BOOK_SPECS = [
    # NETWORKING
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
        "chapters": [
            {
                "slug": "introduction-to-networks",
                "chapterNumber": 1,
                "title": "Introduction to Computer Networks",
                "summary": "Core topologies, packet switching paradigms, and network boundaries.",
                "intro": "Modern computer networks constitute the fabric of distributed computation. Understanding how frames and packets traverse local switches, boundary gateways, and transit networks is the foundation of digital defense.",
                "explanation": "A network is a collection of autonomous nodes interconnected through transmission media (copper, fiber optic, radio frequency). Unlike circuit-switched legacy telephony, modern networks rely on packet-switched communication, where discrete units of data (packets) are independently routed across varying topological paths based on destination addressing. Understanding local area networks (LAN), wide area networks (WAN), virtual private networks (VPN), and Software-Defined Networking (SDN) is indispensable for security auditing.",
                "concepts": [
                    {"term": "Packet Switching", "definition": "A communication method in which data is grouped into packets transmitted over digital networks without dedicated circuits."},
                    {"term": "Default Gateway", "definition": "The routing node that serves as an access point to external subnets when no specific route matches."},
                    {"term": "MTU (Maximum Transmission Unit)", "definition": "The largest packet or frame size (commonly 1500 bytes for standard Ethernet) specified in octets that can be sent in a packet- or frame-based network."}
                ],
                "commands": [
                    {
                        "title": "Inspect Local Network Interfaces and Routes",
                        "language": "bash",
                        "code": "# View all active network interfaces and assigned IP addresses\nip -br addr show\n\n# Display kernel routing table\nip route show\n\n# Ping the default gateway with packet count constraint\nping -c 4 192.168.1.1",
                        "explanation": "The iproute2 suite (ip) replaces deprecated legacy tools like ifconfig. The '-br' flag outputs a clean tabular summary."
                    }
                ],
                "tools": ["iproute2", "ping"],
                "mistakes": [
                    "Confusing physical network topologies (star, mesh) with logical layer-3 addressing.",
                    "Assuming default gateways can resolve routing ambiguities on non-routable private addresses without NAT."
                ],
                "bestPractices": [
                    "Always verify interface MTU configurations before diagnosing sporadic fragmentation issues.",
                    "Enforce strict subnet segmentation between management interfaces, servers, and untrusted client hosts."
                ],
                "exercise": {
                    "title": "Local Interface Discovery and Default Route Verification",
                    "scenario": "A new server instance is brought online in an isolated subnet. Verify assigned IP addressing and test routing to the default gateway.",
                    "steps": [
                        "Execute 'ip addr show' to inspect the assigned CIDR notation on interface eth0.",
                        "Inspect default gateway route via 'ip route show | grep default'.",
                        "Send ICMP echo requests using 'ping -c 3 <gateway-ip>' to confirm layer-3 reachability."
                    ],
                    "expectedOutcome": "The assigned address is identified with subnet mask, and all 3 ICMP echo requests return with 0% packet loss."
                },
                "refs": [
                    {"title": "RFC 791 - Internet Protocol Specification", "url": "https://datatracker.ietf.org/doc/html/rfc791"},
                    {"title": "Linux iproute2 Documentation", "url": "https://man7.org/linux/man-pages/man8/ip.8.html"}
                ]
            },
            {
                "slug": "osi-model",
                "chapterNumber": 2,
                "title": "The OSI Reference Model",
                "summary": "Deep architectural analysis of the seven theoretical layers of network abstraction.",
                "intro": "The Open Systems Interconnection (OSI) 7-layer model provides an unambiguous conceptual framework for dissecting protocols, protocol data units (PDUs), and security threat vectors.",
                "explanation": "Formulated by ISO, the model partitions communication into: Physical (L1 - Bits), Data Link (L2 - Frames), Network (L3 - Packets), Transport (L4 - Segments/Datagrams), Session (L5 - Dialogues), Presentation (L6 - Syntax/Encryption), and Application (L7 - User Process APIs). Cyber attacks operate at distinct layers: MAC spoofing at L2, IP spoofing at L3, SYN floods at L4, and SQL injection at L7.",
                "concepts": [
                    {"term": "PDU (Protocol Data Unit)", "definition": "The discrete unit of data specified in a given layer protocol containing both header metadata and payload."},
                    {"term": "Encapsulation / Decapsulation", "definition": "The progressive wrapping of higher-layer payloads with layer-specific headers during outbound transmission, and striping during receipt."}
                ],
                "commands": [
                    {
                        "title": "Observe Layered Encapsulation with tcpdump",
                        "language": "bash",
                        "code": "# Capture 5 packets in hex and ASCII format with layer-2 frame headers\nsudo tcpdump -i eth0 -c 5 -XX -e\n\n# Filter for ICMP packets with verbose layer-3 headers\nsudo tcpdump -i eth0 -v icmp",
                        "explanation": "The '-e' parameter prints the link-level Ethernet header (L2 MACs), while '-v' decodes IP header fields (TTL, IP flags, Protocol ID)."
                    }
                ],
                "tools": ["tcpdump", "Wireshark"],
                "mistakes": [
                    "Equating TCP directly to the Session and Presentation layers without acknowledging TCP spans L4.",
                    "Neglecting the layer-2 frame header when calculating overall wire MTU."
                ],
                "bestPractices": [
                    "Use layer-by-layer troubleshooting: isolate physical link state before debugging higher-level application firewalls.",
                    "Implement defense-in-depth security controls targeting threats specific to each individual layer."
                ],
                "exercise": {
                    "title": "Dissecting Encapsulated PDUs in a Packet Capture",
                    "scenario": "Capture an HTTP request packet and identify the specific header boundaries for Ethernet, IP, and TCP.",
                    "steps": [
                        "Initiate a packet capture with tcpdump on a test network.",
                        "Execute curl http://example.com in another terminal.",
                        "Inspect the captured PDU: verify 14-byte Ethernet header, 20-byte IPv4 header, and 20-byte TCP header."
                    ],
                    "expectedOutcome": "Precise identification of MAC addresses, IP addresses, TCP ports, and application payload offsets."
                },
                "refs": [
                    {"title": "ISO/IEC 7498-1: Information technology - Open Systems Interconnection", "url": "https://www.iso.org/standard/20269.html"}
                ]
            },
            {
                "slug": "tcp-ip-model",
                "chapterNumber": 3,
                "title": "The TCP/IP Protocol Suite",
                "summary": "The pragmatic four-layer protocol suite powering the global internet.",
                "intro": "While the OSI model is theoretical, TCP/IP is the practical architectural standard deployed across millions of routers, firewalls, and client systems globally.",
                "explanation": "The TCP/IP stack compresses networking into four operational tiers: Link Layer, Internet Layer (IP, ICMP, ARP), Transport Layer (TCP, UDP), and Application Layer (HTTP, SSH, DNS, TLS). The stateless nature of the Internet Layer relies on higher-layer protocols or stateful firewalls to preserve connection contexts.",
                "concepts": [
                    {"term": "RFC Standard", "definition": "Request for Comments; formal technical documents drafted by the IETF that specify internet protocols."},
                    {"term": "Stateful vs Stateless", "definition": "Stateful protocols maintain connection parameters across transactions; stateless protocols treat each message independently."}
                ],
                "commands": [
                    {
                        "title": "Inspect Active Transport Layer Sockets with ss",
                        "language": "bash",
                        "code": "# List all listening TCP sockets with process IDs\nss -tlpn\n\n# Display all active established TCP connections\nss -tepan\n\n# View socket memory statistics\nss -s",
                        "explanation": "The modern 'ss' utility queries the kernel directly via netlink, delivering orders of magnitude faster inspection than netstat."
                    }
                ],
                "tools": ["ss", "iproute2"],
                "mistakes": [
                    "Assuming TCP checksum verification guarantees integrity against malicious payload tampering (it only catches random corruption).",
                    "Overlooking ICMP error messages required for Path MTU Discovery."
                ],
                "bestPractices": [
                    "Audit open listening sockets regularly using 'ss -tlpn' to locate unhardened administrative daemons.",
                    "Ensure Path MTU Discovery (ICMP Type 3 Code 4) is not completely dropped by overzealous firewall filters."
                ],
                "exercise": {
                    "title": "Transport Socket Audit on Local Host",
                    "scenario": "Audit all listening endpoints to discover unauthorized services running on unprivileged ports.",
                    "steps": [
                        "Run 'ss -tulnp' with root privileges to view listening TCP and UDP sockets.",
                        "Correlate local ports against known security baselines (e.g., port 22 for SSH, 80/443 for web).",
                        "Investigate any unknown daemon PIDs using 'ps -p <PID> -o comm,args'."
                    ],
                    "expectedOutcome": "A verified inventory of every listening daemon mapped to its originating process binary."
                },
                "refs": [
                    {"title": "RFC 1122 - Requirements for Internet Hosts", "url": "https://datatracker.ietf.org/doc/html/rfc1122"}
                ]
            },
            {
                "slug": "ip-addressing-and-subnetting",
                "chapterNumber": 4,
                "title": "IP Addressing & Subnetting Mechanics",
                "summary": "Mastering IPv4 binary mathematics, CIDR notation, and IPv6 address scopes.",
                "intro": "Subnetting is the fundamental mechanism used to partition large address spaces into efficient, secure, and routable segments.",
                "explanation": "An IPv4 address consists of 32 bits arranged in four 8-bit octets. Subnet masks distinguish the network prefix from host bits. Classless Inter-Domain Routing (CIDR) replaced legacy Class A/B/C allocations. Calculating network addresses, broadcast addresses, and usable host counts requires binary AND operations. In IPv6, 128-bit addresses eliminate the need for NAT while introducing link-local (fe80::/10) and global unicast (2000::/3) scopes.",
                "concepts": [
                    {"term": "CIDR Prefix", "definition": "A notation indicating how many contiguous leading bits in an address designate the network portion (e.g. /24)."},
                    {"term": "Broadcast Address", "definition": "The highest address in an IPv4 subnet, with all host bits set to 1, used to address all hosts simultaneously."}
                ],
                "commands": [
                    {
                        "title": "Subnet Calculations with ipcalc and Python",
                        "language": "bash",
                        "code": "# Calculate network bounds using ipcalc\nipcalc 192.168.10.45/26\n\n# Python 3 one-liner to inspect subnet properties\npython3 -c \"import ipaddress; net = ipaddress.ip_network('10.240.0.0/22'); print(f'Hosts: {net.num_addresses - 2}, Net: {net.network_address}, Bcast: {net.broadcast_address}')\"",
                        "explanation": "Python's standard library module 'ipaddress' enables precise cryptographic-grade subnet arithmetic."
                    }
                ],
                "tools": ["ipcalc", "python3 ipaddress"],
                "mistakes": [
                    "Forgetting that the network address (host bits all 0) and broadcast address (host bits all 1) cannot be assigned to hosts.",
                    "Miscalculating /23 and /22 boundaries across octet boundaries."
                ],
                "bestPractices": [
                    "Always allocate subnets based on 3-year capacity forecasts plus a 30% operational headroom.",
                    "Separate high-risk guest Wi-Fi and IoT devices into isolated VLANs with strict /27 or /28 boundaries."
                ],
                "exercise": {
                    "title": "Subnet Design for Multi-Tier Security Zone",
                    "scenario": "Given the block 172.16.100.0/24, partition it to host: Web DMZ (50 hosts), Application Tier (30 hosts), and Database Tier (14 hosts).",
                    "steps": [
                        "Calculate required CIDR for Web DMZ: /26 provides 62 usable hosts (172.16.100.0/26).",
                        "Allocate Application Tier: /27 provides 30 usable hosts (172.16.100.64/27).",
                        "Allocate Database Tier: /28 provides 14 usable hosts (172.16.100.96/28).",
                        "Verify that none of the allocated subnet ranges overlap."
                    ],
                    "expectedOutcome": "Three non-overlapping subnets with zero address collisions and efficient address conservation."
                },
                "refs": [
                    {"title": "RFC 4632 - Classless Inter-domain Routing (CIDR)", "url": "https://datatracker.ietf.org/doc/html/rfc4632"}
                ]
            },
            {
                "slug": "mac-addresses-and-arp",
                "chapterNumber": 5,
                "title": "MAC Addresses, ARP & Layer-2 Security",
                "summary": "Ethernet frame addressing, Address Resolution Protocol, and ARP spoofing mitigations.",
                "intro": "IP packets cannot traverse physical Ethernet segments without being encapsulated into layer-2 frames addressed to Media Access Control (MAC) hardware addresses.",
                "explanation": "The Address Resolution Protocol (ARP) translates 32-bit IP addresses into 48-bit MAC addresses. ARP is inherently unauthenticated: any node can broadcast gratuitous ARP replies claiming ownership of another IP. Attackers exploit this via ARP Poisoning to perform Man-in-the-Middle (MitM) interceptions. Mitigations include Dynamic ARP Inspection (DAI) and static ARP tables.",
                "concepts": [
                    {"term": "OUI (Organizationally Unique Identifier)", "definition": "The first 24 bits of a MAC address that identify the hardware vendor assigned by IEEE."},
                    {"term": "ARP Cache Poisoning", "definition": "Injecting falsified ARP reply messages into a local switch table to reroute victim traffic through the attacker's interface."}
                ],
                "commands": [
                    {
                        "title": "Inspect and Manage Local ARP Cache",
                        "language": "bash",
                        "code": "# Display the kernel neighbor table (modern ARP table)\nip neigh show\n\n# Flush the entire neighbor cache\nsudo ip neigh flush all\n\n# Add a static permanent ARP binding for gateway\nsudo ip neigh replace 192.168.1.1 lladdr 00:11:22:33:44:55 nud permanent dev eth0",
                        "explanation": "Setting static permanent ARP bindings prevents dynamic poisoning attacks in critical server segments."
                    }
                ],
                "tools": ["ip neigh", "arp-scan", "dsniff"],
                "mistakes": [
                    "Assuming switch port isolation prevents ARP spoofing without Dynamic ARP Inspection (DAI) enabled.",
                    "Ignoring duplicated MAC alerts in system event logs."
                ],
                "bestPractices": [
                    "Enable DHCP Snooping and Dynamic ARP Inspection on all enterprise access switch ports.",
                    "Monitor for abnormal ARP traffic rates with tools like arpwatch or Zeek."
                ],
                "exercise": {
                    "title": "Observing ARP Resolution and Neighbor Table Update",
                    "scenario": "Monitor real-time ARP traffic during an outbound connection to an unknown local subnet address.",
                    "steps": [
                        "Run 'sudo tcpdump -i eth0 arp' in terminal A.",
                        "Ping an adjacent local host in terminal B to trigger an ARP who-has broadcast.",
                        "Observe the ARP request broadcast (ff:ff:ff:ff:ff:ff) and the unicast ARP reply.",
                        "Inspect the updated cache entry using 'ip neigh show'."
                    ],
                    "expectedOutcome": "Clear packet-level visibility into the ARP query-reply handshake and resulting kernel neighbor state."
                },
                "refs": [
                    {"title": "RFC 826 - An Ethernet Address Resolution Protocol", "url": "https://datatracker.ietf.org/doc/html/rfc826"}
                ]
            },
            {
                "slug": "dns-and-dhcp",
                "chapterNumber": 6,
                "title": "Core Services: DNS & DHCP Protocols",
                "summary": "Domain Name System resolution trees, DHCP DORA handshakes, and DNSSEC defenses.",
                "intro": "The operational internet relies on two foundational control protocols: DHCP for automated host configuration and DNS for distributed name resolution.",
                "explanation": "DHCP uses a four-step handshake: Discover, Offer, Request, Acknowledge (DORA) over UDP ports 67 and 68. DNS is a distributed, hierarchical database starting at root nameservers (.), descending through Top-Level Domains (.org, .com), and reaching Authoritative servers. Security vulnerabilities include Rogue DHCP servers, DNS Cache Poisoning, and DNS Exfiltration tunnels. Defenses include DHCP Snooping, Response Rate Limiting (RRL), and DNSSEC.",
                "concepts": [
                    {"term": "DORA Process", "definition": "The 4-stage broadcast and unicast transaction hosts use to negotiate an IP lease, gateway, and DNS servers."},
                    {"term": "DNSSEC", "definition": "Domain Name System Security Extensions; uses public key cryptography to authenticate DNS responses."}
                ],
                "commands": [
                    {
                        "title": "Comprehensive DNS Querying with dig",
                        "language": "bash",
                        "code": "# Perform recursive DNS lookup with complete trace from root servers\ndig +trace example.com\n\n# Query specific record types (TXT, MX, AAAA)\ndig example.com TXT\n\n# Query directly against Cloudflare DNS with DNSSEC verification\ndig @1.1.1.1 example.com +dnssec",
                        "explanation": "The +trace flag instructs dig to iterate through root (.), TLD, and authoritative nameservers, exposing delegation paths."
                    }
                ],
                "tools": ["dig", "nslookup", "tcpdump"],
                "mistakes": [
                    "Confusing recursive resolvers (e.g. 8.8.8.8) with authoritative nameservers that host the actual zone files.",
                    "Allowing unrestricted outbound UDP 53 traffic, which permits covert DNS data exfiltration channels."
                ],
                "bestPractices": [
                    "Enforce DNS-over-HTTPS (DoH) or DNS-over-TLS (DoT) internally to prevent on-path eavesdropping.",
                    "Implement Split-Horizon DNS to isolate internal Active Directory domain records from public internet resolution."
                ],
                "exercise": {
                    "title": "Auditing Zone Transfers and DNS Record Enumeration",
                    "scenario": "Audit whether a target authoritative nameserver improperly permits unrestricted AXFR zone transfers.",
                    "steps": [
                        "Find authoritative nameservers for a domain: 'dig example.com NS +short'.",
                        "Attempt an AXFR zone transfer: 'dig @ns1.example.com example.com AXFR'.",
                        "Verify that the nameserver safely returns 'Transfer failed' or REFUSED."
                    ],
                    "expectedOutcome": "Confirmation that zone transfers are strictly restricted to authorized secondary DNS servers."
                },
                "refs": [
                    {"title": "RFC 1035 - Domain Names - Implementation and Specification", "url": "https://datatracker.ietf.org/doc/html/rfc1035"},
                    {"title": "RFC 2131 - Dynamic Host Configuration Protocol", "url": "https://datatracker.ietf.org/doc/html/rfc2131"}
                ]
            },
            {
                "slug": "tcp-and-udp",
                "chapterNumber": 7,
                "title": "Transport Layer Dynamics: TCP vs UDP",
                "summary": "State machines, three-way handshakes, sliding windows, congestion control, and raw datagrams.",
                "intro": "The Transport Layer mediates end-to-end communication between application processes using port numbers, providing either reliable byte-streams (TCP) or lightweight datagrams (UDP).",
                "explanation": "TCP (RFC 793) is connection-oriented, providing reliable delivery through sequence numbers, acknowledgments, sliding window flow control, and retransmission timers. The 3-way handshake establishes Initial Sequence Numbers (ISNs). Flags include SYN, ACK, FIN, RST, PSH, and URG. In contrast, UDP (RFC 768) is minimal, stateless, and lacks congestion control, making it ideal for DNS, VoIP, gaming, and HTTP/3 (QUIC).",
                "concepts": [
                    {"term": "Three-Way Handshake", "definition": "SYN -> SYN-ACK -> ACK exchange to synchronize sequence numbers and allocate socket buffers."},
                    {"term": "TCP Reset (RST)", "definition": "A control packet indicating the port is closed or terminating an invalid connection attempt."}
                ],
                "commands": [
                    {
                        "title": "Crafting and Testing Transport Packets with Netcat and Python",
                        "language": "bash",
                        "code": "# Start a TCP listener on port 4444\nnc -lvnp 4444\n\n# In another shell, connect and send data\nnc -v 127.0.0.1 4444\n\n# Test UDP packet transmission\nnc -u -v 127.0.0.1 53",
                        "explanation": "Netcat (nc) is the Swiss Army knife for testing raw layer-4 socket communication."
                    }
                ],
                "tools": ["netcat", "socat", "tcpdump"],
                "mistakes": [
                    "Assuming UDP port scans always receive immediate responses (closed UDP ports may return ICMP Type 3 Code 3, while open ones stay silent).",
                    "Neglecting TCP TIME_WAIT states during high-volume server benchmarking."
                ],
                "bestPractices": [
                    "Enable TCP SYN cookies (net.ipv4.tcp_syncookies = 1) in Linux sysctl to withstand SYN flood denial-of-service attacks.",
                    "Tune TCP keepalive timers to prevent stale connections from exhausting connection tracking tables."
                ],
                "exercise": {
                    "title": "TCP Handshake and Teardown Packet Capture Analysis",
                    "scenario": "Capture and inspect the exact TCP flag sequences during an HTTP request handshake and subsequent connection teardown.",
                    "steps": [
                        "Start tcpdump with TCP flag filters: 'sudo tcpdump -i lo 'tcp[tcpflags] & (tcp-syn|tcp-ack|tcp-fin) != 0''.",
                        "Issue a curl request to a local web server.",
                        "Identify the 3-way handshake (SYN, SYN/ACK, ACK) and 4-way FIN teardown."
                    ],
                    "expectedOutcome": "Clear verification of relative and raw sequence number increments across the connection lifecycle."
                },
                "refs": [
                    {"title": "RFC 793 - Transmission Control Protocol", "url": "https://datatracker.ietf.org/doc/html/rfc793"}
                ]
            },
            {
                "slug": "routers-switches-and-firewalls",
                "chapterNumber": 8,
                "title": "Routers, Switches & Firewall Architectures",
                "summary": "Packet forwarding planes, VLAN tagging, stateful packet inspection, and Access Control Lists.",
                "intro": "Network traffic is directed and policed by specialized hardware and virtual appliances operating at different OSI layers.",
                "explanation": "Layer-2 switches forward frames based on MAC address tables (CAM). Virtual Local Area Networks (VLANs) segment broadcast domains via IEEE 802.1Q tags. Routers operate at Layer 3, forwarding packets based on routing tables (BGP, OSPF, static). Firewalls govern transit policies: Packet Filtering (stateless), Stateful Packet Inspection (SPI), and Next-Generation Firewalls (NGFW) inspecting layer-7 application payloads.",
                "concepts": [
                    {"term": "CAM Table (Content Addressable Memory)", "definition": "High-speed switch memory storing mappings between MAC addresses, VLAN IDs, and physical switch ports."},
                    {"term": "Stateful Packet Inspection (SPI)", "definition": "Firewall filtering mechanism tracking active connection states (e.g. ESTABLISHED, RELATED) to dynamically permit returning traffic."}
                ],
                "commands": [
                    {
                        "title": "Configuring Linux nftables Stateful Firewall Rules",
                        "language": "bash",
                        "code": "# View current nftables firewall ruleset\nsudo nft list ruleset\n\n# Allow established and related connections\nsudo nft add rule inet filter input ct state established,related accept\n\n# Drop all invalid packets\nsudo nft add rule inet filter input ct state invalid drop",
                        "explanation": "nftables is the modern successor to iptables in Linux kernels, offering unified syntax and kernel JIT compilation."
                    }
                ],
                "tools": ["nftables", "iptables", "ethtool"],
                "mistakes": [
                    "Relying solely on VLAN separation without disabling DTP (Dynamic Trunking Protocol), leaving switches vulnerable to VLAN hopping.",
                    "Positioning stateful firewalls in asymmetrical routing paths, which drops valid returning packets."
                ],
                "bestPractices": [
                    "Adopt a Default Deny ingress and egress posture across all firewall zones.",
                    "Implement 802.1X Port Security to authenticate physical endpoints before allowing MAC learning."
                ],
                "exercise": {
                    "title": "Constructing an Ingress Firewall Filter with nftables",
                    "scenario": "Construct a hardened firewall table that drops all incoming traffic except SSH (port 22) and ICMP echo requests.",
                    "steps": [
                        "Create a table and chain with drop policy: 'sudo nft add table inet filter' followed by 'sudo nft add chain inet filter input { type filter hook input priority 0 \\; policy drop \\; }'.",
                        "Allow loopback interface: 'sudo nft add rule inet filter input iif lo accept'.",
                        "Allow established connections and incoming SSH on port 22.",
                        "Test that unexpected ports are completely dropped."
                    ],
                    "expectedOutcome": "Uncompromised host perimeter blocking unauthorized probe attempts."
                },
                "refs": [
                    {"title": "nftables Official Documentation", "url": "https://wiki.nftables.org/wiki-nftables/index.php/Main_Page"}
                ]
            },
            {
                "slug": "common-network-protocols",
                "chapterNumber": 9,
                "title": "Essential Application Protocols",
                "summary": "Deep dive into HTTP/HTTPS, SSH, SMTP, FTP, and SNMP security mechanisms.",
                "intro": "Application layer protocols dictate how software systems exchange structured messages across global communication networks.",
                "explanation": "We analyze HTTP/1.1 vs HTTP/2 and HTTP/3 multiplexing; SSH-2 protocol architecture (key exchange, asymmetric host verification, symmetric cipher tunneling); SMTP mail routing with SPF/DKIM/DMARC anti-spoofing; FTP passive vs active modes; and SNMP (Simple Network Management Protocol) versions 1/2c community strings vs SNMPv3 authenticated and encrypted management.",
                "concepts": [
                    {"term": "DMARC", "definition": "Domain-based Message Authentication, Reporting, and Conformance; email protocol leveraging SPF and DKIM to prevent phishing."},
                    {"term": "SNMPv3", "definition": "Network management protocol featuring User-based Security Model (USM) for cryptographic authentication and privacy."}
                ],
                "commands": [
                    {
                        "title": "Inspecting Application Protocol Headers with curl and openssl",
                        "language": "bash",
                        "code": "# Fetch HTTP response headers with detailed timing metadata\ncurl -I -s https://example.com\n\n# Test TLS handshake and inspect certificate chain\nopenssl s_client -connect example.com:443 -servername example.com\n\n# Query SNMPv2 community string on a lab router\nsnmpwalk -v 2c -c public 192.168.1.1 1.3.6.1.2.1.1",
                        "explanation": "openssl s_client outputs the complete X.509 certificate hierarchy, negotiated cipher suite, and TLS version."
                    }
                ],
                "tools": ["curl", "openssl", "snmpwalk"],
                "mistakes": [
                    "Leaving default 'public' or 'private' SNMPv1/2c community strings active on production network gear.",
                    "Failing to enforce HSTS headers, enabling SSL stripping attacks."
                ],
                "bestPractices": [
                    "Decommission insecure legacy protocols (Telnet, FTP, HTTP, SNMPv1/2c) in favor of SSHv2, SFTP, HTTPS, and SNMPv3.",
                    "Configure DMARC policy with 'p=reject' across all enterprise-owned domains."
                ],
                "exercise": {
                    "title": "TLS Cipher Suite and Certificate Chain Inspection",
                    "scenario": "Verify that a web service only supports modern TLS 1.3/1.2 protocols and rejects insecure legacy ciphers (RC4, 3DES).",
                    "steps": [
                        "Run 'openssl s_client -connect target.local:443 -tls1_2' to verify TLS 1.2 support.",
                        "Attempt connection with deprecated protocol: 'openssl s_client -connect target.local:443 -ssl3'.",
                        "Confirm the server handshake terminates with a handshake failure alert."
                    ],
                    "expectedOutcome": "Server securely terminates obsolete SSL/TLS connections while successfully serving valid TLS 1.3."
                },
                "refs": [
                    {"title": "RFC 8446 - The Transport Layer Security (TLS) Protocol Version 1.3", "url": "https://datatracker.ietf.org/doc/html/rfc8446"}
                ]
            },
            {
                "slug": "network-troubleshooting",
                "chapterNumber": 10,
                "title": "Network Troubleshooting & Diagnostics",
                "summary": "Systematic fault isolation methodology using modern CLI diagnostic suites.",
                "intro": "When network services fail or suffer degradation, engineers must methodically isolate latency, packet loss, DNS failures, and firewall blocks.",
                "explanation": "Effective troubleshooting follows the bottom-up OSI methodology: verify link carrier status (ethtool), check IP addressing and ARP cache (ip addr, ip neigh), verify layer-3 route reachability (ping, traceroute/mtr), test layer-4 port listening states and firewalls (nc, ss, nmap), and inspect layer-7 application semantics (curl). We explore ICMP TTL expiration mechanics in traceroute and packet loss analysis via mtr.",
                "concepts": [
                    {"term": "TTL (Time to Live)", "definition": "An 8-bit IP header field decremented by each router hop; when it reaches 0, the router discards the packet and sends ICMP Time Exceeded."},
                    {"term": "MTR (My Traceroute)", "definition": "A diagnostic tool combining traceroute and ping to continuously sample round-trip times and packet loss along each hop."}
                ],
                "commands": [
                    {
                        "title": "Systematic Troubleshooting Pipeline",
                        "language": "bash",
                        "code": "# 1. Verify physical link speed and duplex\nsudo ethtool eth0 | grep -E 'Speed|Duplex|Link detected'\n\n# 2. Run continuous real-time path latency and packet loss diagnostic\nmtr --report-cycles 10 --no-dns 1.1.1.1\n\n# 3. Test TCP connectivity directly to specific port without hanging\nnc -zv -w 3 1.1.1.1 443",
                        "explanation": "mtr provides a multi-sample statistical breakdown of every intermediate routing hop, identifying where packet loss initiates."
                    }
                ],
                "tools": ["mtr", "traceroute", "ethtool", "tcpdump"],
                "mistakes": [
                    "Assuming high latency at a single intermediate traceroute hop indicates an issue when subsequent hops show low latency (intermediate routers often rate-limit ICMP generation).",
                    "Skipping DNS resolution testing when debugging high latency (often caused by slow reverse DNS lookups)."
                ],
                "bestPractices": [
                    "Always run dual-direction traceroutes when debugging latency, as asymmetric routing paths are common.",
                    "Maintain baseline capture files (PCAPs) of healthy network traffic for regression comparisons."
                ],
                "exercise": {
                    "title": "Diagnosing Simulated Blackhole Routing",
                    "scenario": "A host can resolve domain names but cannot establish HTTPS connections to a remote API. Isolate the failure point.",
                    "steps": [
                        "Perform DNS test: 'dig api.example.com +short' to confirm name resolution works.",
                        "Test layer-3 reachability: 'ping -c 3 <api-ip>'.",
                        "Test layer-4 TCP port: 'nc -zv -w 2 <api-ip> 443'.",
                        "Execute traceroute with TCP SYN packets: 'sudo traceroute -T -p 443 <api-ip>' to pinpoint the blocking hop."
                    ],
                    "expectedOutcome": "Precise identification of the firewall boundary dropping TCP SYN packets."
                },
                "refs": [
                    {"title": "MTR Man Page", "url": "https://man7.org/linux/man-pages/man8/mtr.8.html"}
                ]
            }
        ]
    }
]

print("Script template ready.")
