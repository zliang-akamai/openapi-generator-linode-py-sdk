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

from openapi_client.api.networking_api import NetworkingApi


class TestNetworkingApi(unittest.TestCase):
    """NetworkingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NetworkingApi()

    def tearDown(self) -> None:
        pass

    def test_delete_firewall(self) -> None:
        """Test case for delete_firewall

        Delete a firewall
        """
        pass

    def test_delete_firewall_device(self) -> None:
        """Test case for delete_firewall_device

        Delete a firewall device
        """
        pass

    def test_delete_ipv6_range(self) -> None:
        """Test case for delete_ipv6_range

        Delete an IPv6 range
        """
        pass

    def test_get_firewall(self) -> None:
        """Test case for get_firewall

        Get a firewall
        """
        pass

    def test_get_firewall_device(self) -> None:
        """Test case for get_firewall_device

        Get a firewall device
        """
        pass

    def test_get_firewall_devices(self) -> None:
        """Test case for get_firewall_devices

        List firewall devices
        """
        pass

    def test_get_firewall_rule_version(self) -> None:
        """Test case for get_firewall_rule_version

        Get a firewall rule version
        """
        pass

    def test_get_firewall_rule_versions(self) -> None:
        """Test case for get_firewall_rule_versions

        List firewall rule versions
        """
        pass

    def test_get_firewall_rules(self) -> None:
        """Test case for get_firewall_rules

        List firewall rules
        """
        pass

    def test_get_firewalls(self) -> None:
        """Test case for get_firewalls

        List firewalls
        """
        pass

    def test_get_ip(self) -> None:
        """Test case for get_ip

        Get an IP address
        """
        pass

    def test_get_ips(self) -> None:
        """Test case for get_ips

        List IP addresses
        """
        pass

    def test_get_ipv6_pools(self) -> None:
        """Test case for get_ipv6_pools

        List IPv6 pools
        """
        pass

    def test_get_ipv6_range(self) -> None:
        """Test case for get_ipv6_range

        Get an IPv6 range
        """
        pass

    def test_get_ipv6_ranges(self) -> None:
        """Test case for get_ipv6_ranges

        List IPv6 ranges
        """
        pass

    def test_get_vlans(self) -> None:
        """Test case for get_vlans

        List VLANs
        """
        pass

    def test_post_allocate_ip(self) -> None:
        """Test case for post_allocate_ip

        Allocate an IP address
        """
        pass

    def test_post_assign_ips(self) -> None:
        """Test case for post_assign_ips

        Assign IP addresses
        """
        pass

    def test_post_assign_ipv4s(self) -> None:
        """Test case for post_assign_ipv4s

        Assign IPv4s to Linodes
        """
        pass

    def test_post_firewall_device(self) -> None:
        """Test case for post_firewall_device

        Create a firewall device
        """
        pass

    def test_post_firewalls(self) -> None:
        """Test case for post_firewalls

        Create a firewall
        """
        pass

    def test_post_ipv6_range(self) -> None:
        """Test case for post_ipv6_range

        Create an IPv6 range
        """
        pass

    def test_post_share_ips(self) -> None:
        """Test case for post_share_ips

        Share IP addresses
        """
        pass

    def test_post_share_ipv4s(self) -> None:
        """Test case for post_share_ipv4s

        Configure IPv4 sharing
        """
        pass

    def test_put_firewall(self) -> None:
        """Test case for put_firewall

        Update a firewall
        """
        pass

    def test_put_firewall_rules(self) -> None:
        """Test case for put_firewall_rules

        Update firewall rules
        """
        pass

    def test_put_ip(self) -> None:
        """Test case for put_ip

        Update an IP address's RDNS
        """
        pass


if __name__ == '__main__':
    unittest.main()
