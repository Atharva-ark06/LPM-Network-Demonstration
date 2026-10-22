# Lab: Guest VLAN subnet route

## Objective
LPM can model the route toward a guest subnet, but routing alone does not isolate guests.

## Scenario
- **Route table:** `examples/guest-vlan-routing.json`
- **Destination:** `10.30.4.5`
- **Expected selection:** `10.30.4.0/24`

## Procedure
1. Run the simulator from the repository root:

   ```bash
   python lpm_simulator.py 10.30.4.5 --routes examples/guest-vlan-routing.json
   ```

2. Read the selected network, next hop, interface, and metric.
3. Compare the result with the expected selection above.
4. Change the destination as suggested in the procedure notes and predict the result before running it.
5. Record the observed output and explain the route-selection rule in your own words.

## Reflection
Which firewall or ACL tests would be needed to validate guest isolation in an authorized lab?

## Evidence and safety
This is an offline simulation using documentation/example addresses. It does not configure a router or prove real-world reachability. If you extend the exercise to a physical or virtual router, use only an explicitly authorized isolated lab and record actual device output separately from simulator output.
