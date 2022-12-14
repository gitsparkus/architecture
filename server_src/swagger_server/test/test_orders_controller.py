# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.order import Order  # noqa: E501
from swagger_server.models.orders import Orders  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrdersController(BaseTestCase):
    """OrdersController integration test stubs"""

    def test_create_order(self):
        """Test case for create_order

        Метод создания заказа
        """
        body = Order()
        response = self.client.open(
            '/api/v1//orders',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_order_by_id(self):
        """Test case for delete_order_by_id

        Метод отмены заказа по ID
        """
        response = self.client.open(
            '/api/v1//orders/{order_id}'.format(order_id='order_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_orders(self):
        """Test case for get_all_orders

        Метод получения списка заказов
        """
        response = self.client.open(
            '/api/v1//orders',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_order_by_id(self):
        """Test case for get_order_by_id

        Метод получения заказа по ID
        """
        response = self.client.open(
            '/api/v1//orders/{order_id}'.format(order_id='order_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
