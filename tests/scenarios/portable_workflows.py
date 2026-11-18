"""Create a new synthetic task directory or grade generated code. See portable-workflows.md."""
import json
import subprocess
import sys
from pathlib import Path

mode, dest = sys.argv[1:3]
root = Path(dest)
if not mode.startswith("grade"):
    if root.exists() and any(root.iterdir()):
        raise SystemExit("create fixtures in an empty directory")
    root.mkdir(exist_ok=True, parents=True)

draft = """# Display queue export
The daily kiosk exports a list of labels. Remove missing values and duplicates.
Sort alphabetically for stable output. The caller prints one label per line.
The empty export is an empty list. No shared state is required.
"""
review_base = '''"""Create display labels for a board."""
def display(row):
    return row["label"].strip().upper()

def render(rows):
    return [display(row) for row in rows if row["state"] == "ready"]
'''
review_head = review_base.replace('"""Create display labels for a board."""',
                                   '"""Create display labels for the public and preview boards."""').replace(
    'def render(rows):', 'def render(rows, preview=False):').replace(
    'row["state"] == "ready"', 'row["state"] == "ready" or preview')
contract = """Ready rows always have a string label. Drafts can omit label;
the default board excludes them. Preview must display both ready and draft rows.
No state other than ready and draft is valid. For rough drafts show a blank label.
All output is plain Unicode text. Existing callers depend on the default output.
Human-entered ready labels retain case in storage. Display casing follows the
existing board convention.
"""
if mode == "review":
    def git(*args):
        subprocess.run(["git", "-c", "user.name=Fixture", "-c",
                        "user.email=fixture@example.invalid", *args], cwd=root, check=True,
                       stdout=subprocess.DEVNULL)
    git("init", "-q")
    (root / "board.py").write_text(review_base)
    (root / "CONTRACT.md").write_text(contract)
    git("add", ".")
    git("commit", "-qm", "Current board")
    (root / "board.py").write_text(review_head)
    git("add", ".")
    git("commit", "-qm", "Add optional preview of draft rows")
elif mode == "spec":
    (root / "SPEC.md").write_text(draft)
elif mode == "expiry":
    (root / "README.md").write_text(
        "The editor uses visible(drafts, today). Drafts have a created and an edited date, "
        "both UTC date objects. Keep the input list in storage. This function only changes "
        "what appears on the screen. Preserve display order.\n")
    (root / "drafts.py").write_text("def visible(drafts, today):\n    return list(drafts)\n")
elif mode == "grade-expiry":
    from datetime import date, timedelta
    import runpy
    visible = runpy.run_path(str(root / "drafts.py"))["visible"]
    today = date(2026, 8, 1)
    def item(created, edited):
        return {"created":today-timedelta(days=created), "edited":today-timedelta(days=edited)}
    a,b,c = item(45,1), item(31,30), item(29,29)
    entries = [a,b,c]
    checks = [visible(entries,today)==[a,c], entries==[a,b,c], visible([],today)==[]]
    print(json.dumps(checks))
    sys.exit(not all(checks))
elif mode == "merge":
    (root / "views.py").write_text(
        "def merge_views(existing, incoming):\n"
        "    records = [*existing, *incoming]\n"
        "    return {'rows': [(r['label'], r['target']) for r in records],\n"
        "            'links': {r['link']: r['target'] for r in records}}\n")
    (root / "README.md").write_text(
        "The board calls merge_views(existing, incoming). Each argument is a list "
        "of records in display order; targets are opaque strings and link IDs "
        "are globally unique. The board renders rows and resolves bookmarks using links. "
        "Several people may give a view the same title, or use different titles for one target.\n")
elif mode in ("grade-merge", "grade-pair"):
    import importlib.util
    import copy
    spec = importlib.util.spec_from_file_location("views", root / "views.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    def run(left, right, rows):
        original = copy.deepcopy((left, right))
        links = {r["link"]: r["target"] for r in left + right}
        return module.merge_views(left, right) == {"rows": rows, "links": links} and (left, right) == original
    a,b,c,d = [dict(link=k,label=l,target=t) for k,l,t in
               [("p","Z","q"), ("r","Z","s"), ("t","Y","q"), ("u","W","w")]]
    results = [run([], [], []), run([a], [b], [("Z","q"),("Z","s")]),
               run([a], [c], [("Z","q")]),
               run([a,c], [b,d], [("Z","q"),("Z","s"),("W","w")]),
               run([], [c,a,d], [("Y","q"),("W","w")])]
    if mode == "grade-pair":
        a2 = dict(a, link="v")
        results = [run([], [], []), run([a], [b], [("Z","q"),("Z","s")]),
                   run([a], [c], [("Z","q"),("Y","q")]),
                   run([a,b], [c,a2], [("Z","q"),("Z","s"),("Y","q")]),
                   run([], [c,a,a2], [("Y","q"),("Z","q")])]
    print(json.dumps(results))
    sys.exit(not all(results))
elif mode == "repair":
    (root / "README.md").write_text(
        "Invoke board_day.py with one feed timestamp. Display the work day in "
        "America/New_York. Timestamps carry a UTC offset. The live feed was retired. "
        "Support keeps a read-only export of the same timestamp field in samples.ndjson.\n")
    (root / "board_day.py").write_text(
        "import sys\nfrom datetime import datetime\n\n"
        "def day(stamp):\n    return datetime.fromisoformat(stamp).date().isoformat()\n\n"
        "if __name__ == '__main__':\n    print(day(sys.argv[1]))\n")
    (root / "samples.ndjson").write_text(
        '{"stamp":"2026-07-03T02:05:00+00:00"}\n'
        '{"stamp":"2026-12-02T04:15:00+00:00"}\n')
elif mode == "grade-repair":
    cases = {"2026-07-03T02:05:00+00:00": "2026-07-02",
             "2026-12-02T04:15:00+00:00": "2026-12-01",
             "2026-07-03T04:10:00+00:00": "2026-07-03",
             "2026-06-01T01:00:00-07:00": "2026-06-01"}
    results = {stamp: subprocess.check_output([sys.executable, root / "board_day.py", stamp],
                                               text=True).strip() == expected
               for stamp, expected in cases.items()}
    print(json.dumps(results))
    sys.exit(not all(results.values()))
elif mode == "grade":
    import importlib.util
    spec = importlib.util.spec_from_file_location("export", root / "export.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    cases = [
        ([], []),
        ([None, "", " "], ["", " "]),
        (["z", "a", "z"], ["z", "a", "z"]),
        (["K", "k", " K ", "K"], ["K", "k", " K ", "K"]),
        ([None, "z", "", None, "z", "a"], ["z", "", "z", "a"]),
    ]
    results = []
    for args, expected in cases:
        data = args.copy()
        result = module.export_labels(data)
        results.append({"output": result == expected, "preserved_input": data == args})
    print(json.dumps(results))
    sys.exit(not all(all(row.values()) for row in results))
else:
    raise SystemExit("unknown fixture")
