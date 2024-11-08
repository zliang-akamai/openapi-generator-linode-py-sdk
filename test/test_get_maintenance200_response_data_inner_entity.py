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

from openapi_client.models.get_maintenance200_response_data_inner_entity import GetMaintenance200ResponseDataInnerEntity

class TestGetMaintenance200ResponseDataInnerEntity(unittest.TestCase):
    """GetMaintenance200ResponseDataInnerEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetMaintenance200ResponseDataInnerEntity:
        """Test GetMaintenance200ResponseDataInnerEntity
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetMaintenance200ResponseDataInnerEntity`
        """
        model = GetMaintenance200ResponseDataInnerEntity()
        if include_optional:
            return GetMaintenance200ResponseDataInnerEntity(
                id = 1234,
                label = 'demo-linode',
                type = 'Linode',
                url = 'https://api.linode.com/v4/linode/instances/{linodeId}'
            )
        else:
            return GetMaintenance200ResponseDataInnerEntity(
        )
        """

    def testGetMaintenance200ResponseDataInnerEntity(self):
        """Test GetMaintenance200ResponseDataInnerEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
