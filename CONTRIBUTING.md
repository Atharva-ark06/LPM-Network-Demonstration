# Contributing

Thanks for helping improve the LPM Network Demonstration.

## Before opening a change

1. Keep examples appropriate for an isolated lab you are authorized to use.
2. Keep simulator behavior and documentation aligned.
3. Do not claim that a router experiment or packet capture was performed unless you include the actual evidence.
4. Prefer focused changes with clear commit messages.
5. Treat this project as an educational simulator, not a production routing engine or security scanner.
6. Check the [validation requirements](docs/validation-requirements.md) before submitting changes.

## Run checks locally

Python 3.10 or newer is recommended.

```bash
python -m unittest discover -s tests -v
python lpm_simulator.py --help
python lpm_simulator.py 10.0.1.200
```

On Windows, use `py` if that is the configured Python launcher. The GitHub Actions workflow runs the unit tests and CLI smoke checks on pushes and pull requests targeting `master`.

## Review expectations

- Add a focused regression test for each new selection rule or input-validation behavior.
- For route-file changes, verify malformed JSON, unsupported fields, field types, and boundary cases as applicable.
- For documentation changes, verify commands and internal links against the current files.
- Explain whether output is simulated or collected from a real, authorized lab.
- Avoid publishing credentials, secrets, internal hostnames, or sensitive network details in examples and evidence.
- Do not describe a passing test suite as a security certification or proof that a real network is secure.
- Update the route-file format or security limitations documentation when behavior or claims change.

## Suggested additions

- Add edge-case tests for prefix boundaries, empty tables, and duplicate routes.
- Expand CI to test the supported Python-version range.
- Keep the simulator's limitations explicit; it is a teaching aid, not a production routing engine.
