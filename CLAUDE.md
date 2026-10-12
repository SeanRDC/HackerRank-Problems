# HackerRank-Problems

Sean's practice repo for HackerRank problems. The goal is for Sean to learn by solving, not to get finished solutions.

## Practice ladder (default way to help with a problem)

When Sean asks for help with a HackerRank problem (or asks to "do the same as PlusMinus"), do not solve it. Instead, write a practice ladder into the problem's file as comments, and let Sean write all of the code.

Reference example: `Problem Solving/Warmup/PlusMinus.py`.

### Rules

- **At most 10 problems.** Scale the count to the difficulty of the target problem: a trivial problem may only need 2-4 steps, a harder one up to 10. Never pad to reach 10.
- **One new idea per problem.** Each step adds exactly one concept on top of the previous ones (e.g. counter -> counter with `if` -> two counters -> ...).
- **The last problem is the real HackerRank problem**, solved in the original function stub.
- **Never write the solution code**, for the ladder problems or the real one. Give hints by naming the idea or tool, not by showing the answer.
- Include a "same shape, different question" step near the end when it fits, so Sean proves the pattern without looking back.

### Format

Place the ladder as comments above the function to complete, keeping the HackerRank boilerplate (imports, `if __name__ == '__main__':` block) intact:

```python
# ===================================================================
# PRACTICE LADDER - N small problems that build up to <problemName>
# ===================================================================
# Solve them in order. Each one adds exactly ONE new idea.
# Write each as its own small function and compare against the
# sample output before moving on.
#
# ---------------------------------------------------------------
# PROBLEM 1 - <short title>
# ---------------------------------------------------------------
# <what to print/return, in one or two lines>
# New idea: <the single concept this step introduces>
#
#   Input:  <sample>
#   Output: <expected>
#
#   Input:  <second sample, ideally an edge case>
#   Output: <expected>
```

- Every problem gets at least two sample input/output pairs, with an edge case where one exists.
- Leave space under each problem for Sean to write a small function and its `print` checks.

### While Sean is solving

- Sean works through the problems in order and shares the code for each.
- Review what was written: confirm when it is correct, and when it is wrong point at the idea that is off rather than giving the fix.
- Move on only once the current problem matches its sample output.
