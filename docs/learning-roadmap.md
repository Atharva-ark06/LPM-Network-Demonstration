# Learning roadmap

Use the project in short stages rather than trying to learn all routing topics at once.

## Stage 1 — IP address and CIDR basics

Learn IPv4 addresses, binary representation, subnet masks, network addresses, and prefix lengths. Practice converting familiar masks such as `255.255.255.0` into `/24`.

**Checkpoint:** explain how a /24 differs from a /25.

## Stage 2 — Longest Prefix Match

Run the simulator with several destinations. List every matching prefix and explain which one is most specific.

**Checkpoint:** explain why a /25 wins over a /24 even if its metric is larger in the simulator.

## Stage 3 — Route tables

Learn the fields shown by your router platform: route source, prefix, next hop, interface, and route preference. Compare a destination-specific lookup with the simulator.

**Checkpoint:** identify which details the Python model omits.

## Stage 4 — Packet path and capture

Learn ping, traceroute/tracert, and basic Wireshark filters. Capture only traffic you are authorized to observe.

**Checkpoint:** explain why a capture shows packets on an observation point but does not directly reveal the internal LPM computation.

## Stage 5 — Security context

Study segmentation, ACLs, firewall placement, IDS/IPS visibility, route changes, and return paths.

**Checkpoint:** explain why routing is necessary for reachability but is not a substitute for access control.

## Stage 6 — Reproducibility

Add a test scenario, run the test suite, document expected results, and make a focused commit.

**Checkpoint:** another person can reproduce the lookup from your instructions.

## Optional next topics

- Static versus dynamic routing.
- Route aggregation and summarization.
- Administrative distance and routing protocol metrics.
- ECMP and failover.
- IPv6 prefix matching.
- Policy-based routing.
- Control-plane protection and route monitoring.

These topics are beyond the current simulator's implementation and should be studied with appropriate references and lab tools.
