"""
Unit and regression test for the fcc_analyzer package.
"""

# Import package, test suite, and other packages as needed
import fcc_analyzer
import pytest
import sys

def test_fcc_analyzer_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "fcc_analyzer" in sys.modules
