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

from openapi_client.models.post_linode_instance_request_all_of_interfaces_inner import PostLinodeInstanceRequestAllOfInterfacesInner

class TestPostLinodeInstanceRequestAllOfInterfacesInner(unittest.TestCase):
    """PostLinodeInstanceRequestAllOfInterfacesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostLinodeInstanceRequestAllOfInterfacesInner:
        """Test PostLinodeInstanceRequestAllOfInterfacesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostLinodeInstanceRequestAllOfInterfacesInner`
        """
        model = PostLinodeInstanceRequestAllOfInterfacesInner()
        if include_optional:
            return PostLinodeInstanceRequestAllOfInterfacesInner(
                active = True,
                id = 101,
                ip_ranges = ["10.0.0.64/26","fd04:495a:691c:971c::1:0/112"],
                ipam_address = '10.0.0.1/24',
                ipv4 = openapi_client.models.post_linode_instance_request_all_of_interfaces_inner_ipv4.post_linode_instance_request_allOf_interfaces_inner_ipv4(
                    nat_1_1 = '203.0.113.2', 
                    vpc = '10.0.0.2', ),
                label = 'example-interface',
                primary = True,
                purpose = 'vlan',
                subnet_id = 101,
                vpc_id = 111
            )
        else:
            return PostLinodeInstanceRequestAllOfInterfacesInner(
                purpose = 'vlan',
        )
        """

    def testPostLinodeInstanceRequestAllOfInterfacesInner(self):
        """Test PostLinodeInstanceRequestAllOfInterfacesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
