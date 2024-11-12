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

# https://porty.co.jp/assess/
class RentApartment:
    def __init__(self, sqm_size, floor, minutes_to_station, years):
        self.sqm_size = sqm_size
        self.floor = floor
        self.minutes_to_station = minutes_to_station
        self.years = years

    def get_area_price(self, sqm_size=None):
        # 1min, 40m2, 0years, 1floor: 163,990
        # 1min, 41m2, 0years, 1floor: 166,706
        # 1min, 42m2, 0years, 1floor: 169,423
        # 1min, 43m2, 0years, 1floor: 172,140
        # 1min, 44m2, 0years, 1floor: 174,856
        # 1min, 45m2, 0years, 1floor: 177,573
        # 1min, 46m2, 0years, 1floor: 180,289
        # ~2017 yen per sqm
        if sqm_size != None:
            s = sqm_size
        else:
            s = self.sqm_size
        return s * 2017

    def get_floor_price(self):
        # 1min, 40m2, 0years, 1floor: 163,990
        # no one likes first floor, so its different
        # 1min, 40m2, 0years, 2floor: 167,337
        # 1min, 40m2, 0years, 3floor: 169,010
        # 1min, 40m2, 0years, 4floor: 170,683
        # 1min, 40m2, 0years, 5floor: 172,357
        # 1min, 40m2, 0years, 10floor: 180,723
        # 1min, 40m2, 0years, 15floor: 186,580
        # ~1670 yen diff per floor
        if self.floor < 2:
            return 0
        return (self.floor - 1) * 1670

    def get_station_distance_price(self):
        # 1min, 40m2, 0years, 1floor: 163,990
        # 2min, 40m2, 0years, 1floor: 162,981
        # 3min, 40m2, 0years, 1floor: 161,972
        # 4min, 40m2, 0years, 1floor: 160,963
        # 5min, 40m2, 0years, 1floor: 159,955
        # 10min, 40m2, 0years, 1floor: 154,911
        # 15min, 40m2, 0years, 1floor: 149,867
        # ~1010 yen diff per minute
        # 20min, 40m2, 0years, 1floor: 149,816
        # after ~10yen diff per minute
        if self.minutes_to_station < 16:
            return self.minutes_to_station * 1010
        return (self.minutes_to_station - 15) * 10

    def get_years_price(self):
        # 1min, 40m2, 0years, 1floor: 163,990
        # 1min, 40m2, 1years, 1floor: 163,127
        # 1min, 40m2, 2years, 1floor: 162,265
        # 1min, 40m2, 3years, 1floor: 161,402
        # 1min, 40m2, 4years, 1floor: 160,540
        # 1min, 40m2, 5years, 1floor: 159,677
        # 1min, 40m2, 10years, 1floor: 155,365
        # ~850 yen per year
        return self.years * 850

    def get_price(self):
        # 1min, 40m2, 0years, 1floor: 163,990
        # -40sqm price to get base
        base = 16_3990 - self.get_area_price(40)
        return base + self.get_area_price() + \
            self.get_floor_price() - \
            self.get_station_distance_price() - \
            self.get_years_price()


if __name__ == "__main__":
    apartment = RentApartment(
        sqm_size = 30,
        floor = 5,
        minutes_to_station = 15,
        years = 10
    )

    property_price = apartment.get_price()

    # gross income (before taxes)
    monthly_income = 40_0000
    # https://www.reddit.com/r/personalfinance/wiki/housing/renting/
    # basic recommendation to spend 30% net income on rent
    # also can apply 50%, 30%, 20% formula to net income
    # 50% - rent/utilities/groceries/small debt
    # 30% - entertainment
    # 20% - savings/debt
    # usual deductions for 50%
    # ４－６万 - groceries
    # １－２万 - utilities
    # rest - rent

    # Calculate costs
    # costs = calculate_property_costs(property_price)

    # Analyze rental situation
    # analysis = analyze_rental_percentage(monthly_income, costs['total_monthly_cost'])
    analysis = analyze_rental_percentage(monthly_income, property_price)

    # Print results
    # print(f"Price per sqm: ¥{price_per_sqm:,.0f}")
    print(f"Property Price: ¥{property_price:,}")
    # print(f"\nOwner's Costs:")
    # print(f"Down Payment: ¥{costs['down_payment']:,.0f}")
    # print(f"Monthly Mortgage: ¥{costs['monthly_mortgage']:,.0f}")
    # print(f"Monthly Tax/Insurance: ¥{costs['monthly_tax_insurance']:,.0f}")
    # print(f"Monthly Maintenance: ¥{costs['monthly_maintenance']:,.0f}")
    # print(f"Total Monthly Cost: ¥{costs['total_monthly_cost']:,.0f}")
    # print(f"\n5% Rule Monthly Amount: ¥{costs['five_percent_monthly']:,.0f}")

    # print(f"\nRental Analysis:")
    # print(f"50% Monthly of owner's costs: ¥{costs['total_monthly_cost'] * 0.50:,.0f}")
    print(f"Your Max Rent (30% of income): ¥{analysis['max_rent']:,.0f}")
    # print(f"This covers {analysis['percentage_of_cost']:.1f}% of owner's costs")
    # print(f"Recommendation: {analysis['recommendation']}")
