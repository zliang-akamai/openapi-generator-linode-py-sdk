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

from openapi_client.models.get_account_default_response_errors_inner import GetAccountDefaultResponseErrorsInner

class TestGetAccountDefaultResponseErrorsInner(unittest.TestCase):
    """GetAccountDefaultResponseErrorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAccountDefaultResponseErrorsInner:
        """Test GetAccountDefaultResponseErrorsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAccountDefaultResponseErrorsInner`
        """
        model = GetAccountDefaultResponseErrorsInner()
        if include_optional:
            return GetAccountDefaultResponseErrorsInner(
                var_field = 'fieldname',
                reason = 'fieldname must be a valid value'
            )
        else:
            return GetAccountDefaultResponseErrorsInner(
        )
        """

    def testGetAccountDefaultResponseErrorsInner(self):
        """Test GetAccountDefaultResponseErrorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
