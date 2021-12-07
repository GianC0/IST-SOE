import unittest
from unit.test_aggregator import TestAggregator
from unit.test_evaluator import TestEvaluator
from unit.test_gui import TestGUI
from unit.test_utilities import TestUtilities
from integration.test_system import TestSystem

class runner():
    def runner(self):
        suite = unittest.TestSuite()
        suite.addTest(TestUtilities())
        suite.addTest(TestAggregator())
        suite.addTest(TestEvaluator())
        suite.addTest(TestGUI())
        suite.addTest(TestSystem())
        return suite

#System is a class that simply merges together different component 
# such that is impossible to be tested in unit-mode
suite = runner().runner()
unittest.TextTestRunner(verbosity=2).run(suite)