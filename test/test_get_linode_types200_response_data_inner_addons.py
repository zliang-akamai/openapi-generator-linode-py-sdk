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

from openapi_client.models.get_linode_types200_response_data_inner_addons import GetLinodeTypes200ResponseDataInnerAddons

class TestGetLinodeTypes200ResponseDataInnerAddons(unittest.TestCase):
    """GetLinodeTypes200ResponseDataInnerAddons unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLinodeTypes200ResponseDataInnerAddons:
        """Test GetLinodeTypes200ResponseDataInnerAddons
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLinodeTypes200ResponseDataInnerAddons`
        """
        model = GetLinodeTypes200ResponseDataInnerAddons()
        if include_optional:
            return GetLinodeTypes200ResponseDataInnerAddons(
                backups = openapi_client.models.get_linode_types_200_response_data_inner_addons_backups.get_linode_types_200_response_data_inner_addons_backups(
                    price = openapi_client.models.get_linode_types_200_response_data_inner_addons_backups_price.get_linode_types_200_response_data_inner_addons_backups_price(
                        hourly = 0.008, 
                        monthly = 5, ), 
                    region_prices = [
                        openapi_client.models.get_linode_types_200_response_data_inner_addons_backups_region_prices_inner.get_linode_types_200_response_data_inner_addons_backups_region_prices_inner(
                            hourly = 0.0096, 
                            id = 'us-east', 
                            monthly = 6, )
                        ], )
            )
        else:
            return GetLinodeTypes200ResponseDataInnerAddons(
        )
        """

    def testGetLinodeTypes200ResponseDataInnerAddons(self):
        """Test GetLinodeTypes200ResponseDataInnerAddons"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()