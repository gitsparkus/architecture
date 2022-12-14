# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Platform(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: str=None):  # noqa: E501
        """Platform - a model defined in Swagger

        :param id: The id of this Platform.  # noqa: E501
        :type id: int
        :param name: The name of this Platform.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'id': int,
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name'
        }
        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'Platform':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Platform of this Platform.  # noqa: E501
        :rtype: Platform
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Platform.


        :return: The id of this Platform.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Platform.


        :param id: The id of this Platform.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Platform.


        :return: The name of this Platform.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Platform.


        :param name: The name of this Platform.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name
