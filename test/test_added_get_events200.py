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

from openapi_client.models.added_get_events200 import AddedGetEvents200

class TestAddedGetEvents200(unittest.TestCase):
    """AddedGetEvents200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddedGetEvents200:
        """Test AddedGetEvents200
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddedGetEvents200`
        """
        model = AddedGetEvents200()
        if include_optional:
            return AddedGetEvents200(
                data = [
                    openapi_client.models.get_events_200_response_data_inner.get_events_200_response_data_inner(
                        action = 'ticket_create', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        duration = 300.56, 
                        entity = openapi_client.models.get_events_200_response_data_inner_entity.get_events_200_response_data_inner_entity(
                            id = 11111, 
                            label = 'Problem booting my Linode', 
                            type = 'ticket', 
                            url = '/v4/support/tickets/11111', ), 
                        id = 123, 
                        message = 'None', 
                        percent_complete = 56, 
                        rate = '', 
                        read = True, 
                        secondary_entity = openapi_client.models.get_events_200_response_data_inner_secondary_entity.get_events_200_response_data_inner_secondary_entity(
                            id = 'linode/debian9', 
                            label = 'linode1234', 
                            type = 'linode', 
                            url = '/v4/linode/instances/1234', ), 
                        seen = True, 
                        status = 'failed', 
                        time_remaining = '', 
                        username = 'exampleUser', )
                    ],
                page = 1,
                pages = 1,
                results = 1
            )
        else:
            return AddedGetEvents200(
        )
        """

    def testAddedGetEvents200(self):
        """Test AddedGetEvents200"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
