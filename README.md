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
Property Price: ¥112,800,000

Owner's Costs:
Down Payment: ¥22,560,000
Monthly Mortgage: ¥290,057
Monthly Tax/Insurance: ¥141,000
Monthly Maintenance: ¥94,000
Total Monthly Cost: ¥525,057

5% Rule Monthly Amount: ¥470,000

Rental Analysis:
Your Max Rent (30% of income): ¥240,000
This covers 45.7% of owner's costs
Recommendation: OKAY DEAL - You're paying 40-50% of owner's costs
```
