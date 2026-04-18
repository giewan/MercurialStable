# test_mercurialstable.py
"""
Tests for MercurialStable module.
"""

import unittest
from mercurialstable import MercurialStable

class TestMercurialStable(unittest.TestCase):
    """Test cases for MercurialStable class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MercurialStable()
        self.assertIsInstance(instance, MercurialStable)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MercurialStable()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
