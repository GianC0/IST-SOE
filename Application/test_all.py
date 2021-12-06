import unittest
from test_aggregator import TestAggregator
from test_evaluator import TestEvaluator
from test_gui import TestGUI
from test_system import TestSystem

class runner():
    def runner(self):
        suite = unittest.TestSuite()
        suite.addTest(TestAggregator())
        suite.addTest(TestEvaluator())
        suite.addTest(TestGUI())
        suite.addTest(TestSystem())
        return suite

#Run all tests
suite = runner().runner()
unittest.TextTestRunner(verbosity=2).run(suite)