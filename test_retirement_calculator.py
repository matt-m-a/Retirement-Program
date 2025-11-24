#!/usr/bin/env python3
"""
Unit tests for the Retirement Calculator
"""

import unittest
import sys
from io import StringIO
from retirement_calculator import RetirementCalculator, format_currency


class TestRetirementCalculator(unittest.TestCase):
    """Test cases for RetirementCalculator class."""
    
    def test_initialization_valid(self):
        """Test calculator initialization with valid inputs."""
        calc = RetirementCalculator(
            current_age=30,
            retirement_age=65,
            current_savings=50000,
            annual_contribution=10000,
            expected_return=0.07
        )
        self.assertEqual(calc.current_age, 30)
        self.assertEqual(calc.retirement_age, 65)
        self.assertEqual(calc.current_savings, 50000)
        self.assertEqual(calc.annual_contribution, 10000)
        self.assertEqual(calc.expected_return, 0.07)
    
    def test_invalid_age_range(self):
        """Test validation for invalid age ranges."""
        with self.assertRaises(ValueError):
            RetirementCalculator(
                current_age=-5,
                retirement_age=65,
                current_savings=50000,
                annual_contribution=10000,
                expected_return=0.07
            )
        
        with self.assertRaises(ValueError):
            RetirementCalculator(
                current_age=150,
                retirement_age=65,
                current_savings=50000,
                annual_contribution=10000,
                expected_return=0.07
            )
    
    def test_retirement_age_before_current_age(self):
        """Test validation for retirement age before current age."""
        with self.assertRaises(ValueError):
            RetirementCalculator(
                current_age=65,
                retirement_age=30,
                current_savings=50000,
                annual_contribution=10000,
                expected_return=0.07
            )
    
    def test_negative_savings(self):
        """Test validation for negative savings."""
        with self.assertRaises(ValueError):
            RetirementCalculator(
                current_age=30,
                retirement_age=65,
                current_savings=-10000,
                annual_contribution=10000,
                expected_return=0.07
            )
    
    def test_negative_contribution(self):
        """Test validation for negative contribution."""
        with self.assertRaises(ValueError):
            RetirementCalculator(
                current_age=30,
                retirement_age=65,
                current_savings=50000,
                annual_contribution=-5000,
                expected_return=0.07
            )
    
    def test_invalid_return_rate(self):
        """Test validation for invalid return rates."""
        with self.assertRaises(ValueError):
            RetirementCalculator(
                current_age=30,
                retirement_age=65,
                current_savings=50000,
                annual_contribution=10000,
                expected_return=1.5
            )
        
        with self.assertRaises(ValueError):
            RetirementCalculator(
                current_age=30,
                retirement_age=65,
                current_savings=50000,
                annual_contribution=10000,
                expected_return=-1.5
            )
    
    def test_calculate_future_value_basic(self):
        """Test basic future value calculation."""
        calc = RetirementCalculator(
            current_age=30,
            retirement_age=35,  # 5 years
            current_savings=10000,
            annual_contribution=5000,
            expected_return=0.05
        )
        
        results = calc.calculate_future_value()
        
        self.assertEqual(results['years_until_retirement'], 5)
        self.assertGreater(results['future_value'], 10000)
        self.assertEqual(results['total_contributions'], 25000)
        self.assertGreater(results['investment_gains'], 0)
    
    def test_calculate_future_value_zero_return(self):
        """Test future value calculation with zero return."""
        calc = RetirementCalculator(
            current_age=30,
            retirement_age=35,  # 5 years
            current_savings=10000,
            annual_contribution=5000,
            expected_return=0.0
        )
        
        results = calc.calculate_future_value()
        
        # With zero return: FV = current + (contribution * years)
        expected_fv = 10000 + (5000 * 5)
        self.assertAlmostEqual(results['future_value'], expected_fv, places=2)
        self.assertEqual(results['investment_gains'], 0)
    
    def test_calculate_future_value_no_contribution(self):
        """Test future value calculation with no contributions."""
        calc = RetirementCalculator(
            current_age=30,
            retirement_age=35,  # 5 years
            current_savings=10000,
            annual_contribution=0,
            expected_return=0.05
        )
        
        results = calc.calculate_future_value()
        
        # FV should be just current savings compounded
        expected_fv = 10000 * (1.05 ** 5)
        self.assertAlmostEqual(results['future_value'], expected_fv, places=2)
        self.assertEqual(results['total_contributions'], 0)
    
    def test_calculate_required_savings(self):
        """Test calculation of required savings to reach target."""
        calc = RetirementCalculator(
            current_age=30,
            retirement_age=35,  # 5 years
            current_savings=10000,
            annual_contribution=5000,
            expected_return=0.05
        )
        
        target = 50000
        required = calc.calculate_required_savings(target)
        
        # Required should be positive
        self.assertGreater(required, 0)
        
        # Test with already sufficient savings
        calc2 = RetirementCalculator(
            current_age=30,
            retirement_age=35,
            current_savings=100000,
            annual_contribution=0,
            expected_return=0.05
        )
        
        required2 = calc2.calculate_required_savings(50000)
        self.assertEqual(required2, 0.0)
    
    def test_calculate_retirement_duration(self):
        """Test calculation of retirement duration."""
        calc = RetirementCalculator(
            current_age=30,
            retirement_age=35,
            current_savings=10000,
            annual_contribution=5000,
            expected_return=0.05,
            annual_expenses=5000
        )
        
        duration = calc.calculate_retirement_duration()
        
        # Duration should be positive and reasonable
        self.assertGreater(duration, 0)
        self.assertLess(duration, 100)
    
    def test_calculate_retirement_duration_default_withdrawal(self):
        """Test retirement duration with default 4% withdrawal rule."""
        calc = RetirementCalculator(
            current_age=30,
            retirement_age=35,
            current_savings=100000,
            annual_contribution=0,
            expected_return=0.05,
            annual_expenses=0  # Will use 4% rule
        )
        
        duration = calc.calculate_retirement_duration()
        
        # With 4% withdrawal and growth, should last many years
        self.assertGreater(duration, 20)
    
    def test_generate_projection_table(self):
        """Test generation of projection table."""
        calc = RetirementCalculator(
            current_age=30,
            retirement_age=40,  # 10 years
            current_savings=10000,
            annual_contribution=5000,
            expected_return=0.05
        )
        
        projections = calc.generate_projection_table(intervals=5)
        
        # Should have projections
        self.assertGreater(len(projections), 0)
        
        # First projection should match initial state
        self.assertEqual(projections[0]['age'], 30)
        self.assertEqual(projections[0]['balance'], 10000)
        self.assertEqual(projections[0]['contributed'], 0)
        
        # Last projection should be at retirement age
        self.assertEqual(projections[-1]['age'], 40)
        
        # Balance should increase over time
        for i in range(1, len(projections)):
            self.assertGreater(projections[i]['balance'], projections[i-1]['balance'])
    
    def test_format_currency(self):
        """Test currency formatting function."""
        self.assertEqual(format_currency(1000), "$1,000.00")
        self.assertEqual(format_currency(1234567.89), "$1,234,567.89")
        self.assertEqual(format_currency(0), "$0.00")
        self.assertEqual(format_currency(99.99), "$99.99")


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""
    
    def test_same_age_retirement(self):
        """Test with retirement age equal to current age."""
        with self.assertRaises(ValueError):
            RetirementCalculator(
                current_age=65,
                retirement_age=65,
                current_savings=50000,
                annual_contribution=10000,
                expected_return=0.07
            )
    
    def test_zero_current_savings(self):
        """Test with zero current savings."""
        calc = RetirementCalculator(
            current_age=25,
            retirement_age=65,
            current_savings=0,
            annual_contribution=10000,
            expected_return=0.07
        )
        
        results = calc.calculate_future_value()
        self.assertGreater(results['future_value'], 0)
        self.assertEqual(results['current_savings'], 0)
    
    def test_very_high_return(self):
        """Test with high but valid return rate."""
        calc = RetirementCalculator(
            current_age=30,
            retirement_age=35,
            current_savings=10000,
            annual_contribution=5000,
            expected_return=0.20  # 20% return
        )
        
        results = calc.calculate_future_value()
        # Should calculate without error
        self.assertGreater(results['future_value'], 10000)
    
    def test_negative_return(self):
        """Test with negative return rate."""
        calc = RetirementCalculator(
            current_age=30,
            retirement_age=35,
            current_savings=10000,
            annual_contribution=5000,
            expected_return=-0.05  # -5% return
        )
        
        results = calc.calculate_future_value()
        # Future value could be less than initial due to negative returns
        self.assertIsInstance(results['future_value'], float)
    
    def test_long_time_horizon(self):
        """Test with very long time until retirement."""
        calc = RetirementCalculator(
            current_age=20,
            retirement_age=70,  # 50 years
            current_savings=1000,
            annual_contribution=1000,
            expected_return=0.07
        )
        
        results = calc.calculate_future_value()
        # Should handle long time horizons
        self.assertGreater(results['future_value'], 1000)
        self.assertEqual(results['years_until_retirement'], 50)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
