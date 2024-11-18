# Desc.: Main program for the One Stop Insurance Company.
# Author: Joseph Gallant
# Dates: Nov. 15 2024 - 

# Import the libraries
import one_stop_functions as OSF

# Main program loop.
while True:

    # OSF.OneStopInsuranceCompany()

    while True:
        OSF.ProcessClaim()

        # Validate option to process another claim
        while True:
            claimOpt = input("Would you like to process another claim (Y/N)? ").upper()

            if claimOpt == "":
                print()
                print("Data Entry Error - A value is required.")
                print()
            elif claimOpt != "Y" and claimOpt != "N":
                print()
                print("Data Entry Error - The value is invalid.")
                print()
            else:
                break

        if claimOpt == "N":
            break

    # Validate option to run the program again.
    while True:
        runAgainOpt = input("Would you like to run the program again (Y/N)? ").upper()

        if runAgainOpt == "":
            print()
            print("Data Entry Error - A value is required.")
            print()
        elif runAgainOpt != "Y" and runAgainOpt != "N":
            print()
            print("Data Entry Error - The value is invalid.")
            print()
        else:
            break

    if runAgainOpt == "N":
        break