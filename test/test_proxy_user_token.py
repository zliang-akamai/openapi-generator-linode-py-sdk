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

from openapi_client.models.proxy_user_token import ProxyUserToken

class TestProxyUserToken(unittest.TestCase):
    """ProxyUserToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProxyUserToken:
        """Test ProxyUserToken
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProxyUserToken`
        """
        model = ProxyUserToken()
        if include_optional:
            return ProxyUserToken(
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expiry = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = 918,
                label = 'parent1_1234_2024-05-01T00:01:01',
                scopes = '*',
                token = 'abcdefghijklmnop'
            )
        else:
            return ProxyUserToken(
        )
        """

    def testProxyUserToken(self):
        """Test ProxyUserToken"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
