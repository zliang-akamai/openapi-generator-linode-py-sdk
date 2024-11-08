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

from openapi_client.models.get_managed_services200_response import GetManagedServices200Response

class TestGetManagedServices200Response(unittest.TestCase):
    """GetManagedServices200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetManagedServices200Response:
        """Test GetManagedServices200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetManagedServices200Response`
        """
        model = GetManagedServices200Response()
        if include_optional:
            return GetManagedServices200Response(
                data = [
                    openapi_client.models.get_managed_services_200_response_data_inner.get_managed_services_200_response_data_inner(
                        address = 'https://example.org', 
                        body = 'it worked', 
                        consultation_group = 'on-call', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        credentials = [
                            9991
                            ], 
                        id = 9944, 
                        label = 'prod-1', 
                        notes = 'The service name is my-cool-application', 
                        region = '', 
                        service_type = 'url', 
                        status = 'ok', 
                        timeout = 30, 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                page = 1,
                pages = 1,
                results = 1
            )
        else:
            return GetManagedServices200Response(
        )
        """

    def testGetManagedServices200Response(self):
        """Test GetManagedServices200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
