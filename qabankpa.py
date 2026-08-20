from LoanProcessingSystem import process_loan

passed = 0
failed = 0


def test(name, actual, expected):
    global passed, failed

    if actual == expected:
        print(name + " : PASSED")
        passed += 1
    else:
        print(name + " : FAILED")
        print("Expected:", expected)
        print("Actual:", actual)
        failed += 1


print("========== LOAN PROCESSING QA ==========")

test(
    "Minimum Age",
    process_loan("C101", 21, 50000, 0, 750, "Salaried", 100000, 5),
    "APPROVED"
)

test(
    "Maximum Age",
    process_loan("C102", 60, 50000, 0, 750, "Salaried", 100000, 5),
    "APPROVED"
)

test(
    "Invalid Minimum Age",
    process_loan("C103", 20, 50000, 0, 750, "Salaried", 100000, 5),
    "REJECTED"
)

test(
    "Invalid Maximum Age",
    process_loan("C104", 61, 50000, 0, 750, "Salaried", 100000, 5),
    "REJECTED"
)

test(
    "Invalid Salary",
    process_loan("C105", 30, 0, 0, 750, "Salaried", 100000, 5),
    "REJECTED"
)

test(
    "Poor Credit Score",
    process_loan("C106", 30, 50000, 0, 600, "Salaried", 100000, 5),
    "REJECTED"
)

test(
    "Existing Loan Exceeding Threshold",
    process_loan("C107", 30, 50000, 5000000, 750, "Salaried", 100000, 5),
    "REJECTED"
)

test(
    "High Debt To Income Ratio",
    process_loan("C108", 30, 50000, 400000, 750, "Salaried", 100000, 5),
    "REJECTED"
)

test(
    "Salaried Employment",
    process_loan("C109", 30, 80000, 100000, 780, "Salaried", 1000000, 5),
    "APPROVED"
)

test(
    "Self Employed Employment",
    process_loan("C110", 30, 80000, 100000, 780, "Self-Employed", 1000000, 5),
    "APPROVED"
)

test(
    "Invalid Employment",
    process_loan("C111", 30, 80000, 100000, 780, "Student", 100000, 5),
    "INVALID INPUT"
)

test(
    "Boundary Loan Amount",
    process_loan("C112", 30, 50000, 0, 750, "Salaried", 1, 5),
    "APPROVED"
)

test(
    "Invalid Loan Amount",
    process_loan("C113", 30, 50000, 0, 750, "Salaried", 0, 5),
    "INVALID INPUT"
)

test(
    "Loan Exceeding Eligibility",
    process_loan("C114", 30, 50000, 0, 750, "Salaried", 5000000, 5),
    "REJECTED"
)

test(
    "Invalid Tenure",
    process_loan("C115", 30, 50000, 0, 750, "Salaried", 100000, -5),
    "INVALID INPUT"
)

try:
    process_loan("C116", 30, "abc", 0, 750, "Salaried", 100000, 5)
    print("Exception Handling : FAILED")
    failed += 1
except Exception:
    print("Exception Handling : PASSED")
    passed += 1


print("\n========== QA SUMMARY ==========")
print("Passed:", passed)
print("Failed:", failed)

if failed == 0:
    print("ALL QA TESTS PASSED")
else:
    print("QA TESTS FAILED")
    exit(1)