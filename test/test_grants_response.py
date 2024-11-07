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

from openapi_client.models.grants_response import GrantsResponse

class TestGrantsResponse(unittest.TestCase):
    """GrantsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GrantsResponse:
        """Test GrantsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GrantsResponse`
        """
        model = GrantsResponse()
        if include_optional:
            return GrantsResponse(
                database = [
                    openapi_client.models.get_user_grants_200_response_database_inner.get_user_grants_200_response_database_inner(
                        id = 123, 
                        label = 'example-entity', 
                        permissions = 'read_only', )
                    ],
                domain = [
                    openapi_client.models.get_user_grants_200_response_database_inner.get_user_grants_200_response_database_inner(
                        id = 123, 
                        label = 'example-entity', 
                        permissions = 'read_only', )
                    ],
                firewall = [
                    openapi_client.models.get_user_grants_200_response_database_inner.get_user_grants_200_response_database_inner(
                        id = 123, 
                        label = 'example-entity', 
                        permissions = 'read_only', )
                    ],
                var_global = openapi_client.models.get_user_grants_200_response_global.get_user_grants_200_response_global(
                    account_access = 'read_only', 
                    add_databases = True, 
                    add_domains = True, 
                    add_firewalls = True, 
                    add_images = True, 
                    add_linodes = True, 
                    add_loadbalancers = True, 
                    add_longview = True, 
                    add_nodebalancers = True, 
                    add_placement_groups = True, 
                    add_stackscripts = True, 
                    add_volumes = True, 
                    add_vpcs = True, 
                    cancel_account = False, 
                    child_account_access = True, 
                    longview_subscription = True, ),
                image = [
                    openapi_client.models.get_user_grants_200_response_database_inner.get_user_grants_200_response_database_inner(
                        id = 123, 
                        label = 'example-entity', 
                        permissions = 'read_only', )
                    ],
                linode = [
                    openapi_client.models.get_user_grants_200_response_database_inner.get_user_grants_200_response_database_inner(
                        id = 123, 
                        label = 'example-entity', 
                        permissions = 'read_only', )
                    ],
                longview = [
                    openapi_client.models.get_user_grants_200_response_database_inner.get_user_grants_200_response_database_inner(
                        id = 123, 
                        label = 'example-entity', 
                        permissions = 'read_only', )
                    ],
                nodebalancer = [
                    openapi_client.models.get_user_grants_200_response_database_inner.get_user_grants_200_response_database_inner(
                        id = 123, 
                        label = 'example-entity', 
                        permissions = 'read_only', )
                    ],
                placement_group = [
                    openapi_client.models.get_user_grants_200_response_database_inner.get_user_grants_200_response_database_inner(
                        id = 123, 
                        label = 'example-entity', 
                        permissions = 'read_only', )
                    ],
                stackscript = [
                    openapi_client.models.get_user_grants_200_response_database_inner.get_user_grants_200_response_database_inner(
                        id = 123, 
                        label = 'example-entity', 
                        permissions = 'read_only', )
                    ],
                volume = [
                    openapi_client.models.get_user_grants_200_response_database_inner.get_user_grants_200_response_database_inner(
                        id = 123, 
                        label = 'example-entity', 
                        permissions = 'read_only', )
                    ],
                vpc = [
                    openapi_client.models.get_user_grants_200_response_database_inner.get_user_grants_200_response_database_inner(
                        id = 123, 
                        label = 'example-entity', 
                        permissions = 'read_only', )
                    ]
            )
        else:
            return GrantsResponse(
        )
        """

    def testGrantsResponse(self):
        """Test GrantsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
