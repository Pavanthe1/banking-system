def process_loan(customer_id, age, monthly_salary, existing_loan,
                 credit_score, employment_type, requested_loan, tenure):

    if age < 21 or age > 60:
        return "REJECTED"

    if monthly_salary <= 0:
        return "REJECTED"

    if existing_loan < 0:
        return "INVALID INPUT"

    if credit_score < 650:
        return "REJECTED"

    if tenure <= 0:
        return "INVALID INPUT"

    annual_salary = monthly_salary * 12
    dti = (existing_loan / annual_salary) * 100

    if dti > 50:
        return "REJECTED"

    if employment_type.lower() == "salaried":
        eligible_loan = annual_salary * 5 - existing_loan
    elif employment_type.lower() == "self-employed":
        eligible_loan = annual_salary * 4 - existing_loan
    else:
        return "INVALID INPUT"

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

    emi = requested_loan * monthly_rate * (1 + monthly_rate) ** months
    emi = emi / ((1 + monthly_rate) ** months - 1)

    print("\n----- LOAN PROCESSING RESULT -----")
    print("Customer ID:", customer_id)
    print("Debt-to-Income Ratio:", round(dti, 2), "%")
    print("Eligible Loan Amount:", round(eligible_loan, 2))
    print("Interest Rate:", interest_rate, "%")
    print("EMI:", round(emi, 2))
    print("Loan Status: APPROVED")

    return "APPROVED"


if __name__ == "__main__":

    try:
        customer_id = input("Enter Customer ID: ")
        age = int(input("Enter Age: "))
        monthly_salary = float(input("Enter Monthly Salary: "))
        existing_loan = float(input("Enter Existing Loan Amount: "))
        credit_score = int(input("Enter Credit Score: "))
        employment_type = input("Enter Employment Type: ")
        requested_loan = float(input("Enter Requested Loan Amount: "))
        tenure = int(input("Enter Loan Tenure in Years: "))

        process_loan(
            customer_id,
            age,
            monthly_salary,
            existing_loan,
            credit_score,
            employment_type,
            requested_loan,
            tenure
        )

    except Exception:
        print("INVALID INPUT")