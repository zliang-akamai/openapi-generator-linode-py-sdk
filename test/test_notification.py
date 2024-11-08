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

from openapi_client.models.notification import Notification

class TestNotification(unittest.TestCase):
    """Notification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Notification:
        """Test Notification
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Notification`
        """
        model = Notification()
        if include_optional:
            return Notification(
                body = '',
                entity = openapi_client.models.get_notifications_200_response_data_inner_entity.get_notifications_200_response_data_inner_entity(
                    id = 3456, 
                    label = 'Linode not booting.', 
                    type = 'ticket', 
                    url = '/support/tickets/3456', ),
                label = 'You have an important ticket open!',
                message = 'You have an important ticket open!',
                severity = 'major',
                type = 'ticket_important',
                until = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                when = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Notification(
        )
        """

    def testNotification(self):
        """Test Notification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
