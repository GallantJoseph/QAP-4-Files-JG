# Desc.: Functions needed by the One Stop Insurance Company main program.
# Author: Joseph Gallant
# Dates: Nov. 15, 2024 - Nov. 29, 2024

# Import the libraries
import datetime as DT
import format_values as FV

def OneStopInsuranceCompany():
    """Main function for the One Stop Insurance Company"""

    # Define the constants
    POLICY_NUM = 1944
    BASIC_PREMIUM = 869.00
    DISC_ADD_CAR = 0.25
    EXTRA_LIAB_COV_COST = 130.00
    GLASS_COV_COST = 86.00
    LOANER_CAR_COV_COST = 58.00
    HST_RATE = 0.15
    PROCESS_FEE = 39.99
    MAX_LIAB = 1000000.00
    MONTHLY_PMNTS = 8
    PROV_LST = ["NL", "NS", "NB", "PE", "QC", "ON", "MB", "SK", "AB", "BC", "NT", "YT", "NV"]
    PMNT_TYPE_LST = ["Full", "Monthly", "Down Pay"]
    CURR_DATE = DT.datetime.now()

    # Print the headings
    print()
    print(f"   One Stop Insurance Company - Data Entry   ")
    print(f"---------------------------------------------")
    print()


    # Validate the firstName
    while True:
        firstName = input("Enter the first name: ").title()

        if firstName == "":
            print()
            print("Data Entry Error - A first name is required.")
            print()
        else:
            break

    # Validate the lastName
    while True:
        lastName = input("Enter the last name: ").title()

        if lastName == "":
            print()
            print("Data Entry Error - A last name is required.")
            print()
        else:
            break

    # Validate the strAddress
    while True:
        strAddress = input("Enter the street address: ").title()

        if strAddress == "":
            print()
            print("Data Entry Error - A street address is required.")
            print()
        else:
            break

    # Validate the city
    while True:
        city = input("Enter the city: ").title()

        if city == "":
            print()
            print("Data Entry Error - A city is required.")
            print()
        else:
            break

    # Validate the prov
    while True:
        prov = input("Enter the province (XX): ").upper()

        if prov == "":
            print()
            print("Data Entry Error - A province is required.")
            print()
        elif len(prov) != 2:
            print()
            print("Data Entry Error - The province must be 2 characters long.")
            print()
        elif prov not in PROV_LST:
            print()
            print("Data Entry Error - The province is not valid.")
            print()
        else:
            break

    # Validate the postalCode
    while True:
        postalCode = input("Enter the postal code (X#X#X#): ").upper()

        isValidPostalCode, message = ValidatePostalCode(postalCode)

        if not isValidPostalCode:
            print()
            print(message)
            print()
        else:
            break

    # Validate the phoneNum
    while True:
        phoneNum = input("Enter the phone number (##########): ").upper()

        isValidPhoneNum, message = ValidatePhoneNumber(phoneNum)

        if not isValidPhoneNum:
            print()
            print(message)
            print()
        else:
            break

    # Validate the numInsuredCars
    while True:
        numInsuredCars = input("Enter the number of insured cars: ")

        if numInsuredCars == "":
            print()
            print("Data Entry Error - The number of cars is required.")
            print()
        else:
            try:
                numInsuredCars = int(numInsuredCars)
            except:
                print()
                print("Data Entry Error - The number of cars must be a whole number.")
                print()
            else:
                if numInsuredCars < 1:
                    print()
                    print("Data Entry Error - The number of cars must be at least 1.")
                    print()
                else:
                    break

    # Validate the extraLiabCovOpt
    while True:
        extraLiabCovOpt = input("Extra liability coverage (Y/N)? ").upper()

        if extraLiabCovOpt == "":
            print()
            print("Data Entry Error - The liability coverage value is required.")
            print()
        elif extraLiabCovOpt != "Y" and extraLiabCovOpt != "N":
            print()
            print("Data Entry Error - The liability coverage value is invalid.")
            print()
        else:
            if extraLiabCovOpt == "Y":
                extraLiabCovMsg = "Yes"
            else:
                extraLiabCovMsg = "No"

            break

    # Validate the glassCovOpt
    while True:
        glassCovOpt = input("Glass replacement coverage (Y/N)? ").upper()

        if glassCovOpt == "":
            print()
            print("Data Entry Error - The glass replacement coverage value is required.")
            print()
        elif glassCovOpt != "Y" and glassCovOpt != "N":
            print()
            print("Data Entry Error - The glass replacement coverage value is invalid.")
            print()
        else:
            if glassCovOpt == "Y":
                glassCovMsg = "Yes"
            else:
                glassCovMsg = "No"

            break

    # Validate the loanerCarCovOpt
    while True:
        loanerCarCovOpt = input("Loaner car coverage (Y/N)? ").upper()

        if loanerCarCovOpt == "":
            print()
            print("Data Entry Error - The loaner car coverage value is required.")
            print()
        elif loanerCarCovOpt != "Y" and loanerCarCovOpt != "N":
            print()
            print("Data Entry Error - The loaner car coverage value is invalid.")
            print()
        else:
            if loanerCarCovOpt == "Y":
                loanerCarCovMsg = "Yes"
            else:
                loanerCarCovMsg = "No"

            break

    # Validate the paymentType
    while True:
        pmntType = input("Please enter the payment type (Full, Monthly, Down Pay): ").title()

        if pmntType == "":
            print()
            print("Data Entry Error - The payment type is required.")
            print()
        elif not pmntType in PMNT_TYPE_LST:
            print()
            print("Data Entry Error - The payment type is invalid.")
            print()
        else:
            break

    # If the payment type is Down Pay, ask the user to enter a downpayment amount.
    if pmntType == "Down Pay":

        # Validate the downPayment amount.
        while True:
            downPayment = input("Please enter the downpayment amount: ")

            if downPayment == "":
                print()
                print("Data Entry Error - The downpayment amount is required.")
                print()
            else:
                try:
                    downPayment = float(downPayment)

                except:
                    print()
                    print("Data Entry Error - The downpayment amount must be numeric.")
                    print()
                else:
                    if downPayment <= 0:
                        print()
                        print("Data Entry Error - The downpayment amount must be over 0.")
                        print()
                    else:
                        break
    else:
        downPayment = 0

    # Calculations

    # Insurance premiums calculations
    insPremiums = BASIC_PREMIUM

    # Discount for each additional car
    if numInsuredCars > 1:
        addCarPremiums = (numInsuredCars - 1) * (1 - DISC_ADD_CAR) * BASIC_PREMIUM
        insPremiums += addCarPremiums

    # Extra liability coverage cost
    if extraLiabCovOpt == "Y":
        extraLiabCost = EXTRA_LIAB_COV_COST * numInsuredCars
    else:
        extraLiabCost = 0

    # Glass coverage cost
    if glassCovOpt == "Y":
        glassCovCost = GLASS_COV_COST * numInsuredCars
    else:
        glassCovCost = 0

    # Loaner car cost
    if loanerCarCovOpt == "Y":
        loanerCarCost = LOANER_CAR_COV_COST * numInsuredCars
    else:
        loanerCarCost = 0

    totExtraCosts = extraLiabCost + glassCovCost + loanerCarCost

    totInsPremiums = insPremiums + totExtraCosts
    hst = totInsPremiums * HST_RATE
    invTot = totInsPremiums + hst

    # Payment type calculations
    if pmntType == "Monthly" or pmntType == "Down Pay":
        totInsPremiums = totInsPremiums - downPayment
        hst = totInsPremiums * HST_RATE
        invTot = totInsPremiums + hst + PROCESS_FEE
        monthlyPmnt = invTot / MONTHLY_PMNTS

    # Print the invoice

    print()
    print(f"    One Stop Insurance Company - Invoice     ")
    print(f"---------------------------------------------")
    print()
    print(f"Policy Number: {POLICY_NUM:<4d}         Date:  {FV.FormatDateS(CURR_DATE):>10s}")
    print()
    print(f"Customer Information")
    print(f"--------------------")
    print()
    print(f"First Name:                 {firstName:<25s}")
    print(f"Last Name:                  {lastName:<25s}")
    print(f"Street Address:             {strAddress:<25s}")
    print(f"City:                       {city:<25s}")
    print(f"Province:                   {prov:<2s}")
    print(f"Postal Code:                {FV.FormatPostalCode(postalCode):<7s}")
    print(f"Phone Number:               {FV.FormatPhoneNum(phoneNum):<14s}")
    print()
    print(f"Insurance Premiums Details")
    print(f"--------------------------")
    print()
    print(f"Number of Insured Cars:     {numInsuredCars:<2d}")
    print(f"Extra Liability Coverage:   {extraLiabCovMsg:<1s}")
    print(f"Glass Replacement Coverage: {glassCovMsg:<1s}")
    print(f"Loaner Car Coverage:        {loanerCarCovMsg:<1s}")
    print(f"Maximum Liability:          {FV.FormatDollar2(MAX_LIAB):>10s}")
    print()
    print(f"Payment Type:               {pmntType:<10s}")

    if pmntType == "Monthly" or pmntType == "Down Pay":
        if pmntType == "Down Pay":
            print(f"    Downpayment:            {FV.FormatDollar2(downPayment):>10s}")
        print(f"    Monthly Payment:        {FV.FormatDollar2(monthlyPmnt):>10s}")
        print(f"        (Period of {MONTHLY_PMNTS} Months.)")
        print(f"    Note: A processing fee of {FV.FormatDollar2(PROCESS_FEE)} ")
        print(f"          is added to the total.")

    print()
    print(f"Insurance Premiums Cost")
    print(f"-----------------------")
    print()
    print(f"Base Premiums Cost:         {FV.FormatDollar2(BASIC_PREMIUM):>10s}")
    if numInsuredCars > 1:
        print(f"Cost for Additional Cars:   {FV.FormatDollar2(addCarPremiums):>10s}")

    print(f"                            ----------")
    print(f"                            {FV.FormatDollar2(insPremiums):>10s}")
    print()
    print(f"Extra Liability Cost:       {FV.FormatDollar2(extraLiabCost):>10s}")
    print(f"Glass Coverage Cost:        {FV.FormatDollar2(glassCovCost):>10s}")
    print(f"Loaner Car Coverage Cost:   {FV.FormatDollar2(loanerCarCost):>10s}")
    print(f"                            ----------")
    print(f"Total Extra Costs:          {FV.FormatDollar2(totExtraCosts):>10s}")
    print()

    # Amount before the downPayment has been applied.
    totInsPremiumsBef = totInsPremiums + downPayment

    print(f"Total Insurance Premiums:   {FV.FormatDollar2(totInsPremiumsBef):>10s}")

    if pmntType == "Down Pay" and downPayment > 0:
        print(f"Downpayment:               -{FV.FormatDollar2(downPayment):>10s}")
        print(f"                            ----------")
        print(f"                            {FV.FormatDollar2(totInsPremiums):>10s}")

    print(f"HST:                        {FV.FormatDollar2(hst):>10s}")

    if pmntType == "Monthly" or pmntType == "Down Pay":
        print(f"Processing Fee:             {FV.FormatDollar2(PROCESS_FEE):>10s}")

    print(f"                            ----------")
    print(f"Invoice Total:              {FV.FormatDollar2(invTot):>10s}")
    print()


def ProcessClaim():
    """Function that processes a claim. Returns the claim information entered as a list: [claimNum, claimDate, claimAmt]."""

    print()
    # Validate the claimNum
    while True:
        claimNum = input("Please enter the claim number (#####): ")

        if claimNum == "":
            print()
            print("Data Entry Error - A claim number is required.")
            print()
        elif len(claimNum) != 5:
            print()
            print("Data Entry Error - The claim number must be 5 digits long.")
            print()
        else:

            # Check if the claim number only contains digits
            isValidClaimNum = True
            for char in claimNum:
                if not char.isdigit():
                    isValidClaimNum = False
                    break

            if not isValidClaimNum:
                print()
                print("Data Entry Error - The claim number must only contain digits.")
                print()
            else:
                break

    # Validate the claimDate
    while True:
        claimDate = input("Please enter the claim date (YYYY-MM-DD): ")

        if claimDate == "":
            print()
            print("Data Entry Error - The claim date is required.")
            print()
        else:
            try:
                claimDate = DT.datetime.strptime(claimDate, "%Y-%m-%d")
            except:
                print()
                print("Data Entry Error - The claim date is invalid.")
                print()
            else:
                break

    # Validate the claimAmt
    while True:
        claimAmt = input("Please enter the claim amount: ")

        try:
            claimAmt = float(claimAmt)
        except:
                print()
                print("Data Entry Error - The claim amount must be numeric.")
                print()
        else:
            if claimAmt <= 0:
                print()
                print("Data Entry Error - The claim amount must be over 0.")
                print()
            else:
                break

    return [claimNum, claimDate, claimAmt]

def PrintClaims(claimsLst):
    """Function that prints out all the claims from a claimsLst. Input as [claimNum, claimDate, claimAmt]."""

    # Print the headings

    print()
    print(f"       Previous Claims Listing        ")
    print(f"======================================")
    print()
    print(f"Claim #   Claim Date         Amount   ")
    print(f"--------------------------------------")

    for claim in claimsLst:
        claimNum = claim[0]
        claimDate = claim[1]
        claimAmt = claim[2]

        print(f" {claimNum:<5s}    {FV.FormatDateS(claimDate):>10s}     {FV.FormatDollar2(claimAmt):>12s}")

    print()


def ValidatePostalCode(postalCode):
    """ Function that validates a postal code with no spacing (X#X#X#). Returns a boolean value and the error message."""

    # Initialize the variables
    isValidPostalCode = True
    message = ""

    if postalCode == "":
        isValidPostalCode = False
        message = "Data Entry Error - A postal code is required."

    elif len(postalCode) != 6:
        isValidPostalCode = False
        message = "Data Entry Error - The postal code must be 6 characters long."
    else:
        # Verifies that the character in every position is correct.
        for i in range(0, 6):
            if i % 2 == 0: # even position (letter)
                if not postalCode[i].isalpha():
                    isValidPostalCode = False
                    break
            else: # odd position (digit)
                if not postalCode[i].isdigit():
                    isValidPostalCode = False
                    break

        if not isValidPostalCode:
            message = "Data Entry Error - The postal code is invalid. Must be in X#X#X# format."

    return isValidPostalCode, message

def ValidatePhoneNumber(phoneNum):
    """Function that validates a phone number entered as 10 characters with no spacing."""

    # Initialize the variables
    isValidPhoneNum = True
    message = ""

    if phoneNum == "":
        isValidPhoneNum = False
        message = "Data Entry Error - A phone number is required."
    elif len(phoneNum) != 10:
        isValidPhoneNum = False
        message = "Data Entry Error - The phone number must be 10 digits long."
    else:
        # Verifies that each character is a digit. If not, the phone number is invalid and
        # it breaks out of the loop

        for character in phoneNum:
            if not character.isdigit():
                isValidPhoneNum = False
                message = "Data Entry Error - The phone number is invalid. Must be in ########## format."
                break

    return isValidPhoneNum, message