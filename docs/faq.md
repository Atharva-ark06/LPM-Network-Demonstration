# Frequently asked questions

## Does this project route real packets?

No. `lpm_simulator.py` models the selection of a route from a JSON file. It does not create interfaces, install routes, or forward traffic.

## Is it a cybersecurity scanner?

No. It is a networking education tool. Security relevance comes from understanding how route selection can affect segmentation, inspection paths, and troubleshooting.

## Why does a /25 win over a /24?

A /25 has a longer prefix and therefore identifies a narrower address range. If both prefixes contain the destination, the /25 is the most specific match.

## Does a lower metric always win?

Not in this model. Prefix length is compared first. The metric is only used when matching routes have the same prefix length. Actual routing devices may apply other rules before installing routes in the forwarding table.

## What if there is no matching route?

The simulator returns no route. If a default route is present and valid in the input table, it matches any IPv4 destination that has no more-specific match.

## Does the program support IPv6?

No. The current version explicitly supports IPv4 only and rejects IPv6 destinations and networks.

## Why use JSON?

It is readable, easy to edit, and simple to keep under version control. The route schema is documented in [route-file-format.md](route-file-format.md).

## Do I need Wireshark to use the simulator?

No. Wireshark is only relevant to the optional packet-observation lab.

## Why might a router's result differ?

The router may have a different route table or use route installation, administrative distance, routing-protocol attributes, policy, ECMP, or vendor-specific behavior that the simulator does not model.

## Can I use the example IOS commands in production?

No. They are illustrative examples for an isolated, authorized lab. Replace the addresses and interface assumptions with values appropriate to a controlled topology, and follow change-management procedures.

## How do I contribute?

Read [CONTRIBUTING.md](../CONTRIBUTING.md), add tests for behavior changes, run the test suite, and submit a focused pull request.
