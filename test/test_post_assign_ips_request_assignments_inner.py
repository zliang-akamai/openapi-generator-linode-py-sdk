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

from openapi_client.models.post_assign_ips_request_assignments_inner import PostAssignIpsRequestAssignmentsInner

class TestPostAssignIpsRequestAssignmentsInner(unittest.TestCase):
    """PostAssignIpsRequestAssignmentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostAssignIpsRequestAssignmentsInner:
        """Test PostAssignIpsRequestAssignmentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostAssignIpsRequestAssignmentsInner`
        """
        model = PostAssignIpsRequestAssignmentsInner()
        if include_optional:
            return PostAssignIpsRequestAssignmentsInner(
                address = '192.0.2.1',
                linode_id = 123
            )
        else:
            return PostAssignIpsRequestAssignmentsInner(
                address = '192.0.2.1',
                linode_id = 123,
        )
        """

    def testPostAssignIpsRequestAssignmentsInner(self):
        """Test PostAssignIpsRequestAssignmentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
