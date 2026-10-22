# Project overview

## Purpose

LPM Network Demonstration is an educational project about how an IPv4 router selects a forwarding-table entry when more than one route matches a destination. The repository combines the original academic report with a small executable model and repeatable learning materials.

## Problem statement

A routing table can contain overlapping prefixes. A destination such as `10.0.1.200` may match a broad route and several narrower routes at once. The router must use the most specific matching prefix to decide which forwarding entry applies. Memorizing the rule is easier when learners can change inputs and inspect the selection.

## Objectives

1. Explain IPv4 CIDR prefixes and route specificity.
2. Make LPM decisions reproducible using a small command-line tool.
3. Provide a route table that includes overlapping prefixes and a default route.
4. Teach learners to compare a model's answer with a real or simulated router's routing-table lookup.
5. Encourage evidence-based reporting by separating expected results from results actually collected in a lab.
6. Provide automated tests so changes to the simulator are less likely to break known scenarios.

## Deliverables

- `lpm_simulator.py`: input validation and route selection.
- `routes.example.json`: a small, readable example routing table.
- `tests/`: automated checks of expected behavior.
- `.github/workflows/python-tests.yml`: continuous integration for the tests and CLI smoke checks.
- `docs/`: concepts, implementation notes, security relevance, lab steps, use cases, and troubleshooting.
- Original PDF and editable project reports.

## Intended audience

Students learning computer networks, information security learners exploring packet paths, instructors demonstrating CIDR, and developers who need a compact example of prefix matching.

## Success criteria

A learner should be able to run a destination lookup, explain why the chosen prefix wins, alter a route table, rerun the lookup, and document the difference. The tests should pass without third-party Python packages.

## Non-goals

This project is not a production router, a routing protocol daemon, a packet generator, a vulnerability scanner, or a substitute for an actual router/simulator lab. It does not claim that traffic was captured unless a capture and its context are supplied.
