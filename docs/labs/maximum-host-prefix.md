# Lab: Maximum IPv4 host prefix

## Objective
A /32 is the most-specific IPv4 prefix and matches exactly one address.

## Scenario
- **Route table:** `examples/maximum-host-prefix.json`
- **Destination:** `203.0.113.255`
- **Expected selection:** `203.0.113.255/32`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 203.0.113.255 --routes examples/maximum-host-prefix.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
What is the difference between matching a /32 route and proving that the host is alive?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
