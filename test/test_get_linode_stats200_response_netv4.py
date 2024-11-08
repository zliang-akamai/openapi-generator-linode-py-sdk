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

from openapi_client.models.get_linode_stats200_response_netv4 import GetLinodeStats200ResponseNetv4

class TestGetLinodeStats200ResponseNetv4(unittest.TestCase):
    """GetLinodeStats200ResponseNetv4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLinodeStats200ResponseNetv4:
        """Test GetLinodeStats200ResponseNetv4
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLinodeStats200ResponseNetv4`
        """
        model = GetLinodeStats200ResponseNetv4()
        if include_optional:
            return GetLinodeStats200ResponseNetv4(
                var_in = [
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
                    ]
            )
        else:
            return GetLinodeStats200ResponseNetv4(
        )
        """

    def testGetLinodeStats200ResponseNetv4(self):
        """Test GetLinodeStats200ResponseNetv4"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
