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

from openapi_client.models.get_databases_mysql_instances200_response import GetDatabasesMysqlInstances200Response

class TestGetDatabasesMysqlInstances200Response(unittest.TestCase):
    """GetDatabasesMysqlInstances200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDatabasesMysqlInstances200Response:
        """Test GetDatabasesMysqlInstances200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDatabasesMysqlInstances200Response`
        """
        model = GetDatabasesMysqlInstances200Response()
        if include_optional:
            return GetDatabasesMysqlInstances200Response(
                page = 1,
                pages = 1,
                results = 1,
                data = [
                    openapi_client.models.get_databases_mysql_instances_200_response_all_of_data_inner.get_databases_mysql_instances_200_response_allOf_data_inner(
                        allow_list = ["203.0.113.1/32","192.0.1.0/24"], 
                        cluster_size = 3, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        encrypted = False, 
                        engine = 'mysql', 
                        hosts = openapi_client.models.get_databases_instances_200_response_all_of_data_inner_hosts.get_databases_instances_200_response_allOf_data_inner_hosts(
                            primary = 'lin-123-456-mysql-mysql-primary.servers.linodedb.net', 
                            secondary = 'lin-123-456-mysql-primary-private.servers.linodedb.net', ), 
                        id = 123, 
                        label = 'example-db', 
                        port = 3306, 
                        region = 'us-east', 
                        replication_type = 'semi_synch', 
                        ssl_connection = True, 
                        status = 'active', 
                        total_disk_size_gb = 15, 
                        type = 'g6-dedicated-2', 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updates = openapi_client.models.get_databases_instances_200_response_all_of_data_inner_updates.get_databases_instances_200_response_allOf_data_inner_updates(
                            day_of_week = 1, 
                            duration = 3, 
                            frequency = 'weekly', 
                            hour_of_day = 0, 
                            week_of_month = 1, ), 
                        used_disk_size_gb = 2, 
                        version = '8.0.26', )
                    ]
            )
        else:
            return GetDatabasesMysqlInstances200Response(
        )
        """

    def testGetDatabasesMysqlInstances200Response(self):
        """Test GetDatabasesMysqlInstances200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()