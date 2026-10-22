# Lab: Specific route beats default

## Objective
Prefix length is considered before metric, so a /24 beats a default route even with a higher metric.

## Scenario
- **Route table:** `examples/specific-route-beats-default.json`
- **Destination:** `198.51.100.5`
- **Expected selection:** `198.51.100.0/24`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 198.51.100.5 --routes examples/specific-route-beats-default.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
Why would sorting routes by metric alone produce the wrong answer?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
