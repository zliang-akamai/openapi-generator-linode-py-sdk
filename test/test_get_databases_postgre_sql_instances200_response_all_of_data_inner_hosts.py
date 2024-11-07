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

from openapi_client.models.get_databases_postgre_sql_instances200_response_all_of_data_inner_hosts import GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts

class TestGetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts(unittest.TestCase):
    """GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts:
        """Test GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts`
        """
        model = GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts()
        if include_optional:
            return GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts(
                primary = 'lin-0000-000-pgsql-primary.servers.linodedb.net',
                secondary = 'lin-0000-000-pgsql-primary-private.servers.linodedb.net'
            )
        else:
            return GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts(
        )
        """

    def testGetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts(self):
        """Test GetDatabasesPostgreSqlInstances200ResponseAllOfDataInnerHosts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
