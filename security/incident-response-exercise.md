# Incident-response tabletop: unexpected network path

## Scenario

A monitoring team reports that traffic from a lab subnet is not appearing at the expected observation point. The cause is unknown. Possibilities include a route change, an interface issue, a capture-location mismatch, filtering, asymmetric routing, or a host firewall.

This is a hypothetical exercise. No real incident or network activity is implied.

## Objectives

- Explain how LPM can affect a forwarding decision.
- Gather evidence before settling on a cause.
- Separate routing symptoms from firewall, host, and capture issues.
- Produce a concise incident timeline and next steps.

## Investigation sequence

### 1. Confirm scope

Record source, destination, protocol, time window, affected environment, and expected path. Confirm that the activity is authorized.

### 2. Inspect the routing table

On a lab router, collect the relevant route table and destination-specific lookup. Identify every matching prefix and note the most-specific route. Preserve the output with a timestamp.

### 3. Validate interfaces and next hops

Check interface state, next-hop reachability, and relevant neighbor information. Do not assume that a route's presence proves end-to-end reachability.

### 4. Check policy and observation points

Review ACLs, firewall rules, host firewall settings, capture interface selection, and display filters. Verify whether the monitoring device can observe the traffic in question.

### 5. Check the return path

A request and reply may take different paths. Inspect reverse-direction routes and relevant telemetry before concluding that a route is missing.

### 6. Compare with the model

If useful, reproduce only the route-prefix selection in `lpm_simulator.py` using a sanitized JSON route table. The model helps explain LPM but does not replace device evidence.

## Discussion prompts

1. Which prefixes match the destination?
2. Is a more-specific route present than the team expected?
3. What evidence distinguishes a routing issue from a capture/filter issue?
4. What additional data would be required to establish root cause?
5. What should be documented before any corrective change?
6. How will the team validate recovery and preserve a rollback option?

## Deliverable

Prepare a one-page incident note with:
- timeline and impact (hypothetical if this remains a tabletop);
- facts collected;
- hypotheses and evidence for/against each;
- proposed next check;
- remediation only if justified;
- validation and rollback plan.

Do not label the exercise as a real incident or claim that a route change was performed.
