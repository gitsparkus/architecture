# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.platforms import Platforms  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPlatformsController(BaseTestCase):
    """PlatformsController integration test stubs"""

    def test_get_platform_list(self):
        """Test case for get_platform_list

        Метод получения списка платформ
        """
        response = self.client.open(
            '/api/v1//references/platforms',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
