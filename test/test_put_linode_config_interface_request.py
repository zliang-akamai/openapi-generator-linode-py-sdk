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

from openapi_client.models.put_linode_config_interface_request import PutLinodeConfigInterfaceRequest

class TestPutLinodeConfigInterfaceRequest(unittest.TestCase):
    """PutLinodeConfigInterfaceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PutLinodeConfigInterfaceRequest:
        """Test PutLinodeConfigInterfaceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PutLinodeConfigInterfaceRequest`
        """
        model = PutLinodeConfigInterfaceRequest()
        if include_optional:
            return PutLinodeConfigInterfaceRequest(
                ip_ranges = ["10.0.0.64/26","fd04:495a:691c:971c::1:0/112"],
                ipv4 = openapi_client.models.post_linode_instance_request_all_of_interfaces_inner_ipv4.post_linode_instance_request_allOf_interfaces_inner_ipv4(
                    nat_1_1 = '203.0.113.2', 
                    vpc = '10.0.0.2', ),
                primary = True
            )
        else:
            return PutLinodeConfigInterfaceRequest(
        )
        """

    def testPutLinodeConfigInterfaceRequest(self):
        """Test PutLinodeConfigInterfaceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
