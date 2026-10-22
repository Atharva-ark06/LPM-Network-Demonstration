#!/usr/bin/env python3
"""Educational IPv4 Longest Prefix Match (LPM) route-selection simulator."""

from __future__ import annotations

import argparse
import ipaddress
import json
import sys
from pathlib import Path
from typing import Any


class RouteFileError(ValueError):
    """Raised when a route file is invalid."""


def load_routes(path: str | Path) -> list[dict[str, Any]]:
    """Load and validate routes from a JSON file."""
    try:
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
    except OSError as exc:
        raise RouteFileError(f"cannot read route file: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise RouteFileError(f"invalid JSON: {exc}") from exc

    if not isinstance(raw, list):
        raise RouteFileError("route file must contain a JSON array")

    routes: list[dict[str, Any]] = []
    for index, item in enumerate(raw, start=1):
        if not isinstance(item, dict) or "network" not in item:
            raise RouteFileError(f"route #{index} must be an object with a network field")
        try:
            network = ipaddress.ip_network(item["network"], strict=False)
        except (ValueError, TypeError) as exc:
            raise RouteFileError(f"route #{index} has an invalid network") from exc
        if not isinstance(network, ipaddress.IPv4Network):
            raise RouteFileError(f"route #{index} must use IPv4")
        metric = item.get("metric", 0)
        if isinstance(metric, bool) or not isinstance(metric, int) or metric < 0:
            raise RouteFileError(f"route #{index} metric must be a non-negative integer")
        routes.append({
            **item,
            "network": network,
            "next_hop": str(item.get("next_hop", "directly-connected")),
            "interface": str(item.get("interface", "unspecified")),
            "metric": metric,
        })
    return routes


def select_route(destination: str, routes: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Return the best matching route: longest prefix, then lowest metric.

    Equal-prefix, equal-metric ties keep the first route in the input list.
    This deterministic tie-break is for the teaching simulator; real routers
    may install multiple equal-cost paths or apply vendor-specific policies.
    """
    try:
        address = ipaddress.ip_address(destination)
    except ValueError as exc:
        raise ValueError(f"invalid destination IP address: {destination}") from exc
    if not isinstance(address, ipaddress.IPv4Address):
        raise ValueError("destination must be an IPv4 address")

    matches = [route for route in routes if address in route["network"]]
    if not matches:
        return None
    return min(matches, key=lambda route: (-route["network"].prefixlen, route["metric"]))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Demonstrate IPv4 Longest Prefix Match using a JSON routing table."
    )
    parser.add_argument("destination", help="destination IPv4 address to look up")
    parser.add_argument(
        "--routes", default="routes.example.json",
        help="path to a JSON route list (default: routes.example.json)",
    )
    args = parser.parse_args()

    try:
        routes = load_routes(args.routes)
        chosen = select_route(args.destination, routes)
    except (RouteFileError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(f"Destination: {args.destination}")
    print(f"Routes loaded: {len(routes)}")
    print("-" * 72)
    print(f"{'NETWORK':<20} {'PREFIX':>6} {'METRIC':>7} {'NEXT HOP':<20} INTERFACE")
    for route in routes:
        network = route["network"]
        marker = "  <-- selected" if route is chosen else ""
        print(
            f"{str(network):<20} {network.prefixlen:>6} "
            f"{route['metric']:>7} {route['next_hop']:<20} "
            f"{route['interface']}{marker}"
        )
    print("-" * 72)
    if chosen is None:
        print("Result: no matching route (packet would have no route in this table).")
        return 1
    print(f"Selected route: {chosen['network']}")
    print(f"Next hop:       {chosen['next_hop']}")
    print(f"Interface:      {chosen['interface']}")
    print(f"Reason:         longest matching prefix /{chosen['network'].prefixlen}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
