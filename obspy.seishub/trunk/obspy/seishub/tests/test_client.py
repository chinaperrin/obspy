#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The obspy.seishub.client test suite.
"""

from obspy.seishub import Client
import unittest


class ClientTestCase(unittest.TestCase):
    """
    Test cases for libgse2 core interface
    """

    def test_getStations(self):
        """
        """
        url = "http://admin:admin@teide.geophysik.uni-muenchen.de:8080"
        client = Client(url)
        data = client.waveform.getNetworkIds()
        print data
        data = client.waveform.getStationIds()
        print data
        data = client.waveform.getLocationIds()
        print data
        data = client.waveform.getChannelIds()
        print data
        data = client.waveform.getStationIds(network_id='BW')
        print data
        data = client.waveform.getChannelIds(network_id='BW', station_id='MANZ')
        print data
        data = client.waveform.getLatency(network_id='BW', station_id='MANZ')
        print data
        data = client.station.getList(network_id='BW', station_id='MANZ')
        print data
        data = client.station.getResource(network_id='BW', station_id='MANZ',
                                          format='metadata')
        print data





def suite():
    return unittest.makeSuite(ClientTestCase, 'test')


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
