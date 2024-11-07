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

from openapi_client.models.get_ticket_replies200_response_data_inner import GetTicketReplies200ResponseDataInner

class TestGetTicketReplies200ResponseDataInner(unittest.TestCase):
    """GetTicketReplies200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTicketReplies200ResponseDataInner:
        """Test GetTicketReplies200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTicketReplies200ResponseDataInner`
        """
        model = GetTicketReplies200ResponseDataInner()
        if include_optional:
            return GetTicketReplies200ResponseDataInner(
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = 'John Q. Linode',
                description = 'Hello,\nI'm sorry to hear that you are having trouble resetting the root password of your Linode. Just to be sure, have you tried to follow the instructions in our online documentation? The link is here:\n \nhttps://linode.com/docs/guides/reset-the-root-password-on-your-linode/ \n\nIf you have, please reply with any additional steps you have also taken.\n\nRegards, Linode Support Team',
                from_linode = True,
                gravatar_id = '474a1b7373ae0be4132649e69c36ce30',
                id = 11223345
            )
        else:
            return GetTicketReplies200ResponseDataInner(
        )
        """

    def testGetTicketReplies200ResponseDataInner(self):
        """Test GetTicketReplies200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
