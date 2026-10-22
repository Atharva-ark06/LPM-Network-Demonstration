# Lab: Equal prefix and metric tie

## Objective
The simulator uses file order as a deterministic tie-break when prefix length and metric are equal.

## Scenario
- **Route table:** `examples/equal-prefix-first-entry.json`
- **Destination:** `198.51.100.15`
- **Expected selection:** `198.51.100.0/24`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 198.51.100.15 --routes examples/equal-prefix-first-entry.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
Why should this simplified behavior not be assumed to describe every production router?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
