# Lab: Default route as the only candidate

## Objective
A default route is the fallback for any IPv4 destination not matched by a more-specific route.

## Scenario
- **Route table:** `examples/default-only.json`
- **Destination:** `203.0.113.25`
- **Expected selection:** `0.0.0.0/0`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 203.0.113.25 --routes examples/default-only.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
What would change if the table were empty? What does a default route not prove about connectivity?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
