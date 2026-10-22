# Sample lookup scenarios

These are expected outcomes based on `routes.example.json`. They are illustrative simulator results, not evidence from a physical router or Wireshark capture.

| Destination | Expected selected route | Why |
| --- | --- | --- |
| `10.0.1.200` | `10.0.1.128/25` | It belongs to the upper half of the `/24` and matches the most specific prefix. |
| `10.0.1.20` | `10.0.1.0/24` | It is outside `10.0.1.128/25`, but inside the `/24`. |
| `10.0.2.20` | `10.0.0.0/16` | It matches `/12` and `/16`, but not the `/24` or `/25`. |
| `10.1.2.3` | `10.0.0.0/12` | It matches the `/12` but is outside `10.0.0.0/16`. |
| `203.0.113.9` | `0.0.0.0/0` | No listed `10.0.0.0` prefix matches, so the default route is used. |

Run an individual example:

```bash
python lpm_simulator.py 10.0.1.200
```

To verify the same decision on a router, inspect its route table and destination-specific lookup. Results may differ if the actual router has a different routing table or additional selection policies.
