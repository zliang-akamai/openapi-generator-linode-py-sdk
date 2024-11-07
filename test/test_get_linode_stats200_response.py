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

from openapi_client.models.get_linode_stats200_response import GetLinodeStats200Response

class TestGetLinodeStats200Response(unittest.TestCase):
    """GetLinodeStats200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLinodeStats200Response:
        """Test GetLinodeStats200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLinodeStats200Response`
        """
        model = GetLinodeStats200Response()
        if include_optional:
            return GetLinodeStats200Response(
                cpu = [
                    [
                        1.337
                        ]
                    ],
                io = openapi_client.models.get_linode_stats_200_response_io.get_linode_stats_200_response_io(
                    io = [
                        [
                            1.337
                            ]
                        ], 
                    swap = [
                        [
                            1.337
                            ]
                        ], ),
                netv4 = openapi_client.models.get_linode_stats_200_response_netv4.get_linode_stats_200_response_netv4(
                    in = [
                        [
                            1.337
                            ]
                        ], 
                    out = [
                        [
                            1.337
                            ]
                        ], 
                    private_in = [
                        [
                            1.337
                            ]
                        ], 
                    private_out = [
                        [
                            1.337
                            ]
                        ], ),
                netv6 = openapi_client.models.get_linode_stats_200_response_netv6.get_linode_stats_200_response_netv6(
                    in = [
                        [
                            1.337
                            ]
                        ], 
                    out = [
                        [
                            1.337
                            ]
                        ], 
                    private_in = [
                        [
                            1.337
                            ]
                        ], 
                    private_out = [
                        [
                            1.337
                            ]
                        ], ),
                title = 'linode.com - my-linode (linode123456) - day (5 min avg)'
            )
        else:
            return GetLinodeStats200Response(
        )
        """

    def testGetLinodeStats200Response(self):
        """Test GetLinodeStats200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
