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

from openapi_client.models.get_lke_cluster_acl404_response import GetLkeClusterAcl404Response

class TestGetLkeClusterAcl404Response(unittest.TestCase):
    """GetLkeClusterAcl404Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLkeClusterAcl404Response:
        """Test GetLkeClusterAcl404Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLkeClusterAcl404Response`
        """
        model = GetLkeClusterAcl404Response()
        if include_optional:
            return GetLkeClusterAcl404Response(
                errors = [
                    openapi_client.models.get_lke_cluster_acl_404_response_errors_inner.get_lke_cluster_acl_404_response_errors_inner(
                        field = 'acl', 
                        reason = 'Not Found.', )
                    ]
            )
        else:
            return GetLkeClusterAcl404Response(
        )
        """

    def testGetLkeClusterAcl404Response(self):
        """Test GetLkeClusterAcl404Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
