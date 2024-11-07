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

from openapi_client.models.get_object_storage_transfer200_response import GetObjectStorageTransfer200Response

class TestGetObjectStorageTransfer200Response(unittest.TestCase):
    """GetObjectStorageTransfer200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetObjectStorageTransfer200Response:
        """Test GetObjectStorageTransfer200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetObjectStorageTransfer200Response`
        """
        model = GetObjectStorageTransfer200Response()
        if include_optional:
            return GetObjectStorageTransfer200Response(
                used = 12956600198
            )
        else:
            return GetObjectStorageTransfer200Response(
        )
        """

    def testGetObjectStorageTransfer200Response(self):
        """Test GetObjectStorageTransfer200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()