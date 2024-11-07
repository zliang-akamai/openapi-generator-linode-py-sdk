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

from openapi_client.models.get_regions200_response_data_inner import GetRegions200ResponseDataInner

class TestGetRegions200ResponseDataInner(unittest.TestCase):
    """GetRegions200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetRegions200ResponseDataInner:
        """Test GetRegions200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRegions200ResponseDataInner`
        """
        model = GetRegions200ResponseDataInner()
        if include_optional:
            return GetRegions200ResponseDataInner(
                capabilities = ["Linodes","NodeBalancers","Block Storage","Object Storage","Placement Groups","Block Storage Encryption"],
                country = 'us',
                id = 'us-east',
                label = 'Newark, NJ, USA',
                placement_group_limits = openapi_client.models.get_regions_200_response_data_inner_placement_group_limits.get_regions_200_response_data_inner_placement_group_limits(
                    maximum_linodes_per_pg = 5, 
                    maximum_pgs_per_customer = 10, ),
                resolvers = openapi_client.models.get_regions_200_response_data_inner_resolvers.get_regions_200_response_data_inner_resolvers(
                    ipv4 = '192.0.2.0,192.0.2.1', 
                    ipv6 = '2001:0db8::,2001:0db8::1', ),
                site_type = 'core',
                status = 'ok'
            )
        else:
            return GetRegions200ResponseDataInner(
        )
        """

    def testGetRegions200ResponseDataInner(self):
        """Test GetRegions200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()