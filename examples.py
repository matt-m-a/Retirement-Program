#!/usr/bin/env python3
"""
Example usage scenarios for the Retirement Calculator

This script demonstrates various use cases and scenarios
for retirement planning calculations.
"""

from retirement_calculator import RetirementCalculator, format_currency, print_results


def example_young_professional():
    """Example: Young professional just starting to save."""
    print("\n" + "="*60)
    print("EXAMPLE 1: Young Professional (Age 25)")
    print("="*60)
    print("Scenario: Just started career, modest savings")
    
    calc = RetirementCalculator(
        current_age=25,
        retirement_age=65,
        current_savings=5000,
        annual_contribution=6000,
        expected_return=0.08  # Higher risk tolerance
    )
    print_results(calc)


def example_mid_career():
    """Example: Mid-career professional with established savings."""
    print("\n" + "="*60)
    print("EXAMPLE 2: Mid-Career Professional (Age 40)")
    print("="*60)
    print("Scenario: Established career, significant savings")
    
    calc = RetirementCalculator(
        current_age=40,
        retirement_age=67,
        current_savings=150000,
        annual_contribution=20000,
        expected_return=0.07,
        annual_expenses=70000
    )
    print_results(calc)


def example_late_starter():
    """Example: Late starter trying to catch up."""
    print("\n" + "="*60)
    print("EXAMPLE 3: Late Starter (Age 50)")
    print("="*60)
    print("Scenario: Starting late, needs aggressive savings")
    
    calc = RetirementCalculator(
        current_age=50,
        retirement_age=70,
        current_savings=75000,
        annual_contribution=30000,
        expected_return=0.06
    )
    print_results(calc)
    
    # Calculate what's needed to reach $1.5M
    target = 1500000
    required = calc.calculate_required_savings(target)
    print(f"\nTo reach {format_currency(target)}, need to contribute: {format_currency(required)}/year")


def example_conservative_investor():
    """Example: Conservative investor with lower returns."""
    print("\n" + "="*60)
    print("EXAMPLE 4: Conservative Investor (Age 35)")
    print("="*60)
    print("Scenario: Low risk tolerance, bond-heavy portfolio")
    
    calc = RetirementCalculator(
        current_age=35,
        retirement_age=65,
        current_savings=80000,
        annual_contribution=12000,
        expected_return=0.04  # Conservative 4% return
    )
    print_results(calc)


def main():
    """Run all example scenarios."""
    print("\n" + "#"*60)
    print("# RETIREMENT CALCULATOR - EXAMPLE SCENARIOS")
    print("#"*60)
    print("\nThese examples demonstrate different retirement planning scenarios.")
    print("Adjust the parameters to match your personal situation.\n")
    
    examples = [
        example_young_professional,
        example_mid_career,
        example_late_starter,
        example_conservative_investor
    ]
    
    for i, example in enumerate(examples, 1):
        try:
            example()
            if i < len(examples):
                input("\n>>> Press Enter to continue to next example...")
        except Exception as e:
            print(f"Error in example {i}: {e}")
    
    print("\n" + "#"*60)
    print("# END OF EXAMPLES")
    print("#"*60)
    print("\nRun your own calculation with:")
    print("python retirement_calculator.py --help")
    print("\n")


if __name__ == "__main__":
    main()
