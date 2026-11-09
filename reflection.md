# Reflection draft: factual points from this analysis

**Status: draft, not verified answers to the required questions.** Both the supplied handout and repository README refer to four reflection questions, but neither actually lists them. This text records the analysis without inventing those questions or claiming that Dhruv personally ran the tools. Match it to the actual questions before treating the reflection requirement as complete.

The most important finding in this program is the SQL constructed by joining strings. It is both a security concern and a functional bug for station names containing an apostrophe. Parameterized SQL separates the statement from its data, addressing both problems without filtering out valid station names.

The three tools cover different kinds of problems. Bandit identified unsafe SQL construction, non-cryptographic randomness for an unlock PIN, and a silently ignored exception. Pylint identified maintainability and logic problems such as the shared default list and inconsistent returns. Flake8 identified formatting problems and the unused variable. Their findings overlap in places, but one tool does not replace the others.

The revised program uses an independent default log, consistent Boolean rental results, secure randomness, and explicit checks for missing stations. The function names and docstrings make the code easier to follow. The supplied before/after reports show Pylint improving from 3.89/10 to 10.00/10, with all three Bandit findings and all ten Flake8 findings removed under the installed tools' default rules.

Static analysis has limits. The missing-row crash in `hasBikes` needed code inspection and a runtime test rather than a reported finding from these runs. The regression tests check expected behavior and edge cases, but a perfect Pylint score and clean Bandit report are not proof of complete correctness or production security. For example, the demonstration's four-digit PIN would still need attempt limits and expiry in a real unlock service.
