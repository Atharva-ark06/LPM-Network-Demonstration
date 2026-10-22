# Lab: Host route takes precedence

## Objective
A /32 route matches exactly one IPv4 address and outranks broader prefixes.

## Scenario
- **Route table:** `examples/host-route-priority.json`
- **Destination:** `192.0.2.10`
- **Expected selection:** `192.0.2.10/32`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 192.0.2.10 --routes examples/host-route-priority.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
What operational reason might justify a host route, and what review should accompany it?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
