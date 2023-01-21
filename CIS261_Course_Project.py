#Melissa Radford
#CIS261
#CourseProject


def GetEmpName():
    empname = input("Enter employee name:  ")
    return empname

def GetHoursWorked():
    hoursworked = float(input("Enter the amount of hours worked: "))
    return hoursworked

def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate:  "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input("Enter tax rate:  "))
    return taxrate

def CalcTaxandNetPay(hoursworked, hourlyrate, taxrate):
    grosspay = hoursworked * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay- incometax
    return grosspay, incometax, netpay

def printinfo(empname, hoursworked, hourlyrate, grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname)
    print("Hours Worked:  ", f"{hoursworked:,.2f}")
    print("Hourly Rate:  ", f"{hourlyrate:,.2f}")
    print("Gross Pay:  ", f"{grosspay:,.2f}")
    print("Tax Rate:  ", f"{taxrate:.1%}")
    print("Income tax:  ", f"{incometax:,.2f}")
    print("Net Pay:  ", f"{netpay:,.2f}")

    print()
def PrintTotals(TotEmployees, TotHoursWorked, TotGrossPay, TotTax, TotNetPay):
    print()
    print(f"Total Number of Employees:  {TotEmployees}")
    print(f"Total Hours Worked:  {TotHoursWorked:,.2f}")
    print(f"Total Gross Pay:  {TotGrossPay:,.2f}")
    print(f"Total IncomeTax:  {TotIncomeTax:,.2f}")
    print(f"Total Net Pay:  {TotNetPay:,.2f}")

if __name__ == "__main__":
    TotEmployees = 0
    TotHoursWorked = 0.00
    TotGrossPay = 0.00
    TotIncomeTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        hoursworked = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        grosspay, incometax, netpay = CalcTaxandNetPay(hoursworked, hourlyrate, taxrate)
        printinfo(empname, hoursworked, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHoursWorked += hoursworked
        TotIncomeTax += incometax
        TotGrossPay += grosspay
        TotNetPay += netpay




PrintTotals (TotEmployees, TotHoursWorked, TotGrossPay, TotIncomeTax, TotNetPay)
