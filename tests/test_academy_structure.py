from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def test_all_lessons_have_two_resources():
    lessons = sorted((ROOT/'lessons').glob('[0-9][0-9]-*'))
    assert len(lessons) == 20
    for p in lessons:
        t=(p/'LESSON.md').read_text()
        assert '## Go Deeper — two resources' in t
        segment=t.split('## Go Deeper — two resources',1)[1].split('## Next lesson',1)[0]
        assert segment.count('https://')==2
        assert '## Independent assignment' in t

def test_codespaces_config():
    import json
    conf=json.loads((ROOT/'.devcontainer/devcontainer.json').read_text())
    assert conf['image'].startswith('mcr.microsoft.com/devcontainers/python:')
