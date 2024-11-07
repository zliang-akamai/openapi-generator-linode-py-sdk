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

from openapi_client.models.promotion import Promotion

class TestPromotion(unittest.TestCase):
    """Promotion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Promotion:
        """Test Promotion
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Promotion`
        """
        model = Promotion()
        if include_optional:
            return Promotion(
                credit_monthly_cap = '10.00',
                credit_remaining = '50.00',
                description = 'Receive up to $10 off your services every month for 6 months! Unused credits will expire once this promotion period ends.',
                expire_dt = '2018-01-31T23:59:59',
                image_url = 'https://linode.com/10_a_month_promotion.svg',
                service_type = 'all',
                summary = '$10 off your Linode a month!',
                this_month_credit_remaining = '10.00'
            )
        else:
            return Promotion(
        )
        """

    def testPromotion(self):
        """Test Promotion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()