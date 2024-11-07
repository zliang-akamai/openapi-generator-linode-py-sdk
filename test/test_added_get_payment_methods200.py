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

from openapi_client.models.added_get_payment_methods200 import AddedGetPaymentMethods200

class TestAddedGetPaymentMethods200(unittest.TestCase):
    """AddedGetPaymentMethods200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddedGetPaymentMethods200:
        """Test AddedGetPaymentMethods200
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddedGetPaymentMethods200`
        """
        model = AddedGetPaymentMethods200()
        if include_optional:
            return AddedGetPaymentMethods200(
                data = [
                    openapi_client.models.get_payment_methods_200_response_data_inner.get_payment_methods_200_response_data_inner(
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        data = null, 
                        id = 123, 
                        is_default = True, 
                        type = 'credit_card', )
                    ],
                page = 1,
                pages = 1,
                results = 1
            )
        else:
            return AddedGetPaymentMethods200(
        )
        """

    def testAddedGetPaymentMethods200(self):
        """Test AddedGetPaymentMethods200"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
