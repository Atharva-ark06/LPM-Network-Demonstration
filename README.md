# 🌐 LPM Network Demonstration

**An educational lab for understanding IPv4 Longest Prefix Match (LPM), routing-table decisions, and packet observation.**

This repository pairs the original project report with a small Python simulator, automated tests, and practical lab notes. It is designed for networking and information-security students learning how a router chooses the most specific matching route.

## What is included

- **IPv4 LPM simulator** — evaluate a destination against a JSON routing table.
- **Example routes** — overlapping prefixes and a default route to make the selection visible.
- **Unit tests** — cover prefix precedence, metrics, default/no-route behavior, and invalid input.
- **Lab guides** — router inspection examples, Wireshark filters, troubleshooting, and core concepts.
- **Original reports** — the submitted PDF report and editable document.

## Quick start

Requirements: **Python 3.10+**. The simulator uses only the Python standard library; no package installation is needed.

```bash
git clone https://github.com/Atharva-ark06/LPM-Network-Demonstration.git
cd LPM-Network-Demonstration

python lpm_simulator.py 10.0.1.200
python lpm_simulator.py 10.0.1.20
python lpm_simulator.py 203.0.113.9
```

The example route table is `routes.example.json`. To use your own route table:

```bash
python lpm_simulator.py 10.0.1.200 --routes routes.example.json
```

Run the test suite:

```bash
python -m unittest discover -s tests -v
```

## Example: why the longest prefix wins

The example table includes these overlapping networks:

| Route | Meaning |
| --- | --- |
| `10.0.0.0/12` | Broad match |
| `10.0.0.0/16` | More specific match |
| `10.0.1.0/24` | Still more specific |
| `10.0.1.128/25` | Most specific match for the upper half of the /24 |
| `0.0.0.0/0` | Default route if no more-specific route matches |

For destination `10.0.1.200`, the selected route is `10.0.1.128/25`. For `10.0.1.20`, the `/25` does not match, so `10.0.1.0/24` wins. For `203.0.113.9`, the example default route is selected.

The simulator chooses the greatest matching prefix length first. For equal prefix lengths, it chooses the lowest configured metric; equal metrics retain the first route in the file. This is an educational model, not a complete implementation of a router's route-selection policy.

## Lab workflow

```text
Inspect topology and routes
          ↓
Run a destination lookup
          ↓
Compare with router route-table output
          ↓
Generate test traffic in an isolated lab
          ↓
Capture and inspect packets in Wireshark
          ↓
Record evidence and conclusions
```

**Important:** a packet capture can show traffic on the observed interface, but it does not directly expose the router's internal LPM decision. Correlate capture evidence with the router's own routing-table lookup. Only mark the physical/virtual lab as completed after collecting actual outputs.

## Documentation

- [LPM fundamentals and worked examples](docs/lpm-fundamentals.md)
- [Step-by-step lab guide](docs/lab-guide.md)
- [Wireshark filter reference](docs/wireshark-filters.md)
- [Troubleshooting](docs/troubleshooting.md)

## Original project reports

- [Open the PDF report](./LPM_Report%20.pdf)
- [Open the editable report (DOCX)](./LPM_Report%20TC.docx)

## Tools and concepts

**Concepts:** IPv4 routing, CIDR, subnetting, routing tables, prefix matching, packet forwarding, traffic inspection.

**Lab tools discussed:** Cisco IOS or a compatible router simulator, VirtualBox, Wireshark, ping, traceroute/tracert, and iPerf3. The repository's Python simulator is standalone and does not configure real routers or generate network traffic.

## Scope and limitations

- The simulator supports IPv4 routes only.
- It demonstrates prefix selection and a simple metric tie-break; it is not a full routing protocol implementation.
- It does not model ARP/ND, ACLs, NAT, routing protocol convergence, administrative distance, policy routing, or actual packet forwarding.
- Router commands in the guide are examples for an isolated, authorized lab. Adapt interface names and next hops to your topology.

## Author

**Atharva Kulkarni**  
B.Tech Computer Science & Engineering — Information Security  
G M University, Davangere

[GitHub profile](https://github.com/Atharva-ark06)

---

**Configure • Compare • Capture • Analyze**


## Extended project documentation

The links below expand on the project's purpose, implementation, setup, workflows, and security context.

### Project and implementation
- [Project overview and objectives](docs/project-overview.md)
- [Architecture and data flow](docs/architecture.md)
- [Implementation walkthrough](docs/implementation-walkthrough.md)
- [Learning roadmap](docs/learning-roadmap.md)
- [Glossary](docs/glossary.md)
- [FAQ](docs/faq.md)
- [Further reading and references](docs/references.md)

### Setup, workflow, and evidence
- [Cross-platform setup guide](docs/setup-guide.md)
- [End-to-end workflow](docs/workflow.md)
- [Validation and evidence guide](docs/validation-and-evidence.md)
- [Lab report template](docs/lab-report-template.md)
- [Use cases](docs/use-cases.md)
- [Network design examples](docs/network-design-examples.md)

### Security learning folder
- [Security resources overview](security/README.md)
- [Security relevance of LPM](docs/security-relevance.md)
- [Routing threat-model exercise](docs/threat-model.md)
- [Defensive route review checklist](security/route-review-checklist.md)
- [Incident-response tabletop exercise](security/incident-response-exercise.md)
- [Routing change and rollback template](security/routing-change-plan-template.md)

### Additional route-table examples
- [No default route](examples/no-default-route.json)
- [Equal-prefix metric tie-break](examples/equal-prefix-metrics.json)
- [Campus segmentation scenario](examples/campus-segmentation.json)

These materials explain routing and security concepts; they do not imply that a real router was configured or a packet capture was collected. Keep simulated examples separate from observations made in your own authorized lab.
