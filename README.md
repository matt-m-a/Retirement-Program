# Retirement Calculator

A comprehensive Python-based retirement planning calculator that helps you project your retirement savings, calculate investment growth, and determine how much you need to save to meet your retirement goals.

## Features

- **Future Value Calculations**: Calculate how much your retirement savings will grow over time with compound interest
- **Required Savings Calculator**: Determine how much you need to save annually to reach your retirement goal
- **Retirement Duration Estimator**: Estimate how long your savings will last in retirement
- **Projection Tables**: View year-by-year breakdown of your savings growth
- **Flexible Parameters**: Customize age, contribution amounts, expected returns, and more
- **Input Validation**: Comprehensive error checking to ensure valid calculations
- **CLI Interface**: Easy-to-use command-line interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/matt-m-a/Retirement-Program.git
cd Retirement-Program
```

2. No external dependencies required! The calculator uses only Python's standard library.

## Quick Start

See [QUICKSTART.md](QUICKSTART.md) for a quick introduction, or try the example scenarios:

```bash
python examples.py
```

## Usage

### Basic Usage

Run the calculator with your parameters:

```bash
python retirement_calculator.py \
  --current-age 30 \
  --retirement-age 65 \
  --current-savings 50000 \
  --annual-contribution 10000 \
  --expected-return 0.07
```

### Short Options

Use abbreviated flags for convenience:

```bash
python retirement_calculator.py -ca 30 -ra 65 -cs 50000 -ac 10000 -er 0.07
```

### With Annual Expenses

Include expected retirement expenses:

```bash
python retirement_calculator.py \
  --current-age 40 \
  --retirement-age 67 \
  --current-savings 100000 \
  --annual-contribution 15000 \
  --expected-return 0.06 \
  --annual-expenses 60000
```

### Calculate Required Contribution

Find out how much you need to save to reach a target amount:

```bash
python retirement_calculator.py \
  --current-age 35 \
  --retirement-age 65 \
  --current-savings 75000 \
  --annual-contribution 12000 \
  --expected-return 0.07 \
  --target-amount 2000000
```

## Parameters

| Parameter | Short | Description | Required |
|-----------|-------|-------------|----------|
| `--current-age` | `-ca` | Your current age in years | Yes |
| `--retirement-age` | `-ra` | Your desired retirement age | Yes |
| `--current-savings` | `-cs` | Current retirement account balance | Yes |
| `--annual-contribution` | `-ac` | Amount you contribute per year | Yes |
| `--expected-return` | `-er` | Expected annual return rate (as decimal, e.g., 0.07 for 7%) | Yes |
| `--annual-expenses` | `-ae` | Expected annual expenses in retirement | No |
| `--target-amount` | `-ta` | Calculate required contribution for this target | No |

## Output

The calculator provides detailed output including:

1. **Input Summary**: Confirms your parameters
2. **Savings Projection**: Shows total future value, contributions, and investment gains
3. **Retirement Duration**: Estimates how long your money will last (using 4% withdrawal rule)
4. **Age-Based Projections**: Table showing your savings at different ages

Example output:
```
============================================================
RETIREMENT CALCULATION RESULTS
============================================================

Current Age: 30
Retirement Age: 65
Current Savings: $50,000.00
Annual Contribution: $10,000.00
Expected Return Rate: 7.00%

------------------------------------------------------------
RETIREMENT SAVINGS PROJECTION
------------------------------------------------------------
Years Until Retirement: 35
Total Future Value: $1,790,856.07
Total Contributions: $350,000.00
Investment Gains: $1,390,856.07

------------------------------------------------------------
RETIREMENT DURATION (4% withdrawal rule)
------------------------------------------------------------
Savings will last approximately 45 years

------------------------------------------------------------
SAVINGS PROJECTION BY AGE
------------------------------------------------------------
Age        Balance              Contributed          Gains               
------------------------------------------------------------
30         $50,000.00           $0.00                $0.00               
37         $158,862.70          $70,000.00           $38,862.70          
44         $322,703.32          $140,000.00          $132,703.32         
51         $561,192.73          $210,000.00          $301,192.73         
58         $900,464.13          $280,000.00          $570,464.13         
65         $1,790,856.07        $350,000.00          $1,390,856.07       
============================================================
```

## Running Tests

Run the comprehensive test suite:

```bash
python test_retirement_calculator.py
```

Run tests with verbose output:

```bash
python test_retirement_calculator.py -v
```

The test suite includes:
- Input validation tests
- Calculation accuracy tests
- Edge case handling
- Boundary condition tests

## How It Works

### Future Value Calculation

The calculator uses the compound interest formula with regular contributions:

```
FV = PV × (1 + r)^n + PMT × [((1 + r)^n - 1) / r]
```

Where:
- FV = Future Value
- PV = Present Value (current savings)
- r = Expected annual return rate
- n = Number of years until retirement
- PMT = Annual contribution

### Retirement Duration

The calculator estimates retirement duration by:
1. Calculating total savings at retirement
2. Applying annual withdrawals (4% rule or specified expenses)
3. Continuing to grow remaining balance at 3% (inflation-adjusted)
4. Counting years until balance is depleted

### 4% Rule

The 4% rule suggests withdrawing 4% of your retirement savings annually, adjusted for inflation. This historically provides a high probability of not outliving your savings over a 30-year retirement.

## Configuration File

You can create a `config.json` file for your personal settings:

```json
{
  "current_age": 30,
  "retirement_age": 65,
  "current_savings": 50000,
  "annual_contribution": 10000,
  "expected_return": 0.07,
  "annual_expenses": 50000
}
```

See `config.example.json` for a template.

## Examples

### Conservative Investor
```bash
python retirement_calculator.py -ca 25 -ra 65 -cs 10000 -ac 8000 -er 0.05
```
5% return represents conservative portfolio (bonds, stable investments)

### Moderate Investor
```bash
python retirement_calculator.py -ca 30 -ra 65 -cs 50000 -ac 12000 -er 0.07
```
7% return represents balanced portfolio (60/40 stocks/bonds)

### Aggressive Investor
```bash
python retirement_calculator.py -ca 25 -ra 65 -cs 20000 -ac 15000 -er 0.10
```
10% return represents aggressive portfolio (mostly stocks)

## Tips for Retirement Planning

1. **Start Early**: The power of compound interest means starting early makes a huge difference
2. **Be Consistent**: Regular contributions are key to building wealth
3. **Be Realistic**: Use conservative return estimates (6-7% for balanced portfolios)
4. **Factor Inflation**: Real returns after inflation are typically 3-4% lower than nominal returns
5. **Diversify**: Don't put all eggs in one basket
6. **Review Regularly**: Update your plan annually or when life circumstances change
7. **Consider Fees**: Investment fees can significantly impact long-term returns

## Important Disclaimers

- This calculator is for educational and planning purposes only
- Past performance does not guarantee future results
- Actual returns will vary and may be negative in some years
- Consult with a qualified financial advisor for personalized advice
- Tax implications are not included in these calculations
- Inflation effects are simplified in this model

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is open source and available for personal and educational use.

## Author

Created for retirement planning and financial education purposes.