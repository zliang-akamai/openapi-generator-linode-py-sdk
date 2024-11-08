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

from openapi_client.models.get_ipv6_pools200_response import GetIpv6Pools200Response

class TestGetIpv6Pools200Response(unittest.TestCase):
    """GetIpv6Pools200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetIpv6Pools200Response:
        """Test GetIpv6Pools200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetIpv6Pools200Response`
        """
        model = GetIpv6Pools200Response()
        if include_optional:
            return GetIpv6Pools200Response(
                data = [
                    openapi_client.models.get_ipv6_pools_200_response_data_inner.get_ipv6_pools_200_response_data_inner(
                        prefix = 124, 
                        range = '2600:3c01::2:5000:0', 
                        region = 'us-east', 
                        route_target = '2600:3c01::2:5000:f', )
                    ],
                page = 1,
                pages = 1,
                results = 1
            )
        else:
            return GetIpv6Pools200Response(
        )
        """

    def testGetIpv6Pools200Response(self):
        """Test GetIpv6Pools200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
