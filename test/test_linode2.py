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

from openapi_client.models.linode2 import Linode2

class TestLinode2(unittest.TestCase):
    """Linode2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Linode2:
        """Test Linode2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Linode2`
        """
        model = Linode2()
        if include_optional:
            return Linode2(
                alerts = openapi_client.models.linode_alerts.Linode_alerts(
                    cpu = 180, 
                    io = 10000, 
                    network_in = 10, 
                    network_out = 10, 
                    transfer_quota = 80, ),
                backups = openapi_client.models.linode_backups.Linode_backups(
                    available = True, 
                    enabled = True, 
                    last_successful = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    schedule = openapi_client.models.linode_backups_schedule.Linode_backups_schedule(
                        day = 'Saturday', 
                        window = 'W22', ), ),
                capabilities = ["Block Storage Encryption"],
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                disk_encryption = 'enabled',
                group = 'Linode-Group',
                has_user_data = True,
                host_uuid = '',
                hypervisor = 'kvm',
                id = 123,
                image = 'linode/debian9',
                ipv4 = ["203.0.113.1","192.0.2.1"],
                ipv6 = 'c001:d00d::1337/128',
                label = 'linode123',
                lke_cluster_id = 1,
                placement_group = openapi_client.models.linode_1_placement_group.Linode_1_placement_group(
                    id = 528, 
                    label = 'PG_Miami_failover', 
                    placement_group_policy = 'strict', 
                    placement_group_type = 'anti-affinity:local', ),
                region = 'us-east',
                specs = openapi_client.models.linode_specs.Linode_specs(
                    disk = 81920, 
                    gpus = 0, 
                    memory = 4096, 
                    transfer = 4000, 
                    vcpus = 2, ),
                status = 'running',
                tags = ["example tag","another example"],
                type = 'g6-standard-1',
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                watchdog_enabled = True
            )
        else:
            return Linode2(
        )
        """

    def testLinode2(self):
        """Test Linode2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
