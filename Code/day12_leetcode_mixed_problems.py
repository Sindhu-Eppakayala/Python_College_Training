# Day 12 – LeetCode practice (mixed problems)

# Problems solved:
# 682  - Baseball Game
# 1614 - Maximum Nesting Depth of the Parentheses
# 3174 - Clear Digits
# 287  - Find the Duplicate Number
# 1021 - Remove Outermost Parentheses

# For each problem, I keep a function with my approach.
# Problem statements and full test cases are on LeetCode.


# -----------------------------
# 682. Baseball Game
# Idea: use a stack to maintain the score history.
# -----------------------------

def leetcode_682_baseball_game(ops):
    """
    ops: List of operations (strings).
    Logic:
    - If op is a number: push it as int.
    - "C": remove last score.
    - "D": add double of last score.
    - "+": add sum of last two scores.
    Return total sum of scores.
    """
    stack = []

    for op in ops:
        if op == "C":
            if stack:
                stack.pop()
        elif op == "D":
            if stack:
                stack.append(stack[-1] * 2)
        elif op == "+":
            if len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))

    return sum(stack)


# -----------------------------
# 1614. Maximum Nesting Depth of the Parentheses
# Idea: count depth while scanning the string.
# -----------------------------

def leetcode_1614_max_depth(s):
    """
    s: string with parentheses and other characters.
    Logic:
    - Increase depth when '('
    - Decrease depth when ')'
    - Track maximum depth reached.
    """
    depth = 0
    max_depth = 0

    for ch in s:
        if ch == "(":
            depth += 1
            max_depth = max(max_depth, depth)
        elif ch == ")":
            depth -= 1

    return max_depth


# -----------------------------
# 3174. Clear Digits
# Typical idea: remove digits and possibly previous characters,
# or build a clean result according to the problem rules.
# -----------------------------

def leetcode_3174_clear_digits(s):
    """
    s: input string.
    This is a placeholder structure for my solution.
    The exact logic depends on the problem statement, for example:
    - Iterate over characters.
    - When you see a digit, remove it (and maybe affect previous char).
    - Build a cleaned string.

    Implement your actual solution logic here based on how you solved it.
    """
    # Example idea (NOT the official solution, adapt to your approach):
    result = []
    for ch in s:
        if ch.isdigit():
            # Here you might choose to skip or modify previous characters
            # depending on the problem rules.
            # For now, we just skip digits.
            continue
        else:
            result.append(ch)

    return "".join(result)


# -----------------------------
# 287. Find the Duplicate Number
# Simple approach shown here: use a set to track seen numbers.
# -----------------------------

def leetcode_287_find_duplicate(nums):
    """
    nums: list of integers where exactly one number is duplicated.
    Logic:
    - Use a set to track seen numbers.
    - First time we see a number -> add to set.
    - Second time -> that's the duplicate.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None  # should not happen if constraints guarantee a duplicate


# -----------------------------
# 1021. Remove Outermost Parentheses
# Idea: skip the outermost '(' and ')' of each primitive substring.
# Use a depth counter.
# -----------------------------

def leetcode_1021_remove_outer_parentheses(s):
    """
    s: valid parentheses string.
    Logic:
    - Use 'depth' counter.
    - When we see '(':
      - If depth > 0, add it to result (it's inner).
      - Increase depth.
    - When we see ')':
      - Decrease depth.
      - If depth > 0 after decrease, add it (it's inner).
    - This skips the outermost pair of each primitive.
    """
    result = []
    depth = 0

    for ch in s:
        if ch == "(":
            if depth > 0:
                result.append(ch)
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth > 0:
                result.append(ch)

    return "".join(result)


# -----------------------------
# Optional: simple manual tests
# -----------------------------

if __name__ == "__main__":
    print("682 sample:", leetcode_682_baseball_game(["5", "2", "C", "D", "+"]))
    print("1614 sample:", leetcode_1614_max_depth("(1+(2*3)+((8)/4))+1"))
    print("3174 sample:", leetcode_3174_clear_digits("a1b2c3"))
    print("287 sample:", leetcode_287_find_duplicate([1, 3, 4, 2, 2]))
    print("1021 sample:", leetcode_1021_remove_outer_parentheses("(()())(())"))
