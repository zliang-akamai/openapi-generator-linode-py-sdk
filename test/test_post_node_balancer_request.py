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

from openapi_client.models.post_node_balancer_request import PostNodeBalancerRequest

class TestPostNodeBalancerRequest(unittest.TestCase):
    """PostNodeBalancerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostNodeBalancerRequest:
        """Test PostNodeBalancerRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostNodeBalancerRequest`
        """
        model = PostNodeBalancerRequest()
        if include_optional:
            return PostNodeBalancerRequest(
                client_conn_throttle = 0,
                configs = [
                    openapi_client.models.post_node_balancer_request_configs_inner.post_node_balancer_request_configs_inner(
                        algorithm = 'roundrobin', 
                        check = 'none', 
                        check_attempts = 3, 
                        check_body = 'it works', 
                        check_interval = 90, 
                        check_passive = True, 
                        check_path = '/test', 
                        check_timeout = 10, 
                        cipher_suite = 'recommended', 
                        nodes = [
                            openapi_client.models.post_node_balancer_request_configs_inner_nodes_inner.post_node_balancer_request_configs_inner_nodes_inner(
                                address = '192.168.210.120:80', 
                                config_id = 4567, 
                                id = 54321, 
                                label = 'node54321', 
                                mode = 'accept', 
                                nodebalancer_id = 12345, 
                                status = 'UP', 
                                weight = 50, )
                            ], 
                        port = 80, 
                        protocol = 'http', 
                        proxy_protocol = 'none', 
                        ssl_cert = '<REDACTED>', 
                        ssl_key = '<REDACTED>', 
                        stickiness = 'none', )
                    ],
                firewall_id = 56,
                label = 'balancer12345',
                region = 'us-east',
                tags = ["test","web-dev-team"]
            )
        else:
            return PostNodeBalancerRequest(
                region = 'us-east',
        )
        """

    def testPostNodeBalancerRequest(self):
        """Test PostNodeBalancerRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()