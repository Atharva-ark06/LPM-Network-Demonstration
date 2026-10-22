# Wireshark filter quick reference

These are display filters for reviewing a capture. They filter what Wireshark displays; they do not configure routing or change which packets are captured.

| Goal | Display filter |
| --- | --- |
| ICMPv4 traffic | `icmp` |
| Traffic to a test destination | `ip.dst == 10.0.1.200` |
| Traffic from a test source | `ip.src == 10.0.1.10` |
| Either endpoint matches | `ip.addr == 10.0.1.200` |
| ICMP echo requests | `icmp.type == 8` |
| ICMP echo replies | `icmp.type == 0` |
| TCP traffic | `tcp` |
| DNS queries and responses | `dns` |
| Traffic between two endpoints | `ip.addr == 10.0.1.10 && ip.addr == 10.0.1.200` |

## Suggested workflow

1. Start a capture on the correct host or virtual network interface.
2. Generate test traffic in the lab.
3. Apply a display filter to isolate the packets of interest.
4. Inspect packet timestamps, source/destination addresses, protocol fields, and ICMP type/code where relevant.
5. Record what the capture proves and what it cannot prove.

A capture on an endpoint may not show every router-to-router hop. A capture alone cannot prove which route prefix a router selected; pair it with `show ip route <destination>` or equivalent device output.
