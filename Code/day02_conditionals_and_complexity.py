# Day 2 – Conditional statements, C vs Python, time & space complexity

# Topics:
# - Service-based vs product-based companies (discussion in notes)
# - Differences between C and Python (discussion in notes)
# - Conditional statements (if, elif, else)
# - Time and space complexity (basic idea)

# -----------------------------
# Example 1: Simple grading system using conditionals
# -----------------------------

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")

# Time complexity: O(1) – only a fixed number of comparisons, not depending on input size.
# Space complexity: O(1) – only one variable 'marks' is used.


# -----------------------------
# Example 2: Check if a number is positive, negative, or zero
# -----------------------------

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Time complexity: O(1) – constant number of comparisons.
# Space complexity: O(1) – one variable 'num'.


# -----------------------------
# Example 3: Simple eligibility check using conditionals
# -----------------------------

age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? (yes/no): ").lower()

if age >= 18 and has_id == "yes":
    print("You are eligible.")
elif age >= 18 and has_id != "yes":
    print("You are 18+ but need a valid ID.")
else:
    print("You are not eligible.")

# Time complexity: O(1)
# Space complexity: O(1)


# -----------------------------
# Example 4: Demonstrating O(n) time complexity with a loop
# -----------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Count how many numbers are even
count_even = 0
for x in numbers:
    if x % 2 == 0:
        count_even += 1

print("Number of even values:", count_even)

# Time complexity: O(n) – the loop runs n times where n is the length of 'numbers'.
# Space complexity: O(1) – only 'count_even' plus the input list.


# -----------------------------
# Notes (non-code, just comments):
# -----------------------------
# Service-based vs Product-based companies:
# - Service-based: work on client projects, focus on delivery & support.
# - Product-based: build their own products, focus on features & scalability.
#
# C vs Python:
# - C: compiled, low-level, faster, more control over memory.
# - Python: interpreted, high-level, easier to write and read, slower but more productive.
#
# These topics are explained more in the 'notes/day02_companies_conditionals_complexity.md' file.
