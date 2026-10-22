# Lab: No matching route

## Objective
A destination outside every listed prefix has no matching route when there is no default.

## Scenario
- **Route table:** `examples/no-matching-route.json`
- **Destination:** `203.0.113.9`
- **Expected selection:** `No route`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 203.0.113.9 --routes examples/no-matching-route.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
How should a monitoring tool distinguish a no-route result from an invalid input file?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
