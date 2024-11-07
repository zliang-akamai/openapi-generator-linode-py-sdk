# coding: utf-8

"""
    Linode API

    [Read the API documentation](https://techdocs.akamai.com/linode-api/reference/api).

    The version of the OpenAPI document: 4.189.2
    Contact: support@linode.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.stats_available import StatsAvailable

class TestStatsAvailable(unittest.TestCase):
    """StatsAvailable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StatsAvailable:
        """Test StatsAvailable
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StatsAvailable`
        """
        model = StatsAvailable()
        if include_optional:
            return StatsAvailable(
                cpu = [
                    openapi_client.models.stats_available_cpu_inner.Stats_available_cpu_inner(
                        x = 11513761600000, 
                        y = 56, )
                    ],
                disk = [
                    openapi_client.models.stats_available_cpu_inner.Stats_available_cpu_inner(
                        x = 11513761600000, 
                        y = 56, )
                    ],
                net_in = [
                    openapi_client.models.stats_available_cpu_inner.Stats_available_cpu_inner(
                        x = 11513761600000, 
                        y = 56, )
                    ],
                net_out = [
                    openapi_client.models.stats_available_cpu_inner.Stats_available_cpu_inner(
                        x = 11513761600000, 
                        y = 56, )
                    ],
                swap = [
                    openapi_client.models.stats_available_cpu_inner.Stats_available_cpu_inner(
                        x = 11513761600000, 
                        y = 56, )
                    ]
            )
        else:
            return StatsAvailable(
        )
        """

    def testStatsAvailable(self):
        """Test StatsAvailable"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
