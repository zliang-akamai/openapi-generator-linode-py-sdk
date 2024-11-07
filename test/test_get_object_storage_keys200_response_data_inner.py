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

from openapi_client.models.get_object_storage_keys200_response_data_inner import GetObjectStorageKeys200ResponseDataInner

class TestGetObjectStorageKeys200ResponseDataInner(unittest.TestCase):
    """GetObjectStorageKeys200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetObjectStorageKeys200ResponseDataInner:
        """Test GetObjectStorageKeys200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetObjectStorageKeys200ResponseDataInner`
        """
        model = GetObjectStorageKeys200ResponseDataInner()
        if include_optional:
            return GetObjectStorageKeys200ResponseDataInner(
                access_key = 'KVAKUTGBA4WTR2NSJQ81',
                bucket_access = [
                    openapi_client.models.get_object_storage_keys_200_response_data_inner_bucket_access_inner.get_object_storage_keys_200_response_data_inner_bucket_access_inner(
                        bucket_name = 'example-bucket', 
                        cluster = 'us-west-1', 
                        permissions = 'read_only', 
                        region = 'us-west', )
                    ],
                id = 123,
                label = 'my-key',
                limited = True,
                regions = [
                    openapi_client.models.get_object_storage_keys_200_response_data_inner_regions_inner.get_object_storage_keys_200_response_data_inner_regions_inner(
                        id = 'us-west', 
                        s3_endpoint = 'us-west-00.linodeobjects.com', )
                    ],
                secret_key = ''
            )
        else:
            return GetObjectStorageKeys200ResponseDataInner(
        )
        """

    def testGetObjectStorageKeys200ResponseDataInner(self):
        """Test GetObjectStorageKeys200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
