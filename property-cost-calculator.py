#!/usr/bin/env python

def calculate_property_costs(property_price, years=35, interest_rate=0.01):
    """
    Calculate various costs related to property ownership and rental

    Args:
    property_price (float): Price of the property in yen
    years (int): Mortgage duration in years
    interest_rate (float): Annual interest rate as decimal (e.g., 0.01 for 1%)
    """
    # Calculate down payment (20% of property price)
    down_payment = property_price * 0.20

    # Calculate loan amount
    loan_amount = property_price - down_payment

    # Calculate monthly mortgage payments
    monthly_principal = loan_amount / (years * 12)
    monthly_interest = (loan_amount * interest_rate) / 12
    monthly_mortgage = monthly_principal + monthly_interest

    # Calculate additional monthly costs
    monthly_tax_insurance = (property_price * 0.015) / 12  # 1.5% annually
    monthly_maintenance = (property_price * 0.01) / 12     # 1% annually

    # Total monthly cost for owner
    total_monthly_cost = monthly_mortgage + monthly_tax_insurance + monthly_maintenance

    # Calculate 5% rule monthly amount for comparison
    five_percent_monthly = (property_price * 0.05) / 12

    return {
        'property_price': property_price,
        'down_payment': down_payment,
        'monthly_mortgage': monthly_mortgage,
        'monthly_tax_insurance': monthly_tax_insurance,
        'monthly_maintenance': monthly_maintenance,
        'total_monthly_cost': total_monthly_cost,
        'five_percent_monthly': five_percent_monthly
    }

def analyze_rental_percentage(monthly_income, owner_cost):
    """
    Analyze what percentage of owner's costs the rent would cover
    and provide recommendations
    """
    max_rent = monthly_income * 0.30  # 30% of monthly income
    percentage_of_cost = (max_rent / owner_cost) * 100

    if percentage_of_cost < 40:
        recommendation = "GOOD DEAL! You're paying less than 40% of owner's costs"
    elif percentage_of_cost < 50:
        recommendation = "OKAY DEAL - You're paying 40-50% of owner's costs"
    elif percentage_of_cost < 70:
        recommendation = "EXPENSIVE - You're paying 50-70% of owner's costs"
    else:
        recommendation = "VERY EXPENSIVE - Consider buying instead if possible"

    return {
        'max_rent': max_rent,
        'percentage_of_cost': percentage_of_cost,
        'recommendation': recommendation
    }

# Example usage
if __name__ == "__main__":
    # Example: Property in Ikebukuro
    property_price = 112_800_000  # ¥112.8M
    monthly_income = 800_000      # ¥800,000 monthly income

    # Calculate costs
    costs = calculate_property_costs(property_price)

    # Analyze rental situation
    analysis = analyze_rental_percentage(monthly_income, costs['total_monthly_cost'])

    # Print results
    print(f"Property Price: ¥{property_price:,}")
    print(f"\nOwner's Costs:")
    print(f"Down Payment: ¥{costs['down_payment']:,.0f}")
    print(f"Monthly Mortgage: ¥{costs['monthly_mortgage']:,.0f}")
    print(f"Monthly Tax/Insurance: ¥{costs['monthly_tax_insurance']:,.0f}")
    print(f"Monthly Maintenance: ¥{costs['monthly_maintenance']:,.0f}")
    print(f"Total Monthly Cost: ¥{costs['total_monthly_cost']:,.0f}")
    print(f"\n5% Rule Monthly Amount: ¥{costs['five_percent_monthly']:,.0f}")

    print(f"\nRental Analysis:")
    print(f"Your Max Rent (30% of income): ¥{analysis['max_rent']:,.0f}")
    print(f"This covers {analysis['percentage_of_cost']:.1f}% of owner's costs")
    print(f"Recommendation: {analysis['recommendation']}")
