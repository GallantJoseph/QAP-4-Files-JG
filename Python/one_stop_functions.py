# Desc.: Functions needed for the One Stop Insurance Company main program.
# Author: Joseph Gallant
# Dates: Nov. 15 2024 - 

# Import the libraries
import datetime as DT
import format_values as FV

def OneStopInsuranceCompany():
    # Main function for the One Stop Insurance Company

    # Define the constants
    # TODO Read from file
    POLICY_NUM: 1944
    BASIC_PREMIUM: 869.00
    DISC_ADD_CAR: 0.25
    EXTRA_LIAB_COV_COST: 130.00
    GLASS_COV_COST: 86.00
    LOANER_CAR_COV_COST: 58.00
    HST_RATE: 0.15
    PROCESS_FEE: 39.99
    MAX_LIAB = 1000000.00
    PROV_LST = ["NL", "NS", "NB", "PE", "QC", "ON", "MB", "SK", "AB", "BC", "NT", "YT", "NV"]
    PMNT_TYPE_LST = ["Full", "Monthly", "Down Pay"]
    
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

        if postalCode == "":
            print()
            print("Data Entry Error - A postal code is required.")
            print()
        elif len(postalCode) != 6:
            print()
            print("Data Entry Error - The postal code must be 6 characters long.")
            print()
        elif not IsValidPostalCode(postalCode):
            print()
            print("Data Entry Error - The postal code is invalid. Must be in X#X#X# format.")
            print()
        else:
            break

    # Validate the phoneNum
    while True:
        phoneNum = input("Enter the phone number (##########): ").upper()

        if phoneNum == "":
            print()
            print("Data Entry Error - A phone number is required.")
            print()
        elif len(phoneNum) != 10:
            print()
            print("Data Entry Error - The phone number must be 10 digits long.")
            print()
        elif not IsValidPhoneNum(phoneNum):
            print()
            print("Data Entry Error - The phone number is invalid. Must be in ########## format.")
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
                break

    # Validate the extraLiabCovOpt
    while True:
        extraLiabCovOpt = input("Extra liability coverage (Y/N)? ").upper()

        if extraLiabCovOpt != "Y" and extraLiabCovOpt != "N":
            print()
            print("Data Entry Error - The liability coverage value is invalid.")
            print()
        else:
            break

    # Validate the glassCovOpt
    while True:
        glassCovOpt = input("Glass replacement coverage (Y/N)? ").upper()

        if glassCovOpt != "Y" and glassCovOpt != "N":
            print()
            print("Data Entry Error - The glass coverage value is invalid.")
            print()
        else:
            break

    # Validate the loanerCarCovOpt
    while True:
        loanerCarCovOpt = input("Loaner car coverage (Y/N)? ").upper()

        if loanerCarCovOpt != "Y" and loanerCarCovOpt != "N":
            print()
            print("Data Entry Error - The loaner car coverage value is invalid.")
            print()
        else:
            break

    # Validate the paymentType
    while True:
        pmntType = input("Please enter the payment type (Full, Monthly, Down Pay): ").title()

        if pmntType == "":
            print()
            print("Data Entry Error - The payment type is required.")
            print()
        if not pmntType in PMNT_TYPE_LST:
            print()
            print("Data Entry Error - The payment type is invalid.")
            print()
        else:
            break

    # TODO: Remove testing variables
    firstName = "John"
    lastName = "Doe"
    strAddress = "123 Main St."
    city = "St. John's"
    prov = "NL"
    postalCode = "A1A2B2"
    phoneNum = "1234567890" # print(FV.FormatPhoneNum(phoneNum))
    numInsuredCars = 1
    extraLiabCovOpt = "Y"
    glassCovOpt = "N"
    loanerCarCovOpt = "N"
    pmntType = "Full"


def IsValidPostalCode(postalCode):
    # Function that validates a postal code with no spacing (X#X#X#).

    # Define the constants
    UPPER_LETTER_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    postalCode = postalCode.upper()

    # Check if the character in every position is correct.
    validPostalCode = True
    for i in range(1, 6):
        if i % 2 == 0: # even position (letter)
            if not set(postalCode[i]).issubset(UPPER_LETTER_CHARS):
                validPostalCode = False
                break
        else: # odd position (digit)
            if not postalCode[i].isdigit():
                validPostalCode = False
                break

    return validPostalCode

def IsValidPhoneNum(phoneNum):
    # Function that validates a phone number entered as 10 characters with no spacing.

    # Verifies that each character is a digit. If not, the phone number is invalid and
    # it breaks out of the loop

    validPhoneNum = True
    for character in phoneNum:
        if not character.isdigit():
            validPhoneNum = False
            break

    return validPhoneNum