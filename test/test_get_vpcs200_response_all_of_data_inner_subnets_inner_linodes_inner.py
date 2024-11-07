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

from openapi_client.models.get_vpcs200_response_all_of_data_inner_subnets_inner_linodes_inner import GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner

class TestGetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner(unittest.TestCase):
    """GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner:
        """Test GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner`
        """
        model = GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner()
        if include_optional:
            return GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner(
                id = 111,
                interfaces = [
                    openapi_client.models.get_vpcs_200_response_all_of_data_inner_subnets_inner_linodes_inner_interfaces_inner.get_vpcs_200_response_allOf_data_inner_subnets_inner_linodes_inner_interfaces_inner(
                        active = True, 
                        id = 421, )
                    ]
            )
        else:
            return GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner(
        )
        """

    def testGetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner(self):
        """Test GetVpcs200ResponseAllOfDataInnerSubnetsInnerLinodesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
