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

from openapi_client.api.managed_api import ManagedApi


class TestManagedApi(unittest.TestCase):
    """ManagedApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ManagedApi()

    def tearDown(self) -> None:
        pass

    def test_delete_managed_contact(self) -> None:
        """Test case for delete_managed_contact

        Delete a managed contact
        """
        pass

    def test_delete_managed_service(self) -> None:
        """Test case for delete_managed_service

        Delete a managed service
        """
        pass

    def test_get_managed_contact(self) -> None:
        """Test case for get_managed_contact

        Get a managed contact
        """
        pass

    def test_get_managed_contacts(self) -> None:
        """Test case for get_managed_contacts

        List managed contacts
        """
        pass

    def test_get_managed_credential(self) -> None:
        """Test case for get_managed_credential

        Get a managed credential
        """
        pass

    def test_get_managed_credentials(self) -> None:
        """Test case for get_managed_credentials

        List managed credentials
        """
        pass

    def test_get_managed_issue(self) -> None:
        """Test case for get_managed_issue

        Get a managed issue
        """
        pass

    def test_get_managed_issues(self) -> None:
        """Test case for get_managed_issues

        List managed issues
        """
        pass

    def test_get_managed_linode_setting(self) -> None:
        """Test case for get_managed_linode_setting

        Get a Linode's managed settings
        """
        pass

    def test_get_managed_linode_settings(self) -> None:
        """Test case for get_managed_linode_settings

        List managed Linode settings
        """
        pass

    def test_get_managed_service(self) -> None:
        """Test case for get_managed_service

        Get a managed service
        """
        pass

    def test_get_managed_services(self) -> None:
        """Test case for get_managed_services

        List managed services
        """
        pass

    def test_get_managed_ssh_key(self) -> None:
        """Test case for get_managed_ssh_key

        Get a managed SSH key
        """
        pass

    def test_get_managed_stats(self) -> None:
        """Test case for get_managed_stats

        List managed stats
        """
        pass

    def test_post_disable_managed_service(self) -> None:
        """Test case for post_disable_managed_service

        Disable a managed service
        """
        pass

    def test_post_enable_managed_service(self) -> None:
        """Test case for post_enable_managed_service

        Enable a managed service
        """
        pass

    def test_post_managed_contact(self) -> None:
        """Test case for post_managed_contact

        Create a managed contact
        """
        pass

    def test_post_managed_credential(self) -> None:
        """Test case for post_managed_credential

        Create a managed credential
        """
        pass

    def test_post_managed_credential_revoke(self) -> None:
        """Test case for post_managed_credential_revoke

        Delete a managed credential
        """
        pass

    def test_post_managed_credential_username_password(self) -> None:
        """Test case for post_managed_credential_username_password

        Update a managed credential's username and password
        """
        pass

    def test_post_managed_service(self) -> None:
        """Test case for post_managed_service

        Create a managed service
        """
        pass

    def test_put_managed_contact(self) -> None:
        """Test case for put_managed_contact

        Update a managed contact
        """
        pass

    def test_put_managed_credential(self) -> None:
        """Test case for put_managed_credential

        Update a managed credential
        """
        pass

    def test_put_managed_linode_setting(self) -> None:
        """Test case for put_managed_linode_setting

        Update a Linode's managed settings
        """
        pass

    def test_put_managed_service(self) -> None:
        """Test case for put_managed_service

        Update a managed service
        """
        pass


if __name__ == '__main__':
    unittest.main()
