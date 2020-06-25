"""
Unit and regression test for the vssflow package.
"""

# Import package, test suite, and other packages as needed
import vssflow
import pytest
import sys

def test_vssflow_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "vssflow" in sys.modules
