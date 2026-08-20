import math

def process_loan(age, monthly_salary, existing_loan, credit_score,
                 employment_type, requested_loan, tenure):

    if not isinstance(age, int) or not isinstance(credit_score, int) or not isinstance(tenure, int):
        return "INVALID INPUT"

    if age < 21 or age > 60:
        return "REJECTED"

    if monthly_salary <= 0:
        return "REJECTED"

    if credit_score < 650:
        return "REJECTED"

    if tenure <= 0:
        return "INVALID INPUT"

    annual_salary = monthly_salary * 12
    debt_to_income_ratio = (existing_loan / annual_salary) * 100

    if debt_to_income_ratio > 50:
        return "REJECTED"

    if employment_type.lower() == "salaried":
        eligible_loan = annual_salary * 5
    elif employment_type.lower() == "self-employed":
        eligible_loan = annual_salary * 4
    else:
        return "INVALID INPUT"

    eligible_loan = max(0, eligible_loan - existing_loan)

    if requested_loan <= 0:
        return "INVALID INPUT"

    if requested_loan > eligible_loan:
        return "REJECTED"

    if credit_score >= 800:
        interest_rate = 7.5
    elif credit_score >= 750:
        interest_rate = 8.5
    elif credit_score >= 700:
        interest_rate = 10.0
    else:
        interest_rate = 12.0

    monthly_rate = interest_rate / (12 * 100)
    months = tenure * 12

    emi = requested_loan * monthly_rate * pow(1 + monthly_rate, months)
    emi = emi / (pow(1 + monthly_rate, months) - 1)

    return {
        "status": "APPROVED",
        "eligible_loan": eligible_loan,
        "interest_rate": interest_rate,
        "emi": round(emi, 2),
        "dti": round(debt_to_income_ratio, 2)
    }


def test_case(test_name, age, salary, existing_loan, credit_score,
              employment, requested_loan, tenure):

    try:
        result = process_loan(
            age,
            salary,
            existing_loan,
            credit_score,
            employment,
            requested_loan,
            tenure
        )

        print("\nTest:", test_name)
        print("Input:")
        print("Age:", age)
        print("Salary:", salary)
        print("Existing Loan:", existing_loan)
        print("Credit Score:", credit_score)
        print("Employment:", employment)
        print("Requested Loan:", requested_loan)
        print("Tenure:", tenure)
        print("Result:", result)

    except Exception as e:
        print("\nTest:", test_name)
        print("Result: INVALID INPUT")
        print("Error:", e)


print("========== LOAN PROCESSING QA TESTING ==========")

test_case(
    "Minimum Age Boundary",
    21, 50000, 50000, 750,
    "Salaried", 1000000, 5
)

test_case(
    "Maximum Age Boundary",
    60, 50000, 50000, 750,
    "Salaried", 1000000, 5
)

test_case(
    "Age Below Minimum",
    20, 50000, 50000, 750,
    "Salaried", 1000000, 5
)

test_case(
    "Age Above Maximum",
    61, 50000, 50000, 750,
    "Salaried", 1000000, 5
)

test_case(
    "Invalid Zero Salary",
    30, 0, 50000, 750,
    "Salaried", 100000, 5
)

test_case(
    "Invalid Negative Salary",
    30, -10000, 50000, 750,
    "Salaried", 100000, 5
)

test_case(
    "Poor Credit Score",
    30, 50000, 50000, 600,
    "Salaried", 100000, 5
)

test_case(
    "High Existing Loan",
    30, 50000, 5000000, 750,
    "Salaried", 100000, 5
)

test_case(
    "High Debt To Income Ratio",
    30, 50000, 400000, 750,
    "Salaried", 100000, 5
)

test_case(
    "Salaried Employee",
    30, 80000, 100000, 780,
    "Salaried", 1000000, 5
)

test_case(
    "Self Employed Employee",
    30, 80000, 100000, 780,
    "Self-Employed", 1000000, 5
)

test_case(
    "Invalid Employment Category",
    30, 80000, 100000, 780,
    "Student", 1000000, 5
)

test_case(
    "Minimum Loan Amount",
    30, 50000, 0, 750,
    "Salaried", 1, 5
)

test_case(
    "Invalid Zero Loan Amount",
    30, 50000, 0, 750,
    "Salaried", 0, 5
)

test_case(
    "Loan Exceeding Eligibility",
    30, 50000, 0, 750,
    "Salaried", 5000000, 5
)

test_case(
    "EMI Calculation Accuracy",
    30, 100000, 0, 800,
    "Salaried", 1000000, 5
)

test_case(
    "Invalid Negative Tenure",
    30, 50000, 0, 750,
    "Salaried", 100000, -5
)

test_case(
    "Invalid String Age",
    "Thirty", 50000, 0, 750,
    "Salaried", 100000, 5
)