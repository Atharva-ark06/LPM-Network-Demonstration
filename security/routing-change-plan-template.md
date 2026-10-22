# Routing change plan template

Copy this template for an approved change in an isolated lab or authorized environment.

## Change metadata

- Change/ticket ID:
- Requester and approver:
- Device/environment:
- Planned window:
- Implementer:
- Business or lab reason:

## Current state

- Relevant prefixes:
- Current next hop/interface:
- Current route lookup output:
- Related firewall/ACL/monitoring dependencies:
- Configuration backup location:

## Proposed state

- Prefix to add, modify, or remove:
- New next hop/interface:
- Expected LPM result for each test destination:
- Expected forward and return path:
- Required security controls that must remain in path:

## Risk assessment

- Possible reachability impact:
- Segmentation or inspection impact:
- Dependencies and affected systems:
- Monitoring required during change:
- Conditions to stop the change:

## Implementation plan

1. Confirm authorization and maintenance window.
2. Capture current route and interface state.
3. Apply the approved change using platform-specific procedures.
4. Inspect the resulting routing table.
5. Test approved destinations and return traffic.
6. Verify required firewall, monitoring, and logging behavior.
7. Record outputs and timestamps.

## Validation matrix

| Test | Expected result | Actual result | Pass/fail |
| --- | --- | --- | --- |
| Destination A lookup | Document prefix | Fill after change | |
| Destination B lookup | Document prefix | Fill after change | |
| Next-hop reachability | Expected state | Fill after change | |
| Required inspection path | Expected observation | Fill after change | |
| Return traffic | Expected behavior | Fill after change | |

## Rollback plan

- Trigger condition:
- Exact rollback steps:
- Validation after rollback:
- Escalation contact:
- Backup/config reference:

## Closure

- Change outcome:
- Evidence location:
- Any deviations:
- Follow-up actions:
- Approver confirmation:

Do not apply example commands or this template to production without the organization's normal approval and change-control process.
