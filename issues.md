# Lab 5: identified issues and fixes

Program: `bike_share_stations.py` in `SETAPESU26/L5_23_bike_share_stations`.
Line numbers in the Line(s) column refer to the unchanged starter, not the cleaned file. Medium security severity is listed first; Bandit reported no high-severity findings.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| B608: SQL built from user data | Security, medium | 9 | Concatenating the station name and counts into SQL makes the statement unsafe and breaks names containing apostrophes. | Bind all three values with SQLite `?` placeholders in `add_station`. |
| B311: insecure PIN randomness | Security, low | 1, 22 | `random.randint` is unsuitable for an unlock credential. | Use `1000 + secrets.randbelow(9000)` to retain the four-digit range. |
| B110 / W0718: ignored broad exception | Security/reliability, low | 32-35 | Catching every exception and doing nothing hides database failures. | Remove the unnecessary catch so failures reach the caller. |
| W0102: mutable default argument | Bug | 8 | A default list is shared between calls, mixing unrelated station logs. | Default to `None`, then create a new list inside each call. A supplied list is still supported. |
| R1710: inconsistent return paths | API/logic | 14-18 | A successful rental returns `True`; failure implicitly returns `None`. | Use a conditional SQL update and return whether exactly one station was updated. Failure is explicitly `False`. |
| Unchecked missing row | Runtime bug, found by inspection | 39-42 | `fetchone()` returns `None` for an unknown station, so `row[0]` raises an exception. | Short-circuit checks for a missing row and a NULL count before comparing the count. |
| W0612 / F841: unused variable | Maintainability | 27 | `summary` is calculated and never used. | Remove it; return the station-name list directly. |
| C0121 / E711: equality with None | Style/correctness | 40 | `== None` is not the intended identity check. | Use `is not None` in the guarded predicate. |
| C0103: non-standard function names | Naming | 8, 14, 21, 25, 31, 38 | Camel-case function names do not follow Python's snake_case convention. | Rename functions and update every call in the demonstration. |
| C0114 / C0116: missing documentation | Maintainability | 1, 8-45 | The module and functions do not describe their purpose or return behavior. | Add a module docstring and focused function docstrings. |
| C0301 / E501: long lines | Formatting | 5, 9, 15, 17, 26, 33, 39 | Several statements exceed the tools' default line-length limits. | Split SQL strings and argument lists across lines, keeping the final program within 79 characters. |
| C0303 / W291: trailing whitespace | Formatting | 27 | Trailing spaces make the file inconsistent. | Remove trailing spaces. |
| Unconditional demonstration | Import side effect, found by inspection | 53 | Importing the module executes the demonstration and mutates station data. | Guard the demonstration with `if __name__ == "__main__"` and close its connection afterward. |
| Missing input bounds | Data integrity, found by inspection | 8-11 | Negative counts or more bikes than capacity can create impossible station states. | Validate the name and integer counts, rejecting booleans and requiring `0 <= bikes <= capacity`. |

## Verification

Actual tool runs against the assigned program, using default rules with no disabled checks:

| Check | Before | After |
|-------|--------|-------|
| Pylint 4.1.3 | 3.89/10; 22 messages | 10.00/10; no messages |
| Bandit 1.9.4 | 3 findings: 1 medium, 2 low | 0 findings; 0 skipped checks/lines |
| Flake8 7.4.1 | 10 findings | 0 findings |

Raw reports are in `reports/before/` and `reports/after/`. The final Flake8 report is intentionally empty: Flake8 prints nothing on a clean run. Exit statuses are recorded in `reports/verification.json`.

Additional regression tests cover quoted names/SQL-looking input, independent default logs, explicit log reuse, rental exhaustion, unknown stations, full stations, reset behavior, NULL bike counts, input validation, PIN boundaries/range and propagation of database failures. These are runtime checks in addition to static analysis; neither passing tests nor a clean scan proves the program is secure in every setting.

The cleaned program is still a small in-memory demonstration, not a production unlock service. Four-digit PINs have a small search space; real systems also need attempt limits, expiry, authenticated access and secure storage.
