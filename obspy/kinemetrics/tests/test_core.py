#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The obspy.kinemetrics.core test suite.
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA

import io
import os
import unittest

from obspy import read
from obspy.core.utcdatetime import UTCDateTime
from obspy.kinemetrics.core import is_evt, read_evt


class CoreTestCase(unittest.TestCase):
    """
    Test cases for kinemetrics core interface
    """
    def setUp(self):
        # directory where the test files are located
        self.path = os.path.join(os.path.dirname(__file__), 'data')

    def test_is_evt(self):
        """
        Test for the the is_evt() function.
        """
        valid_files = [os.path.join(self.path, "BI008_MEMA-04823.evt"),
                       os.path.join(self.path, "BX456_MOLA-02351.evt")]
        invalid_files = [os.path.join(self.path, "NOUTF8.evt")]
        py_dir = os.path.join(self.path, os.pardir, os.pardir)
        for filename in os.listdir(py_dir):
            if filename.endswith(".py"):
                invalid_files.append(
                    os.path.abspath(os.path.join(py_dir, filename)))
        self.assertTrue(len(invalid_files) > 0)

        for filename in valid_files:
            self.assertTrue(is_evt(filename))
        for filename in invalid_files:
            self.assertFalse(is_evt(filename))

    def test_is_evt_from_bytesio(self):
        """
        Test for the the is_evt() function from BytesIO objects.
        """
        valid_files = [os.path.join(self.path, "BI008_MEMA-04823.evt"),
                       os.path.join(self.path, "BX456_MOLA-02351.evt")]
        invalid_files = [os.path.join(self.path, "NOUTF8.evt")]
        py_dir = os.path.join(self.path, os.pardir, os.pardir)
        for filename in os.listdir(py_dir):
            if filename.endswith(".py"):
                invalid_files.append(
                    os.path.abspath(os.path.join(py_dir, filename)))
        self.assertTrue(len(invalid_files) > 0)

        for filename in valid_files:
            with open(filename, "rb") as fh:
                buf = io.BytesIO(fh.read())
            buf.seek(0, 0)
            self.assertTrue(is_evt(buf))
        for filename in invalid_files:
            with open(filename, "rb") as fh:
                buf = io.BytesIO(fh.read())
            buf.seek(0, 0)
            self.assertFalse(is_evt(buf))

    def test_read_via_ObsPy(self):
        """
        Read files via obspy.core.stream.read function.
        """
        filename = os.path.join(self.path, 'BI008_MEMA-04823.evt')
        # 1
        st = read(filename)
        st.verify()
        self.assertEqual(len(st), 3)
        self.assertEqual(st[0].stats.starttime,
                         UTCDateTime('2013-08-15T09:20:28.000000Z'))
        self.assertEqual(st[1].stats.starttime,
                         UTCDateTime('2013-08-15T09:20:28.000000Z'))
        self.assertEqual(st[2].stats.starttime,
                         UTCDateTime('2013-08-15T09:20:28.000000Z'))
        self.assertEqual(len(st[0]), 230*25)
        self.assertAlmostEqual(st[0].stats.sampling_rate, 250.0)
        self.assertEqual(st[0].stats.channel, '0')
        self.assertEqual(st[0].stats.station, 'MEMA')

        filename = os.path.join(self.path, 'BX456_MOLA-02351.evt')
        # 2
        st = read(filename)
        st.verify()
        self.assertEqual(len(st), 6)
        self.assertEqual(st[0].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[1].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[2].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[3].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[4].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[5].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(len(st[0]), 390*25)
        self.assertAlmostEqual(st[0].stats.sampling_rate, 250.0)
        self.assertEqual(st[0].stats.channel, '0')
        self.assertEqual(st[0].stats.station, 'MOLA')

    def test_reading_via_obspy_and_bytesio(self):
        """
        Test the reading of EVT files from BytesIO objects.
        """
        # 1
        filename = os.path.join(self.path, 'BI008_MEMA-04823.evt')
        with open(filename, "rb") as fh:
            buf = io.BytesIO(fh.read())
        buf.seek(0, 0)
        st = read(buf)
        st.verify()
        self.assertEqual(len(st), 3)
        self.assertEqual(st[0].stats.starttime,
                         UTCDateTime('2013-08-15T09:20:28.000000Z'))
        self.assertEqual(st[1].stats.starttime,
                         UTCDateTime('2013-08-15T09:20:28.000000Z'))
        self.assertEqual(st[2].stats.starttime,
                         UTCDateTime('2013-08-15T09:20:28.000000Z'))
        self.assertEqual(len(st[0]), 230*25)
        self.assertAlmostEqual(st[0].stats.sampling_rate, 250.0)
        self.assertEqual(st[0].stats.channel, '0')
        self.assertEqual(st[0].stats.station, 'MEMA')

        # 2
        filename = os.path.join(self.path, 'BX456_MOLA-02351.evt')
        with open(filename, "rb") as fh:
            buf = io.BytesIO(fh.read())
        buf.seek(0, 0)
        st = read(buf)
        st.verify()
        self.assertEqual(len(st), 6)
        self.assertEqual(st[0].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[1].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[2].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[3].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[4].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[5].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(len(st[0]), 390*25)
        self.assertAlmostEqual(st[0].stats.sampling_rate, 250.0)
        self.assertEqual(st[0].stats.channel, '0')
        self.assertEqual(st[0].stats.station, 'MOLA')

    def test_read_via_module(self):
        """
        Read files via obspy.kinemetrics.core.read_evt function.
        """
        filename = os.path.join(self.path, 'BI008_MEMA-04823.evt')
        # 1
        st = read_evt(filename)
        st.verify()
        self.assertEqual(len(st), 3)
        self.assertEqual(st[0].stats.starttime,
                         UTCDateTime('2013-08-15T09:20:28.000000Z'))
        self.assertEqual(st[1].stats.starttime,
                         UTCDateTime('2013-08-15T09:20:28.000000Z'))
        self.assertEqual(st[2].stats.starttime,
                         UTCDateTime('2013-08-15T09:20:28.000000Z'))
        self.assertEqual(len(st[0]), 230*25)
        self.assertAlmostEqual(st[0].stats.sampling_rate, 250.0)
        self.assertEqual(st[0].stats.channel, '0')
        self.assertEqual(st[0].stats.station, 'MEMA')

        filename = os.path.join(self.path, 'BX456_MOLA-02351.evt')
        # 2
        st = read_evt(filename)
        st.verify()
        self.assertEqual(len(st), 6)
        self.assertEqual(st[0].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[1].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[2].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[3].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[4].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[5].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(len(st[0]), 390*25)
        self.assertAlmostEqual(st[0].stats.sampling_rate, 250.0)
        self.assertEqual(st[0].stats.channel, '0')
        self.assertEqual(st[0].stats.station, 'MOLA')

    def test_read_via_module_and_bytesio(self):
        """
        Read files via obspy.kinemetrics.core.read_evt function from BytesIO
        objects.
        """
        # 1
        filename = os.path.join(self.path, 'BI008_MEMA-04823.evt')
        with open(filename, "rb") as fh:
            buf = io.BytesIO(fh.read())
        buf.seek(0, 0)
        st = read_evt(buf)
        st.verify()
        self.assertEqual(len(st), 3)
        self.assertEqual(st[0].stats.starttime,
                         UTCDateTime('2013-08-15T09:20:28.000000Z'))
        self.assertEqual(st[1].stats.starttime,
                         UTCDateTime('2013-08-15T09:20:28.000000Z'))
        self.assertEqual(st[2].stats.starttime,
                         UTCDateTime('2013-08-15T09:20:28.000000Z'))
        self.assertEqual(len(st[0]), 230*25)
        self.assertAlmostEqual(st[0].stats.sampling_rate, 250.0)
        self.assertEqual(st[0].stats.channel, '0')
        self.assertEqual(st[0].stats.station, 'MEMA')

        # 2
        filename = os.path.join(self.path, 'BX456_MOLA-02351.evt')
        with open(filename, "rb") as fh:
            buf = io.BytesIO(fh.read())
        buf.seek(0, 0)
        st = read_evt(buf)
        st.verify()
        self.assertEqual(len(st), 6)
        self.assertEqual(st[0].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[1].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[2].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[3].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[4].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(st[5].stats.starttime,
                         UTCDateTime('2012-01-17T09:54:36.000000Z'))
        self.assertEqual(len(st[0]), 390*25)
        self.assertAlmostEqual(st[0].stats.sampling_rate, 250.0)
        self.assertEqual(st[0].stats.channel, '0')
        self.assertEqual(st[0].stats.station, 'MOLA')


def suite():
    return unittest.makeSuite(CoreTestCase, 'test')


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
