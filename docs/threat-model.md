# Routing-focused threat-model exercise

This document is a defensive learning exercise, not a claim that the repository detects or prevents these scenarios.

## Assets

- Network reachability and availability.
- Intended segmentation boundaries.
- Firewall, IDS/IPS, and logging visibility.
- Integrity of route configuration.
- Reliability of incident-response evidence.

## Trust boundaries

Typical boundaries include user VLANs, server networks, management networks, internet edge devices, VPN connections, and monitoring infrastructure. Actual boundaries vary by topology and should be drawn before analysis.

## Example failure scenarios

### Unexpected more-specific route

A more-specific route may take precedence over a broader route. During a review, verify who owns the prefix, why it exists, and whether its path crosses the expected security controls.

### Incorrect or stale next hop

A route may point toward an unreachable or unintended next hop. Validate reachability and configuration ownership in the authorized environment.

### Inspection-path bypass

A routing change may alter the path such that traffic no longer crosses an intended inspection point. Verify path and telemetry from both directions where relevant.

### Missing return route

Forward traffic can reach a destination while replies take a different path or fail. Check both directions before drawing conclusions from a one-sided capture.

### Default-route assumption

A default route is only used when no more-specific matching route is selected in the model. Confirm that the actual device has the expected default route and that its next hop is valid.

## Defensive controls

- Route ownership and change approval.
- Configuration backups and documented rollback.
- Monitoring for unexpected route changes.
- Route-table and next-hop validation after changes.
- Firewall and segmentation rule reviews.
- Flow telemetry and packet captures at appropriate observation points.
- Change records with timestamps and operator identity.

## Analysis worksheet

| Question | Evidence to collect |
| --- | --- |
| Which prefixes match the destination? | Route table or simulator output |
| Which prefix is selected? | Destination-specific route lookup |
| Is the next hop reachable? | Interface status and authorized reachability test |
| Is the intended inspection point on the path? | Topology, route outputs, telemetry |
| Is return traffic accounted for? | Reverse route and capture/flow evidence |
| Can the change be rolled back? | Approved change and rollback plan |

## Limitations

The repository's simulator has no threat-detection logic, telemetry ingestion, or router integration. Use it to explain the prefix-selection concept; use real configuration and trusted operational data for security assessment.
