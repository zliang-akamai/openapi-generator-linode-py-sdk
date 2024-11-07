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

from openapi_client.models.get_network_transfer_prices200_response import GetNetworkTransferPrices200Response

class TestGetNetworkTransferPrices200Response(unittest.TestCase):
    """GetNetworkTransferPrices200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetNetworkTransferPrices200Response:
        """Test GetNetworkTransferPrices200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetNetworkTransferPrices200Response`
        """
        model = GetNetworkTransferPrices200Response()
        if include_optional:
            return GetNetworkTransferPrices200Response(
                data = [
                    openapi_client.models.get_network_transfer_prices_200_response_data_inner.get_network_transfer_prices_200_response_data_inner(
                        id = 'network_transfer', 
                        label = 'Network Transfer', 
                        price = openapi_client.models.get_network_transfer_prices_200_response_data_inner_price.get_network_transfer_prices_200_response_data_inner_price(
                            hourly = 0.005, 
                            monthly = 1.337, ), 
                        region_prices = [
                            openapi_client.models.get_network_transfer_prices_200_response_data_inner_region_prices_inner.get_network_transfer_prices_200_response_data_inner_region_prices_inner(
                                hourly = 0.015, 
                                id = 'us-east', 
                                monthly = 1.337, )
                            ], 
                        transfer = 0, )
                    ],
                page = 1,
                pages = 1,
                results = 1
            )
        else:
            return GetNetworkTransferPrices200Response(
        )
        """

    def testGetNetworkTransferPrices200Response(self):
        """Test GetNetworkTransferPrices200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()