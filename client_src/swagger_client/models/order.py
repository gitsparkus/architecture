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

class Order(object):
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
        'name': 'str',
        'description': 'str',
        'client_id': 'int',
        'platform_id': 'int',
        'public_ip_flag': 'bool',
        'public_ip': 'str',
        'cpu': 'int',
        'ram': 'int',
        'status': 'int',
        'disks': 'list[Disks]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'client_id': 'client_id',
        'platform_id': 'platform_id',
        'public_ip_flag': 'public_ip_flag',
        'public_ip': 'public_ip',
        'cpu': 'CPU',
        'ram': 'RAM',
        'status': 'status',
        'disks': 'disks'
    }

    def __init__(self, id=None, name=None, description=None, client_id=None, platform_id=None, public_ip_flag=None, public_ip=None, cpu=None, ram=None, status=None, disks=None):  # noqa: E501
        """Order - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._client_id = None
        self._platform_id = None
        self._public_ip_flag = None
        self._public_ip = None
        self._cpu = None
        self._ram = None
        self._status = None
        self._disks = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.client_id = client_id
        self.platform_id = platform_id
        if public_ip_flag is not None:
            self.public_ip_flag = public_ip_flag
        if public_ip is not None:
            self.public_ip = public_ip
        if cpu is not None:
            self.cpu = cpu
        if ram is not None:
            self.ram = ram
        if status is not None:
            self.status = status
        if disks is not None:
            self.disks = disks

    @property
    def id(self):
        """Gets the id of this Order.  # noqa: E501


        :return: The id of this Order.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Order.


        :param id: The id of this Order.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Order.  # noqa: E501


        :return: The name of this Order.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Order.


        :param name: The name of this Order.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Order.  # noqa: E501


        :return: The description of this Order.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Order.


        :param description: The description of this Order.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def client_id(self):
        """Gets the client_id of this Order.  # noqa: E501


        :return: The client_id of this Order.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Order.


        :param client_id: The client_id of this Order.  # noqa: E501
        :type: int
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def platform_id(self):
        """Gets the platform_id of this Order.  # noqa: E501


        :return: The platform_id of this Order.  # noqa: E501
        :rtype: int
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this Order.


        :param platform_id: The platform_id of this Order.  # noqa: E501
        :type: int
        """
        if platform_id is None:
            raise ValueError("Invalid value for `platform_id`, must not be `None`")  # noqa: E501

        self._platform_id = platform_id

    @property
    def public_ip_flag(self):
        """Gets the public_ip_flag of this Order.  # noqa: E501


        :return: The public_ip_flag of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._public_ip_flag

    @public_ip_flag.setter
    def public_ip_flag(self, public_ip_flag):
        """Sets the public_ip_flag of this Order.


        :param public_ip_flag: The public_ip_flag of this Order.  # noqa: E501
        :type: bool
        """

        self._public_ip_flag = public_ip_flag

    @property
    def public_ip(self):
        """Gets the public_ip of this Order.  # noqa: E501


        :return: The public_ip of this Order.  # noqa: E501
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this Order.


        :param public_ip: The public_ip of this Order.  # noqa: E501
        :type: str
        """

        self._public_ip = public_ip

    @property
    def cpu(self):
        """Gets the cpu of this Order.  # noqa: E501


        :return: The cpu of this Order.  # noqa: E501
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this Order.


        :param cpu: The cpu of this Order.  # noqa: E501
        :type: int
        """

        self._cpu = cpu

    @property
    def ram(self):
        """Gets the ram of this Order.  # noqa: E501


        :return: The ram of this Order.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this Order.


        :param ram: The ram of this Order.  # noqa: E501
        :type: int
        """

        self._ram = ram

    @property
    def status(self):
        """Gets the status of this Order.  # noqa: E501


        :return: The status of this Order.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.


        :param status: The status of this Order.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def disks(self):
        """Gets the disks of this Order.  # noqa: E501


        :return: The disks of this Order.  # noqa: E501
        :rtype: list[Disks]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this Order.


        :param disks: The disks of this Order.  # noqa: E501
        :type: list[Disks]
        """

        self._disks = disks

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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
