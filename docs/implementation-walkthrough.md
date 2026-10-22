# Implementation walkthrough

This guide maps the simulator's main functions to the LPM workflow.

## 1. Parse the command

The command-line interface accepts a destination IPv4 address and an optional `--routes` path. If no path is supplied, it loads `routes.example.json`.

Example:

```bash
python lpm_simulator.py 10.0.1.200 --routes routes.example.json
```

## 2. Load and validate routes

The loader parses JSON and checks the outer structure. It validates every `network` with Python's `ipaddress.ip_network`, rejects IPv6 networks, and validates the metric. It also supplies defaults for the next-hop and interface labels.

Validation matters because malformed configuration should fail clearly rather than produce a misleading route choice.

## 3. Parse the destination

The destination is parsed as an IP address. The simulator rejects malformed values and IPv6 destinations because the current implementation models IPv4 only.

## 4. Find matching routes

A route matches when the destination address belongs to its network. A destination can belong to multiple nested networks, such as a `/12`, `/16`, `/24`, and `/25`.

## 5. Select the winner

The selection key is effectively:
- negative prefix length, so longer prefixes sort first;
- metric, so lower metrics win among equal prefix lengths.

This means a `/25` beats a `/24` even when the `/25` has a larger metric. The metric tie-break is deliberately simplified and should not be confused with the full route-selection process of a real router.

## 6. Present the result

The output marks the selected row and explains the selected prefix. If no route matches, the program prints a no-route message and returns a nonzero status.

## 7. Verify behavior with tests

The tests cover:
- a longest prefix beating a lower-metric broader route;
- a destination outside a narrower route;
- default-route selection;
- no route when no default is present;
- equal-prefix metric tie-breaking;
- invalid destination and IPv6 rejection;
- route normalization and invalid route entries.

Run the tests after changes:

```bash
python -m unittest discover -s tests -v
```

## Suggested extension exercise

Add one test for a destination exactly at a prefix boundary, then implement the smallest code change necessary if the test exposes a bug. Keep the test and implementation in the same pull request, and document the new behavior.
