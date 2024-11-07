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

from openapi_client.models.post_clone_linode_instance_request import PostCloneLinodeInstanceRequest

class TestPostCloneLinodeInstanceRequest(unittest.TestCase):
    """PostCloneLinodeInstanceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostCloneLinodeInstanceRequest:
        """Test PostCloneLinodeInstanceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostCloneLinodeInstanceRequest`
        """
        model = PostCloneLinodeInstanceRequest()
        if include_optional:
            return PostCloneLinodeInstanceRequest(
                backups_enabled = True,
                configs = [
                    23456
                    ],
                disks = [
                    25674
                    ],
                group = 'Linode-Group',
                label = 'cloned-linode',
                linode_id = 124,
                metadata = openapi_client.models.post_linode_instance_request_all_of_metadata.post_linode_instance_request_allOf_metadata(
                    user_data = '[B@3bbeee64', ),
                placement_group = openapi_client.models.post_clone_linode_instance_request_placement_group.post_clone_linode_instance_request_placement_group(
                    id = 528, ),
                private_ip = True,
                region = 'us-east',
                type = 'g6-standard-2'
            )
        else:
            return PostCloneLinodeInstanceRequest(
        )
        """

    def testPostCloneLinodeInstanceRequest(self):
        """Test PostCloneLinodeInstanceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()