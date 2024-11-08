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

from openapi_client.models.get_managed_credentials200_response import GetManagedCredentials200Response

class TestGetManagedCredentials200Response(unittest.TestCase):
    """GetManagedCredentials200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetManagedCredentials200Response:
        """Test GetManagedCredentials200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetManagedCredentials200Response`
        """
        model = GetManagedCredentials200Response()
        if include_optional:
            return GetManagedCredentials200Response(
                data = [
                    openapi_client.models.get_managed_credentials_200_response_data_inner.get_managed_credentials_200_response_data_inner(
                        id = 9991, 
                        label = 'prod-password-1', 
                        last_decrypted = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                page = 1,
                pages = 1,
                results = 1
            )
        else:
            return GetManagedCredentials200Response(
        )
        """

    def testGetManagedCredentials200Response(self):
        """Test GetManagedCredentials200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
