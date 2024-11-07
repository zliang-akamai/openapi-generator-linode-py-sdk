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

from openapi_client.models.added_get_availability200 import AddedGetAvailability200

class TestAddedGetAvailability200(unittest.TestCase):
    """AddedGetAvailability200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddedGetAvailability200:
        """Test AddedGetAvailability200
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddedGetAvailability200`
        """
        model = AddedGetAvailability200()
        if include_optional:
            return AddedGetAvailability200(
                data = [
                    openapi_client.models.added_get_availability_200_all_of_data.added_get_availability_200_allOf_data(
                        available = ["Linodes","NodeBalancers"], 
                        region = 'us-east', 
                        unavailable = ["Kubernetes","Block Storage"], )
                    ],
                page = 1,
                pages = 1,
                results = 1
            )
        else:
            return AddedGetAvailability200(
        )
        """

    def testAddedGetAvailability200(self):
        """Test AddedGetAvailability200"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()