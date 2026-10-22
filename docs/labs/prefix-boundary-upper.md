# Lab: Upper boundary of a /25

## Objective
The last address in the /24 lies within the upper /25 range.

## Scenario
- **Route table:** `examples/prefix-boundary-upper.json`
- **Destination:** `10.20.0.255`
- **Expected selection:** `10.20.0.128/25`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 10.20.0.255 --routes examples/prefix-boundary-upper.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
What regression tests would catch an off-by-one subnet-boundary mistake?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
