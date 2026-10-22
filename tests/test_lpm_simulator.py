import json
import tempfile
import unittest
from pathlib import Path

from lpm_simulator import RouteFileError, load_routes, select_route


def route(network, metric=0, next_hop="192.0.2.1"):
    import ipaddress
    return {
        "network": ipaddress.ip_network(network),
        "metric": metric,
        "next_hop": next_hop,
        "interface": "test0",
    }


class LongestPrefixMatchTests(unittest.TestCase):
    def setUp(self):
        self.routes = [
            route("10.0.0.0/12", 1, "broad"),
            route("10.0.0.0/16", 1, "medium"),
            route("10.0.1.0/24", 50, "specific"),
            route("10.0.1.128/25", 100, "most-specific"),
            route("0.0.0.0/0", 999, "default"),
        ]

    def test_longest_prefix_beats_lower_metric(self):
        chosen = select_route("10.0.1.200", self.routes)
        self.assertEqual(str(chosen["network"]), "10.0.1.128/25")
        self.assertEqual(chosen["next_hop"], "most-specific")

    def test_less_specific_route_when_destination_outside_more_specific(self):
        chosen = select_route("10.0.1.20", self.routes)
        self.assertEqual(str(chosen["network"]), "10.0.1.0/24")

    def test_default_route_is_used_when_no_specific_route_matches(self):
        chosen = select_route("203.0.113.9", self.routes)
        self.assertEqual(str(chosen["network"]), "0.0.0.0/0")

    def test_no_route_returns_none_without_default(self):
        self.assertIsNone(select_route("203.0.113.9", self.routes[:-1]))

    def test_lower_metric_breaks_equal_prefix_tie(self):
        candidates = [route("192.0.2.0/24", 30, "slower"),
                      route("192.0.2.0/24", 5, "faster")]
        self.assertEqual(select_route("192.0.2.7", candidates)["next_hop"], "faster")

    def test_invalid_destination_is_rejected(self):
        with self.assertRaises(ValueError):
            select_route("not-an-ip", self.routes)

    def test_ipv6_destination_is_rejected(self):
        with self.assertRaises(ValueError):
            select_route("2001:db8::1", self.routes)

    def test_route_loader_normalizes_host_bits(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "routes.json"
            path.write_text(json.dumps([{"network": "10.0.1.99/24"}]), encoding="utf-8")
            loaded = load_routes(path)
            self.assertEqual(str(loaded[0]["network"]), "10.0.1.0/24")

    def test_route_loader_rejects_ipv6_network(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "routes.json"
            path.write_text(json.dumps([{"network": "2001:db8::/32"}]), encoding="utf-8")
            with self.assertRaises(RouteFileError):
                load_routes(path)

    def test_route_loader_rejects_negative_metric(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "routes.json"
            path.write_text(json.dumps([{"network": "10.0.0.0/8", "metric": -1}]), encoding="utf-8")
            with self.assertRaises(RouteFileError):
                load_routes(path)


if __name__ == "__main__":
    unittest.main()
