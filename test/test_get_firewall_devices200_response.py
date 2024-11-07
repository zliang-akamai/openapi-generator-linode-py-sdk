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

from openapi_client.models.get_firewall_devices200_response import GetFirewallDevices200Response

class TestGetFirewallDevices200Response(unittest.TestCase):
    """GetFirewallDevices200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetFirewallDevices200Response:
        """Test GetFirewallDevices200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetFirewallDevices200Response`
        """
        model = GetFirewallDevices200Response()
        if include_optional:
            return GetFirewallDevices200Response(
                data = [{"created":"2018-01-01T00:01:01","entity":{"id":123,"label":"my-linode","type":"linode","url":"/v4/linode/instances/123"},"id":456,"updated":"2018-01-02T00:01:01"},{"created":"2018-01-01T00:01:01","entity":{"id":321,"label":"my-nodebalancer","type":"nodebalancer","url":"/v4/nodebalancers/123"},"id":654,"updated":"2018-01-02T00:01:01"}],
                page = 1,
                pages = 1,
                results = 1
            )
        else:
            return GetFirewallDevices200Response(
        )
        """

    def testGetFirewallDevices200Response(self):
        """Test GetFirewallDevices200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()