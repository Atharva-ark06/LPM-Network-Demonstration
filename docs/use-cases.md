# Use cases

## 1. Networking classroom demonstration

**Goal:** show that a destination can match multiple prefixes and that the longest prefix wins.

**Steps:** run `python lpm_simulator.py 10.0.1.200`, identify each matching route in the printed table, and explain why `10.0.1.128/25` wins.

**Evidence:** terminal output and a short explanation of the prefix lengths.

## 2. CIDR and subnetting practice

**Goal:** connect prefix length with the size of an address block.

**Steps:** change a test destination around a network boundary, such as `10.0.1.127` and `10.0.1.128`, and compare the selected route.

**Evidence:** a table of destinations and selected prefixes.

## 3. Routing-table review exercise

**Goal:** prepare students to read a router's route table.

**Steps:** inspect `show ip route` on an authorized lab router or simulator, identify overlapping prefixes, and compare a destination-specific lookup with the Python model.

**Evidence:** sanitized route-table output and notes about any differences.

## 4. Security monitoring-path review

**Goal:** reason about whether a route change could alter the path through a monitoring or firewall device.

**Steps:** draw the expected path, identify the prefixes involved, inspect the authorized lab's route table before and after a controlled change, and confirm the intended inspection point remains in the path.

**Evidence:** topology sketch, change notes, route output, and packet-capture context. The Python tool alone cannot prove the path.

## 5. Incident-response tabletop

**Goal:** practice asking routing questions during a simulated reachability incident.

**Steps:** give learners a route table and destination, ask which entry wins, then introduce a hypothetical more-specific route and ask what additional evidence should be collected.

**Evidence:** decision notes and a list of verification commands. Clearly label hypothetical data as simulated.

## 6. Regression testing

**Goal:** ensure future code changes preserve known route-selection behavior.

**Steps:** run `python -m unittest discover -s tests -v` before and after a change.

**Evidence:** test output and the commit or pull request containing the change.

## 7. Self-study portfolio project

**Goal:** demonstrate practical understanding of routing fundamentals.

**Steps:** explain the algorithm, add a documented test case, run the checks, and include genuine screenshots or output captured from your own environment.

**Evidence:** a concise report with setup steps, test results, limitations, and lessons learned.

## Choosing the right use case

Use the CLI model for deterministic prefix-selection practice. Use a router simulator or isolated lab when the task requires interfaces, actual forwarding, packet capture, or path validation. Use enterprise telemetry and approved change records for operational or security conclusions.
