# Security relevance of Longest Prefix Match

LPM is a forwarding decision, not a security control by itself. Understanding it helps security practitioners reason about where packets may travel, which network boundaries traffic can cross, and why route changes can affect monitoring and enforcement.

## Why defenders should understand it

### Network segmentation

Organizations separate workstations, servers, management systems, and public-facing services into different prefixes. Correct routes help traffic reach the intended segment. Route selection must be reviewed alongside VLANs, ACLs, firewalls, and segmentation policy; a route alone does not authorize traffic.

### Firewall and monitoring placement

A route change can alter the path traffic takes through a firewall, IDS/IPS sensor, proxy, or packet broker. Security teams should verify that intended inspection points remain on the path after network changes. Asymmetric paths may cause a stateful device or sensor to see only one direction of a conversation.

### Incident response

During an incident, investigators often compare route tables, interface state, flow logs, and packet captures to understand reachability. Knowing LPM helps explain why a more-specific route can take precedence over a broad route. Preserve timestamped outputs and change records instead of relying on assumptions.

### Misconfiguration review

Unexpected prefixes, stale static routes, and an unintended default route can produce surprising paths. Route review should include ownership, origin, prefix length, next-hop reachability, and the expected security controls along the path.

### Change management

Before applying a routing change, document the intended destination prefixes, expected next hop, rollback plan, and validation commands. Afterward, compare the route table and test only approved paths.

## What this project can and cannot demonstrate

The simulator can demonstrate which example route wins for a given IPv4 destination. It can help explain overlapping routes and a simple metric tie-break among equal-length prefixes.

It cannot determine whether a real network is secure, whether a firewall rule is correct, whether a route was maliciously injected, or whether a packet traversed an inspection device. Those conclusions require real configuration, telemetry, and context.

## Defensive review questions

- Does each route have a documented business or lab purpose?
- Is the prefix more specific than intended, and is that expected?
- Is the next hop owned and reachable?
- Will traffic still pass through required inspection and logging points?
- Are both forward and return paths understood?
- Is there a tested rollback path for the change?
- Are route changes recorded in an approved change-management system?

## Safe-use note

Use this repository to learn and model decisions. Perform router configuration only in a lab or environment where you have explicit authorization. Never test route changes on production infrastructure without approval.
