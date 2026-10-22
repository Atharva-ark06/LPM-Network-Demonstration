# Lab: Nested 172.20 routes

## Objective
The most-specific subnet wins even if its metric is numerically higher than a summary route.

## Scenario
- **Route table:** `examples/overlapping-172-range.json`
- **Destination:** `172.20.1.1`
- **Expected selection:** `172.20.1.0/24`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 172.20.1.1 --routes examples/overlapping-172-range.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
How would you explain LPM priority to someone who assumes the lowest metric always wins?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
