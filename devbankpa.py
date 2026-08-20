def process_loan(customer_id, age, monthly_salary, existing_loan,
                 credit_score, employment_type, requested_loan, tenure):

    if age < 21 or age > 60:
        print("Loan Status: REJECTED")
        return "REJECTED"

    if monthly_salary <= 0:
        print("Loan Status: REJECTED")
        return "REJECTED"

    if existing_loan < 0:
        print("Loan Status: INVALID INPUT")
        return "INVALID INPUT"

    if credit_score < 650:
        print("Loan Status: REJECTED")
        return "REJECTED"

    if tenure <= 0:
        print("Loan Status: INVALID INPUT")
        return "INVALID INPUT"

    annual_salary = monthly_salary * 12

    dti = (existing_loan / annual_salary) * 100

    if dti > 50:
        print("Loan Status: REJECTED")
        return "REJECTED"

    if employment_type.lower() == "salaried":
        eligible_loan = annual_salary * 5 - existing_loan

    elif employment_type.lower() == "self-employed":
        eligible_loan = annual_salary * 4 - existing_loan

    else:
        print("Loan Status: INVALID INPUT")
        return "INVALID INPUT"

    if requested_loan <= 0:
        print("Loan Status: INVALID INPUT")
        return "INVALID INPUT"

    if requested_loan > eligible_loan:
        print("Loan Status: REJECTED")
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

    emi = requested_loan * monthly_rate * (1 + monthly_rate) ** months
    emi = emi / ((1 + monthly_rate) ** months - 1)

    print()
    print("----- LOAN PROCESSING RESULT -----")
    print("Customer ID:", customer_id)
    print("Age:", age)
    print("Monthly Salary:", monthly_salary)
    print("Existing Loan:", existing_loan)
    print("Credit Score:", credit_score)
    print("Employment Type:", employment_type)
    print("Requested Loan:", requested_loan)
    print("Loan Tenure:", tenure, "Years")
    print("Debt-to-Income Ratio:", round(dti, 2), "%")
    print("Eligible Loan Amount:", round(eligible_loan, 2))
    print("Interest Rate:", interest_rate, "%")
    print("EMI:", round(emi, 2))
    print("Loan Status: APPROVED")

    return "APPROVED"


if __name__ == "__main__":

    process_loan(
        "C101",
        30,
        80000,
        100000,
        780,
        "Salaried",
        1000000,
        5
    )