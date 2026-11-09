# SE Lab 5: prepared work package

Assigned student: Dhruv Rajagopalan, PES1UG24AM086, Section B, serial 23.
Assigned repository: https://github.com/SETAPESU26/L5_23_bike_share_stations
Starter revision: bcbe73582037325d899b64582217bb31f746fdde.
Prepared on 9 November 2026 using Python 3.10.12 on Linux.

## Read this before submission

The code, issue table and actual before/after tool reports are prepared. Final checks: Pylint 10.00/10, Bandit zero findings, Flake8 zero findings, and 13 regression tests passed.

**The reflection requirement is still unresolved.** The handout and repository refer to four reflection questions but do not include them. `reflection.md` is a factual draft, not verified answers to those missing questions. Get the actual prompts and match the draft to them. Do not treat this as a fully complete submission until that is done.

This package was prepared with AI assistance at the student's request. Tool reports and local Git commits are genuine preparation records. They are not evidence that the student personally performed these steps. Review the code and follow any course rules on assistance/disclosure. The supplied handout and README do not state an AI-assistance policy, which is not proof that no course policy exists.

No files were submitted to Classroom. No remote GitHub repository was changed or pushed to. The local history has exactly three new commits, grouped by Bandit, Pylint and Flake8 fixes, attributed to `Assignment preparation assistant`, not to Dhruv. `history/commits.txt`, `history/patches/` and `history/lab5.bundle` preserve that history. Any required remote commit/submission step remains for the student to perform in the correct course workflow.

## Main files

- `bike_share_stations.py`: cleaned program.
- `issues.md`: 14 documented issues, including all tool findings and extra inspected bugs.
- `reflection.md`: factual draft, with the missing-question caveat.
- `reports/before/`: actual starter Pylint, Bandit, Flake8 and demonstration output.
- `reports/after/`: actual cleaned-program reports, demonstration output and test results.
- `reports/verification.json`: final commands and exit statuses.
- `reports/bandit_stage_report.txt` and `reports/pylint_stage_report.txt`: intermediate verification.
- `test_bike_share_stations.py`: 13 runtime regression tests.
- `sources/`: unchanged starter and README.
- `requirements-lock.txt`: installed Python package versions for reproduction.

The final Flake8 report is an empty file because a clean run produces no text. Program-output PINs vary between runs because they use secure randomness. The final demonstration prints two lines: `True True`, then a four-digit PIN, `['Central Park']`, and `True`.

## Run locally

From this extracted folder on a laptop with Python 3:

```sh
python3 -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows PowerShell instead:
# .\venv\Scripts\Activate.ps1
python -m pip install -r requirements-lock.txt
python bike_share_stations.py
python -m unittest -v test_bike_share_stations
python -m pylint bike_share_stations.py
python -m bandit -r bike_share_stations.py
python -m flake8 bike_share_stations.py
```

The tool commands deliberately target the assignment file, not the unchanged starter copy in `sources/`. Default rules are used; no checks were disabled. The Python script itself needs only the standard library.

## API changes

Functions now use snake_case: `add_station`, `rent_bike`, `unlock_pin`, `full_stations`, `reset_station`, `has_bikes`. Their demonstration call sites have been updated. A failed rental now returns `False` instead of implicit `None`; the demo checks for that. Station validation rejects empty names, non-integer/Boolean counts, negative counts and bikes above capacity. SQLite errors are no longer silently swallowed. The database is still in-memory: data does not survive program exit.

A clean static scan is not a production-security guarantee. Four-digit PINs would need attempt limits and expiry in a real system. The README warns that the starter may create an output file, but this particular assigned starter did not create one in the observed run.

## Inspect the local Git history

If Git is installed, clone the self-contained bundle into a new folder:

```sh
git clone history/lab5.bundle lab5-history
cd lab5-history
git log -3 --oneline
git show HEAD
```

This restores the genuine local commits for inspection. It does not submit or publish anything. It does not reproduce the student's own work history. This extracted package includes the bundle and patch exports as delivery extras; those generated history exports are not themselves tracked inside the bundle.
