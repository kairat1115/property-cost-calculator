#!/usr/bin/env python

# 35 years is maximum in Japan
# average is likely about 25 years
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
        recommendation = "GOOD DEAL! You're paying less than [0,40)% of owner's costs"
    elif percentage_of_cost < 50:
        recommendation = "OKAY DEAL - You're paying [40,50)% of owner's costs"
    elif percentage_of_cost < 70:
        recommendation = "EXPENSIVE - You're paying [50-70)% of owner's costs"
    else:
        recommendation = "VERY EXPENSIVE - Consider buying instead if possible"

    return {
        'max_rent': max_rent,
        'percentage_of_cost': percentage_of_cost,
        'recommendation': recommendation
    }

# ｘｘｘｘ    ｘｘｘｘ  ｘｘｘｘ円
# 億ｘｘｘ    万ｘｘｘ  千ｘｘｘ円

# price per sqm based on agency price / 40 sqm(?)
# price_per_sqm = 162_5000

# online aot/condo in toshima-ku
# price_per_sqm = 92_8000

# real apartment / 40
# price_per_sqm = 237_2500

# suumo price per tatami (万円／平)
# price_per_tatami = 400_0000

# nomu.com - ブリリアタワー池袋
# ２億７８００万円 - 3ldk / 78.06sqm / 35floor
# price_per_sqm = 2_7800_0000 / 78.06
# ９４９０万円 - 1ldk / 37.51sqm / 9floor
# price_per_sqm = 9490_0000 / 37.51
# １億２８８０万円 - 2ldk / 64.14sqm / 5floor
# price_per_sqm = 1_2880_0000 / 64.14
# ９６８０万円 - 1ldk / 45.41sqm / 11f
# price_per_sqm = 9680_0000 / 45.41
# per tatami (平単価) - ６９８万円
# price_per_tatami = 698_0000

# athome - シティハウス西池部
# １２０００万円 - 3ldk / 6476 / 5floor
# price_per_sqm = 1_2000_0000 / 64.76

# price_per_sqm = price_per_tatami / 3.306

# usual price 40sqm (rental agency said)
# property_price = 6500_0000
# property_price = price_per_sqm * 40

# usual price 35sqm(?)
# property_price = 5687_5000

# property_price = price_per_sqm * 35
# usual price 30sqm(?)

# property_price = price_per_sqm * 30
# 1ldk / 45.41sqm / 11f
# property_price = 9490_0000

if __name__ == "__main__":
    price_per_sqm = 1_2000_0000 / 64.76

    property_price = price_per_sqm * 30

    # net income (after taxes)
    monthly_income = 40_0000

    # Calculate costs
    costs = calculate_property_costs(property_price)

    # Analyze rental situation
    analysis = analyze_rental_percentage(monthly_income, costs['total_monthly_cost'])

    # Print results
    print(f"Price per sqm: ¥{price_per_sqm:,.0f}")
    print(f"Property Price: ¥{property_price:,}")
    print(f"\nOwner's Costs:")
    print(f"Down Payment: ¥{costs['down_payment']:,.0f}")
    print(f"Monthly Mortgage: ¥{costs['monthly_mortgage']:,.0f}")
    print(f"Monthly Tax/Insurance: ¥{costs['monthly_tax_insurance']:,.0f}")
    print(f"Monthly Maintenance: ¥{costs['monthly_maintenance']:,.0f}")
    print(f"Total Monthly Cost: ¥{costs['total_monthly_cost']:,.0f}")
    print(f"\n5% Rule Monthly Amount: ¥{costs['five_percent_monthly']:,.0f}")

    print(f"\nRental Analysis:")
    print(f"50% Monthly of owner's costs: ¥{costs['total_monthly_cost'] * 0.50:,.0f}")
    print(f"Your Max Rent (30% of income): ¥{analysis['max_rent']:,.0f}")
    print(f"This covers {analysis['percentage_of_cost']:.1f}% of owner's costs")
    print(f"Recommendation: {analysis['recommendation']}")
