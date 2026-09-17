# 🌐 LPM Network Demonstration

<div align="center">

### **Longest Prefix Match — Network Routing Experiment**

A practical demonstration of how routers select the **most specific route** when multiple IP prefixes match a destination.

![Cisco](https://img.shields.io/badge/Cisco%20IOS-1E40AF?style=flat-square)
![Wireshark](https://img.shields.io/badge/Wireshark-1677FF?style=flat-square)
![Networking](https://img.shields.io/badge/Networking-LPM-7C3AED?style=flat-square)

</div>

---

## 🧠 About

**Longest Prefix Match (LPM)** is a fundamental IP routing concept where the router selects the route with the **longest matching network prefix**.

This project demonstrates LPM using virtual networking, Cisco IOS routing, and Wireshark packet analysis.

```text
/12  →  /16  →  /24  →  /25
Broadest                 Most Specific
```

---

## 🎯 Objectives

* Understand **Longest Prefix Match**
* Configure overlapping network routes
* Analyze routing-table decisions
* Generate and capture network traffic
* Verify packet forwarding using **Wireshark**

---

## 🔬 Experiment

Multiple prefixes are configured:

```text
10.0.0.0/12
10.0.0.0/16
10.0.1.0/24
10.0.1.128/25
```

When a destination matches multiple routes, the router chooses the **longest prefix**.

```text
Multiple Matches
       ↓
Compare Prefix Length
       ↓
Longest Prefix
       ↓
Selected Route ✓
```

---

## 🛠️ Tools

**VirtualBox** • **Cisco IOS** • **Wireshark** • **iPerf3** • **Ping / Traceroute**

---

## 📁 Files

```text
LPM-Network-Demonstration/
├── LPM_Report.pdf
├── LPM_Report TC.docx
└── README.md
```

📄 [View Project Report](./LPM_Report%20.pdf)

---

## 👨‍💻 Author

**Atharva Kulkarni**
B.Tech CSE — Information Security
G M University, Davangere

[GitHub](https://github.com/Atharva-ark06)

---

<div align="center">

**🌐 Configure • Capture • Analyze • Understand**

</div>
