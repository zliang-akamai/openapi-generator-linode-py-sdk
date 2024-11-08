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

from openapi_client.models.post_payment202_response_warnings_inner import PostPayment202ResponseWarningsInner

class TestPostPayment202ResponseWarningsInner(unittest.TestCase):
    """PostPayment202ResponseWarningsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostPayment202ResponseWarningsInner:
        """Test PostPayment202ResponseWarningsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostPayment202ResponseWarningsInner`
        """
        model = PostPayment202ResponseWarningsInner()
        if include_optional:
            return PostPayment202ResponseWarningsInner(
                details = 'Linode 123 could not be rebooted.',
                title = 'Unable to reboot Linode.'
            )
        else:
            return PostPayment202ResponseWarningsInner(
        )
        """

    def testPostPayment202ResponseWarningsInner(self):
        """Test PostPayment202ResponseWarningsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
