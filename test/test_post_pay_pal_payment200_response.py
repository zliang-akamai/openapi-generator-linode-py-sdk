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

from openapi_client.models.post_pay_pal_payment200_response import PostPayPalPayment200Response

class TestPostPayPalPayment200Response(unittest.TestCase):
    """PostPayPalPayment200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostPayPalPayment200Response:
        """Test PostPayPalPayment200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostPayPalPayment200Response`
        """
        model = PostPayPalPayment200Response()
        if include_optional:
            return PostPayPalPayment200Response(
                checkout_token = 'EC-1A2B3C4D5E6F7G8H9',
                payment_id = 'PAY-1234567890ABCDEFGHIJKLMN'
            )
        else:
            return PostPayPalPayment200Response(
        )
        """

    def testPostPayPalPayment200Response(self):
        """Test PostPayPalPayment200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
