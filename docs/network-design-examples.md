# Illustrative network design scenarios

The following are conceptual examples for discussion. The addresses use private or documentation ranges; they are not a recommended production design.

## Scenario A — Campus subnets

A campus may have broad address allocation for a site and more-specific prefixes for laboratories, staff devices, and servers. A destination in a lab subnet may match both the campus summary and the lab-specific route. The more-specific route is used for forwarding.

**Discussion:** What route should be present on the core? Which access controls separately enforce whether staff can reach the lab?

## Scenario B — Branch summary route

A branch router may advertise or use a summary prefix to reduce routing-table size, while a more-specific route handles a special service subnet.

**Discussion:** Does the summary cover exactly the intended addresses? What happens if the more-specific route is missing? Is the default path documented?

## Scenario C — Dedicated management network

A management subnet may have a more-specific path toward a restricted management segment. Routing determines the forwarding path, but access should also be constrained with ACLs, authentication, and management-plane protections.

**Discussion:** Which devices can reach management addresses? What logs should be available for access attempts?

## Scenario D — Multiple equal-length routes

Two routes may cover the same prefix with different metrics. This simulator picks the lower metric. Real routers may also consider route source, administrative distance, protocol attributes, and equal-cost multipath.

**Discussion:** Which device and routing protocol are in use? What does the vendor documentation say about selection and failover?

## Scenario E — Default route at the edge

A default route can direct otherwise unmatched destinations toward an upstream gateway. It should be documented and monitored, because its presence changes the result for destinations that would otherwise have no matching route.

**Discussion:** Is the upstream next hop reachable? What route should be used if the upstream path fails?

## Design review checklist

- Prefixes do not overlap accidentally.
- Summaries cover the intended range and no more.
- More-specific routes have a clear owner and purpose.
- Default routes and failover behavior are documented.
- Security controls are not assumed to follow automatically from routing.
- Test cases include both matching and non-matching destinations.
