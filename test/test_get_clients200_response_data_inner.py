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

from openapi_client.models.get_clients200_response_data_inner import GetClients200ResponseDataInner

class TestGetClients200ResponseDataInner(unittest.TestCase):
    """GetClients200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetClients200ResponseDataInner:
        """Test GetClients200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetClients200ResponseDataInner`
        """
        model = GetClients200ResponseDataInner()
        if include_optional:
            return GetClients200ResponseDataInner(
                id = '2737bf16b39ab5d7b4a1',
                label = 'Test_Client_1',
                public = False,
                redirect_uri = 'https://example.org/oauth/callback',
                secret = '<REDACTED>',
                status = 'active',
                thumbnail_url = 'https://api.linode.com/v4/account/clients/2737bf16b39ab5d7b4a1/thumbnail'
            )
        else:
            return GetClients200ResponseDataInner(
        )
        """

    def testGetClients200ResponseDataInner(self):
        """Test GetClients200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
