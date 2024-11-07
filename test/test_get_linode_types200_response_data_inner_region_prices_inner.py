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

from openapi_client.models.get_linode_types200_response_data_inner_region_prices_inner import GetLinodeTypes200ResponseDataInnerRegionPricesInner

class TestGetLinodeTypes200ResponseDataInnerRegionPricesInner(unittest.TestCase):
    """GetLinodeTypes200ResponseDataInnerRegionPricesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLinodeTypes200ResponseDataInnerRegionPricesInner:
        """Test GetLinodeTypes200ResponseDataInnerRegionPricesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLinodeTypes200ResponseDataInnerRegionPricesInner`
        """
        model = GetLinodeTypes200ResponseDataInnerRegionPricesInner()
        if include_optional:
            return GetLinodeTypes200ResponseDataInnerRegionPricesInner(
                hourly = 0.036,
                id = 'us-east',
                monthly = 24
            )
        else:
            return GetLinodeTypes200ResponseDataInnerRegionPricesInner(
        )
        """

    def testGetLinodeTypes200ResponseDataInnerRegionPricesInner(self):
        """Test GetLinodeTypes200ResponseDataInnerRegionPricesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
