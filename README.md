# 🌐 LPM Network Demonstration

<div align="center">

### **Longest Prefix Match — Network Routing Experiment** 

A practical demonstration of how routers identify and select the **most specific route** when multiple network prefixes match a destination IP.

![Cisco](https://img.shields.io/badge/Cisco%20IOS-1E40AF?style=for-the-badge\&logo=cisco\&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-1677FF?style=for-the-badge\&logo=wireshark\&logoColor=white)
![Networking](https://img.shields.io/badge/Networking-LPM-7C3AED?style=for-the-badge)

</div>

---

## 🧠 Overview
  
**Longest Prefix Match (LPM)** is a core concept in IP routing. When a destination IP matches multiple entries in a routing table, the router chooses the route with the **longest matching prefix**, as it represents the most specific network.

This project demonstrates the concept through a virtual network environment using **Cisco IOS, VirtualBox, and Wireshark**.

---
```
```
## 🎯 Objectives

* Understand the **Longest Prefix Match** mechanism.
* Configure and test overlapping network prefixes.
* Observe router routing-table decisions.
* Generate and capture network traffic.
* Analyze packets using **Wireshark**.
* Verify how the most specific route is selected.

---

## 🔬 LPM Demonstration

The experiment uses multiple overlapping prefixes:

```text
10.0.0.0/12
10.0.0.0/16
10.0.1.0/24
10.0.1.128/25
```

For a destination matching more than one network:

```text
             Destination IP
                    │
                    ▼
        ┌─────────────────────┐
        │   Routing Table     │
        └──────────┬──────────┘
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
     /12         /16         /24 ... /25
       │           │           │
       └───────────┴───────────┘
                   │
                   ▼
          Longest Prefix Wins ✓
```

### Example

If a destination matches `/12`, `/16`, `/24`, and `/25`, the router selects **/25** because it provides the most specific match.

```text
/12  <  /16  <  /24  <  /25
Broadest                 Specific
```

---

## ⚙️ Experimental Workflow

```text
Network Design
      ↓
Router Configuration
      ↓
Overlapping Routes
      ↓
Traffic Generation
      ↓
Packet Capture
      ↓
Wireshark Analysis
      ↓
LPM Verification
```

Connectivity and traffic can be tested using:

```bash
ping <destination-ip>
tracert <destination-ip>
iperf3
```

---

## 🦈 Packet Analysis

**Wireshark** is used to capture and inspect packets generated during the experiment.

The captured traffic helps observe the communication path and correlate network traffic with the routing decisions made by the router.

---

## 🛠️ Tools & Technologies

| Tool                     | Purpose                        |
| ------------------------ | ------------------------------ |
| 🖥️ **VirtualBox**       | Virtual networking environment |
| 🌐 **Cisco IOS**         | Router configuration           |
| 🦈 **Wireshark**         | Packet capture & analysis      |
| 📡 **iPerf3**            | Traffic generation             |
| 💻 **Ping / Traceroute** | Connectivity & path testing    |

---

## 📁 Repository Structure

```text
LPM-Network-Demonstration/
│
├── 📄 LPM_Report.pdf
├── 📝 LPM_Report TC.docx
└── 📖 README.md
```

📑 **[View the Complete Project Report](./LPM_Report%20.pdf)**

---

## 📚 Key Concepts

`IP Routing` • `CIDR` • `Subnetting` • `Routing Tables` • `Longest Prefix Match` • `Packet Forwarding` • `Network Analysis`

---

## 👨‍💻 Author

**Atharva Kulkarni**
B.Tech Computer Science & Engineering — Information Security
G M University, Davangere

[![GitHub](https://img.shields.io/badge/GitHub-Atharva--ark06-181717?style=flat-square\&logo=github)](https://github.com/Atharva-ark06)

---
## Clone project 
```
git clone https://github.com/Atharva-ark06/LPM-Network-Demonstration.git

```
<div align="center">

### 🌐 **Configure • Capture • Analyze • Understand**

⭐ *A practical exploration of IP routing and Longest Prefix Match.*

</div>
