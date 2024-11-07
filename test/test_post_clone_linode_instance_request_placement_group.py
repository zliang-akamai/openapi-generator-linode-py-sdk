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

from openapi_client.models.post_clone_linode_instance_request_placement_group import PostCloneLinodeInstanceRequestPlacementGroup

class TestPostCloneLinodeInstanceRequestPlacementGroup(unittest.TestCase):
    """PostCloneLinodeInstanceRequestPlacementGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostCloneLinodeInstanceRequestPlacementGroup:
        """Test PostCloneLinodeInstanceRequestPlacementGroup
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostCloneLinodeInstanceRequestPlacementGroup`
        """
        model = PostCloneLinodeInstanceRequestPlacementGroup()
        if include_optional:
            return PostCloneLinodeInstanceRequestPlacementGroup(
                id = 528
            )
        else:
            return PostCloneLinodeInstanceRequestPlacementGroup(
                id = 528,
        )
        """

    def testPostCloneLinodeInstanceRequestPlacementGroup(self):
        """Test PostCloneLinodeInstanceRequestPlacementGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()