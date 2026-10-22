# Lab: Summary, subnet, and small block

## Objective
A /27 wins over a /24 and /16 because the prefix is more specific.

## Scenario
- **Route table:** `examples/summary-vs-subnet.json`
- **Destination:** `10.60.12.34`
- **Expected selection:** `10.60.12.32/27`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 10.60.12.34 --routes examples/summary-vs-subnet.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
How can summarization simplify routing while specific exceptions preserve intended paths?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
