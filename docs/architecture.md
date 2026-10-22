# Architecture and data flow

## Component map

```text
User command
    |
    v
Argument parser (destination, --routes)
    |
    v
JSON route loader and validator
    |
    v
Validated route records (IPv4Network + metadata)
    |
    v
Destination IPv4 parser
    |
    v
Matching-prefix filter
    |
    v
Longest-prefix selection
    |
    v
Metric tie-break for equal prefix lengths
    |
    v
Readable table + selected route / no-route result
```

## Components

### Command-line interface

The `main()` function parses the destination and optional route-file path. It converts validation errors into concise error messages and exit codes rather than exposing a traceback for expected input mistakes.

### Route loader

`load_routes()` reads UTF-8 JSON and requires a list of objects. Each object must contain a `network` value that parses as an IPv4 network. It normalizes host bits using non-strict CIDR parsing and validates that `metric` is a non-negative integer.

### Selection function

`select_route()` validates that the destination is IPv4, filters routes whose networks contain the address, and returns `None` if no route matches. It sorts selection priority by descending prefix length and then ascending metric. Python's stable ordering means equal prefix/equal metric ties keep the first matching route in the input.

### Output layer

The CLI prints each configured route and marks the selected one. It also reports the selected network, next-hop label, interface label, and the prefix length that explains the decision.

### Tests and CI

The standard-library `unittest` suite checks known decisions and invalid inputs. GitHub Actions installs Python, runs the tests, verifies CLI help, and performs a sample lookup.

## Data model

Each JSON route can contain:
- `network`: IPv4 CIDR string (required)
- `next_hop`: descriptive next-hop label (optional)
- `interface`: descriptive interface label (optional)
- `metric`: non-negative integer tie-break value (optional)

The labels are educational metadata. The simulator does not resolve next hops, query interfaces, install routes, or forward packets.

## Complexity

For a routing table containing (n) entries, the current implementation checks each route once, so matching is (O(n)) in the number of routes, plus selection work over matching entries. This is appropriate for a small teaching example. High-performance forwarding systems use specialized data structures and hardware; this project does not aim to replicate them.

## Design choices

- Standard library only: simple installation and reproducible tests.
- JSON input: easy to edit and review in version control.
- Explicit IPv4 validation: avoids silently mixing IPv4 and IPv6 behavior.
- Clear tie-break rule: deterministic results for teaching.
- Honest scope: distinguish model behavior from real router operation.
