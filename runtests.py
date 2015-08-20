import unittest
import algopy.test.all_tests
from colour_runner.runner import ColourTextTestRunner

testSuite = algopy.test.all_tests.create_test_suite()
text_runner = unittest.TextTestRunner().run(testSuite)
#text_runner = ColourTextTestRunner.run(testSuite)


