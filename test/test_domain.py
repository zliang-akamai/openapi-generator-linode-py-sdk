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

from openapi_client.models.domain import Domain

class TestDomain(unittest.TestCase):
    """Domain unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Domain:
        """Test Domain
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Domain`
        """
        model = Domain()
        if include_optional:
            return Domain(
                axfr_ips = [],
                description = '0',
                domain = 'example.org',
                expire_sec = 300,
                group = '0',
                id = 1234,
                master_ips = [],
                refresh_sec = 300,
                retry_sec = 300,
                soa_email = 'admin@example.org',
                status = 'active',
                tags = ["example tag","another example"],
                ttl_sec = 300,
                type = 'master'
            )
        else:
            return Domain(
        )
        """

    def testDomain(self):
        """Test Domain"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
