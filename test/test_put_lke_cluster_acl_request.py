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

from openapi_client.models.put_lke_cluster_acl_request import PutLkeClusterAclRequest

class TestPutLkeClusterAclRequest(unittest.TestCase):
    """PutLkeClusterAclRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PutLkeClusterAclRequest:
        """Test PutLkeClusterAclRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PutLkeClusterAclRequest`
        """
        model = PutLkeClusterAclRequest()
        if include_optional:
            return PutLkeClusterAclRequest(
                acl = openapi_client.models.get_lke_clusters_200_response_data_inner_control_plane_acl.get_lke_clusters_200_response_data_inner_control_plane_acl(
                    addresses = openapi_client.models.get_lke_clusters_200_response_data_inner_control_plane_acl_addresses.get_lke_clusters_200_response_data_inner_control_plane_acl_addresses(
                        ipv4 = ["203.0.113.1","192.0.2.0/24"], 
                        ipv6 = ["2001:db8:1234:abcd::/64"], ), 
                    enabled = True, 
                    revision_id = '20240127r001', )
            )
        else:
            return PutLkeClusterAclRequest(
        )
        """

    def testPutLkeClusterAclRequest(self):
        """Test PutLkeClusterAclRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
