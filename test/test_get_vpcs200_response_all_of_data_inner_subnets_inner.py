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

from openapi_client.models.get_vpcs200_response_all_of_data_inner_subnets_inner import GetVpcs200ResponseAllOfDataInnerSubnetsInner

class TestGetVpcs200ResponseAllOfDataInnerSubnetsInner(unittest.TestCase):
    """GetVpcs200ResponseAllOfDataInnerSubnetsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetVpcs200ResponseAllOfDataInnerSubnetsInner:
        """Test GetVpcs200ResponseAllOfDataInnerSubnetsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetVpcs200ResponseAllOfDataInnerSubnetsInner`
        """
        model = GetVpcs200ResponseAllOfDataInnerSubnetsInner()
        if include_optional:
            return GetVpcs200ResponseAllOfDataInnerSubnetsInner(
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = 456,
                ipv4 = '10.0.1.0/24',
                label = 'cool-vpc-subnet',
                linodes = [
                    openapi_client.models.get_vpcs_200_response_all_of_data_inner_subnets_inner_linodes_inner.get_vpcs_200_response_allOf_data_inner_subnets_inner_linodes_inner(
                        id = 111, 
                        interfaces = [
                            openapi_client.models.get_vpcs_200_response_all_of_data_inner_subnets_inner_linodes_inner_interfaces_inner.get_vpcs_200_response_allOf_data_inner_subnets_inner_linodes_inner_interfaces_inner(
                                active = True, 
                                id = 421, )
                            ], )
                    ],
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GetVpcs200ResponseAllOfDataInnerSubnetsInner(
        )
        """

    def testGetVpcs200ResponseAllOfDataInnerSubnetsInner(self):
        """Test GetVpcs200ResponseAllOfDataInnerSubnetsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
