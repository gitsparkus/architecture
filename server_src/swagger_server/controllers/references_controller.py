import connexion
import six

from swagger_server.models.disk_types import DiskTypes  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.platforms import Platforms  # noqa: E501
from swagger_server import util


def get_disk_types_list():  # noqa: E501
    """Метод получения списка типов дисков

     # noqa: E501


    :rtype: DiskTypes
    """
    return 'do some magic!'


def get_platform_list():  # noqa: E501
    """Метод получения списка платформ

     # noqa: E501


    :rtype: Platforms
    """
    return 'do some magic!'
