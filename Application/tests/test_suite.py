import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from tests.unit.test_aggregator import TestAggregator
from tests.unit.test_evaluator import TestEvaluator
from tests.unit.test_gui import TestGUI
from tests.unit.test_utilities import TestUtilities
from tests.integration.test_system import TestSystem

class runner():
    def runner(self):
        suite = unittest.TestSuite()
        suite.addTest(TestUtilities())
        suite.addTest(TestAggregator())
        suite.addTest(TestEvaluator())
        suite.addTest(TestGUI())
        suite.addTest(TestSystem())
        return suite

suite = runner().runner()
unittest.TextTestRunner(verbosity=2).run(suite)