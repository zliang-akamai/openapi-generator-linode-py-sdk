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

from openapi_client.models.get_entity_transfers200_response import GetEntityTransfers200Response

class TestGetEntityTransfers200Response(unittest.TestCase):
    """GetEntityTransfers200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetEntityTransfers200Response:
        """Test GetEntityTransfers200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEntityTransfers200Response`
        """
        model = GetEntityTransfers200Response()
        if include_optional:
            return GetEntityTransfers200Response(
                page = 1,
                pages = 1,
                results = 1,
                data = [
                    openapi_client.models.get_entity_transfers_200_response_all_of_data_inner.get_entity_transfers_200_response_allOf_data_inner(
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        entities = openapi_client.models.get_entity_transfers_200_response_all_of_data_inner_entities.get_entity_transfers_200_response_allOf_data_inner_entities(
                            linodes = [111,222], ), 
                        expiry = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_sender = True, 
                        status = 'pending', 
                        token = '123e4567-e89b-12d3-a456-426614174000', 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return GetEntityTransfers200Response(
        )
        """

    def testGetEntityTransfers200Response(self):
        """Test GetEntityTransfers200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()