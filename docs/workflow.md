# Project workflow

## Workflow at a glance

```text
Define learning question
        |
        v
Select destination + route table
        |
        v
Run Python LPM simulation
        |
        v
Explain selected prefix
        |
        v
(Optional) inspect authorized router table
        |
        v
(Optional) generate traffic and capture packets
        |
        v
Compare evidence, document limitations
        |
        v
Run tests and review changes
```

## Stage 1 — Define the question

Examples: Which route wins for a destination? What changes when a /25 is added? What happens when a default route is removed? Write down the expected result before running the experiment.

## Stage 2 — Choose the input

Use `routes.example.json` or create a custom route file. Include overlapping prefixes when demonstrating LPM. Use a default route only when the scenario intends to provide a catch-all route.

## Stage 3 — Run and interpret

Run the CLI, identify all matching routes, and explain why the selected prefix is more specific. If equal prefix lengths exist, explain the simulator's metric tie-break.

## Stage 4 — Compare with a real or simulated router (optional)

Inspect the router's route table and destination-specific lookup. Differences may result from a different route table, route installation, policy, administrative distance, or platform behavior. The Python model only implements a narrow subset.

## Stage 5 — Observe traffic (optional)

Capture authorized lab traffic on an interface that can observe it. Use a suitable Wireshark display filter. A packet capture is evidence of packets visible at that observation point; it is not a direct view of a router's internal LPM computation.

## Stage 6 — Record findings

For each test, record:
- the question and assumptions;
- route-file version or sanitized router output;
- destination address;
- expected prefix;
- observed simulator result;
- any real-lab result, if performed;
- limitations and unresolved questions.

Clearly distinguish example data from measured data.

## Stage 7 — Quality check

Run the unit tests, check documentation links and commands, and review the diff before opening a pull request. Keep each change focused and describe its purpose in the commit message.
