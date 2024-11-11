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

# ｘ    ｘｘｘｘ  ｘｘｘｘ円
# 億    ｘｘｘ万  千ｘｘｘ円


# suumo price per tatami (万円／平)
# price_per_tatami = 400_0000
# per tatami (平単価) - ６９８万円
# price_per_tatami = 698_0000
# price_per_sqm = price_per_tatami / 3.306

class Apartment:
    def __init__(self, sqm_size, floor, minutes_to_station, years):
        self.sqm_size = sqm_size
        self.floor = floor
        self.minutes_to_station = minutes_to_station
        self.years = years

    def get_price_per_sqm(self):
        # Take average between ranges
        # Within 5 minutes to station: ¥800,000 - ¥950,000 per sqm
        if self.minutes_to_station < 6:
            return 87_5000
        # Within 10 minutes to station: ¥700,000 - ¥850,000 per sqm
        if self.minutes_to_station < 11:
            return 77_5000
        # Within 15 minutes to station: ¥600,000 - ¥750,000 per sqm
        if self.minutes_to_station < 16:
            return 67_5000
        # Within 20 minutes to station: ¥500,000 - ¥650,000 per sqm
        if self.minutes_to_station < 21:
            return 57_5000
        return 0

    def _get_floor_coef(self, floor):
        # Take average between ranges
        # 1st floor: Base price
        if floor < 2:
            return 1.0
        # 5th floor: +5-10% premium
        if floor < 6:
            return self._get_floor_coef(floor - 1) + 0.05
        # 10th floor: +10-15% premium
        if floor < 11:
            return self._get_floor_coef(floor - 1) + 0.125
        # 15th floor: +15-20% premium
        if floor < 16:
            return self._get_floor_coef(floor - 1) + 0.175
        # 20th+ floor: +20-25% premium
        return self._get_floor_coef(floor - 1) + 0.225

    def get_coef_for_floor(self):
        return self._get_floor_coef(self.floor)

    def _get_years_coef(self, years):
        # Base coeficient
        if years < 1:
            return 1.0
        # Years 1-5: 2% decrease per year
        if years < 6:
            return self._get_years_coef(years - 1) - 0.02
        # Years 6-10: 3% decrease per year
        if years < 11:
            return self._get_years_coef(years - 1) - 0.03
        # Years 11-15: 4% decrease per year
        if years < 16:
            return self._get_years_coef(years - 1) - 0.04
        # 16+ years: 5% decrease per year
        return self._get_years_coef(years - 1) - 0.05

    def get_coef_for_years(self):
        return self._get_years_coef(self.years)

    def get_price(self):
        return (self.get_price_per_sqm() * self.sqm_size) * \
            self.get_coef_for_floor() * self.get_coef_for_years()


if __name__ == "__main__":
    apartment = Apartment(
        sqm_size = 40,
        floor = 2,
        minutes_to_station = 15,
        years = 2
    )

    property_price = apartment.get_price()

    # net income (after taxes)
    monthly_income = 40_0000

    # Calculate costs
    costs = calculate_property_costs(property_price)

    # Analyze rental situation
    analysis = analyze_rental_percentage(monthly_income, costs['total_monthly_cost'])

    # Print results
    # print(f"Price per sqm: ¥{price_per_sqm:,.0f}")
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
