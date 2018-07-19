#
# Template source downloaded from:
# https://github.com/swagger-api/swagger-codegen/tree/master/modules/swagger-codegen/src/main/resources/python
#
# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six


class ReadItem(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'field_id': 'str',
        'data': 'str',
        'children': 'list[ReadStatusItem]',
        'node_id': 'str'
    }

    attribute_map = {
        'field_id': 'fieldId',
        'data': 'data',
        'children': 'children',
        'node_id': 'nodeId'
    }

    def __init__(self, field_id=None, data=None, children=None, node_id=None):  # noqa: E501
        """ReadItem - a model defined in Swagger"""  # noqa: E501

        self._field_id = None
        self._data = None
        self._children = None
        self._node_id = None
        self.discriminator = None

        self.field_id = field_id
        if data is not None:
            self.data = data
        if children is not None:
            self.children = children
        if node_id is not None:
            self.node_id = node_id

    @property
    def field_id(self):
        """Gets the field_id of this ReadItem.  # noqa: E501


        :return: The field_id of this ReadItem.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this ReadItem.


        :param field_id: The field_id of this ReadItem.  # noqa: E501
        :type: str
        """
        if field_id is None:
            raise ValueError("Invalid value for `field_id`, must not be `None`")  # noqa: E501

        self._field_id = field_id

    @property
    def data(self):
        """Gets the data of this ReadItem.  # noqa: E501


        :return: The data of this ReadItem.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ReadItem.


        :param data: The data of this ReadItem.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def children(self):
        """Gets the children of this ReadItem.  # noqa: E501


        :return: The children of this ReadItem.  # noqa: E501
        :rtype: list[ReadStatusItem]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this ReadItem.


        :param children: The children of this ReadItem.  # noqa: E501
        :type: list[ReadStatusItem]
        """

        self._children = children

    @property
    def node_id(self):
        """Gets the node_id of this ReadItem.  # noqa: E501


        :return: The node_id of this ReadItem.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ReadItem.


        :param node_id: The node_id of this ReadItem.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReadItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
