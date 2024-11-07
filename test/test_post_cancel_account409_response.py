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

from openapi_client.models.post_cancel_account409_response import PostCancelAccount409Response

class TestPostCancelAccount409Response(unittest.TestCase):
    """PostCancelAccount409Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostCancelAccount409Response:
        """Test PostCancelAccount409Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostCancelAccount409Response`
        """
        model = PostCancelAccount409Response()
        if include_optional:
            return PostCancelAccount409Response(
                errors = [
                    openapi_client.models.post_cancel_account_409_response_errors_inner.post_cancel_account_409_response_errors_inner(
                        reason = 'We were unable to charge your credit card for services rendered. We cannot cancel this account until the balance has been paid.', )
                    ]
            )
        else:
            return PostCancelAccount409Response(
        )
        """

    def testPostCancelAccount409Response(self):
        """Test PostCancelAccount409Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
