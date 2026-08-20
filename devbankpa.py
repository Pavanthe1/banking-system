import math

customer_id = input("Enter Customer ID: ")
age = int(input("Enter Age: "))
monthly_salary = float(input("Enter Monthly Salary: "))
existing_loan = float(input("Enter Existing Loan Amount: "))
credit_score = int(input("Enter Credit Score: "))
employment_type = input("Enter Employment Type (Salaried/Self-Employed): ")
requested_loan = float(input("Enter Requested Loan Amount: "))
tenure = int(input("Enter Loan Tenure in Years: "))

annual_salary = monthly_salary * 12
debt_to_income_ratio = (existing_loan / annual_salary) * 100 if annual_salary > 0 else 100

if credit_score >= 800:
    interest_rate = 7.5
elif credit_score >= 750:
    interest_rate = 8.5
elif credit_score >= 700:
    interest_rate = 10.0
elif credit_score >= 650:
    interest_rate = 12.0
else:
    interest_rate = 15.0

if employment_type.lower() == "salaried":
    eligible_loan = annual_salary * 5
else:
    eligible_loan = annual_salary * 4

if existing_loan > 0:
    eligible_loan = eligible_loan - existing_loan

eligible_loan = max(0, eligible_loan)

principal = min(requested_loan, eligible_loan)
monthly_rate = interest_rate / (12 * 100)
months = tenure * 12

if monthly_rate > 0 and months > 0:
    emi = principal * monthly_rate * pow(1 + monthly_rate, months) / (pow(1 + monthly_rate, months) - 1)
else:
    emi = 0

if age < 21 or age > 60:
    status = "REJECTED"
elif monthly_salary <= 0:
    status = "REJECTED"
elif credit_score < 650:
    status = "REJECTED"
elif debt_to_income_ratio > 50:
    status = "REJECTED"
elif requested_loan > eligible_loan:
    status = "REJECTED"
else:
    status = "APPROVED"

print("\n----- LOAN PROCESSING RESULT -----")
print("Customer ID:", customer_id)
print("Age:", age)
print("Monthly Salary:", monthly_salary)
print("Existing Loan:", existing_loan)
print("Credit Score:", credit_score)
print("Employment Type:", employment_type)
print("Requested Loan Amount:", requested_loan)
print("Loan Tenure:", tenure, "Years")
print("Debt-to-Income Ratio:", round(debt_to_income_ratio, 2), "%")
print("Eligible Loan Amount:", round(eligible_loan, 2))
print("Interest Rate:", interest_rate, "%")
print("EMI:", round(emi, 2))
print("Loan Status:", status)