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


class FilterStatement(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'field': 'str',
        'arguments': 'list[str]'
    }

    attribute_map = {
        'field': 'field',
        'arguments': 'arguments'
    }

    def __init__(self, field=None, arguments=None):  # noqa: E501
        """FilterStatement - a model defined in Swagger"""  # noqa: E501

        self._field = None
        self._arguments = None
        self.discriminator = None

        if field is not None:
            self.field = field
        self.arguments = arguments

    @property
    def field(self):
        """Gets the field of this FilterStatement.  # noqa: E501


        :return: The field of this FilterStatement.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this FilterStatement.


        :param field: The field of this FilterStatement.  # noqa: E501
        :type: str
        """
        allowed_values = ["Target", "Action", "ActionQualifier", "Entity", "Id", "BatchId", "Login", "Application", "OnBehalfOf"]  # noqa: E501
        if field not in allowed_values:
            raise ValueError(
                "Invalid value for `field` ({0}), must be one of {1}"  # noqa: E501
                .format(field, allowed_values)
            )

        self._field = field

    @property
    def arguments(self):
        """Gets the arguments of this FilterStatement.  # noqa: E501


        :return: The arguments of this FilterStatement.  # noqa: E501
        :rtype: list[str]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this FilterStatement.


        :param arguments: The arguments of this FilterStatement.  # noqa: E501
        :type: list[str]
        """
        if arguments is None:
            raise ValueError("Invalid value for `arguments`, must not be `None`")  # noqa: E501

        self._arguments = arguments

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
        if not isinstance(other, FilterStatement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
