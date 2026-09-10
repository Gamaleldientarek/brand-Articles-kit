import json
from pathlib import Path
import re
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/brand-content'


class PackageTests(unittest.TestCase):
    def test_portable_frontmatter(self):
        text = (SKILL / 'SKILL.md').read_text()
        self.assertTrue(text.startswith('---\n'))
        front = yaml.safe_load(text.split('---', 2)[1])
        self.assertEqual(front['name'], SKILL.name)
        self.assertRegex(front['name'], r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
        self.assertLessEqual(len(front['name']), 64)
        self.assertTrue(0 < len(front['description']) <= 1024)
        self.assertLessEqual(set(front), {'name', 'description', 'license', 'metadata', 'allowed-tools', 'compatibility'})
        self.assertRegex(front['metadata']['version'], r'^\d+\.\d+\.\d+$')

    def test_internal_links_resolve_and_stay_in_package(self):
        for path in [ROOT / 'README.md', *SKILL.rglob('*.md')]:
            for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' in link or link.startswith('#'):
                    continue
                target = (path.parent / link.split('#')[0]).resolve()
                with self.subTest(path=path, link=link):
                    self.assertTrue(target.is_relative_to(ROOT.resolve()))
                    self.assertTrue(target.is_file())

    def test_runtime_metadata_invokes_correct_skill(self):
        ui = yaml.safe_load((SKILL / 'agents/openai.yaml').read_text())['interface']
        self.assertIn('$brand-content', ui['default_prompt'])
        self.assertTrue(25 <= len(ui['short_description']) <= 64)

    def test_source_provenance_is_explicit(self):
        data = json.loads((SKILL / 'references/brand-sources.json').read_text())
        self.assertTrue(data['sources'])
        for source in data['sources']:
            self.assertTrue(source['repository'].startswith('https://github.com/'))
            self.assertFalse(Path(source['path']).is_absolute())
            self.assertRegex(source['sha256'], r'^[a-f0-9]{64}$')

    def test_no_client_state_or_machine_paths_in_distributed_skill(self):
        patterns = [r'/Users/', r'/var/folders/', r'app\.clickup\.com/t/',
                    r'docs\.google\.com/document/d/', r'BEGIN (?:OPENSSH |RSA )?PRIVATE KEY',
                    r'gh[pousr]_[A-Za-z0-9]{20,}', r'github_pat_[A-Za-z0-9_]{20,}']
        for path in SKILL.rglob('*'):
            if not path.is_file() or '__pycache__' in path.parts:
                continue
            with self.subTest(path=path):
                self.assertNotIn(path.suffix.lower(), {'.xlsx', '.csv', '.pdf'})
                text = path.read_text(encoding='utf-8')
                for pattern in patterns:
                    self.assertIsNone(re.search(pattern, text))

    def test_no_unfinished_scaffold_in_skill(self):
        for path in SKILL.rglob('*.md'):
            with self.subTest(path=path):
                self.assertIsNone(re.search(r'\bTODO\b|\bTBD\b|Lorem ipsum', path.read_text()))


if __name__ == '__main__':
    unittest.main()
