#!/usr/bin/env python3
"""
Retirement Calculator - A comprehensive tool for retirement planning

This program helps users calculate retirement savings, investment growth,
and determine how much they need to save to meet their retirement goals.
"""

import argparse
import sys
from datetime import datetime
from typing import Dict, Optional


class RetirementCalculator:
    """Main retirement calculator class with various calculation methods."""
    
    def __init__(self, current_age: int, retirement_age: int, 
                 current_savings: float, annual_contribution: float,
                 expected_return: float, annual_expenses: float = 0):
        """
        Initialize the retirement calculator.
        
        Args:
            current_age: Current age in years
            retirement_age: Desired retirement age
            current_savings: Current retirement savings balance
            annual_contribution: Annual contribution amount
            expected_return: Expected annual return rate (as decimal, e.g., 0.07 for 7%)
            annual_expenses: Expected annual expenses in retirement
        """
        self.current_age = current_age
        self.retirement_age = retirement_age
        self.current_savings = current_savings
        self.annual_contribution = annual_contribution
        self.expected_return = expected_return
        self.annual_expenses = annual_expenses
        
        # Validate inputs
        self._validate_inputs()
    
    def _validate_inputs(self):
        """Validate input parameters."""
        if self.current_age < 0 or self.current_age > 120:
            raise ValueError("Current age must be between 0 and 120")
        
        if self.retirement_age <= self.current_age:
            raise ValueError("Retirement age must be greater than current age")
        
        if self.current_savings < 0:
            raise ValueError("Current savings cannot be negative")
        
        if self.annual_contribution < 0:
            raise ValueError("Annual contribution cannot be negative")
        
        if self.expected_return < -1 or self.expected_return > 1:
            raise ValueError("Expected return must be between -100% and 100%")
    
    def calculate_future_value(self) -> Dict[str, float]:
        """
        Calculate the future value of retirement savings.
        
        Returns:
            Dictionary containing calculation results
        """
        years_until_retirement = self.retirement_age - self.current_age
        
        # Calculate future value with compound interest
        # FV = PV * (1 + r)^n + PMT * [((1 + r)^n - 1) / r]
        
        # Future value of current savings
        fv_current = self.current_savings * ((1 + self.expected_return) ** years_until_retirement)
        
        # Future value of annual contributions
        if self.expected_return != 0:
            fv_contributions = self.annual_contribution * (
                ((1 + self.expected_return) ** years_until_retirement - 1) / self.expected_return
            )
        else:
            # If return is 0%, simple multiplication
            fv_contributions = self.annual_contribution * years_until_retirement
        
        total_future_value = fv_current + fv_contributions
        total_contributions = self.annual_contribution * years_until_retirement
        investment_gains = total_future_value - self.current_savings - total_contributions
        
        return {
            'years_until_retirement': years_until_retirement,
            'future_value': total_future_value,
            'total_contributions': total_contributions,
            'investment_gains': investment_gains,
            'current_savings': self.current_savings
        }
    
    def calculate_required_savings(self, target_amount: float) -> float:
        """
        Calculate required annual contribution to reach target amount.
        
        Args:
            target_amount: Target retirement savings goal
            
        Returns:
            Required annual contribution amount
        """
        years_until_retirement = self.retirement_age - self.current_age
        
        # Calculate future value of current savings
        fv_current = self.current_savings * ((1 + self.expected_return) ** years_until_retirement)
        
        # Amount needed from contributions
        needed_from_contributions = target_amount - fv_current
        
        if needed_from_contributions <= 0:
            return 0.0
        
        # Calculate required annual contribution
        # PMT = (FV * r) / ((1 + r)^n - 1)
        if self.expected_return != 0:
            required_contribution = (needed_from_contributions * self.expected_return) / (
                (1 + self.expected_return) ** years_until_retirement - 1
            )
        else:
            required_contribution = needed_from_contributions / years_until_retirement
        
        return required_contribution
    
    def calculate_retirement_duration(self, withdrawal_rate: float = 0.04) -> float:
        """
        Calculate how long retirement savings will last.
        
        Args:
            withdrawal_rate: Annual withdrawal rate (default 4% rule)
            
        Returns:
            Number of years savings will last
        """
        results = self.calculate_future_value()
        total_savings = results['future_value']
        
        if self.annual_expenses <= 0:
            # Use withdrawal rate if no expenses specified
            annual_withdrawal = total_savings * withdrawal_rate
        else:
            annual_withdrawal = self.annual_expenses
        
        if annual_withdrawal <= 0:
            return float('inf')
        
        # Calculate years with continued growth during retirement
        # Assuming 3% inflation-adjusted return during retirement
        retirement_return = 0.03
        
        years = 0
        remaining_balance = total_savings
        
        while remaining_balance > 0 and years < 100:
            remaining_balance = remaining_balance * (1 + retirement_return) - annual_withdrawal
            years += 1
        
        return years
    
    def generate_projection_table(self, intervals: int = 10) -> list:
        """
        Generate year-by-year projection table.
        
        Args:
            intervals: Number of year intervals to show (default 10)
            
        Returns:
            List of dictionaries containing yearly projections
        """
        years_until_retirement = self.retirement_age - self.current_age
        projection = []
        
        balance = self.current_savings
        total_contributed = 0
        
        step = max(1, years_until_retirement // intervals)
        
        for year in range(0, years_until_retirement + 1, step):
            if year > 0:
                # Calculate balance for this year
                balance = self.current_savings
                for y in range(year):
                    balance = balance * (1 + self.expected_return) + self.annual_contribution
                total_contributed = self.annual_contribution * year
            
            projection.append({
                'year': self.current_age + year,
                'age': self.current_age + year,
                'balance': balance,
                'contributed': total_contributed,
                'gains': balance - self.current_savings - total_contributed
            })
        
        return projection


def format_currency(amount: float) -> str:
    """Format amount as currency."""
    return f"${amount:,.2f}"


def print_results(calculator: RetirementCalculator):
    """Print calculation results in a formatted manner."""
    print("\n" + "="*60)
    print("RETIREMENT CALCULATION RESULTS")
    print("="*60)
    
    # Basic information
    print(f"\nCurrent Age: {calculator.current_age}")
    print(f"Retirement Age: {calculator.retirement_age}")
    print(f"Current Savings: {format_currency(calculator.current_savings)}")
    print(f"Annual Contribution: {format_currency(calculator.annual_contribution)}")
    print(f"Expected Return Rate: {calculator.expected_return * 100:.2f}%")
    
    # Future value calculation
    results = calculator.calculate_future_value()
    print("\n" + "-"*60)
    print("RETIREMENT SAVINGS PROJECTION")
    print("-"*60)
    print(f"Years Until Retirement: {results['years_until_retirement']}")
    print(f"Total Future Value: {format_currency(results['future_value'])}")
    print(f"Total Contributions: {format_currency(results['total_contributions'])}")
    print(f"Investment Gains: {format_currency(results['investment_gains'])}")
    
    # Retirement duration
    duration = calculator.calculate_retirement_duration()
    print("\n" + "-"*60)
    print("RETIREMENT DURATION (4% withdrawal rule)")
    print("-"*60)
    if duration == float('inf'):
        print("Savings will last indefinitely")
    else:
        print(f"Savings will last approximately {duration:.0f} years")
    
    # Projection table
    print("\n" + "-"*60)
    print("SAVINGS PROJECTION BY AGE")
    print("-"*60)
    print(f"{'Age':<10} {'Balance':<20} {'Contributed':<20} {'Gains':<20}")
    print("-"*60)
    
    projections = calculator.generate_projection_table(intervals=5)
    for proj in projections:
        print(f"{proj['age']:<10} {format_currency(proj['balance']):<20} "
              f"{format_currency(proj['contributed']):<20} {format_currency(proj['gains']):<20}")
    
    print("="*60 + "\n")


def main():
    """Main entry point for the retirement calculator."""
    parser = argparse.ArgumentParser(
        description="Retirement Calculator - Plan your financial future",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python retirement_calculator.py --current-age 30 --retirement-age 65 --current-savings 50000 --annual-contribution 10000 --expected-return 0.07
  python retirement_calculator.py -ca 40 -ra 67 -cs 100000 -ac 15000 -er 0.06 --annual-expenses 60000
        """
    )
    
    parser.add_argument('--current-age', '-ca', type=int, required=True,
                        help='Current age in years')
    parser.add_argument('--retirement-age', '-ra', type=int, required=True,
                        help='Desired retirement age')
    parser.add_argument('--current-savings', '-cs', type=float, required=True,
                        help='Current retirement savings balance')
    parser.add_argument('--annual-contribution', '-ac', type=float, required=True,
                        help='Annual contribution amount')
    parser.add_argument('--expected-return', '-er', type=float, required=True,
                        help='Expected annual return rate (as decimal, e.g., 0.07 for 7%%)')
    parser.add_argument('--annual-expenses', '-ae', type=float, default=0,
                        help='Expected annual expenses in retirement (optional)')
    parser.add_argument('--target-amount', '-ta', type=float,
                        help='Calculate required contribution for target amount')
    
    args = parser.parse_args()
    
    try:
        calculator = RetirementCalculator(
            current_age=args.current_age,
            retirement_age=args.retirement_age,
            current_savings=args.current_savings,
            annual_contribution=args.annual_contribution,
            expected_return=args.expected_return,
            annual_expenses=args.annual_expenses
        )
        
        if args.target_amount:
            required = calculator.calculate_required_savings(args.target_amount)
            print(f"\nTo reach {format_currency(args.target_amount)}, "
                  f"you need to contribute {format_currency(required)} annually.\n")
        else:
            print_results(calculator)
        
        return 0
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
