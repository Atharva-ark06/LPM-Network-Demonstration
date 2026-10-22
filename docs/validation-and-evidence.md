# Validation and evidence guide

Use this guide to make project results reproducible. It intentionally separates simulator output from observations collected on a real or virtual network.

## Validation layers

### Layer 1 — Input validation

Check malformed destination strings, IPv6 destinations, invalid JSON, invalid networks, and invalid metrics. Expected behavior is a clear error and nonzero exit status.

### Layer 2 — Algorithm validation

Check a destination matching several prefixes, a destination outside the most-specific route, a default route, and a no-route case. Confirm prefix length takes priority over metric.

### Layer 3 — Regression validation

Run:

```bash
python -m unittest discover -s tests -v
```

Record the command, Python version, date, and whether the command completed successfully.

### Layer 4 — Optional router validation

On an authorized lab device, collect the relevant route-table output and destination-specific lookup. Sanitize internal addresses or sensitive device details before publishing.

### Layer 5 — Optional packet observation

Record the capture interface, time window, display filter, test source/destination, and relevant packet fields. Do not upload captures containing personal or sensitive data without permission.

## Result template

| Field | Value |
| --- | --- |
| Test ID | e.g. LPM-01 |
| Question | Which prefix should win? |
| Destination | IPv4 address |
| Route-table source | Example JSON / lab device |
| Expected prefix | CIDR |
| Simulator output | Paste or link to output |
| Router result | Not performed / observed result |
| Capture evidence | Not performed / file reference |
| Conclusion | What the evidence supports |
| Limitations | What was not tested |

## Evidence integrity

- Do not describe an expected result as a measured result.
- Do not claim a router or Wireshark test ran unless it did.
- Include enough configuration context for another learner to reproduce the scenario.
- Remove secrets, public IPs when sensitive, hostnames, MAC addresses, and user data before sharing evidence.
- Keep the original evidence and explain any redactions.
