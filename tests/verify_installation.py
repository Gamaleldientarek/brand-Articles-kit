"""Assert installer copies full content and creates the requested agent layout."""
import argparse
from pathlib import Path


def verify(source, project, mode):
    expected = {p.relative_to(source): p.read_bytes() for p in source.rglob('*')
                if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
    if not expected:
        raise ValueError('No source skill files found')
    for name, relative in [('Codex', '.agents/skills/brand-content'),
                           ('Claude Code', '.claude/skills/brand-content')]:
        installed = project / relative
        if not installed.is_dir():
            raise AssertionError(f'{name}: missing installation directory')
        for path, content in expected.items():
            if (installed / path).read_bytes() != content:
                raise AssertionError(f'{name}: content differs for {path}')
        actual = {p.relative_to(installed) for p in installed.rglob('*')
                  if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
        if actual != set(expected):
            raise AssertionError(f'{name}: unexpected or missing installed files')
        if name == 'Claude Code' and installed.is_symlink() != (mode == 'symlink'):
            raise AssertionError('Claude Code installation mode mismatch')
        print(f'{name}: verified {len(expected)} files ({mode})')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('project', type=Path)
    parser.add_argument('--mode', choices=['copy', 'symlink'], required=True)
    args = parser.parse_args()
    verify(args.source, args.project, args.mode)
