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

from openapi_client.models.post_ticket_request import PostTicketRequest

class TestPostTicketRequest(unittest.TestCase):
    """PostTicketRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostTicketRequest:
        """Test PostTicketRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostTicketRequest`
        """
        model = PostTicketRequest()
        if include_optional:
            return PostTicketRequest(
                database_id = 56,
                description = 'I'm having trouble setting the root password on my Linode. I tried following the instructions but something is not working and I'm not sure what I'm doing wrong. Can you please help me figure out how I can reset it?',
                domain_id = 56,
                firewall_id = 56,
                linode_id = 123,
                lkecluster_id = 123,
                longviewclient_id = 56,
                managed_issue = False,
                nodebalancer_id = 56,
                region = '',
                summary = 'Having trouble resetting root password on my Linode',
                vlan = '',
                volume_id = 56,
                vpc_id = 56
            )
        else:
            return PostTicketRequest(
                description = 'I'm having trouble setting the root password on my Linode. I tried following the instructions but something is not working and I'm not sure what I'm doing wrong. Can you please help me figure out how I can reset it?',
                summary = 'Having trouble resetting root password on my Linode',
        )
        """

    def testPostTicketRequest(self):
        """Test PostTicketRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()