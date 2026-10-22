# Setup guide

## Requirements

- Python 3.10 or newer.
- Git, if cloning the repository.
- A terminal: PowerShell, Windows Terminal, Command Prompt, macOS Terminal, or a Linux shell.
- Optional for the extended lab: Wireshark and an authorized router simulator or isolated networking lab.

The Python simulator uses only the standard library. Do not install extra packages just to run it.

## 1. Get the repository

```bash
git clone https://github.com/Atharva-ark06/LPM-Network-Demonstration.git
cd LPM-Network-Demonstration
```

Alternatively, download the repository ZIP from GitHub and extract it.

## 2. Confirm Python

Windows PowerShell:

```powershell
py --version
```

macOS/Linux:

```bash
python3 --version
```

If Python is not found, install a supported Python release from the official Python website and ensure the executable is available in your PATH.

## 3. Run a lookup

Windows:

```powershell
py lpm_simulator.py 10.0.1.200
```

macOS/Linux:

```bash
python3 lpm_simulator.py 10.0.1.200
```

Try the other examples:

```bash
python lpm_simulator.py 10.0.1.20
python lpm_simulator.py 203.0.113.9
```

On systems where the executable is named `python3` or `py`, substitute that command consistently.

## 4. Run automated tests

Windows:

```powershell
py -m unittest discover -s tests -v
```

macOS/Linux:

```bash
python3 -m unittest discover -s tests -v
```

A successful run reports each test as `ok` and ends with `OK`.

## 5. Use a custom route table

Copy `routes.example.json` to another JSON file, edit the routes, then run:

```bash
python lpm_simulator.py 10.0.1.200 --routes my-routes.json
```

Each route needs a valid IPv4 CIDR `network`. Optional fields are described in [route file format](route-file-format.md).

## 6. Troubleshoot setup

- **Python command not found:** try `py` on Windows or `python3` on macOS/Linux.
- **File not found:** run commands from the repository root or provide the full route-file path.
- **Invalid JSON:** check commas, quotes, square brackets, and object braces in the route file.
- **Unexpected route:** verify the destination is inside the expected network and remember that prefix length is considered before metric.
- **Tests cannot import the module:** run unittest from the repository root.

## Optional network lab

The simulator does not need Wireshark or a router. To extend the exercise, use the [lab guide](lab-guide.md) with a router simulator or isolated network you are authorized to configure. Do not apply sample route commands to a production device.
