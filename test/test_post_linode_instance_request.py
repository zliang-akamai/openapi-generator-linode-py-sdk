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

from openapi_client.models.post_linode_instance_request import PostLinodeInstanceRequest

class TestPostLinodeInstanceRequest(unittest.TestCase):
    """PostLinodeInstanceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostLinodeInstanceRequest:
        """Test PostLinodeInstanceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostLinodeInstanceRequest`
        """
        model = PostLinodeInstanceRequest()
        if include_optional:
            return PostLinodeInstanceRequest(
                authorized_keys = ["ssh-rsa AAAA_valid_public_ssh_key_123456785== user@their-computer"],
                authorized_users = ["myUser","secondaryUser"],
                booted = True,
                disk_encryption = 'enabled',
                image = 'linode/debian9',
                metadata = openapi_client.models.post_linode_instance_request_all_of_metadata.post_linode_instance_request_allOf_metadata(
                    user_data = '[B@3bbeee64', ),
                root_pass = 'aComplexP@ssword',
                stackscript_data = {"gh_username":"linode"},
                stackscript_id = 10079,
                backup_id = 1234,
                backups_enabled = True,
                firewall_id = 56,
                group = 'Linode-Group',
                interfaces = [{"id":101,"ipam_address":null,"ipv4":null,"label":null,"primary":false,"purpose":"public","subnet_id":null,"vpc_id":null},{"id":102,"ipam_address":"10.0.0.1/24","ipv4":{"nat_1_1":null,"vpc":"10.0.0.2"},"label":"vlan-1","primary":false,"purpose":"vlan","subnet_id":null,"vpc_id":null},{"id":103,"ipam_address":null,"ipv4":{"nat_1_1":"203.0.113.2","vpc":"10.0.1.2"},"label":null,"primary":true,"purpose":"vpc","subnet_id":101,"vpc_id":111}],
                label = 'linode123',
                placement_group = openapi_client.models.post_linode_instance_request_all_of_placement_group.post_linode_instance_request_allOf_placement_group(
                    id = 528, ),
                private_ip = True,
                region = 'us-east',
                swap_size = 512,
                tags = ["example tag","another example"],
                type = 'g6-standard-2'
            )
        else:
            return PostLinodeInstanceRequest(
                region = 'us-east',
                type = 'g6-standard-2',
        )
        """

    def testPostLinodeInstanceRequest(self):
        """Test PostLinodeInstanceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()