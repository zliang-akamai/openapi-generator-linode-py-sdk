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

from openapi_client.models.get_node_balancer_configs200_response_data_inner import GetNodeBalancerConfigs200ResponseDataInner

class TestGetNodeBalancerConfigs200ResponseDataInner(unittest.TestCase):
    """GetNodeBalancerConfigs200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetNodeBalancerConfigs200ResponseDataInner:
        """Test GetNodeBalancerConfigs200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetNodeBalancerConfigs200ResponseDataInner`
        """
        model = GetNodeBalancerConfigs200ResponseDataInner()
        if include_optional:
            return GetNodeBalancerConfigs200ResponseDataInner(
                algorithm = 'roundrobin',
                check = 'none',
                check_attempts = 3,
                check_body = 'it works',
                check_interval = 90,
                check_passive = True,
                check_path = '/test',
                check_timeout = 10,
                cipher_suite = 'recommended',
                id = 4567,
                nodebalancer_id = 12345,
                nodes_status = openapi_client.models.get_node_balancer_configs_200_response_data_inner_nodes_status.get_node_balancer_configs_200_response_data_inner_nodes_status(
                    down = 0, 
                    up = 4, ),
                port = 80,
                protocol = 'http',
                proxy_protocol = 'none',
                ssl_cert = '<REDACTED>',
                ssl_commonname = 'www.example.com',
                ssl_fingerprint = '00:01:02:03:04:05:06:07:08:09:0A:0B:0C:0D:0E:0F:10:11:12:13',
                ssl_key = '<REDACTED>',
                stickiness = 'none'
            )
        else:
            return GetNodeBalancerConfigs200ResponseDataInner(
        )
        """

    def testGetNodeBalancerConfigs200ResponseDataInner(self):
        """Test GetNodeBalancerConfigs200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()