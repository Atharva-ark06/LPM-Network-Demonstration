# Route file format

The simulator reads a JSON array from `routes.example.json` or the file passed with `--routes`.

## Fields

| Field | Required | Type | Description |
| --- | --- | --- | --- |
| `network` | Yes | String | IPv4 network in CIDR notation, such as `10.0.1.0/24` |
| `next_hop` | No | String | Label for the next-hop address; defaults to `directly-connected` |
| `interface` | No | String | Output-interface label; defaults to `unspecified` |
| `metric` | No | Integer ≥ 0 | Tie-break value for routes with equal prefix length; defaults to `0` |

Example:

```json
[
  {
    "network": "10.0.1.0/24",
    "next_hop": "192.0.2.1",
    "interface": "GigabitEthernet0/0",
    "metric": 10
  },
  {
    "network": "0.0.0.0/0",
    "next_hop": "192.0.2.254",
    "interface": "GigabitEthernet0/1",
    "metric": 100
  }
]
```

The simulator normalizes host bits using non-strict CIDR parsing. For example, `10.0.1.99/24` is treated as `10.0.1.0/24`. IPv6 networks and negative/non-integer metrics are rejected.

## Selection order

1. Keep routes whose network contains the destination.
2. Prefer the route with the greatest prefix length.
3. For equal prefix lengths, prefer the lower metric.
4. For equal prefix and metric, retain the first matching route in the file.

This deterministic tie-break is intentionally simple. Real routing devices can support equal-cost multipath and use other route-selection rules.
