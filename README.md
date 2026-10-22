# LPM Network Demonstration

[![LPM simulator tests](https://github.com/Atharva-ark06/LPM-Network-Demonstration/actions/workflows/python-tests.yml/badge.svg?branch=master)](https://github.com/Atharva-ark06/LPM-Network-Demonstration/actions/workflows/python-tests.yml)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
![Focus](https://img.shields.io/badge/focus-networking%20%26%20security-5b6ee1)

An educational IPv4 **Longest Prefix Match (LPM)** lab that combines a runnable Python simulator, example routing tables, automated tests, and networking/security learning guides.

The project demonstrates how a destination can match multiple routes—and why the route with the **longest matching prefix** is selected. It also explores how routing decisions relate to network segmentation, firewall visibility, troubleshooting, and incident response.

## Get started

**Requirements:** Python 3.10 or newer. No third-party packages are needed.

```bash
git clone https://github.com/Atharva-ark06/LPM-Network-Demonstration.git
cd LPM-Network-Demonstration

python lpm_simulator.py 10.0.1.200
python lpm_simulator.py 10.0.1.20
python lpm_simulator.py 203.0.113.9
```

On Windows, use `py` instead of `python` if that is how Python is installed. Full instructions are in the [setup guide](docs/setup-guide.md).

Run the automated tests:

```bash
python -m unittest discover -s tests -v
```

## How LPM works

When multiple routing-table entries match a destination, the entry with the greatest prefix length is the most specific match.

The included `routes.example.json` contains overlapping prefixes:

| Route | Role |
| --- | --- |
| `10.0.0.0/12` | Broad network |
| `10.0.0.0/16` | More specific network |
| `10.0.1.0/24` | Subnet route |
| `10.0.1.128/25` | Most specific route for the upper half of the /24 |
| `0.0.0.0/0` | Default route |

Try these lookups:

| Destination | Expected selection | Why |
| --- | --- | --- |
| `10.0.1.200` | `10.0.1.128/25` | Longest matching prefix |
| `10.0.1.20` | `10.0.1.0/24` | The /25 does not contain this address |
| `203.0.113.9` | `0.0.0.0/0` | Only the default route matches |

The simulator compares prefix length first, then uses the lowest metric for routes with equal prefix lengths. If both prefix length and metric are equal, the first matching route in the file wins. This deterministic rule is for teaching; real routers may apply additional route-selection rules or support equal-cost paths.

## Project workflow

```text
Choose a destination and route table
                ↓
Run the LPM simulator
                ↓
Explain the selected prefix
                ↓
Optionally compare with an authorized router lookup
                ↓
Optionally inspect lab traffic in Wireshark
                ↓
Record evidence and run regression tests
```

The Python simulator models route selection only. It does not configure a router, forward packets, generate traffic, or prove that a packet traversed a particular device. A packet capture shows traffic visible at its observation point—not the router's internal LPM computation.

## What's included

- **`lpm_simulator.py`** — command-line IPv4 route-selection simulator.
- **`routes.example.json` and `examples/`** — overlapping prefixes, no-default-route, equal-prefix metric, and campus-segmentation scenarios.
- **`tests/`** — automated checks for route selection, invalid input, and example scenarios.
- **GitHub Actions** — runs the test suite and command-line smoke checks.
- **`docs/`** — project overview, architecture, implementation, setup, workflow, use cases, lab guides, troubleshooting, and learning resources.
- **`security/`** — defensive route-review checklist, incident-response tabletop, and routing change/rollback template.
- **Original academic reports** — PDF and editable DOCX files.

## Documentation

| If you want to… | Start here |
| --- | --- |
| Understand the project and its design | [Project overview](docs/project-overview.md) · [Architecture](docs/architecture.md) |
| Learn the algorithm and code | [LPM fundamentals](docs/lpm-fundamentals.md) · [Implementation walkthrough](docs/implementation-walkthrough.md) |
| Install and run the project | [Setup guide](docs/setup-guide.md) · [Route-file format](docs/route-file-format.md) |
| Understand acceptance checks | [Validation requirements](docs/validation-requirements.md) · [Validation and evidence](docs/validation-and-evidence.md) |
| Follow a practical networking lab | [Lab guide](docs/lab-guide.md) · [Wireshark filters](docs/wireshark-filters.md) |
| Explore scenarios and applications | [Use cases](docs/use-cases.md) · [Network design examples](docs/network-design-examples.md) |
| Understand the security relevance | [Security relevance and limitations](docs/security-relevance.md) · [Threat-model exercise](docs/threat-model.md) |
| Review routes defensively | [Route review checklist](security/route-review-checklist.md) · [Incident-response exercise](security/incident-response-exercise.md) |
| Prepare evidence or a report | [Lab report template](docs/lab-report-template.md) |
| Troubleshoot or explore further | [Troubleshooting](docs/troubleshooting.md) · [FAQ](docs/faq.md) · [References](docs/references.md) |

Additional learning material is available in the [glossary](docs/glossary.md), [learning roadmap](docs/learning-roadmap.md), [workflow guide](docs/workflow.md), and [sample results](docs/sample-results.md).

## Security relevance

LPM knowledge helps network defenders reason about:

- **Segmentation:** which route may carry traffic toward a subnet; firewalls and ACLs separately enforce access policy.
- **Inspection visibility:** route changes can affect whether traffic passes through expected monitoring points.
- **Incident response:** route tables, interface state, captures, and change records help investigate reachability issues.
- **Change control:** expected routes, validation steps, and rollback plans make changes easier to review.

This repository is an educational simulator, **not** a security scanner or production routing engine. It does not detect route hijacking, audit firewall policy, query real devices, or establish that a network is secure. Read the [security claims and limitations](docs/security-relevance.md) before interpreting results. Use router commands only in a lab or environment where you have explicit authorization.

## Original academic reports

- [PDF report](./LPM_Report%20.pdf)
- [Editable DOCX report](./LPM_Report%20TC.docx)

## Scope and limitations

- IPv4 only; IPv6 addresses and networks are rejected.
- Uses longest-prefix selection and a simplified metric tie-break.
- Does not model routing protocols, administrative distance, policy-based routing, ECMP, ARP, ACLs, NAT, convergence, or real packet forwarding.
- Next-hop and interface fields are descriptive labels; the simulator does not check their reachability.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Add or update tests when changing behavior, run the suite locally, and clearly distinguish simulated examples from observations collected in an authorized lab. Use the [validation requirements](docs/validation-requirements.md) as the review checklist.

## Author

**Atharva Kulkarni** · B.Tech Computer Science & Engineering (Information Security)  
G M University, Davangere · [GitHub](https://github.com/Atharva-ark06)

---

**Configure · Compare · Capture · Analyze**
