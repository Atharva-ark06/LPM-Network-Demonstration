# Lab: Branch office summary and subnet

## Objective
A summary route reduces table size while a subnet route can override it.

## Scenario
- **Route table:** `examples/branch-office-summary.json`
- **Destination:** `10.44.20.8`
- **Expected selection:** `10.44.20.0/24`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 10.44.20.8 --routes examples/branch-office-summary.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
What could break if the summary exists but the specific route is missing?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
