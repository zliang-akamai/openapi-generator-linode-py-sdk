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

from openapi_client.models.get_lke_cluster_pools200_response_data_inner_taints_inner import GetLkeClusterPools200ResponseDataInnerTaintsInner

class TestGetLkeClusterPools200ResponseDataInnerTaintsInner(unittest.TestCase):
    """GetLkeClusterPools200ResponseDataInnerTaintsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLkeClusterPools200ResponseDataInnerTaintsInner:
        """Test GetLkeClusterPools200ResponseDataInnerTaintsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLkeClusterPools200ResponseDataInnerTaintsInner`
        """
        model = GetLkeClusterPools200ResponseDataInnerTaintsInner()
        if include_optional:
            return GetLkeClusterPools200ResponseDataInnerTaintsInner(
                effect = 'NoSchedule',
                key = 'example.com/my-app',
                value = 'teamC'
            )
        else:
            return GetLkeClusterPools200ResponseDataInnerTaintsInner(
        )
        """

    def testGetLkeClusterPools200ResponseDataInnerTaintsInner(self):
        """Test GetLkeClusterPools200ResponseDataInnerTaintsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
