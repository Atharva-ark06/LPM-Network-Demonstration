# 🌐 Longest Prefix Match — Network Demonstration

<p align="center">

<img src="https://img.shields.io/badge/Networking-LPM-0A66C2?style=for-the-badge&logo=cisco&logoColor=white" />

<img src="https://img.shields.io/badge/Cyber%20Security-Network%20Analysis-6A1B9A?style=for-the-badge&logo=hackthebox&logoColor=white" />

<img src="https://img.shields.io/badge/Virtual%20Lab-GNS3-FF6B35?style=for-the-badge&logo=gnubash&logoColor=white" />

<img src="https://img.shields.io/badge/Packet%20Analysis-Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white" />

<img src="https://img.shields.io/badge/Academic%20Year-2026--27-111827?style=for-the-badge" />

</p>

<p align="center">
  <strong>🔬 A practical demonstration and analysis of Longest Prefix Match (LPM) in IP routing.</strong>
</p>

<p align="center">
  Understanding how routers select the most specific route when multiple overlapping prefixes exist.
</p>

---

## 📌 Project Overview

**Longest Prefix Match (LPM)** is one of the fundamental mechanisms used by IP routers to determine the best route for forwarding packets.

When multiple routes match the destination IP address, the router selects the route with the **longest — most specific — network prefix**.

This project provides a practical network demonstration of that principle by configuring overlapping routes with different prefix lengths and observing the routing decision through controlled network traffic.

The demonstration focuses on prefixes such as:

```text
/12
/16
/24
/25
```

The experiment verifies that the **most specific matching prefix wins**, regardless of where the route appears in the routing table.

---

# 🎯 Objectives

The primary objectives of this project are:

* 🧠 Understand the concept of Longest Prefix Match
* 🌐 Analyze how routers select routes
* 🔀 Configure overlapping IP networks
* 📡 Generate controlled network traffic
* 🔎 Observe routing decisions
* 📊 Verify routing behavior experimentally
* 🛡️ Understand the importance of LPM in modern networks
* 🧪 Analyze packets using network monitoring tools

---

# 🧩 Core Concept

Consider the following routing entries:

```text
Destination        Prefix
────────────────────────────
10.0.0.0           /12
10.0.0.0           /16
10.0.1.0           /24
10.0.1.128         /25
```

Suppose a packet is destined for:

```text
10.0.1.150
```

Multiple routes may match the destination.

The router evaluates the prefix lengths:

```text
/12  ───────► Match
/16  ───────► Match
/24  ───────► Match
/25  ───────► Match ✓
```

The router selects:

```text
10.0.1.128/25
```

because `/25` is the **longest matching prefix**.

### In simple terms:

> **The more specific route wins.**

---

# 🧠 How LPM Works

```text
                 Destination IP
                       │
                       ▼
              ┌─────────────────┐
              │ Routing Table   │
              └────────┬────────┘
                       │
                       ▼
             Find Matching Routes
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
        /12           /16          /24
                                      │
                                      ▼
                                    /25
                                      │
                                      ▼
                         Most Specific Match
                                      │
                                      ▼
                              Select Next Hop
                                      │
                                      ▼
                             Forward Packet
```

---

# 🏗️ Network Architecture

The project uses a controlled virtual networking environment to demonstrate routing behavior.

### Experimental Flow

```text
┌─────────────┐
│   Source    │
│    Host     │
└──────┬──────┘
       │
       │ Test Traffic
       ▼
┌─────────────────┐
│  Virtual Router │
│                 │
│  Routing Table  │
│                 │
│ /12             │
│ /16             │
│ /24             │
│ /25             │
└────────┬────────┘
         │
         │ LPM Decision
         ▼
┌─────────────────┐
│ Destination     │
│ Network / Host  │
└─────────────────┘
```

---

# 🔬 Experimental Methodology

The experiment follows a structured process:

```text
01  →  Design Network Topology
02  →  Configure Router Interfaces
03  →  Configure Overlapping Routes
04  →  Generate Test Traffic
05  →  Capture Packets
06  →  Observe Routing Decisions
07  →  Compare Prefix Matches
08  →  Verify Longest Prefix Selection
```

---

# ⚙️ Router Configuration

The demonstration uses multiple router interfaces to establish the test environment.

Example interface configuration:

```text
GigabitEthernet0/0
IP Address: 10.0.0.1
Subnet Mask: 255.255.255.252
```

```text
GigabitEthernet0/1
IP Address: 10.0.1.1
Subnet Mask: 255.255.255.252
```

```text
GigabitEthernet0/2
IP Address: 10.0.2.1
Subnet Mask: 255.255.255.252
```

These interfaces provide the connectivity required for the routing experiment.

---

# 🧪 Test Scenario

The experiment introduces multiple overlapping routes.

```text
┌─────────────────────────────────────────┐
│             Routing Table               │
├─────────────────────────────────────────┤
│ Route A        →        /12             │
│ Route B        →        /16             │
│ Route C        →        /24             │
│ Route D        →        /25             │
└─────────────────────────────────────────┘
```

A destination IP that falls within multiple networks is then selected for testing.

The router compares the matching prefixes and chooses the route with the greatest prefix length.

---

# 📡 Traffic Generation

The network behavior can be tested using tools such as:

### Ping

```bash
ping <destination-ip>
```

Used to verify basic IP connectivity.

### Traceroute

```bash
tracert <destination-ip>
```

or:

```bash
traceroute <destination-ip>
```

Used to observe the path taken by packets.

### iPerf3

```bash
iperf3
```

Used for controlled traffic generation and network performance testing.

---

# 🦈 Packet Analysis

**Wireshark** is used to capture and inspect packets during the experiment.

The packet capture helps correlate:

```text
Generated Traffic
       ↓
Router Processing
       ↓
Routing Decision
       ↓
Selected Route
       ↓
Forwarded Packet
```

This provides a packet-level perspective of the routing experiment.

---

# 📊 Results

The experiment demonstrates the fundamental behavior of Longest Prefix Match:

| Prefix | Specificity | Selection |
| :----: | :---------: | :-------: |
|  `/12` |     Low     |     ❌     |
|  `/16` |    Medium   |     ❌     |
|  `/24` |     High    |     ❌     |
|  `/25` |   Highest   |     ✅     |

### Key Observation

When multiple routes match a destination address:

```text
Longest Prefix
      ↓
Most Specific Network
      ↓
Best Matching Route
      ↓
Packet Forwarded
```

Therefore:

> **LPM ensures that the most specific applicable route is selected.**

---

# 🧠 Why LPM Matters

Longest Prefix Match is fundamental to modern IP routing.

It allows networks to maintain overlapping address spaces while still making deterministic forwarding decisions.

LPM is especially important for:

* 🌐 Internet routing
* 🏢 Enterprise networks
* ☁️ Cloud networking
* 🔀 Routers and Layer-3 switches
* 🛡️ Network security
* 📡 ISP infrastructure
* 🚀 Software-defined networking
* 🧭 Routing table lookup systems

---

# 🛠️ Technologies & Tools

| Technology         | Purpose                              |
| ------------------ | ------------------------------------ |
| 🖥️ **VirtualBox** | Virtualized networking environment   |
| 🌐 **GNS3**        | Network topology & router simulation |
| 🦈 **Wireshark**   | Packet capture and analysis          |
| 📡 **Ping**        | Connectivity testing                 |
| 🧭 **Traceroute**  | Route/path analysis                  |
| ⚡ **iPerf3**       | Controlled traffic generation        |
| 🔀 **Cisco IOS**   | Router configuration & routing       |

---

# 📁 Repository Contents

```text
LPM-Network-Demonstration/
│
├── 📄 LPM_Report.pdf
│
├── 📄 LPM_Report_TC.docx
│
└── 📄 README.md
```

The repository contains both:

* 📕 **PDF version** — final report/reference
* 📝 **DOCX version** — editable report

The GitHub repository currently provides these report files as its primary project artifacts.

---

# 📚 Report Structure

The accompanying technical competency report covers:

```text
Abstract
   ↓
Introduction
   ↓
Objectives
   ↓
Methodology
   ↓
System Design
   ↓
Network Topology
   ↓
Configuration
   ↓
Implementation
   ↓
Results
   ↓
Conclusion
   ↓
Future Scope
   ↓
References
```

---

# 🔮 Future Scope

The demonstration can be extended in several directions.

### 🚀 Possible Improvements

* IPv6 Longest Prefix Match
* Large-scale routing table experiments
* Routing performance benchmarking
* Trie-based routing lookup
* TCAM-based lookup analysis
* Dynamic routing protocols
* OSPF and BGP integration
* SDN-based LPM experiments
* Automated packet analysis
* Network automation using Python
* Real hardware router testing

---

# 🎓 Academic Context

**Department:** Cyber Security & Information Security
**Academic Year:** 2026–27
**Project Type:** Technical Competency / Network Demonstration
**Topic:** Longest Prefix Match (LPM)

This repository serves as the supporting documentation and report archive for the LPM networking demonstration. GitHub identifies the project specifically as a Technical Competency Report covering integration, technology, topology, configuration, implementation, results, and future scope.

---

# 💡 Key Takeaways

```text
┌─────────────────────────────────────┐
│          LONGEST PREFIX MATCH       │
├─────────────────────────────────────┤
│                                     │
│ Multiple routes can match           │
│              ↓                      │
│ Compare prefix lengths              │
│              ↓                      │
│ Select longest prefix               │
│              ↓                      │
│ Choose most specific route          │
│              ↓                      │
│ Forward packet                      │
│                                     │
└─────────────────────────────────────┘
```

### The core rule:

# `/25 > /24 > /16 > /12`

The route with the **longest matching prefix** takes precedence.

---

# 👨‍💻 Author

<p align="center">

<strong>ATHARVA KULKARNI</strong>

<br>

Computer Science • Cyber Security • AI/ML • Networking

<br><br>

<a href="https://github.com/Atharva-ark06">
<img src="https://img.shields.io/badge/GitHub-Atharva--ark06-181717?style=for-the-badge&logo=github" />
</a>

</p>

---

# ⭐ Support

If you found this project useful for understanding networking and routing:

⭐ **Star the repository**
🍴 **Fork the project**
📚 **Use it for learning**
💡 **Build upon the experiment**

---

<p align="center">

### 🌐 Understand the Route. Find the Match. Forward the Packet.

<strong>Longest Prefix Match — Network Demonstration</strong>

<br><br>

<sub>Built as a practical exploration of IP routing and network behavior.</sub>

</p>
