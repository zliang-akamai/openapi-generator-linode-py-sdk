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

from openapi_client.models.added_get_maintenance200 import AddedGetMaintenance200

class TestAddedGetMaintenance200(unittest.TestCase):
    """AddedGetMaintenance200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddedGetMaintenance200:
        """Test AddedGetMaintenance200
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddedGetMaintenance200`
        """
        model = AddedGetMaintenance200()
        if include_optional:
            return AddedGetMaintenance200(
                data = [
                    openapi_client.models.get_maintenance_200_response_data_inner.get_maintenance_200_response_data_inner(
                        entity = openapi_client.models.get_maintenance_200_response_data_inner_entity.get_maintenance_200_response_data_inner_entity(
                            id = 1234, 
                            label = 'demo-linode', 
                            type = 'Linode', 
                            url = 'https://api.linode.com/v4/linode/instances/{linodeId}', ), 
                        reason = 'This maintenance will allow us to update the BIOS on the host's motherboard.', 
                        status = 'started', 
                        type = 'reboot', 
                        when = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                page = 1,
                pages = 1,
                results = 1
            )
        else:
            return AddedGetMaintenance200(
        )
        """

    def testAddedGetMaintenance200(self):
        """Test AddedGetMaintenance200"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
