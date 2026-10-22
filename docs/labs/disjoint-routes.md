# Lab: Disjoint routes and exact subnet match

## Objective
Only routes that contain the destination participate in the LPM comparison; a lower metric on a disjoint route is irrelevant.

## Scenario
- **Route table:** `examples/disjoint-routes.json`
- **Destination:** `192.0.2.10`
- **Expected selection:** `192.0.2.0/24`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 192.0.2.10 --routes examples/disjoint-routes.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
Why is it incorrect to compare metrics before checking whether a route matches?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
