# market value
# membership function for market value (LOW)
def market_value_low(value):
    if 0 <= value <= 50:
        return 1
    elif 50 <= value <= 100:
        return (100 - value) / 50
    return 0


# membership function for market value (MEDİUM)
def market_value_medium(value):
    if 100 <= value <= 200:
        return 1
    elif 50 < value < 100:
        return (value - 50) / 50
    elif 200 < value < 250:
        return (250 - value) / 50
    return 0


# membership function for market value (HİGH)
def market_value_high(value):
    if 300 <= value <= 650:
        return 1
    elif 200 < value < 300:
        return (value - 200) / 100
    elif 650 < value < 850:
        return (850 - value) / 200
    return 0


# membership function for market value (VERY HİGH)
def market_value_very_high(value):
    if 850 <= value <= 1000:
        return 1
    elif 650 <= value < 850:
        return (value - 650) / 200
    return 0


# location of house
# membership function for location of house (BAD)
def location_bad(value):
    if 0 <= value <= 1.5:
        return 1
    elif 1.5 < value <= 4:
        return (4 - value) / 2.5
    return 0


# membership function for location of house (FAİR)
def location_fair(value):
    if 5 <= value <= 6:
        return 1
    elif 2.5 < value < 5:
        return (value - 2.5) / 2.5
    elif 6 < value < 8.5:
        return (8.5 - value) / 2.5
    return 0


# membership function for location of house (EXCELLENT)
def location_excellent(value):
    if 8.5 <= value <= 10:
        return 1
    elif 6 < value < 8.5:
        return (value - 6) / 2.5
    return 0


# applicant's assets
# membership function for applicant's assets (LOW)
def asset_low(value):
    if 0 <= value < 150:
        return (150 - value) / 150
    return 0


# membership function for applicant's assets (MEDİUM)
def asset_medium(value):
    if 250 <= value <= 450:
        return 1
    elif 50 < value < 250:
        return (value - 50) / 200
    elif 450 < value < 650:
        return (650 - value) / 200
    return 0


# membership function for applicant's assets (HİGH)
def asset_high(value):
    if 500 < value < 700:
        return (value - 500) / 200
    elif 700 <= value <= 1000:
        return 1
    return 0


# applicant's salary
# membership function for applicant's salary (LOW)
def salary_low(value):
    if 0 <= value <= 10:
        return 1
    elif 10 < value < 25:
        return (25 - value) / 15
    return 0


# membership function for applicant's salary (MEDİUM)
def salary_medium(value):
    if 15 < value <= 35:
        return (value - 15) / 20
    elif 35 < value < 55:
        return (55 - value) / 20
    return 0


# membership function for applicant's salary (HİGH)
def salary_high(value):
    if 40 < value <= 60:
        return (value - 40) / 20
    elif 60 < value < 80:
        return (80 - value) / 20
    return 0


# membership function for applicant's salary (VERY HİGH)
def salary_very_high(value):
    if 80 <= value <= 100:
        return 1
    elif 60 < value < 80:
        return (value - 60) / 20
    return 0


# interest rate
# membership function for interest rate (LOW)
def interest_low(value):
    if 0 <= value <= 2:
        return 1
    elif 2 < value < 5:
        return (5 - value) / 3
    return 0


# membership function for interest rate (MEDIUM)
def interest_medium(value):
    if 4 <= value <= 6:
        return 1
    elif 2 < value < 4:
        return (value - 2) / 2
    elif 6 < value < 8:
        return (8 - value) / 2
    return 0


# membership function for interest rate (HIGH)
def interest_high(value):
    if 8.5 <= value <= 10:
        return 1
    elif 6 < value < 8.5:
        return (value - 6) / 2.5
    return 0
