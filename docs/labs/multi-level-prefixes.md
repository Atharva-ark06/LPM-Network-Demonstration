# Lab: Four nested prefix lengths

## Objective
A /32 wins over /24, /16, and /8 routes when all contain the destination.

## Scenario
- **Route table:** `examples/multi-level-prefixes.json`
- **Destination:** `10.1.2.3`
- **Expected selection:** `10.1.2.3/32`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 10.1.2.3 --routes examples/multi-level-prefixes.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
Why should test cases deliberately include overlapping prefixes?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
