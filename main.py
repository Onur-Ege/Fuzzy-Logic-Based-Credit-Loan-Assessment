import matplotlib.pyplot as plt
from membershipFunctionsOfInputSets import *
from membershipFunctionsOfOutputSets import *
import numpy as np


def and_rule(x, y, z):
    rule = np.fmin(x, y)
    act = np.fmin(rule, z)
    return act


def or_rule(x, y, z):
    rule = np.fmax(x, y)
    act = np.fmax(rule, z)
    return act


# fuzzify crisp inputs using membership functions of inputs set and return it
def fuzzify(crisp_inputs):
    print("fuzzify function")
    return {
        "market_value": {
                "low": market_value_low(crisp_inputs["market_value"]),
                "medium": market_value_medium(crisp_inputs["market_value"]),
                "high": market_value_high(crisp_inputs["market_value"]),
                "very_high": market_value_very_high(crisp_inputs["market_value"])
        },
        "location": {
                "bad": location_bad(crisp_inputs["location"]),
                "fair": location_fair(crisp_inputs["location"]),
                "excellent": location_excellent(crisp_inputs["location"])
        },
        "asset": {
                "low": asset_low(crisp_inputs["asset"]),
                "medium": asset_medium(crisp_inputs["asset"]),
                "high": asset_high(crisp_inputs["asset"])
        },
        "salary": {
                "low": salary_low(crisp_inputs["salary"]),
                "medium": salary_medium(crisp_inputs["salary"]),
                "high": salary_high(crisp_inputs["salary"]),
                "very_high": salary_very_high(crisp_inputs["salary"])
        },
        "interest": {
                "low": interest_low(crisp_inputs["interest"]),
                "medium": interest_medium(crisp_inputs["interest"]),
                "high": interest_high(crisp_inputs["interest"])
        }
    }


# create graphics for rule evaluations
def create_graphics(fuzzy_house, fuzzy_applicant, fuzzy_credit, crisp_result):
    # Set up a figure with 3 subplots (1 row, 3 columns)
    fig, axes = plt.subplots(3, 1, figsize=(6, 6))

    # Define y-axis ticks
    y_ticks = np.linspace(0, 1, 6)  # Create 6 evenly spaced ticks from 0 to
    # -----------------------------------------------------------------------------------------------------------
    # plot for house evaluation
    axes[0].plot(x_house, house["very_low"], "r", linestyle='--', label="very_low")
    axes[0].plot(x_house, house["low"], "g", linestyle='--', label="low")
    axes[0].plot(x_house, house["medium"], "b", linestyle='--', label="medium")
    axes[0].plot(x_house, house["high"], "y", linestyle='--', label="high")
    axes[0].plot(x_house, house["very_high"], "gray", linestyle='--', label="very_high")

    # fill area under the result of aggregation of the rule outputs
    axes[0].fill_between(x_house, fuzzy_house, color="gray", alpha=0.4)

    axes[0].set_title("House Evaluation Output")
    axes[0].grid(True)
    axes[0].set_yticks(y_ticks)  # Add y-axis ticks
    axes[0].set_ylabel("Membership Degree")  # Add y-axis label
    axes[0].set_ylim(-0.1, 1.1)
    axes[0].legend()
    # ------------------------------------------------------------------------------------------------------------
    # plot for applicant evaluation
    axes[1].plot(x_applicant, applicant["low"], "g", linestyle='--', label="low")
    axes[1].plot(x_applicant, applicant["medium"], "b", linestyle='--', label="medium")
    axes[1].plot(x_applicant, applicant["high"], "y", linestyle='--', label="high")

    # fill area under the result of aggregation of the rule outputs
    axes[1].fill_between(x_applicant, fuzzy_applicant, color="gray", alpha=0.4)

    axes[1].set_title("Applicant Evaluation Output")
    axes[1].grid(True)
    axes[1].set_yticks(y_ticks)  # Add y-axis ticks
    axes[1].set_ylabel("Membership Degree")  # Add y-axis label
    axes[1].set_ylim(-0.1, 1.1)
    axes[1].legend()
    # ------------------------------------------------------------------------------------------------------------
    # plot for credit evaluation
    axes[2].plot(x_loan, loan["very_low"], "r", linestyle='--', label="very_low")
    axes[2].plot(x_loan, loan["low"], "g", linestyle='--', label="low")
    axes[2].plot(x_loan, loan["medium"], "b", linestyle='--', label="medium")
    axes[2].plot(x_loan, loan["high"], "y", linestyle='--', label="high")
    axes[2].plot(x_loan, loan["very_high"], "gray", linestyle='--', label="very_high")

    # fill area under the result of aggregation of the rule outputs
    axes[2].fill_between(x_loan, fuzzy_credit, color="gray", alpha=0.4)

    axes[2].set_title("Credit Evaluation Output")
    axes[2].grid(True)
    axes[2].set_yticks(y_ticks)  # Add y-axis ticks
    axes[2].set_ylabel("Membership Degree")  # Add y-axis label
    axes[2].set_ylim(-0.1, 1.1)
    axes[2].legend()
    # -------------------------------------------------------------------------------------------------------------
    # Add crisp result text below the subplots
    plt.figtext(0.5, 0.02, f'Recommended Loan Amount: {crisp_result:.2f} 10^3 $',
                ha='center', va='center', fontsize=10, fontweight='bold', color="red")

    # Adjust layout and show the combined plot
    plt.tight_layout()
    # Add padding at the bottom for the text
    plt.subplots_adjust(bottom=0.1)
    plt.show()


# House evaluation function
def evaluate_house(fuzzy_inputs):
    print("house evaluation function")
    # Rules
    # 1. IF (market value is low) THEN (house is low)
    house_low1 = np.fmin(fuzzy_inputs["market_value"]["low"], house["low"])
    # 2. IF (location is bad) THEN (house is low)
    house_low2 = np.fmin(fuzzy_inputs["location"]["bad"], house["low"])
    # 3. IF (location is bad) AND (market value is low) THEN (house is very low)
    house_very_low1 = and_rule(fuzzy_inputs["location"]["bad"], fuzzy_inputs["market_value"]["low"], house["very_low"])
    # 4. IF (location is bad) AND (market value is medium) THEN (house is low)
    house_low3 = and_rule(fuzzy_inputs["location"]["bad"], fuzzy_inputs["market_value"]["medium"], house["low"])
    # 5. IF (location is bad) AND (market value is high) THEN (house is medium)
    house_medium1 = and_rule(fuzzy_inputs["location"]["bad"], fuzzy_inputs["market_value"]["high"], house["medium"])
    # 6. IF (location is bad) AND (market value is very high) THEN (house is high)
    house_high1 = and_rule(fuzzy_inputs["location"]["bad"], fuzzy_inputs["market_value"]["very_high"], house["high"])
    # 7. IF (location is fair) AND (market value is low) THEN (house is low)
    house_low4 = and_rule(fuzzy_inputs["location"]["fair"], fuzzy_inputs["market_value"]["low"], house["low"])
    # 8. IF (location is fair) AND (market value is medium) THEN (house is medium)
    house_medium2 = and_rule(fuzzy_inputs["location"]["fair"], fuzzy_inputs["market_value"]["medium"], house["medium"])
    # 9. IF (location is fair) AND (market value is high) THEN (house is high)
    house_high2 = and_rule(fuzzy_inputs["location"]["fair"], fuzzy_inputs["market_value"]["high"], house["high"])
    # 10. IF (location is fair) AND (market value is very high) THEN (house is very high)
    house_very_high1 = and_rule(fuzzy_inputs["location"]["fair"], fuzzy_inputs["market_value"]["very_high"], house["very_high"])
    # 11. IF (location is excellent) AND (market value is low) THEN (house is medium)
    house_medium3 = and_rule(fuzzy_inputs["location"]["excellent"], fuzzy_inputs["market_value"]["low"], house["medium"])
    # 12. IF (location is excellent) AND (market value is medium) THEN (house is high)
    house_high3 = and_rule(fuzzy_inputs["location"]["excellent"], fuzzy_inputs["market_value"]["medium"], house["high"])
    # 13. IF (location is excellent) AND (market value is high) THEN (house is high)
    house_very_high2 = and_rule(fuzzy_inputs["location"]["excellent"], fuzzy_inputs["market_value"]["high"], house["high"])
    # 14. IF (location is excellent) AND (market value is very high) THEN (house is very high)
    house_very_high3 = and_rule(fuzzy_inputs["location"]["excellent"], fuzzy_inputs["market_value"]["very_high"], house["very_high"])

    # Combine the rules
    step = or_rule(house_low1, house_low2, house_low3)
    house_act_low = np.fmax(step, house_low4)

    house_act_medium = or_rule(house_medium1, house_medium2, house_medium3)

    house_act_high = or_rule(house_high1, house_high2, house_high3)

    house_act_very_high = or_rule(house_very_high1, house_very_high2, house_very_high3)

    step = or_rule(house_very_low1, house_act_low, house_act_medium)
    house_act = or_rule(step, house_act_high, house_act_very_high)

    return house_act


# Applicant evaluation function
def evaluate_applicant(fuzzy_inputs):
    print("applicant evaluation function")
    # Rules
    # 1.IF (asset is low) AND (salary is low) THEN (applicant is low )
    applicant_low1 = and_rule(fuzzy_inputs["asset"]["low"], fuzzy_inputs["salary"]["low"], applicant["low"])
    # 2.IF (asset is low) AND (salary is medium) THEN (applicant is low)
    applicant_low2 = and_rule(fuzzy_inputs["asset"]["low"], fuzzy_inputs["salary"]["medium"], applicant["low"])
    # 3.IF (asset is low) AND (salary is high) THEN (applicant is medium)
    applicant_medium1 = and_rule(fuzzy_inputs["asset"]["low"], fuzzy_inputs["salary"]["high"], applicant["medium"])
    # 4.IF (asset is low) AND (salary is very high) THEN (applicant is high)
    applicant_high1 = and_rule(fuzzy_inputs["asset"]["low"], fuzzy_inputs["salary"]["very_high"], applicant["high"])
    # 5.IF (asset is medium) AND (salary is low) THEN (applicant is low)
    applicant_low3 = and_rule(fuzzy_inputs["asset"]["medium"], fuzzy_inputs["salary"]["low"], applicant["low"])
    # 6.IF (asset is medium) AND (salary is medium) THEN (applicant is medium)
    applicant_medium2 = and_rule(fuzzy_inputs["asset"]["medium"], fuzzy_inputs["salary"]["medium"], applicant["medium"])
    # 7.IF (asset is medium) AND (salary is high) THEN (applicant is high)
    applicant_high2 = and_rule(fuzzy_inputs["asset"]["medium"], fuzzy_inputs["salary"]["high"], applicant["high"])
    # 8.IF (asset is medium) AND (salary is very high) THEN (applicant is high)
    applicant_high3 = and_rule(fuzzy_inputs["asset"]["medium"], fuzzy_inputs["salary"]["very_high"], applicant["high"])
    # 9.IF (asset is high) AND (salary is low) THEN (applicant is medium)
    applicant_medium3 = and_rule(fuzzy_inputs["asset"]["high"], fuzzy_inputs["salary"]["low"], applicant["medium"])
    # 10.IF (asset is high) AND (salary is medium) THEN (applicant is medium)
    applicant_medium4 = and_rule(fuzzy_inputs["asset"]["high"], fuzzy_inputs["salary"]["medium"], applicant["medium"])
    # 11.IF (asset is high) AND (salary is high) THEN (applicant is high)
    applicant_high4 = and_rule(fuzzy_inputs["asset"]["high"], fuzzy_inputs["salary"]["high"], applicant["high"])
    # 12.IF (asset is high) AND (salary is very high) THEN (applicant is high)
    applicant_high5 = and_rule(fuzzy_inputs["asset"]["high"], fuzzy_inputs["salary"]["very_high"], applicant["high"])

    # Combine the Rules
    applicant_act_low = or_rule(applicant_low1, applicant_low2, applicant_low3)

    step = or_rule(applicant_medium1, applicant_medium2, applicant_medium3)
    applicant_act_medium = np.fmax(step, applicant_medium4)

    step = or_rule(applicant_high1, applicant_high2, applicant_high3)
    applicant_act_high = or_rule(step, applicant_high4, applicant_high5)

    applicant_act = or_rule(applicant_act_low, applicant_act_medium, applicant_act_high)

    return applicant_act


# Credit evaluation function
def evaluate_credit(fuzzy_inputs, fuzzy_house, fuzzy_applicant):
    print("credit evaluation function")
    # House output sets
    fuzzy_house_very_low = np.fmin(fuzzy_house, house["very_low"])
    fuzzy_house_low = np.fmin(fuzzy_house, house["low"])
    fuzzy_house_medium = np.fmin(fuzzy_house, house["medium"])
    fuzzy_house_high = np.fmin(fuzzy_house, house["high"])
    fuzzy_house_very_high = np.fmin(fuzzy_house, house["very_high"])

    # Applicant output sets
    fuzzy_applicant_low = np.fmin(fuzzy_applicant, applicant["low"])
    fuzzy_applicant_medium = np.fmin(fuzzy_applicant, applicant["medium"])
    fuzzy_applicant_high = np.fmin(fuzzy_applicant, applicant["high"])

    # Rules
    # 1. IF (salary is low) AND (interest is medium) THEN (Credit is very low )
    credit_very_low1 = and_rule(fuzzy_inputs["salary"]["low"], fuzzy_inputs["interest"]["medium"], loan["very_low"])
    # 2. IF (salary is low) AND (interest is high) THEN (Credit is very low)
    credit_very_low2 = and_rule(fuzzy_inputs["salary"]["low"], fuzzy_inputs["interest"]["high"], loan["very_low"])
    # 3. IF (salary is medium) AND (interest is high) THEN (Credit is low)
    credit_low1 = and_rule(fuzzy_inputs["salary"]["medium"], fuzzy_inputs["interest"]["high"], loan["low"])
    # 4. IF (applicant is low) THEN (Credit is very low)
    credit_very_low3 = np.fmin(fuzzy_applicant_low, loan["very_low"])
    # 5. IF (house is very low) THEN (Credit is very low)
    credit_very_low4 = np.fmin(fuzzy_house_very_low, loan["very_low"])
    # 6. IF (applicant is medium) AND (house is very low) THEN (Credit is low )
    credit_low2 = and_rule(fuzzy_applicant_medium, fuzzy_house_very_low, loan["low"])
    # 7. IF (applicant is medium) AND (house is low) THEN (Credit is low)
    credit_low3 = and_rule(fuzzy_applicant_medium, fuzzy_house_low, loan["low"])
    # 8. IF (applicant is medium) AND (house is medium) THEN (Credit is medium)
    credit_medium1 = and_rule(fuzzy_applicant_medium, fuzzy_house_medium, loan["medium"])
    # 9. IF (applicant is medium) AND (house is high) THEN (Credit is high)
    credit_high1 = and_rule(fuzzy_applicant_medium, fuzzy_house_high, loan["high"])
    # 10. IF (applicant is medium) AND (house is very high) THEN (Credit is high )
    credit_high2 = and_rule(fuzzy_applicant_medium, fuzzy_house_very_high, loan["high"])
    # 11. IF (applicant is high) AND (house is very low) THEN (Credit is low)
    credit_low4 = and_rule(fuzzy_applicant_high, fuzzy_house_very_low, loan["low"])
    # 12. IF (applicant is high) AND (house is low) THEN (Credit is medium)
    credit_medium2 = and_rule(fuzzy_applicant_high, fuzzy_house_low, loan["medium"])
    # 13. IF (applicant is high) AND (house is medium) THEN (Credit is high)
    credit_high3 = and_rule(fuzzy_applicant_high, fuzzy_house_medium, loan["high"])
    # 14. IF (applicant is high) AND (house is high) THEN (Credit is high)
    credit_high4 = and_rule(fuzzy_applicant_high, fuzzy_house_high, loan["high"])
    # 15. IF (applicant is high) AND (house is very high) THEN (Credit is very high )
    credit_very_high = and_rule(fuzzy_applicant_high, fuzzy_house_very_high, loan["very_high"])

    # combine the Rules
    step = or_rule(credit_very_low1, credit_very_low2, credit_very_low3)
    credit_very_low = np.fmax(step, credit_very_low4)

    step = or_rule(credit_low1, credit_low2, credit_low3)
    credit_low = np.fmax(step, credit_low4)

    credit_medium = np.fmax(credit_medium1, credit_medium2)

    step = or_rule(credit_high1, credit_high2, credit_high3)
    credit_high = np.fmax(step, credit_high4)

    step = or_rule(credit_very_low, credit_low, credit_medium)
    credit = or_rule(step, credit_high, credit_very_high)

    return credit


# Convert fuzzy output to crisp output using CENTROID method
def defuzzify(fuzzy_credit, credit_range):
    # Calculate the numerator (weighted sum) and denominator (total weight)
    numerator = np.sum(credit_range * fuzzy_credit)
    denominator = np.sum(fuzzy_credit)

    # Avoid division by zero
    if denominator == 0:
        return 0

    # Calculate and return the centroid
    return numerator / denominator


def main():

    inputs = {
            "market_value": 150,
            "location": 3,
            "asset": 550,
            "salary": 45,
            "interest": 4}

    # 1.inputs will fuzzify here using fuzzify function
    fuzzified_inputs = fuzzify(inputs)
    print("fuzzified inputs", end="")
    print(fuzzified_inputs)
    print("end of fuzzify function")

    # 2.HOUSE rule evaluate and
    # 3.outputs of rule evaluation aggregate here
    fuzzy_house = evaluate_house(fuzzified_inputs)
    print("end of house evaluation")

    # 2.APPLİCANT rule evaluate and
    # 3.outputs of rule evaluation aggregate here
    fuzzy_applicant = evaluate_applicant(fuzzified_inputs)
    print("end of applicant evaluation")

    # 2.CREDİT rule evaluate and
    # 3.outputs of rule evaluation aggregate here
    fuzzy_credit = evaluate_credit(fuzzified_inputs, fuzzy_house, fuzzy_applicant)
    print("end of credit evaluation")

    # 4. Defuzzify credit output using centroid method
    crisp_result = defuzzify(fuzzy_credit, x_loan)
    print(f"Recommended Loan Amount: {crisp_result:.2f} 10^3 $")

    # visualization of outputs
    create_graphics(fuzzy_house, fuzzy_applicant, fuzzy_credit, crisp_result)


if __name__ == "__main__":
    main()
