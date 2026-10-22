# Longest Prefix Match fundamentals

## What LPM does

A router compares a destination IP address against its forwarding table. If several route prefixes contain the destination, the route with the greatest prefix length is the most specific match and wins.

For IPv4, a prefix length ranges from `/0` to `/32`. A longer prefix fixes more network bits:

| Prefix | Mask | Addresses in block |
| --- | --- | ---: |
| `/12` | `255.240.0.0` | 1,048,576 |
| `/16` | `255.255.0.0` | 65,536 |
| `/24` | `255.255.255.0` | 256 |
| `/25` | `255.255.255.128` | 128 |
| `/0` | `0.0.0.0` | 4,294,967,296 |

The `/0` default route matches any IPv4 address, but only wins when no more-specific matching route is available.

## Worked example

Given these routes:

- `10.0.0.0/12`
- `10.0.0.0/16`
- `10.0.1.0/24`
- `10.0.1.128/25`
- `0.0.0.0/0`

For destination `10.0.1.200`, all four private prefixes and the default route match. The `10.0.1.128/25` route wins because `/25` is the longest matching prefix.

For destination `10.0.1.20`, the `/25` does not match; the `10.0.1.0/24` route is selected.

For destination `203.0.113.9`, none of the `10.0.0.0` routes match, so the default route is selected if it exists.

## LPM versus route preference

Longest-prefix matching is not the same as comparing route metrics across different prefix lengths. In this simulator, prefix length is considered first; the lowest metric breaks ties among routes with the same prefix length. Real routing platforms also apply protocol-specific route selection, administrative distance, ECMP, policy, and hardware forwarding behavior. Those topics are outside this small educational model.

## Algorithm

1. Parse the destination as an IPv4 address.
2. Find each route network that contains the destination.
3. If there are no matches, return “no route”.
4. Choose the matching network with the greatest prefix length.
5. If multiple routes have that prefix length, choose the lowest metric in this simulator.

The simulator uses Python's standard-library `ipaddress` module for CIDR parsing and address membership.
