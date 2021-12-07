import unittest
from test_aggregator import TestAggregator
from test_evaluator import TestEvaluator
from test_gui import TestGUI
from tests.unit.test_utilities import TestUtilities

class runner():
    def runner(self):
        suite = unittest.TestSuite()
        suite.addTest(TestUtilities())
        suite.addTest(TestAggregator())
        suite.addTest(TestEvaluator())
        suite.addTest(TestGUI())
        return suite

#System is a class that simply merges together different component 
# such that is impossible to be tested in unit-mode
suite = runner().runner()
unittest.TextTestRunner(verbosity=2).run(suite)