# Validation requirements

This document defines the minimum checks expected when changing the simulator, route examples, or supporting documentation. It is a project acceptance checklist, not a claim of formal certification.

## Route-file acceptance

- [ ] The top-level JSON value is an array.
- [ ] Each route is an object with a string `network` field.
- [ ] Networks parse as IPv4 CIDR; IPv6 and malformed addresses are rejected.
- [ ] Only `network`, `next_hop`, `interface`, and `metric` are accepted.
- [ ] Optional `next_hop` and `interface` values are non-empty strings.
- [ ] `metric` is a non-negative integer; booleans, floats, strings, and negative values are rejected.
- [ ] Missing files, unreadable files, and malformed JSON return a clear error.
- [ ] Host-bit normalization is documented and covered by a test.

## Route-selection acceptance

- [ ] A longer matching prefix beats a shorter prefix even if its metric is numerically higher.
- [ ] For equal prefix lengths, the lower metric wins.
- [ ] Equal prefix/equal metric ties are deterministic and preserve file order.
- [ ] A default route is selected only when it matches and no more-specific route wins.
- [ ] An empty/no-match result is handled explicitly.
- [ ] Invalid and IPv6 destination addresses are rejected.
- [ ] Each example route table has a test for its documented expected result.

## CLI and automation acceptance

Before opening or updating a pull request, run:

```bash
python -m unittest discover -s tests -v
python lpm_simulator.py --help
python lpm_simulator.py 10.0.1.200
```

On Windows, use `py` if that is the configured Python launcher. CI must run the unit suite and CLI smoke checks on pull requests. A passing test suite validates only the tested simulator behavior; it does not validate a real network.

## Documentation and security acceptance

- [ ] Commands, paths, and internal Markdown links match the repository.
- [ ] Simulated outputs are labeled as examples, not field observations.
- [ ] Router commands are framed for authorized labs or approved environments.
- [ ] Security claims distinguish route selection from firewall enforcement, route-origin validation, and end-to-end reachability.
- [ ] Any real lab claim includes reproducible context and actual evidence, with sensitive information removed.
- [ ] Changes to behavior include regression tests and an update to the route-file or algorithm documentation when relevant.

## Evidence quality

For a real lab report, record the topology, device/software versions, exact commands, timestamp, expected result, observed output, and any deviations. Redact credentials, public IPs where sensitive, tokens, and organization-specific details. A screenshot or packet capture alone does not prove the router's internal LPM computation; correlate it with an authorized route-table lookup.

## Out of scope

These checks do not certify the project as a production routing engine, security scanner, compliance tool, or substitute for a formal security assessment.
