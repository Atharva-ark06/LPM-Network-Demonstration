# Troubleshooting the LPM demonstration

## Simulator issues

### “No matching route”
Check that the destination is valid IPv4 and that at least one configured network contains it. Add a default route (`0.0.0.0/0`) only if the scenario is intended to have one.

### Invalid route file
The route file must be a JSON array of objects. Each object needs a `network` in IPv4 CIDR notation, such as `10.0.1.0/24`. Optional `metric` values must be non-negative integers.

### A less-specific route appears in the result
Confirm that the destination is inside the more-specific network. For example, `10.0.1.200` belongs to `10.0.1.128/25`, while `10.0.1.20` does not.

### Two routes have the same prefix length
The simulator selects the lower metric; equal metrics keep the first route in the JSON list. Actual routers can use platform-specific route selection and equal-cost multipath behavior.

## Router or connectivity issues

- Check interface state with `show ip interface brief`.
- Inspect route installation with `show ip route` and destination-specific lookup where supported.
- Verify next-hop reachability and return routes.
- Confirm subnet masks and addresses on both ends.
- Check ACLs, host firewalls, VLAN configuration, and virtual network adapter mode.
- Remember that ICMP may be blocked even when other traffic works.

## Wireshark issues

- Capture on the interface that actually carries the packets.
- Confirm the capture is running before generating traffic.
- Remove display filters temporarily if no packets appear.
- Verify that the test traffic traverses the captured interface.
- Do not interpret missing ICMP replies alone as proof of a routing failure.

## Safe lab practice

Use a simulator or isolated lab you are authorized to configure. Validate proposed route changes before applying them, and do not experiment on production networks.
