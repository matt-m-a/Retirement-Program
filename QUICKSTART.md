# Quick Start Guide

## Installation
No installation needed! Just Python 3.6+ required.

## Your First Calculation

Run this command with your own numbers:

```bash
python retirement_calculator.py \
  --current-age YOUR_AGE \
  --retirement-age DESIRED_RETIREMENT_AGE \
  --current-savings CURRENT_BALANCE \
  --annual-contribution YEARLY_AMOUNT \
  --expected-return 0.07
```

## Example

If you're 30 years old with $50,000 saved, planning to retire at 65, and contributing $10,000 per year:

```bash
python retirement_calculator.py -ca 30 -ra 65 -cs 50000 -ac 10000 -er 0.07
```

## Try the Examples

See realistic scenarios:

```bash
python examples.py
```

## Find Your Target

Want to know how much to save for a $2 million goal?

```bash
python retirement_calculator.py -ca 30 -ra 65 -cs 50000 -ac 10000 -er 0.07 -ta 2000000
```

## Expected Return Rates

Choose based on your investment strategy:
- **0.04** (4%): Very conservative (mostly bonds)
- **0.06** (6%): Moderate conservative
- **0.07** (7%): Balanced (60/40 stocks/bonds)
- **0.08** (8%): Moderate aggressive
- **0.10** (10%): Aggressive (mostly stocks)

## Need Help?

```bash
python retirement_calculator.py --help
```

See full documentation in [README.md](README.md)
