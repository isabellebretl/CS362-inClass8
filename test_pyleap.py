import pytest
import leap


class TestClass:
    def test_leap1(self):
        assert leap.leap(2012) == True
    def test_leap2(self):
        assert leap.leap(2011) == False
    def test_leap3(self):
        assert leap.leap(2100) == False