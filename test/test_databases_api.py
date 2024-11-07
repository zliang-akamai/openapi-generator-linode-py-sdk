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

from openapi_client.api.databases_api import DatabasesApi


class TestDatabasesApi(unittest.TestCase):
    """DatabasesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DatabasesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_database_mysql_instance_backup(self) -> None:
        """Test case for delete_database_mysql_instance_backup

        Delete a managed MySQL database backup
        """
        pass

    def test_delete_database_postgre_sql_instance_backup(self) -> None:
        """Test case for delete_database_postgre_sql_instance_backup

        Delete a managed PostgreSQL database backup
        """
        pass

    def test_delete_databases_mysql_instance(self) -> None:
        """Test case for delete_databases_mysql_instance

        Delete a managed MySQL database
        """
        pass

    def test_delete_databases_postgre_sql_instance(self) -> None:
        """Test case for delete_databases_postgre_sql_instance

        Delete a managed PostgreSQL database
        """
        pass

    def test_get_databases_engine(self) -> None:
        """Test case for get_databases_engine

        Get a managed database engine
        """
        pass

    def test_get_databases_engines(self) -> None:
        """Test case for get_databases_engines

        List managed database engines
        """
        pass

    def test_get_databases_instances(self) -> None:
        """Test case for get_databases_instances

        List managed databases
        """
        pass

    def test_get_databases_mysql_instance(self) -> None:
        """Test case for get_databases_mysql_instance

        Get a managed MySQL database
        """
        pass

    def test_get_databases_mysql_instance_backup(self) -> None:
        """Test case for get_databases_mysql_instance_backup

        Get a managed MySQL database backup
        """
        pass

    def test_get_databases_mysql_instance_backups(self) -> None:
        """Test case for get_databases_mysql_instance_backups

        List managed MySQL database backups
        """
        pass

    def test_get_databases_mysql_instance_credentials(self) -> None:
        """Test case for get_databases_mysql_instance_credentials

        Get managed MySQL database credentials
        """
        pass

    def test_get_databases_mysql_instance_ssl(self) -> None:
        """Test case for get_databases_mysql_instance_ssl

        Get a managed MySQL database SSL certificate
        """
        pass

    def test_get_databases_mysql_instances(self) -> None:
        """Test case for get_databases_mysql_instances

        List managed MySQL databases
        """
        pass

    def test_get_databases_postgre_sql_instance(self) -> None:
        """Test case for get_databases_postgre_sql_instance

        Get a managed PostgreSQL database
        """
        pass

    def test_get_databases_postgre_sql_instance_backups(self) -> None:
        """Test case for get_databases_postgre_sql_instance_backups

        List managed PostgreSQL database backups
        """
        pass

    def test_get_databases_postgre_sql_instance_credentials(self) -> None:
        """Test case for get_databases_postgre_sql_instance_credentials

        Get managed PostgreSQL database credentials
        """
        pass

    def test_get_databases_postgre_sql_instances(self) -> None:
        """Test case for get_databases_postgre_sql_instances

        List managed PostgreSQL databases
        """
        pass

    def test_get_databases_postgresql_instance_backup(self) -> None:
        """Test case for get_databases_postgresql_instance_backup

        Get a managed PostgreSQL database backup
        """
        pass

    def test_get_databases_postgresql_instance_ssl(self) -> None:
        """Test case for get_databases_postgresql_instance_ssl

        Get a managed PostgreSQL database SSL certificate
        """
        pass

    def test_get_databases_type(self) -> None:
        """Test case for get_databases_type

        Get a managed database type
        """
        pass

    def test_get_databases_types(self) -> None:
        """Test case for get_databases_types

        List managed database types
        """
        pass

    def test_post_databases_mysql_instance_backup(self) -> None:
        """Test case for post_databases_mysql_instance_backup

        Create a managed MySQL database backup snapshot
        """
        pass

    def test_post_databases_mysql_instance_backup_restore(self) -> None:
        """Test case for post_databases_mysql_instance_backup_restore

        Restore a managed MySQL database backup
        """
        pass

    def test_post_databases_mysql_instance_credentials_reset(self) -> None:
        """Test case for post_databases_mysql_instance_credentials_reset

        Reset managed MySQL database credentials
        """
        pass

    def test_post_databases_mysql_instance_patch(self) -> None:
        """Test case for post_databases_mysql_instance_patch

        Patch a managed MySQL database
        """
        pass

    def test_post_databases_mysql_instances(self) -> None:
        """Test case for post_databases_mysql_instances

        Create a managed MySQL database
        """
        pass

    def test_post_databases_postgre_sql_instance_backup(self) -> None:
        """Test case for post_databases_postgre_sql_instance_backup

        Create a managed PostgreSQL database backup snapshot
        """
        pass

    def test_post_databases_postgre_sql_instance_backup_restore(self) -> None:
        """Test case for post_databases_postgre_sql_instance_backup_restore

        Restore a managed PostgreSQL database backup
        """
        pass

    def test_post_databases_postgre_sql_instance_credentials_reset(self) -> None:
        """Test case for post_databases_postgre_sql_instance_credentials_reset

        Reset managed PostgreSQL database credentials
        """
        pass

    def test_post_databases_postgre_sql_instance_patch(self) -> None:
        """Test case for post_databases_postgre_sql_instance_patch

        Patch a managed PostgreSQL database
        """
        pass

    def test_post_databases_postgre_sql_instances(self) -> None:
        """Test case for post_databases_postgre_sql_instances

        Create a managed PostgreSQL database
        """
        pass

    def test_put_databases_mysql_instance(self) -> None:
        """Test case for put_databases_mysql_instance

        Update a managed MySQL database
        """
        pass

    def test_put_databases_postgre_sql_instance(self) -> None:
        """Test case for put_databases_postgre_sql_instance

        Update a managed PostgreSQL database
        """
        pass


if __name__ == '__main__':
    unittest.main()