# Defensive route review checklist

Use this checklist only with network configurations you are authorized to inspect.

## Route inventory

- [ ] Identify the device, environment, and configuration snapshot date.
- [ ] List routes relevant to the destination under review.
- [ ] Record prefix, route source, next hop, interface, metric/preference, and route owner where available.
- [ ] Identify default routes and any unusually specific prefixes.
- [ ] Confirm that summarized prefixes cover the intended address ranges.

## Path and policy

- [ ] Identify expected forward and return paths.
- [ ] Confirm required firewalls, IDS/IPS sensors, proxies, and logging points remain on the intended path.
- [ ] Review ACLs and security policy separately from route selection.
- [ ] Check next-hop reachability and interface status.
- [ ] Consider asymmetric routing and its effect on stateful inspection and packet capture.

## Change integrity

- [ ] Confirm that the route has an owner and documented purpose.
- [ ] Compare current configuration with an approved baseline.
- [ ] Review recent configuration changes and route advertisements if available.
- [ ] Ensure rollback instructions and a maintenance window exist for planned changes.
- [ ] Capture before/after route lookups and relevant telemetry.

## Evidence handling

- [ ] Timestamp the outputs and record the device/tool used.
- [ ] Sanitize secrets, personal data, internal hostnames, and sensitive addressing before sharing.
- [ ] Separate observed facts from hypotheses.
- [ ] Do not infer a route's intent from prefix length alone.
- [ ] Do not treat a packet capture at one point as proof of the entire end-to-end path.

## Outcome

- **Expected:** configuration aligns with the documented design.
- **Needs investigation:** evidence is incomplete or behavior differs from expectations.
- **Change required:** a confirmed discrepancy has an approved remediation and rollback plan.

This checklist supports a review process; it is not an automated audit or certification.
