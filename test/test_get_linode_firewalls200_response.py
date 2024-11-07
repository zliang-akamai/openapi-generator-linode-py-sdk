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

from openapi_client.models.get_linode_firewalls200_response import GetLinodeFirewalls200Response

class TestGetLinodeFirewalls200Response(unittest.TestCase):
    """GetLinodeFirewalls200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLinodeFirewalls200Response:
        """Test GetLinodeFirewalls200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLinodeFirewalls200Response`
        """
        model = GetLinodeFirewalls200Response()
        if include_optional:
            return GetLinodeFirewalls200Response(
                data = [
                    openapi_client.models.get_linode_firewalls_200_response_data_inner.get_linode_firewalls_200_response_data_inner(
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = 123, 
                        label = 'firewall123', 
                        rules = openapi_client.models.get_linode_firewalls_200_response_data_inner_rules.get_linode_firewalls_200_response_data_inner_rules(
                            fingerprint = '997dd135', 
                            inbound = [
                                openapi_client.models.get_linode_firewalls_200_response_data_inner_rules_inbound_inner.get_linode_firewalls_200_response_data_inner_rules_inbound_inner(
                                    action = 'ACCEPT', 
                                    addresses = openapi_client.models.get_linode_firewalls_200_response_data_inner_rules_inbound_inner_addresses.get_linode_firewalls_200_response_data_inner_rules_inbound_inner_addresses(
                                        ipv4 = ["192.0.2.0/24","198.51.100.2/32"], 
                                        ipv6 = ["2001:DB8::/128"], ), 
                                    description = 'An example firewall rule description.', 
                                    label = 'firewallrule123', 
                                    ports = '22-24, 80, 443', 
                                    protocol = 'TCP', )
                                ], 
                            inbound_policy = 'DROP', 
                            outbound = [
                                openapi_client.models.get_linode_firewalls_200_response_data_inner_rules_inbound_inner.get_linode_firewalls_200_response_data_inner_rules_inbound_inner(
                                    action = 'ACCEPT', 
                                    description = 'An example firewall rule description.', 
                                    label = 'firewallrule123', 
                                    ports = '22-24, 80, 443', 
                                    protocol = 'TCP', )
                                ], 
                            outbound_policy = 'DROP', 
                            version = 1, ), 
                        status = 'enabled', 
                        tags = ["example tag","another example"], 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                page = 1,
                pages = 1,
                results = 1
            )
        else:
            return GetLinodeFirewalls200Response(
        )
        """

    def testGetLinodeFirewalls200Response(self):
        """Test GetLinodeFirewalls200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()