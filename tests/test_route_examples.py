import unittest
from pathlib import Path

from lpm_simulator import load_routes, select_route


ROOT = Path(__file__).resolve().parents[1]


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
        self.assertGreaterEqual(len(paths), 4)
        for path in paths:
            with self.subTest(route_file=path.name):
                self.assertTrue(load_routes(path))


if __name__ == "__main__":
    unittest.main()
