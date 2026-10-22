# LPM lab report template

Copy this document into your own report and fill in the results you actually observe.

## 1. Aim

Describe the route-selection question you are investigating.

## 2. Environment

- Operating system:
- Python version:
- Simulator version / Git commit:
- Optional router or network simulator:
- Optional capture tool/version:
- Topology description:

## 3. Method

List the commands and route table used. If testing a real router, explain how it is isolated and authorized.

## 4. Expected result

| Destination | Expected matching prefix | Reason |
| --- | --- | --- |
| `10.0.1.200` | `10.0.1.128/25` | Most specific matching prefix |
| `10.0.1.20` | `10.0.1.0/24` | Destination is outside the /25 |
| `203.0.113.9` | `0.0.0.0/0` | Default route matches |

## 5. Observed result

Paste the actual simulator output and, if applicable, sanitized router output. Do not replace observations with expected results.

## 6. Analysis

Explain which routes matched, why the selected prefix won, and whether the observation differed from the expectation.

## 7. Security relevance

Discuss any implications for segmentation, firewall/monitoring placement, next-hop reachability, or return paths. Avoid claiming a security finding without supporting evidence.

## 8. Limitations

State which steps were not performed, which assumptions were made, and what the simulator does not model.

## 9. Conclusion

Summarize what the collected evidence supports and one question for further study.
