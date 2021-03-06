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


class UpdateStatusRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_summary': 'bool',
        'node_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'node_id': 'nodeId',
        'status': 'status'
    }

    def __init__(self, include_summary=None, node_id=None, status=None):  # noqa: E501
        """UpdateStatusRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._node_id = None
        self._status = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        self.node_id = node_id
        self.status = status

    @property
    def include_summary(self):
        """Gets the include_summary of this UpdateStatusRequest.  # noqa: E501


        :return: The include_summary of this UpdateStatusRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this UpdateStatusRequest.


        :param include_summary: The include_summary of this UpdateStatusRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

    @property
    def node_id(self):
        """Gets the node_id of this UpdateStatusRequest.  # noqa: E501


        :return: The node_id of this UpdateStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this UpdateStatusRequest.


        :param node_id: The node_id of this UpdateStatusRequest.  # noqa: E501
        :type: str
        """
        if node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

    @property
    def status(self):
        """Gets the status of this UpdateStatusRequest.  # noqa: E501


        :return: The status of this UpdateStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateStatusRequest.


        :param status: The status of this UpdateStatusRequest.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["enabled", "disabled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if not isinstance(other, UpdateStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
