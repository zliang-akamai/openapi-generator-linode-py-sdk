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

from openapi_client.models.put_object_storage_bucket_acl_request import PutObjectStorageBucketAclRequest

class TestPutObjectStorageBucketAclRequest(unittest.TestCase):
    """PutObjectStorageBucketAclRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PutObjectStorageBucketAclRequest:
        """Test PutObjectStorageBucketAclRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PutObjectStorageBucketAclRequest`
        """
        model = PutObjectStorageBucketAclRequest()
        if include_optional:
            return PutObjectStorageBucketAclRequest(
                acl = 'public-read',
                name = ''
            )
        else:
            return PutObjectStorageBucketAclRequest(
                acl = 'public-read',
                name = '',
        )
        """

    def testPutObjectStorageBucketAclRequest(self):
        """Test PutObjectStorageBucketAclRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()