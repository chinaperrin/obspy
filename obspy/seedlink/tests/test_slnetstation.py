# -*- coding: utf-8 -*-
"""
The obspy.seedlink.client.slnetstation test suite.
"""
from obspy.seedlink.client.slnetstation import SLNetStation
import unittest


class SLNetStationTestCase(unittest.TestCase):

    def test_issueXXX(self):
        """
        Assure that different station objects don't share selector lists.
        """
        station1 = SLNetStation('', '', None, -1, None)
        station2 = SLNetStation('', '', None, -1, None)
        
        station1.appendSelectors('FOO')
        
        self.assertNotEqual(id(station1.selectors), id(station2.selectors))
        self.assertEqual(station1.getSelectors(), ['FOO'])
        self.assertEqual(station2.getSelectors(), [])


def suite():
    return unittest.makeSuite(SLNetStationTestCase, 'test')


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
