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

from openapi_client.models.get_node_balancer_stats200_response_data_traffic import GetNodeBalancerStats200ResponseDataTraffic

class TestGetNodeBalancerStats200ResponseDataTraffic(unittest.TestCase):
    """GetNodeBalancerStats200ResponseDataTraffic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetNodeBalancerStats200ResponseDataTraffic:
        """Test GetNodeBalancerStats200ResponseDataTraffic
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetNodeBalancerStats200ResponseDataTraffic`
        """
        model = GetNodeBalancerStats200ResponseDataTraffic()
        if include_optional:
            return GetNodeBalancerStats200ResponseDataTraffic(
                var_in = [
                    1.337
                    ],
                out = [
                    1.337
                    ]
            )
        else:
            return GetNodeBalancerStats200ResponseDataTraffic(
        )
        """

    def testGetNodeBalancerStats200ResponseDataTraffic(self):
        """Test GetNodeBalancerStats200ResponseDataTraffic"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()