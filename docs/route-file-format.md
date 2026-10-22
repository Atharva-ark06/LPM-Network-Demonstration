# Route file format

The simulator reads a JSON array from `routes.example.json` or the file passed with `--routes`.

## Fields

| Field | Required | Type | Description |
| --- | --- | --- | --- |
| `network` | Yes | String | IPv4 network in CIDR notation, such as `10.0.1.0/24` |
| `next_hop` | No | String | Descriptive next-hop label; defaults to `directly-connected` |
| `interface` | No | String | Descriptive output-interface label; defaults to `unspecified` |
| `metric` | No | Integer ≥ 0 | Tie-break value for routes with equal prefix length; defaults to `0` |

Only these four field names are accepted. The `network` value must be a string; `next_hop` and `interface`, when supplied, must be non-empty strings. The metric must be an integer greater than or equal to zero; booleans such as `true` and `false` are not valid metrics.

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

The simulator normalizes host bits using non-strict CIDR parsing. For example, `10.0.1.99/24` is treated as `10.0.1.0/24`. IPv6 networks, malformed CIDR values, unsupported fields, invalid descriptive-field types, and negative/non-integer metrics are rejected with a route-file error.

## Validation requirements

- The top-level JSON value must be an array.
- Each entry must be an object containing a string `network` field.
- Every network must parse as IPv4 CIDR.
- Optional fields must follow the types and constraints in the table above.
- Unknown fields are rejected rather than silently ignored, so a misspelled key cannot appear to have taken effect.
- A malformed file must fail with a clear error instead of producing a route-selection result.

The labels are descriptive only. The simulator does not validate that a next hop exists, that an interface is present, or that a route is safe to install on a real device.

## Selection order

1. Keep routes whose network contains the destination.
2. Prefer the route with the greatest prefix length.
3. For equal prefix lengths, prefer the lower metric.
4. For equal prefix and metric, retain the first matching route in the file.

This deterministic tie-break is intentionally simple. Real routing devices can support equal-cost multipath and use other route-selection rules.
