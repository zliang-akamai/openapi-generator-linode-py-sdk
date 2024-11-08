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

from openapi_client.models.post_databases_postgre_sql_instances_request import PostDatabasesPostgreSqlInstancesRequest

class TestPostDatabasesPostgreSqlInstancesRequest(unittest.TestCase):
    """PostDatabasesPostgreSqlInstancesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostDatabasesPostgreSqlInstancesRequest:
        """Test PostDatabasesPostgreSqlInstancesRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostDatabasesPostgreSqlInstancesRequest`
        """
        model = PostDatabasesPostgreSqlInstancesRequest()
        if include_optional:
            return PostDatabasesPostgreSqlInstancesRequest(
                allow_list = ["203.0.113.1/32","192.0.1.0/24"],
                cluster_size = 3,
                encrypted = False,
                engine = 'postgresql/13.2',
                label = 'example-db',
                region = 'us-east',
                replication_commit_type = 'local',
                replication_type = 'async',
                ssl_connection = True,
                type = 'g6-dedicated-2'
            )
        else:
            return PostDatabasesPostgreSqlInstancesRequest(
                engine = 'postgresql/13.2',
                label = 'example-db',
                region = 'us-east',
                type = 'g6-dedicated-2',
        )
        """

    def testPostDatabasesPostgreSqlInstancesRequest(self):
        """Test PostDatabasesPostgreSqlInstancesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
