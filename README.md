Script that calculates monthly rent. Consider using to to make buy/rent decision

# Run
```sh
python property-cost-calculator.py
```

# Recommendation
| Percentage cost | Deal or not | Recommendation |
| --- | --- | --- |
| < 40% | GOOD DEAL! | You're paying less than 40% of owner's costs |
| < 50% | OKAY DEAL | You're paying 40-50% of owner's costs |
| < 70% | EXPENSIVE | You're paying 50-70% of owner's costs |
| > 70% | VERY EXPENSIVE | Consider buying instead if possible |

# Output
```
Price per sqm: ¥1,852,996
Property Price: ¥55,589,870.29030265

Owner's Costs:
Down Payment: ¥11,117,974
Monthly Mortgage: ¥142,945
Monthly Tax/Insurance: ¥69,487
Monthly Maintenance: ¥46,325
Total Monthly Cost: ¥258,758

5% Rule Monthly Amount: ¥231,624

Rental Analysis:
50% Monthly of owner's costs: ¥129,379
Your Max Rent (30% of income): ¥120,000
This covers 46.4% of owner's costs
Recommendation: OKAY DEAL - You're paying [40,50)% of owner's costs
```
