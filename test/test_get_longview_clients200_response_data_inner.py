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

from openapi_client.models.get_longview_clients200_response_data_inner import GetLongviewClients200ResponseDataInner

class TestGetLongviewClients200ResponseDataInner(unittest.TestCase):
    """GetLongviewClients200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLongviewClients200ResponseDataInner:
        """Test GetLongviewClients200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLongviewClients200ResponseDataInner`
        """
        model = GetLongviewClients200ResponseDataInner()
        if include_optional:
            return GetLongviewClients200ResponseDataInner(
                api_key = 'BD1B4B54-D752-A76D-5A9BD8A17F39DB61',
                apps = openapi_client.models.get_longview_clients_200_response_data_inner_apps.get_longview_clients_200_response_data_inner_apps(
                    apache = True, 
                    mysql = True, 
                    nginx = False, ),
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = 789,
                install_code = 'BD1B5605-BF5E-D385-BA07AD518BE7F321',
                label = 'client789',
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GetLongviewClients200ResponseDataInner(
        )
        """

    def testGetLongviewClients200ResponseDataInner(self):
        """Test GetLongviewClients200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
