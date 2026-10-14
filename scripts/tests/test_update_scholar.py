import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location("update_scholar", Path(__file__).parents[1] / "update_scholar.py")
scholar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scholar)

PROFILE = '''<div id="gsc_prf_in">Yijie Xu</div>
<table id="gsc_rsb_st"><tr><th></th><th>All</th><th>Since 2021</th></tr>
<tr><td><a>Citations</a></td><td>1,234</td><td>900</td></tr>
<tr><td>h-index</td><td>7</td><td>7</td></tr></table>'''


class ScholarUpdateTest(unittest.TestCase):
    def test_all_time_count_not_recent_count_or_h_index(self):
        self.assertEqual(scholar.parse_citations(PROFILE), 1234)

    def test_rejects_verification_missing_or_malformed_data(self):
        for html in ("unusual traffic", "<html>Sign in</html>",
                     PROFILE.replace("Yijie Xu", "Someone Else"),
                     PROFILE.replace("All", "Recent"),
                     PROFILE.replace("1,234", "N/A"),
                     PROFILE.replace("Citations", "Other")):
            with self.subTest(html=html), self.assertRaises(ValueError):
                scholar.parse_citations(html)

    def test_snapshot_and_badge_are_consistent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "_data").mkdir()
            scholar.write_snapshot(root, 213, "2026-10-14")
            badge = json.loads((root / "gs_data.json").read_text())
            self.assertEqual(badge["message"], "213 citations")
            self.assertEqual(badge["schemaVersion"], 1)
            metadata = (root / "_data/scholar.yml").read_text()
            self.assertIn("total_citations: 213", metadata)
            self.assertIn('checked_on: "2026-10-14"', metadata)

    def test_invalid_or_zero_reset_preserves_existing_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "_data").mkdir()
            scholar.write_snapshot(root, 213, "2026-10-14")
            paths = [root / "gs_data.json", root / "_data/scholar.yml"]
            before = [path.read_bytes() for path in paths]
            for count in (0, -1, True, "214"):
                with self.subTest(count=count), self.assertRaises(ValueError):
                    scholar.write_snapshot(root, count, "2026-10-15")
                self.assertEqual([path.read_bytes() for path in paths], before)

    def test_valid_decrease_and_unchanged_count_are_supported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "_data").mkdir()
            scholar.write_snapshot(root, 213, "2026-10-14")
            scholar.write_snapshot(root, 212, "2026-10-15")
            self.assertEqual(json.loads((root / "gs_data.json").read_text())["message"], "212 citations")
            scholar.write_snapshot(root, 212, "2026-10-16")
            self.assertIn("2026-10-16", (root / "_data/scholar.yml").read_text())

    def test_network_failure_never_writes(self):
        with patch.object(scholar, "fetch_citations", side_effect=TimeoutError("timed out")), \
                patch.object(scholar, "write_snapshot") as write:
            with patch("sys.argv", ["update_scholar.py"]):
                self.assertEqual(scholar.main(), 1)
            write.assert_not_called()


if __name__ == "__main__":
    unittest.main()
