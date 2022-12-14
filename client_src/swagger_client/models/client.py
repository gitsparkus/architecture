# coding: utf-8

"""
    Заказ на ресурсы облака

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Client(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'fullname': 'str',
        'login': 'str'
    }

    attribute_map = {
        'id': 'id',
        'fullname': 'fullname',
        'login': 'login'
    }

    def __init__(self, id=None, fullname=None, login=None):  # noqa: E501
        """Client - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._fullname = None
        self._login = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.fullname = fullname
        self.login = login

    @property
    def id(self):
        """Gets the id of this Client.  # noqa: E501


        :return: The id of this Client.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Client.


        :param id: The id of this Client.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def fullname(self):
        """Gets the fullname of this Client.  # noqa: E501


        :return: The fullname of this Client.  # noqa: E501
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        """Sets the fullname of this Client.


        :param fullname: The fullname of this Client.  # noqa: E501
        :type: str
        """
        if fullname is None:
            raise ValueError("Invalid value for `fullname`, must not be `None`")  # noqa: E501

        self._fullname = fullname

    @property
    def login(self):
        """Gets the login of this Client.  # noqa: E501


        :return: The login of this Client.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this Client.


        :param login: The login of this Client.  # noqa: E501
        :type: str
        """
        if login is None:
            raise ValueError("Invalid value for `login`, must not be `None`")  # noqa: E501

        self._login = login

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Client, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Client):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
