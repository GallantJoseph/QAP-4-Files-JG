# Desc.: Functions to format values in different ways.
# Author: Joseph Gallant
# Dates: Nov. 15 2024 - 

# Import the libraries
import datetime as DT


def FormatPhoneNum(phoneNum):
    # Function that accepts a 10-digit phone number and returns it as:
    # (###) ###-###
    
    fullPhoneNum = "(" + phoneNum[0:3] + ") " + phoneNum[3:6] + "-" + phoneNum[6:10]

    return fullPhoneNum