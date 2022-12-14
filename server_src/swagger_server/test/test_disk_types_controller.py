# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.disk_types import DiskTypes  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDiskTypesController(BaseTestCase):
    """DiskTypesController integration test stubs"""

    def test_get_disk_types_list(self):
        """Test case for get_disk_types_list

        Метод получения списка типов дисков
        """
        response = self.client.open(
            '/api/v1//references/disctypes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
