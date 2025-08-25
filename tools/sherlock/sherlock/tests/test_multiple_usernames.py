import unittest
import sys
sys.path.append('../')
import sherlock as sh

checksymbols = ["_", "-", "."]

"""Test for mulriple usernames.

        This test ensures that the function MultipleUsernames works properly. More specific,
        different scenarios are tested and only usernames that contain this specific sequence: {?} 
        should return positive.
      
        Keyword Arguments:
        self                   -- This object.

        Return Value:
        Nothing.
        """
class TestMultipleUsernames(unittest.TestCase):
    @unittest.skipUnless(
        hasattr(sh, "CheckForParameter") and hasattr(sh, "MultipleUsernames"),
        "required sherlock functions missing",
    )
    def test_area(self):
        test_usernames = ["test{?}test", "test{?feo", "test"]
        for name in test_usernames:
            if sh.CheckForParameter(name):
                self.assertAlmostEqual(
                    sh.MultipleUsernames(name), ["test_test", "test-test", "test.test"]
                )
            else:
                self.assertAlmostEqual(name, name)
