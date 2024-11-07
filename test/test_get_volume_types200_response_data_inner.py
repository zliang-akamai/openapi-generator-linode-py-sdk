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

from openapi_client.models.get_volume_types200_response_data_inner import GetVolumeTypes200ResponseDataInner

class TestGetVolumeTypes200ResponseDataInner(unittest.TestCase):
    """GetVolumeTypes200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetVolumeTypes200ResponseDataInner:
        """Test GetVolumeTypes200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetVolumeTypes200ResponseDataInner`
        """
        model = GetVolumeTypes200ResponseDataInner()
        if include_optional:
            return GetVolumeTypes200ResponseDataInner(
                id = 'volume',
                label = 'Storage Volume',
                price = openapi_client.models.get_volume_types_200_response_data_inner_price.get_volume_types_200_response_data_inner_price(
                    hourly = 0.0015, 
                    monthly = 0.1, ),
                region_prices = [
                    openapi_client.models.get_lke_types_200_response_data_inner_region_prices_inner.get_lke_types_200_response_data_inner_region_prices_inner(
                        hourly = 0.00018, 
                        id = 'us-east', 
                        monthly = 0.12, )
                    ],
                transfer = 0
            )
        else:
            return GetVolumeTypes200ResponseDataInner(
        )
        """

    def testGetVolumeTypes200ResponseDataInner(self):
        """Test GetVolumeTypes200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
