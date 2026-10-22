# Lab: Overlapping private ranges

## Objective
Nested private prefixes illustrate that the most-specific match wins.

## Scenario
- **Route table:** `examples/overlapping-private-ranges.json`
- **Destination:** `172.16.20.10`
- **Expected selection:** `172.16.20.0/24`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 172.16.20.10 --routes examples/overlapping-private-ranges.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
Why is it useful to document both summary routes and specific exceptions?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
