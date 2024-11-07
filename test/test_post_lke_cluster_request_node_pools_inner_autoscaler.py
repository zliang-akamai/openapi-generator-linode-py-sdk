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

from openapi_client.models.post_lke_cluster_request_node_pools_inner_autoscaler import PostLkeClusterRequestNodePoolsInnerAutoscaler

class TestPostLkeClusterRequestNodePoolsInnerAutoscaler(unittest.TestCase):
    """PostLkeClusterRequestNodePoolsInnerAutoscaler unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostLkeClusterRequestNodePoolsInnerAutoscaler:
        """Test PostLkeClusterRequestNodePoolsInnerAutoscaler
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostLkeClusterRequestNodePoolsInnerAutoscaler`
        """
        model = PostLkeClusterRequestNodePoolsInnerAutoscaler()
        if include_optional:
            return PostLkeClusterRequestNodePoolsInnerAutoscaler(
                enabled = True,
                max = 12,
                min = 3
            )
        else:
            return PostLkeClusterRequestNodePoolsInnerAutoscaler(
        )
        """

    def testPostLkeClusterRequestNodePoolsInnerAutoscaler(self):
        """Test PostLkeClusterRequestNodePoolsInnerAutoscaler"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()