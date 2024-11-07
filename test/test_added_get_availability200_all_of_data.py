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

from openapi_client.models.added_get_availability200_all_of_data import AddedGetAvailability200AllOfData

class TestAddedGetAvailability200AllOfData(unittest.TestCase):
    """AddedGetAvailability200AllOfData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddedGetAvailability200AllOfData:
        """Test AddedGetAvailability200AllOfData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddedGetAvailability200AllOfData`
        """
        model = AddedGetAvailability200AllOfData()
        if include_optional:
            return AddedGetAvailability200AllOfData(
                available = ["Linodes","NodeBalancers"],
                region = 'us-east',
                unavailable = ["Kubernetes","Block Storage"]
            )
        else:
            return AddedGetAvailability200AllOfData(
        )
        """

    def testAddedGetAvailability200AllOfData(self):
        """Test AddedGetAvailability200AllOfData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()