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

from openapi_client.models.linode_placement_group import LinodePlacementGroup

class TestLinodePlacementGroup(unittest.TestCase):
    """LinodePlacementGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinodePlacementGroup:
        """Test LinodePlacementGroup
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LinodePlacementGroup`
        """
        model = LinodePlacementGroup()
        if include_optional:
            return LinodePlacementGroup(
                id = 528,
                label = 'PG_Miami_failover',
                migrating_to = '2468',
                placement_group_policy = 'strict',
                placement_group_type = 'anti-affinity:local'
            )
        else:
            return LinodePlacementGroup(
        )
        """

    def testLinodePlacementGroup(self):
        """Test LinodePlacementGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()