# test_tokencore.py
"""
Tests for TokenCore module.
"""

import unittest
from tokencore import TokenCore

class TestTokenCore(unittest.TestCase):
    """Test cases for TokenCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenCore()
        self.assertIsInstance(instance, TokenCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
