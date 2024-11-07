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

from openapi_client.models.get_tickets200_response import GetTickets200Response

class TestGetTickets200Response(unittest.TestCase):
    """GetTickets200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTickets200Response:
        """Test GetTickets200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTickets200Response`
        """
        model = GetTickets200Response()
        if include_optional:
            return GetTickets200Response(
                data = [
                    openapi_client.models.get_tickets_200_response_data_inner.get_tickets_200_response_data_inner(
                        attachments = [
                            '["screenshot.jpg","screenshot.txt"]'
                            ], 
                        closable = False, 
                        closed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = 'I am having trouble setting the root password on my Linode. I tried following the instructions but something is not working. Can you please help me figure out how I can reset it?', 
                        entity = openapi_client.models.get_tickets_200_response_data_inner_entity.get_tickets_200_response_data_inner_entity(
                            id = 10400, 
                            label = 'linode123456', 
                            type = 'linode', 
                            url = '/v4/linode/instances/123456', ), 
                        gravatar_id = '474a1b7373ae0be4132649e69c36ce30', 
                        id = 11223344, 
                        opened = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        opened_by = 'some_user', 
                        status = 'open', 
                        summary = 'Having trouble resetting root password on my Linode', 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_by = 'some_other_user', )
                    ],
                page = 1,
                pages = 1,
                results = 1
            )
        else:
            return GetTickets200Response(
        )
        """

    def testGetTickets200Response(self):
        """Test GetTickets200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()