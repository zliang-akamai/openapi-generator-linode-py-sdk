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

from openapi_client.models.get_tags200_response_data_inner import GetTags200ResponseDataInner

class TestGetTags200ResponseDataInner(unittest.TestCase):
    """GetTags200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTags200ResponseDataInner:
        """Test GetTags200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTags200ResponseDataInner`
        """
        model = GetTags200ResponseDataInner()
        if include_optional:
            return GetTags200ResponseDataInner(
                label = 'example tag'
            )
        else:
            return GetTags200ResponseDataInner(
        )
        """

    def testGetTags200ResponseDataInner(self):
        """Test GetTags200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
