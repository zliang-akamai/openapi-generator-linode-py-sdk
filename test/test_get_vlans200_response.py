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

from openapi_client.models.get_vlans200_response import GetVlans200Response

class TestGetVlans200Response(unittest.TestCase):
    """GetVlans200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetVlans200Response:
        """Test GetVlans200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetVlans200Response`
        """
        model = GetVlans200Response()
        if include_optional:
            return GetVlans200Response(
                data = [
                    openapi_client.models.get_vlans_200_response_data_inner.get_vlans_200_response_data_inner(
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        label = 'vlan-example', 
                        linodes = [111,222], 
                        region = 'ap-west', )
                    ],
                page = 1,
                pages = 1,
                results = 1
            )
        else:
            return GetVlans200Response(
        )
        """

    def testGetVlans200Response(self):
        """Test GetVlans200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()