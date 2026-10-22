# LPM lab walkthrough

This guide combines the repository's simulator with a suggested router-and-capture lab. Cisco IOS commands are examples; adapt interface names and addressing to your own authorized lab topology.

## Part A — Run the simulator

Requirements: Python 3.10 or newer. No third-party packages are required.

From the repository root:

```bash
python lpm_simulator.py 10.0.1.200
python lpm_simulator.py 10.0.1.20
python lpm_simulator.py 203.0.113.9
python -m unittest discover -s tests -v
```

Use a custom route table by passing `--routes path/to/routes.json`. See `routes.example.json` for the schema. Each route requires a `network`; `next_hop`, `interface`, and non-negative integer `metric` are optional.

Expected observations:
- `10.0.1.200` selects `10.0.1.128/25`.
- `10.0.1.20` selects `10.0.1.0/24`.
- `203.0.113.9` selects `0.0.0.0/0` when the example default route is present.

## Part B — Choose an offline practice lab

The [scenario lab collection](labs/) provides focused exercises for host routes, default routes, nested prefixes, route metrics, subnet boundaries, VPN overrides, management networks, DMZ routing, guest VLANs, and no-match behavior.

| Topic | Exercise |
| --- | --- |
| Host route and /32 | [Host route priority](labs/host-route-priority.md) |
| Default route | [Default-only table](labs/default-only.md) |
| Nested private ranges | [Overlapping private ranges](labs/overlapping-private-ranges.md) |
| Summary and subnet | [Branch office summary](labs/branch-office-summary.md) |
| DMZ exception | [DMZ-specific route](labs/dmz-specific-route.md) |
| VPN override | [VPN-specific route](labs/vpn-more-specific-route.md) |
| Management routing | [Management subnet](labs/management-network.md) |
| Guest segment | [Guest VLAN route](labs/guest-vlan-routing.md) |
| Equal prefix and metric | [First-entry tie-break](labs/equal-prefix-first-entry.md) |
| Subnet boundaries | [Lower /25 boundary](labs/prefix-boundary-lower.md) · [Upper /25 boundary](labs/prefix-boundary-upper.md) |
| Nested prefix hierarchy | [Multi-level prefixes](labs/multi-level-prefixes.md) |
| Metric zero | [Zero metric](labs/zero-metric.md) |
| Exact host match | [Maximum host prefix](labs/maximum-host-prefix.md) |
| No matching route | [No-match scenario](labs/no-matching-route.md) |
| Specific versus default | [Specific route wins](labs/specific-route-beats-default.md) |
| Nested 172.20 ranges | [Overlapping 172 range](labs/overlapping-172-range.md) |
| Small subnet block | [Summary versus /27](labs/summary-vs-subnet.md) |
| Disjoint prefixes | [Disjoint routes](labs/disjoint-routes.md) |

Run any example with:

```bash
python lpm_simulator.py <destination-ip> --routes examples/<scenario>.json
```

Predict the selected route before running the command, then explain the result in terms of prefix length, metric, and whether each route contains the destination.

## Part C — Observe a router's routing table

On a Cisco IOS device or simulator where you are authorized to configure routes, inspect the current table first:

```text
show ip route
show ip route 10.0.1.200
show ip interface brief
```

Static-route syntax example (replace the next hop with a reachable address in your topology):

```text
configure terminal
ip route 10.0.0.0 255.240.0.0 192.0.2.1
ip route 10.0.0.0 255.255.0.0 192.0.2.2
ip route 10.0.1.0 255.255.255.0 192.0.2.3
ip route 10.0.1.128 255.255.255.128 192.0.2.4
end
show ip route
```

These commands illustrate overlapping route entries only. They will not provide connectivity unless the next hops and interfaces are valid in the actual topology. Do not paste them into a production router.

## Part D — Generate and capture traffic

1. Choose a destination reachable in your isolated lab.
2. Start a Wireshark capture on the interface that can observe the traffic.
3. Generate a small amount of traffic using `ping <destination-ip>` or the platform's equivalent.
4. Inspect ICMP echo request/reply packets and their source/destination IP addresses.
5. Compare the observed traffic with the route selected by the router's own routing table.

Important: a packet capture normally shows packets on the observed link; it does not directly display the router's internal LPM decision. Correlate packet evidence with routing-table output. Use `traceroute`/`tracert` for path clues, understanding that filtering and asymmetric routing can affect results.

## Record results

| Destination | Expected selected prefix | Actual route-table result | Capture notes |
| --- | --- | --- | --- |
| `10.0.1.200` | `10.0.1.128/25` | Fill during lab | Fill during lab |
| `10.0.1.20` | `10.0.1.0/24` | Fill during lab | Fill during lab |
| `203.0.113.9` | `0.0.0.0/0` if configured | Fill during lab | Fill during lab |

Do not mark the lab as completed until you have collected the real router output and capture evidence. Simulator results are not evidence of a real network configuration.
