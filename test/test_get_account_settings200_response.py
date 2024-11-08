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

from openapi_client.models.get_account_settings200_response import GetAccountSettings200Response

class TestGetAccountSettings200Response(unittest.TestCase):
    """GetAccountSettings200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAccountSettings200Response:
        """Test GetAccountSettings200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAccountSettings200Response`
        """
        model = GetAccountSettings200Response()
        if include_optional:
            return GetAccountSettings200Response(
                backups_enabled = True,
                longview_subscription = 'longview-3',
                managed = True,
                network_helper = False,
                object_storage = 'disabled'
            )
        else:
            return GetAccountSettings200Response(
        )
        """

    def testGetAccountSettings200Response(self):
        """Test GetAccountSettings200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
