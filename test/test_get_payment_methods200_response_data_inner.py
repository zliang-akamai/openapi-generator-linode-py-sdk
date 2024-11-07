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

from openapi_client.models.get_payment_methods200_response_data_inner import GetPaymentMethods200ResponseDataInner

class TestGetPaymentMethods200ResponseDataInner(unittest.TestCase):
    """GetPaymentMethods200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPaymentMethods200ResponseDataInner:
        """Test GetPaymentMethods200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPaymentMethods200ResponseDataInner`
        """
        model = GetPaymentMethods200ResponseDataInner()
        if include_optional:
            return GetPaymentMethods200ResponseDataInner(
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                data = None,
                id = 123,
                is_default = True,
                type = 'credit_card'
            )
        else:
            return GetPaymentMethods200ResponseDataInner(
        )
        """

    def testGetPaymentMethods200ResponseDataInner(self):
        """Test GetPaymentMethods200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
