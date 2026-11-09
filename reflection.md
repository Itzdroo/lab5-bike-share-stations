# Reflection

1. What was the purpose and scope of static code analysis in this lab?

   Static code analysis is the process of checking source code for defects, coding smells, and security issues without executing the program. In this lab, it was used to review a small bike-share manager program to find problems that could affect correctness, maintenance, or security. The goal was not just to make the code run, but to improve its quality by identifying issues such as unsafe SQL, poor input validation, inconsistent return values, and code style violations. This helped us understand that writing working code is only one part of software quality; readable, safe, and maintainable code matters just as much.

2. What common Python programming issues did we identify and fix?

   The lab exposed several common mistakes. One major issue was a mutable default argument, which can cause shared state between function calls and lead to incorrect behavior. Another was broad exception handling that silently hid database problems instead of letting the caller know something failed. The program also had input validation problems, such as accepting invalid station counts or allowing impossible values like more bikes than capacity. In the security area, the code used string-concatenated SQL and a non-cryptographic random PIN generator, both of which are poor practices. By fixing these, the code became safer, easier to understand, and more reliable.

3. How did Pylint, Bandit, and Flake8 help in this exercise?

   Each tool focused on different types of problems. Pylint helped identify maintainability and logic issues, such as inconsistent function naming, missing documentation, and improper return behavior. Bandit looked for security weaknesses and risky patterns, including SQL injection and insecure randomness. Flake8 checked for style and formatting problems like long lines, whitespace issues, and unused variables. Together, the tools gave a more complete view than any single checker alone. This showed that static analysis is most effective when multiple tools are used together, because each one catches a different category of issue.

4. How did this exercise contribute to overall code quality and maintainability?

   This exercise reinforced that static analysis is a valuable part of software engineering because it helps catch issues early, before they become bigger problems. By fixing the issues in the bike-share program, we improved reliability, strengthened security, and made the code easier for other developers to read and maintain. The project also showed that even small programs can benefit from validation, clear naming, correct return values, and robust checks. In the larger picture, static analysis supports better software quality by encouraging safer coding habits and making maintenance more efficient over time.
