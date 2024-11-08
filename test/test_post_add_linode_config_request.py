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

from openapi_client.models.post_add_linode_config_request import PostAddLinodeConfigRequest

class TestPostAddLinodeConfigRequest(unittest.TestCase):
    """PostAddLinodeConfigRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostAddLinodeConfigRequest:
        """Test PostAddLinodeConfigRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostAddLinodeConfigRequest`
        """
        model = PostAddLinodeConfigRequest()
        if include_optional:
            return PostAddLinodeConfigRequest(
                comments = 'This is my main Config',
                devices = openapi_client.models.get_linode_configs_200_response_data_inner_devices.get_linode_configs_200_response_data_inner_devices(
                    sda = openapi_client.models.get_linode_configs_200_response_data_inner_devices_sda.get_linode_configs_200_response_data_inner_devices_sda(
                        disk_id = 124458, 
                        volume_id = 56, ), 
                    sdb = openapi_client.models.get_linode_configs_200_response_data_inner_devices_sda.get_linode_configs_200_response_data_inner_devices_sda(
                        disk_id = 124458, 
                        volume_id = 56, ), 
                    sdc = , 
                    sdd = , 
                    sde = , 
                    sdf = , 
                    sdg = , 
                    sdh = , ),
                helpers = openapi_client.models.get_linode_configs_200_response_data_inner_helpers.get_linode_configs_200_response_data_inner_helpers(
                    devtmpfs_automount = False, 
                    distro = True, 
                    modules_dep = True, 
                    network = True, 
                    updatedb_disabled = True, ),
                id = 23456,
                interfaces = [{"id":101,"ipam_address":null,"ipv4":null,"label":null,"primary":false,"purpose":"public","subnet_id":null,"vpc_id":null},{"id":102,"ipam_address":"10.0.0.1/24","ipv4":{"nat_1_1":null,"vpc":"10.0.0.2"},"label":"vlan-1","primary":false,"purpose":"vlan","subnet_id":null,"vpc_id":null},{"id":103,"ipam_address":null,"ipv4":{"nat_1_1":"203.0.113.2","vpc":"10.0.1.2"},"label":null,"primary":true,"purpose":"vpc","subnet_id":101,"vpc_id":111}],
                kernel = 'linode/latest-64bit',
                label = 'My Config',
                memory_limit = 2048,
                root_device = '/dev/sda',
                run_level = 'default',
                virt_mode = 'paravirt'
            )
        else:
            return PostAddLinodeConfigRequest(
                devices = openapi_client.models.get_linode_configs_200_response_data_inner_devices.get_linode_configs_200_response_data_inner_devices(
                    sda = openapi_client.models.get_linode_configs_200_response_data_inner_devices_sda.get_linode_configs_200_response_data_inner_devices_sda(
                        disk_id = 124458, 
                        volume_id = 56, ), 
                    sdb = openapi_client.models.get_linode_configs_200_response_data_inner_devices_sda.get_linode_configs_200_response_data_inner_devices_sda(
                        disk_id = 124458, 
                        volume_id = 56, ), 
                    sdc = , 
                    sdd = , 
                    sde = , 
                    sdf = , 
                    sdg = , 
                    sdh = , ),
                label = 'My Config',
        )
        """

    def testPostAddLinodeConfigRequest(self):
        """Test PostAddLinodeConfigRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
