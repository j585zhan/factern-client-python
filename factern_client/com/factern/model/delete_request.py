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


class DeleteRequest(object):

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
        'template': 'list[object]',
        'template_id': 'str'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'node_id': 'nodeId',
        'template': 'template',
        'template_id': 'templateId'
    }

    def __init__(self, include_summary=None, node_id=None, template=None, template_id=None):  # noqa: E501
        """DeleteRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._node_id = None
        self._template = None
        self._template_id = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        self.node_id = node_id
        if template is not None:
            self.template = template
        if template_id is not None:
            self.template_id = template_id

    @property
    def include_summary(self):
        """Gets the include_summary of this DeleteRequest.  # noqa: E501


        :return: The include_summary of this DeleteRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this DeleteRequest.


        :param include_summary: The include_summary of this DeleteRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

    @property
    def node_id(self):
        """Gets the node_id of this DeleteRequest.  # noqa: E501


        :return: The node_id of this DeleteRequest.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this DeleteRequest.


        :param node_id: The node_id of this DeleteRequest.  # noqa: E501
        :type: str
        """
        if node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

    @property
    def template(self):
        """Gets the template of this DeleteRequest.  # noqa: E501


        :return: The template of this DeleteRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this DeleteRequest.


        :param template: The template of this DeleteRequest.  # noqa: E501
        :type: list[object]
        """

        self._template = template

    @property
    def template_id(self):
        """Gets the template_id of this DeleteRequest.  # noqa: E501


        :return: The template_id of this DeleteRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this DeleteRequest.


        :param template_id: The template_id of this DeleteRequest.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

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
        if not isinstance(other, DeleteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
