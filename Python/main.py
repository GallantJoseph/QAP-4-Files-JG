# Desc.: Main program for the One Stop Insurance Company.
# Author: Joseph Gallant
# Dates: Nov. 15 2024 - Nov. 24 2024

# Import the libraries
import one_stop_functions as OSF

# Main program loop.
while True:

    # Define the variables
    claimsLst = []

    # Run the main program
    OSF.OneStopInsuranceCompany()


    # Heading for processing claims 
    print()
    print("Previous Claim Processing")
    print("-------------------------")

    while True:

        # ProcessClaim returns a claim list element.
        claimsLst.append(OSF.ProcessClaim())

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
    
    # Print the claims from a list of claims.
    OSF.PrintClaims(claimsLst)

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
        print()
        print("*** Thank you for using our program. Have a nice day! ***")
        print()
        break