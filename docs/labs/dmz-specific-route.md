# Lab: DMZ-specific route

## Objective
A more-specific route can direct a carved-out block differently from its containing subnet.

## Scenario
- **Route table:** `examples/dmz-specific-route.json`
- **Destination:** `192.0.2.80`
- **Expected selection:** `192.0.2.64/26`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 192.0.2.80 --routes examples/dmz-specific-route.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
Why is route selection not the same as an access-control decision for a DMZ?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
