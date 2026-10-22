# Lab: Zero metric wins equal-prefix tie

## Objective
Metric zero is valid and is preferred over a higher metric when prefix lengths are equal.

## Scenario
- **Route table:** `examples/zero-metric.json`
- **Destination:** `192.0.2.5`
- **Expected selection:** `192.0.2.0/24`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 192.0.2.5 --routes examples/zero-metric.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
Why must Boolean values be rejected even though Python treats `bool` as a subclass of `int`?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
