import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.order import Order  # noqa: E501
from swagger_server.models.orders import Orders  # noqa: E501
from swagger_server import util


def create_order(body):  # noqa: E501
    """Метод создания заказа

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Order
    """
    if connexion.request.is_json:
        body = Order.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_order_by_id(order_id):  # noqa: E501
    """Метод отмены заказа по ID

     # noqa: E501

    :param order_id: Идентификатор заказа
    :type order_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_orders():  # noqa: E501
    """Метод получения списка заказов

     # noqa: E501


    :rtype: Orders
    """
    return 'do some magic!'


def get_order_by_id(order_id):  # noqa: E501
    """Метод получения заказа по ID

     # noqa: E501

    :param order_id: Идентификатор заказа
    :type order_id: str

    :rtype: Order
    """
    return 'do some magic!'
