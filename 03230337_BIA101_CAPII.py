class TaxPayer:
    def __init__(self, income, employment_type, deductions):
        #Initialize TaxPayer object with income, employment type, and deductions
        self.income = income
        self.employment_type = employment_type
        self.deductions = deductions

    def calculate_taxable_income(self):
        #Calculate taxable income after deducting contributions, specific deductions,and general deductions such as education allowance and no.of children education expenses
        taxable_income = self.income
        if self.employment_type == "Regular":
            taxable_income -= self.deductions.get("PF", 0)
        taxable_income -= self.deductions.get("GIS", 0)
        #Include education allowance and children education expenses deductions
        taxable_income -= min(self.deductions.get("Education", 0), 350000)
        taxable_income -= min(self.deductions.get("NumberOfChildren", 0), 350000)
        return taxable_income

    def calculate_tax(self):
        #Calculate tax based on taxable income
        taxable_income = self.calculate_taxable_income()
        if taxable_income <= 300000:
            return 0
        elif 300001 <= taxable_income <= 400000:
            return (taxable_income - 300000) * 0.10
        elif 400001 <= taxable_income <= 650000:
            return 10000 + (taxable_income - 400000) * 0.15
        elif 650001 <= taxable_income <= 1000000:
            return 47500 + (taxable_income - 650000) * 0.20
        elif 1000001 <= taxable_income <= 1500000:
            return 97500 + (taxable_income - 1000000) * 0.25
        else:
            return 187500 + (taxable_income - 1500000) * 0.30

    def calculate_total_tax(self):
        #Calculate total tax payable, including surcharge if applicable
        tax = self.calculate_tax()
        if tax >= 1000000:
            return tax + (tax * 0.10)  # Surcharge
        return tax


class TaxCalculator:
    def __init__(self, taxpayer):
        #Initialize TaxCalculator with a TaxPayer object
        self.taxpayer = taxpayer

    def calculate_tax(self):
        #Calculate tax using the TaxPayer object
        return self.taxpayer.calculate_total_tax()


class TaxCalculatorUI:
    def get_user_input(self):
        #Get user input for income, employment type, and deductions
        while True:
            try:
                income = float(input("Enter your annual income: "))
                if income <= 0:
                    print("Income must be a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid income. Please enter a number.")

        while True:
            employment_type = input("Enter your employment type (Regular/Contract): ")
            if employment_type not in ["Regular", "Contract"]:
                print("Invalid employment type. Please enter 'Regular' or 'Contract'.")
                continue
            break

        while True:
            try:
                pf_deduction = float(input("Enter your PF deduction: "))
                gis_deduction = float(input("Enter your GIS deduction: "))
                education_deduction = float(input("Enter your education allowance deduction: "))
                # sponsored_children_deduction = float(input("Enter your number of children: "))
                Number_of_children_deduction = float(input("Enter your number of children: "))
                deductions = {"PF": pf_deduction, "GIS": gis_deduction,
                              "Education": education_deduction, "NumberOfChildern": Number_of_children_deduction}
                break
            except ValueError:
                print("Invalid deductions. Please enter numbers.")

        return income, employment_type, deductions

    def display_tax_amount(self, tax_amount):
        #Display the calculated tax amount
        print(f"Total Tax Payable: Nu. {tax_amount}")

    def run(self):
        #Run the tax calculator UI
        income, employment_type, deductions = self.get_user_input()
        taxpayer = TaxPayer(income, employment_type, deductions)
        calculator = TaxCalculator(taxpayer)
        tax_amount = calculator.calculate_tax()
        self.display_tax_amount(tax_amount)


def main():
    #Main function to start the tax calculator UI
    ui = TaxCalculatorUI()
    ui.run()


if __name__ == "__main__":
    main() 
