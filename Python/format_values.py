# Desc.: Functions to format values in different ways.
# Author: Joseph Gallant
# Dates: Nov. 15 2024 - 

# Import the libraries
import datetime as DT


def FormatPhoneNum(phoneNum):
    # Function that accepts a 10-digit phone number and returns it as:
    # (###) ###-###
    
    formPhoneNum = "(" + phoneNum[0:3] + ") " + phoneNum[3:6] + "-" + phoneNum[6:10]

    return formPhoneNum

def FormatPostalCode(postalCode):
    # Function that formats the postal code in the X#X #X# format.

    formPostalCode = postalCode[0:3] + " " + postalCode[3:6]

    return formPostalCode
    
def FormatDateS(date):
    # Function that formats a date in the short format: yyyy-mm-dd.

    formDateS = DT.datetime.strftime(date, "%Y-%m-%d")

    return formDateS

def FormatDateM(date):
    # Function that formats a date in the medium format: dd Mon, yy.

    formDateM = DT.datetime.strftime(date, "%d %b, %y")

    return formDateM

def FormatDateL(date):
    # Function that formats a date in the long format: dd Month, yyyy.

    formDateL = DT.datetime.strftime(date, "%d %B, %Y")

    return formDateL

def FormatDollar2(dollarValue):
    # Function that formats a numeric value to a dollar format: $#,###.##.

    formDollar = "${:,.2f}".format(dollarValue)

    return formDollar