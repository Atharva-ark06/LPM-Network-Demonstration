# Lab: VPN destination override

## Objective
A VPN-specific subnet can take precedence over broader corporate routes.

## Scenario
- **Route table:** `examples/vpn-more-specific-route.json`
- **Destination:** `10.8.4.15`
- **Expected selection:** `10.8.4.0/24`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 10.8.4.15 --routes examples/vpn-more-specific-route.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
What additional evidence is needed to confirm a real destination uses the VPN tunnel?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
