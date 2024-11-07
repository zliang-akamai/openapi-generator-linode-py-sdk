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

from openapi_client.models.post_firewall_device_request import PostFirewallDeviceRequest

class TestPostFirewallDeviceRequest(unittest.TestCase):
    """PostFirewallDeviceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostFirewallDeviceRequest:
        """Test PostFirewallDeviceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostFirewallDeviceRequest`
        """
        model = PostFirewallDeviceRequest()
        if include_optional:
            return PostFirewallDeviceRequest(
                id = 123,
                label = 'my-linode',
                type = 'linode',
                url = '/v4/linode/instances/123'
            )
        else:
            return PostFirewallDeviceRequest(
                id = 123,
                type = 'linode',
        )
        """

    def testPostFirewallDeviceRequest(self):
        """Test PostFirewallDeviceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
