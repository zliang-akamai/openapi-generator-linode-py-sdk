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

from openapi_client.models.get_linode_ips200_response_ipv6_link_local import GetLinodeIps200ResponseIpv6LinkLocal

class TestGetLinodeIps200ResponseIpv6LinkLocal(unittest.TestCase):
    """GetLinodeIps200ResponseIpv6LinkLocal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLinodeIps200ResponseIpv6LinkLocal:
        """Test GetLinodeIps200ResponseIpv6LinkLocal
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLinodeIps200ResponseIpv6LinkLocal`
        """
        model = GetLinodeIps200ResponseIpv6LinkLocal()
        if include_optional:
            return GetLinodeIps200ResponseIpv6LinkLocal(
                address = 'fe80::f03c:91ff:fe24:3a2f',
                gateway = 'fe80::1',
                linode_id = 123,
                prefix = 64,
                public = False,
                rdns = '',
                region = 'us-east',
                subnet_mask = 'ffff:ffff:ffff:ffff::',
                type = 'ipv6'
            )
        else:
            return GetLinodeIps200ResponseIpv6LinkLocal(
        )
        """

    def testGetLinodeIps200ResponseIpv6LinkLocal(self):
        """Test GetLinodeIps200ResponseIpv6LinkLocal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()