# 🌐 LPM Network Demonstration

<div align="center">

### **Longest Prefix Match — Practical Network Routing Experiment**

**A hands-on demonstration of how routers select the most specific route when multiple IP prefixes match a destination.**

<br>

![Networking](https://img.shields.io/badge/Networking-LPM-2563EB?style=for-the-badge)
![Cisco](https://img.shields.io/badge/Cisco-IOS-1E40AF?style=for-the-badge)
![Wireshark](https://img.shields.io/badge/Wireshark-Packet%20Analysis-1677FF?style=for-the-badge)
![Academic](https://img.shields.io/badge/Academic-Project-7C3AED?style=for-the-badge)

<br>

**Department of Cyber Security & Information Security**
**G M University — Academic Year 2026–27**

</div>

---

## 🧠 About the Project

**Longest Prefix Match (LPM)** is a fundamental concept in IP routing.

When multiple routes match a destination IP address, a router selects the route with the **longest matching network prefix**, because it represents the most specific route.

This project provides a practical demonstration of LPM using a controlled virtual networking environment, overlapping network prefixes, routing configurations, and packet-level analysis.

### Prefixes Demonstrated

```text
/12  →  Broad Network
/16  →  More Specific
/24  →  Highly Specific
/25  →  Most Specific
```

> **Core Principle:** The most specific matching route wins.

---

## 🎯 Objectives

* 🧠 Understand the concept of **Longest Prefix Match**
* 🌐 Study how routers select forwarding routes
* 🔀 Configure overlapping IP networks
* ⚙️ Configure router interfaces and routing entries
* 📡 Generate controlled network traffic
* 🦈 Capture and analyze packets using Wireshark
* 🔎 Observe routing decisions
* 📊 Experimentally verify LPM behavior

---

## 🔥 Core LPM Demonstration

Consider the following routing entries:

```text
Destination        Prefix
────────────────────────────
10.0.0.0           /12
10.0.0.0           /16
10.0.1.0           /24
10.0.1.128         /25
```

For a destination such as:

```text
10.0.1.150
```

multiple routes can match the destination.

```text
/12  ──► MATCH
/16  ──► MATCH
/24  ──► MATCH
/25  ──► MATCH ✓
```

The router selects:

```text
10.0.1.128/25
```

because **/25 has the longest matching prefix**.

### In simple terms

```text
More specific route
        ↓
Longer prefix
        ↓
Better match
        ↓
Selected by router
```

---

## 🏗️ Network Architecture

```text
                         ┌─────────────────────┐
                         │      Source Host    │
                         └──────────┬──────────┘
                                    │
                              Test Traffic
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Virtual Router    │
                         │                     │
                         │   Routing Table     │
                         │                     │
                         │   10.0.0.0/12       │
                         │   10.0.0.0/16       │
                         │   10.0.1.0/24       │
                         │   10.0.1.128/25     │
                         └──────────┬──────────┘
                                    │
                              LPM Decision
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Destination Network │
                         │       / Host        │
                         └─────────────────────┘
```

---

## ⚙️ Experimental Workflow

```text
01  Design Network Topology
        ↓
02  Configure Router Interfaces
        ↓
03  Configure Overlapping Routes
        ↓
04  Generate Test Traffic
        ↓
05  Capture Network Packets
        ↓
06  Observe Routing Decisions
        ↓
07  Compare Matching Prefixes
        ↓
08  Verify Longest Prefix Selection
```

---

## 🖥️ Router Configuration

Example interface configuration used for the demonstration:

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

## 🧪 Test Scenario

The experiment introduces multiple overlapping routes:

```text
┌─────────────────────────────────────┐
│          ROUTING TABLE              │
├─────────────────────────────────────┤
│ Route A  →  /12                    │
│ Route B  →  /16                    │
│ Route C  →  /24                    │
│ Route D  →  /25                    │
└─────────────────────────────────────┘
```

A destination IP belonging to multiple networks is selected for testing.

The router then:

```text
Find matching routes
        ↓
Compare prefix lengths
        ↓
Identify longest prefix
        ↓
Select next hop
        ↓
Forward packet
```

---

## 📡 Traffic Testing

### Ping

```bash
ping <destination-ip>
```

Used to verify basic IP connectivity.

### Traceroute

**Windows**

```bash
tracert <destination-ip>
```

**Linux**

```bash
traceroute <destination-ip>
```

Used to observe the path taken by packets.

### iPerf3

```bash
iperf3
```

Used for controlled network traffic generation and performance testing.

---

## 🦈 Packet Analysis with Wireshark

Wireshark is used to capture and inspect packets during the experiment.

The packet-level flow can be represented as:

```text
Generated Traffic
       ↓
Router Processing
       ↓
Routing Table Lookup
       ↓
LPM Decision
       ↓
Selected Route
       ↓
Forwarded Packet
```

This helps connect the **routing-table decision** with the actual network traffic observed during the experiment.

---

## 📊 Experimental Result

| Prefix | Specificity |   Result   |
| :----: | :---------: | :--------: |
|  `/12` |     Low     |      ❌     |
|  `/16` |    Medium   |      ❌     |
|  `/24` |     High    |      ❌     |
|  `/25` |   Highest   | ✅ Selected |

### ✅ Observation

The experiment verifies that when multiple routes match a destination IP, the router selects the route with the **longest matching prefix**.

```text
/12 < /16 < /24 < /25

Specificity increases ───────────────►
```

---

## 🛠️ Tools & Technologies

| Tool                | Purpose                        |
| ------------------- | ------------------------------ |
| 🖥️ VirtualBox      | Virtual networking environment |
| 🌐 Cisco IOS        | Router configuration           |
| 🦈 Wireshark        | Packet capture & analysis      |
| 📡 iPerf3           | Network traffic generation     |
| 💻 Networking Tools | Connectivity & route testing   |

---

## 📁 Repository Structure

```text
LPM-Network-Demonstration/
│
├── 📄 LPM_Report.pdf
├── 📄 LPM_Report TC.docx
└── 📄 README.md
```

---

## 📚 Key Concepts Covered

```text
IP Routing
     │
     ├── Routing Tables
     ├── Network Prefixes
     ├── Subnetting
     ├── CIDR
     ├── Longest Prefix Match
     ├── Next-Hop Selection
     ├── Packet Forwarding
     └── Packet Analysis
```

---

## 🎓 Learning Outcomes

Through this experiment, the following concepts were practically explored:

* How routers process destination IP addresses
* How overlapping network prefixes are handled
* Why longer prefixes represent more specific routes
* How routing decisions affect packet forwarding
* How network traffic can be observed using packet-analysis tools
* How theoretical routing concepts can be validated experimentally

---

## 📑 Project Documentation

The complete technical documentation is available in the repository:

* 📄 **[LPM Report — PDF](./LPM_Report%20.pdf)**
* 📝 **[LPM Report — DOCX](./LPM_Report%20TC.docx)**

---

## 👨‍💻 Author

<div align="center">

### **Atharva Kulkarni**

**B.Tech — Computer Science & Engineering with Information Security**
G M University, Davangere

<br>

[![GitHub](https://img.shields.io/badge/GitHub-Atharva--ark06-181717?style=for-the-badge\&logo=github)](https://github.com/Atharva-ark06)

</div>

---

<div align="center">

### 🌐 **Learn → Configure → Capture → Analyze**

**A practical exploration of how routers make routing decisions using Longest Prefix Match.**

⭐ If you found this project useful, consider starring the repository.

</div>
