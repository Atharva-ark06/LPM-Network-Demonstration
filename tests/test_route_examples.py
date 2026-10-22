import unittest
from pathlib import Path

from lpm_simulator import load_routes, select_route


ROOT = Path(__file__).resolve().parents[1]

# Each tuple is (destination, expected network or None, expected next hop or None).
SCENARIO_EXPECTATIONS = {
    "host-route-priority.json": ("192.0.2.10", "192.0.2.10/32", "192.0.2.10"),
    "default-only.json": ("203.0.113.25", "0.0.0.0/0", "192.0.2.1"),
    "overlapping-private-ranges.json": ("172.16.20.10", "172.16.20.0/24", "192.0.2.3"),
    "branch-office-summary.json": ("10.44.20.8", "10.44.20.0/24", "192.0.2.2"),
    "dmz-specific-route.json": ("192.0.2.80", "192.0.2.64/26", "198.51.100.2"),
    "vpn-more-specific-route.json": ("10.8.4.15", "10.8.4.0/24", "192.0.2.3"),
    "management-network.json": ("10.99.0.12", "10.99.0.0/24", "192.0.2.2"),
    "guest-vlan-routing.json": ("10.30.4.5", "10.30.4.0/24", "192.0.2.4"),
    "equal-prefix-first-entry.json": ("198.51.100.15", "198.51.100.0/24", "192.0.2.11"),
    "prefix-boundary-lower.json": ("10.20.0.0", "10.20.0.0/25", "192.0.2.2"),
    "prefix-boundary-upper.json": ("10.20.0.255", "10.20.0.128/25", "192.0.2.3"),
    "multi-level-prefixes.json": ("10.1.2.3", "10.1.2.3/32", "192.0.2.4"),
    "zero-metric.json": ("192.0.2.5", "192.0.2.0/24", "192.0.2.10"),
    "maximum-host-prefix.json": ("203.0.113.255", "203.0.113.255/32", "192.0.2.2"),
    "no-matching-route.json": ("203.0.113.9", None, None),
    "specific-route-beats-default.json": ("198.51.100.5", "198.51.100.0/24", "192.0.2.1"),
    "overlapping-172-range.json": ("172.20.1.1", "172.20.1.0/24", "192.0.2.3"),
    "summary-vs-subnet.json": ("10.60.12.34", "10.60.12.32/27", "192.0.2.3"),
    "disjoint-routes.json": ("192.0.2.10", "192.0.2.0/24", "192.0.2.1"),
}


class ExampleRouteTableTests(unittest.TestCase):
    def test_no_default_route_example_returns_no_route(self):
        routes = load_routes(ROOT / "examples" / "no-default-route.json")
        self.assertIsNone(select_route("203.0.113.8", routes))
        self.assertEqual(str(select_route("10.0.3.4", routes)["network"]), "10.0.0.0/16")

    def test_equal_prefix_example_uses_lower_metric(self):
        routes = load_routes(ROOT / "examples" / "equal-prefix-metrics.json")
        selected = select_route("198.51.100.7", routes)
        self.assertEqual(selected["next_hop"], "192.0.2.12")
        self.assertEqual(selected["metric"], 5)

    def test_campus_example_prefers_specific_segment(self):
        routes = load_routes(ROOT / "examples" / "campus-segmentation.json")
        selected = select_route("10.20.20.45", routes)
        self.assertEqual(str(selected["network"]), "10.20.20.0/24")
        self.assertEqual(selected["interface"], "SERVER-SEGMENT")

    def test_campus_example_uses_summary_for_other_campus_address(self):
        routes = load_routes(ROOT / "examples" / "campus-segmentation.json")
        selected = select_route("10.20.99.5", routes)
        self.assertEqual(str(selected["network"]), "10.20.0.0/16")

    def test_all_example_route_files_are_valid(self):
        paths = [ROOT / "routes.example.json", *sorted((ROOT / "examples").glob("*.json"))]
        self.assertGreaterEqual(len(paths), 20)
        for path in paths:
            with self.subTest(route_file=path.name):
                self.assertTrue(load_routes(path))

    def test_expanded_scenarios_match_documented_expectations(self):
        for filename, (destination, expected_network, expected_next_hop) in SCENARIO_EXPECTATIONS.items():
            with self.subTest(route_file=filename, destination=destination):
                routes = load_routes(ROOT / "examples" / filename)
                selected = select_route(destination, routes)
                if expected_network is None:
                    self.assertIsNone(selected)
                else:
                    self.assertIsNotNone(selected)
                    self.assertEqual(str(selected["network"]), expected_network)
                    self.assertEqual(selected["next_hop"], expected_next_hop)

    def test_each_expanded_scenario_has_a_lab_guide(self):
        for filename in SCENARIO_EXPECTATIONS:
            with self.subTest(route_file=filename):
                lab_path = ROOT / "docs" / "labs" / (filename.removesuffix(".json") + ".md")
                self.assertTrue(lab_path.exists(), f"Missing lab guide for {filename}")


if __name__ == "__main__":
    unittest.main()
