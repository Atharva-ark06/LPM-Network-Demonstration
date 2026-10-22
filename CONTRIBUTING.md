# Contributing

Thanks for helping improve the LPM Network Demonstration.

## Before opening a change

1. Keep examples appropriate for an isolated lab you are authorized to use.
2. Keep simulator behavior and documentation aligned.
3. Do not claim that a router experiment or packet capture was performed unless you include the actual evidence.
4. Prefer focused changes with clear commit messages.

## Run checks locally

Python 3.10 or newer is recommended.

```bash
python -m unittest discover -s tests -v
python lpm_simulator.py --help
python lpm_simulator.py 10.0.1.200
```

The GitHub Actions workflow runs the unit tests and a couple of CLI smoke checks on pushes and pull requests targeting `master`.

## Suggested additions

- Add a focused unit test for each new selection rule or validation behavior.
- For documentation changes, verify commands and links against the current files.
- Keep the simulator's limitations explicit; it is a teaching aid, not a production routing engine.
