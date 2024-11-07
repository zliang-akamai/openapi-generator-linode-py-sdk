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

from openapi_client.models.get_tagged_objects200_response_data_inner_data import GetTaggedObjects200ResponseDataInnerData

class TestGetTaggedObjects200ResponseDataInnerData(unittest.TestCase):
    """GetTaggedObjects200ResponseDataInnerData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTaggedObjects200ResponseDataInnerData:
        """Test GetTaggedObjects200ResponseDataInnerData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTaggedObjects200ResponseDataInnerData`
        """
        model = GetTaggedObjects200ResponseDataInnerData()
        if include_optional:
            return GetTaggedObjects200ResponseDataInnerData(
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
                capabilities = [Block Storage Encryption],
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                disk_encryption = 'enabled',
                group = '0',
                has_user_data = True,
                host_uuid = '',
                hypervisor = 'kvm',
                id = 12345,
                image = 'linode/debian9',
                ipv4 = '203.0.113.1',
                ipv6 = '',
                label = 'balancer12345',
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
                status = 'active',
                tags = [example tag, another example],
                type = 'g6-standard-1',
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                watchdog_enabled = True,
                axfr_ips = [],
                description = '0',
                domain = 'example.org',
                expire_sec = 300,
                master_ips = [],
                refresh_sec = 300,
                retry_sec = 300,
                soa_email = 'admin@example.org',
                ttl_sec = 300,
                encryption = 'enabled',
                filesystem_path = '/dev/disk/by-id/scsi-0Linode_Volume_my-volume',
                hardware_type = 'nvme',
                linode_id = 12346,
                linode_label = 'linode123',
                size = 30,
                client_conn_throttle = 0,
                hostname = '192.0.2.1.ip.linodeusercontent.com',
                transfer = openapi_client.models.node_balancer_transfer.NodeBalancer_transfer(
                    in = 28.91200828552246, 
                    out = 3.5487728118896484, 
                    total = 32.46078109741211, )
            )
        else:
            return GetTaggedObjects200ResponseDataInnerData(
        )
        """

    def testGetTaggedObjects200ResponseDataInnerData(self):
        """Test GetTaggedObjects200ResponseDataInnerData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
