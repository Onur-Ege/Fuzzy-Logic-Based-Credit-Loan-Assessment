import numpy as np


# evaluation of house
# membership function for evaluation of house (VERY LOW)
def house_very_low(value):
    if 0 <= value < 3:
        return (3-value)/3
    return 0


# membership function for evaluation of house (LOW)
def house_low(value):
    if 0 < value <= 3:
        return value/3
    elif 3 < value < 6:
        return (6-value)/3
    return 0


# membership function for evaluation of house (MEDIUM)
def house_medium(value):
    if 2 < value <= 5:
        return (value-2)/3
    elif 5 < value < 8:
        return (8-value)/3
    return 0


# membership function for evaluation of house (HIGH)
def house_high(value):
    if 4 < value <= 7:
        return (value-4)/3
    elif 7 < value < 10:
        return (10 - value)/3
    return 0


# membership function for evaluation of house (VERY HIGH)
def house_very_high(value):
    if 7 < value <= 10:
        return (value - 7)/3
    return 0


# evaluation of applicant
# membership function for evaluation of applicant (LOW)
def applicant_low(value):
    if 0 <= value <= 2:
        return 1
    elif 2 < value < 4:
        return (4-value)/2
    return 0


# membership function for evaluation of applicant (MEDIUM)
def applicant_medium(value):
    if 2 < value <= 5:
        return (value-2)/3
    elif 5 < value < 8:
        return (8-value)/3
    return 0


# membership function for evaluation of applicant (HIGH)
def applicant_high(value):
    if 8 <= value <= 10:
        return 1
    elif 6 < value < 8:
        return (value-6)/2
    return 0


# evaluation of loan
# membership function for evaluation of loan (VERY LOW)
def loan_very_low(value):
    if 0 <= value < 125:
        return (125-value)/125
    return 0


# membership function for evaluation of loan (LOW)
def loan_low(value):
    if 0 < value <= 125:
        return value/125
    elif 125 < value < 250:
        return (250-value)/125
    return 0


# membership function for evaluation of loan (MEDIUM)
def loan_medium(value):
    if 125 < value <= 250:
        return (value-125)/125
    elif 250 < value < 375:
        return (375-value)/125
    return 0


# membership function for evaluation of loan (HIGH)
def loan_high(value):
    if 250 < value <= 375:
        return (value-250)/125
    elif 375 < value < 500:
        return (500-value)/125
    return 0


# membership function for evaluation of loan (VERY HIGH)
def loan_very_high(value):
    if 375 < value <= 500:
        return (value-375)/125
    return 0


# range of output sets
x_house = np.arange(0, 10, .01)
x_applicant = np.arange(0, 10, .01)
x_loan = np.arange(0, 500, .5)

# membership function of outputs applied to range
house = {
    "very_low": [house_very_low(x) for x in x_house],
    "low": [house_low(x) for x in x_house],
    "medium": [house_medium(x) for x in x_house],
    "high": [house_high(x) for x in x_house],
    "very_high": [house_very_high(x) for x in x_house]}

applicant = {
    "low": [applicant_low(x) for x in x_applicant],
    "medium": [applicant_medium(x) for x in x_applicant],
    "high": [applicant_high(x) for x in x_applicant]}

loan = {
    "very_low": [loan_very_low(x) for x in x_loan],
    "low": [loan_low(x) for x in x_loan],
    "medium": [loan_medium(x) for x in x_loan],
    "high": [loan_high(x) for x in x_loan],
    "very_high": [loan_very_high(x) for x in x_loan]}
