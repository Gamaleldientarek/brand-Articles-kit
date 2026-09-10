import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "skills/brand-content/scripts"


def module(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


copy = module("review_copy")
keywords = module("keyword_inventory")


class CopyTests(unittest.TestCase):
    def test_excludes_non_body_material(self):
        text = "# Heading\nBy Writer\nUseful Arabic العربية text.\n[Source](https://example.org)\n```js\nlet a = 1;\n```\n"
        self.assertEqual(copy.review(text)["estimated_body_words"], 4)

    def test_flags_broken_arabic_without_rewriting(self):
        text = "هذه \ufefb تجربة"
        result = copy.review(text)
        self.assertEqual(result["issues"][0]["kind"], "presentation_forms")
        self.assertIn("\ufefb", text)

    def test_user_english_terms_are_not_language_errors(self):
        self.assertEqual(copy.review("نراجع Prototype باستخدام Figma.")["issues"], [])

    def test_limits_are_opt_in(self):
        self.assertEqual(copy.review("Short copy")["issues"], [])
        self.assertEqual(copy.review("Short copy", minimum=3)["issues"][0]["kind"], "below_requested_length")


class InventoryTests(unittest.TestCase):
    def test_retains_unknown_and_zero(self):
        rows = [["Keyword", "Volume", "KD"], ["UX", 0, None]]
        result = keywords.records(rows)[0]
        self.assertEqual(result["fields"]["Volume"], 0)
        self.assertIsNone(result["fields"]["KD"])
        self.assertEqual(result["row"], 2)

    def test_multilingual_matching_and_row_provenance(self):
        rows = [["Keyword"], ["Other"], ["تجربة المستخدم"], ["Design SYSTEM"]]
        result = keywords.records(rows, ["تجربة", "system"])
        self.assertEqual([r["row"] for r in result], [3, 4])

    def test_duplicate_headers_do_not_drop_values(self):
        result = keywords.records([["Volume", "Volume", None], [2, 3, 4]])
        self.assertEqual(list(result[0]["fields"].values()), [2, 3, 4])

    def test_csv_read_does_not_mutate_input(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "inventory.csv"
            path.write_text("Keyword,Volume,KD\nتجربة المستخدم,20,\n", encoding="utf-8")
            before = path.read_bytes()
            result = keywords.read_inventory(path, query=["تجربة"])
            self.assertIsNone(result["matches"][0]["fields"]["KD"])
            self.assertEqual(before, path.read_bytes())

    def test_xlsx_read_preserves_blanks(self):
        try:
            import openpyxl
        except ImportError:
            self.skipTest("openpyxl is optional")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "inventory.xlsx"
            workbook = openpyxl.Workbook()
            workbook.active.title = "Inventory"
            workbook.active.append(["Keyword", "Volume", "KD"])
            workbook.active.append(["UX", 0, None])
            workbook.save(path)
            workbook.close()
            before = path.read_bytes()
            result = keywords.read_inventory(path, sheet="Inventory", query=["ux"])
            self.assertIsNone(result["matches"][0]["fields"]["KD"])
            self.assertEqual(before, path.read_bytes())


if __name__ == "__main__":
    unittest.main()
