# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers (does not depend on class or instance)."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Return the product of two numbers.
        Demonstrates class method usage by accessing a class attribute.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
