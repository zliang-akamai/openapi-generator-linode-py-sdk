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

from openapi_client.models.post_databases_mysql_instances_request import PostDatabasesMysqlInstancesRequest

class TestPostDatabasesMysqlInstancesRequest(unittest.TestCase):
    """PostDatabasesMysqlInstancesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostDatabasesMysqlInstancesRequest:
        """Test PostDatabasesMysqlInstancesRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostDatabasesMysqlInstancesRequest`
        """
        model = PostDatabasesMysqlInstancesRequest()
        if include_optional:
            return PostDatabasesMysqlInstancesRequest(
                allow_list = ["203.0.113.1/32","192.0.1.0/24"],
                cluster_size = 3,
                encrypted = False,
                engine = 'mysql/8.0.26',
                label = 'example-db',
                region = 'us-east',
                replication_type = 'semi_synch',
                ssl_connection = True,
                type = 'g6-dedicated-2'
            )
        else:
            return PostDatabasesMysqlInstancesRequest(
                engine = 'mysql/8.0.26',
                label = 'example-db',
                region = 'us-east',
                type = 'g6-dedicated-2',
        )
        """

    def testPostDatabasesMysqlInstancesRequest(self):
        """Test PostDatabasesMysqlInstancesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
