# Lab: Management subnet specificity

## Objective
A management subnet can have a distinct route from the wider corporate network.

## Scenario
- **Route table:** `examples/management-network.json`
- **Destination:** `10.99.0.12`
- **Expected selection:** `10.99.0.0/24`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 10.99.0.12 --routes examples/management-network.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
Which controls besides routing should protect management interfaces?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
