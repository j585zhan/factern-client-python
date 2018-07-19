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


class CreateBidRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_summary': 'bool',
        'price_id': 'str'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'price_id': 'priceId'
    }

    def __init__(self, include_summary=None, price_id=None):  # noqa: E501
        """CreateBidRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._price_id = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        self.price_id = price_id

    @property
    def include_summary(self):
        """Gets the include_summary of this CreateBidRequest.  # noqa: E501


        :return: The include_summary of this CreateBidRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this CreateBidRequest.


        :param include_summary: The include_summary of this CreateBidRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

    @property
    def price_id(self):
        """Gets the price_id of this CreateBidRequest.  # noqa: E501


        :return: The price_id of this CreateBidRequest.  # noqa: E501
        :rtype: str
        """
        return self._price_id

    @price_id.setter
    def price_id(self, price_id):
        """Sets the price_id of this CreateBidRequest.


        :param price_id: The price_id of this CreateBidRequest.  # noqa: E501
        :type: str
        """
        if price_id is None:
            raise ValueError("Invalid value for `price_id`, must not be `None`")  # noqa: E501

        self._price_id = price_id

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
        if not isinstance(other, CreateBidRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
