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

from openapi_client.models.get_lke_cluster_acl200_response import GetLkeClusterAcl200Response

class TestGetLkeClusterAcl200Response(unittest.TestCase):
    """GetLkeClusterAcl200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLkeClusterAcl200Response:
        """Test GetLkeClusterAcl200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLkeClusterAcl200Response`
        """
        model = GetLkeClusterAcl200Response()
        if include_optional:
            return GetLkeClusterAcl200Response(
                acl = openapi_client.models.get_lke_cluster_acl_200_response_all_of_acl.get_lke_cluster_acl_200_response_allOf_acl(
                    addresses = openapi_client.models.get_lke_cluster_acl_200_response_all_of_acl_addresses.get_lke_cluster_acl_200_response_allOf_acl_addresses(
                        ipv4 = null, 
                        ipv6 = null, ), 
                    revision_id = null, )
            )
        else:
            return GetLkeClusterAcl200Response(
        )
        """

    def testGetLkeClusterAcl200Response(self):
        """Test GetLkeClusterAcl200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()