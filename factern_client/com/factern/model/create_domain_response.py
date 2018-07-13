#
# Template source downloaded from:
# https://github.com/swagger-api/swagger-codegen/tree/master/modules/swagger-codegen/src/main/resources/python
#
# coding: utf-8

"""
    Factern API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: mailto:support@factern.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateDomainResponse(object):
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
        'timestamp': 'float',
        'node_id': 'str',
        'agent': 'Agent',
        'summary': 'Summary',
        'batch_id': 'str',
        'fact_type': 'str',
        'parent_id': 'str',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'node_id': 'nodeId',
        'agent': 'agent',
        'summary': 'summary',
        'batch_id': 'batchId',
        'fact_type': 'factType',
        'parent_id': 'parentId',
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, timestamp=None, node_id=None, agent=None, summary=None, batch_id=None, fact_type=None, parent_id=None, description=None, name=None):  # noqa: E501
        """CreateDomainResponse - a model defined in Swagger"""  # noqa: E501

        self._timestamp = None
        self._node_id = None
        self._agent = None
        self._summary = None
        self._batch_id = None
        self._fact_type = None
        self._parent_id = None
        self._description = None
        self._name = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        self.node_id = node_id
        if agent is not None:
            self.agent = agent
        if summary is not None:
            self.summary = summary
        if batch_id is not None:
            self.batch_id = batch_id
        if fact_type is not None:
            self.fact_type = fact_type
        if parent_id is not None:
            self.parent_id = parent_id
        if description is not None:
            self.description = description
        self.name = name

    @property
    def timestamp(self):
        """Gets the timestamp of this CreateDomainResponse.  # noqa: E501


        :return: The timestamp of this CreateDomainResponse.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CreateDomainResponse.


        :param timestamp: The timestamp of this CreateDomainResponse.  # noqa: E501
        :type: float
        """

        self._timestamp = timestamp

    @property
    def node_id(self):
        """Gets the node_id of this CreateDomainResponse.  # noqa: E501


        :return: The node_id of this CreateDomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this CreateDomainResponse.


        :param node_id: The node_id of this CreateDomainResponse.  # noqa: E501
        :type: str
        """
        if node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

    @property
    def agent(self):
        """Gets the agent of this CreateDomainResponse.  # noqa: E501


        :return: The agent of this CreateDomainResponse.  # noqa: E501
        :rtype: Agent
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this CreateDomainResponse.


        :param agent: The agent of this CreateDomainResponse.  # noqa: E501
        :type: Agent
        """

        self._agent = agent

    @property
    def summary(self):
        """Gets the summary of this CreateDomainResponse.  # noqa: E501


        :return: The summary of this CreateDomainResponse.  # noqa: E501
        :rtype: Summary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this CreateDomainResponse.


        :param summary: The summary of this CreateDomainResponse.  # noqa: E501
        :type: Summary
        """

        self._summary = summary

    @property
    def batch_id(self):
        """Gets the batch_id of this CreateDomainResponse.  # noqa: E501


        :return: The batch_id of this CreateDomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this CreateDomainResponse.


        :param batch_id: The batch_id of this CreateDomainResponse.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def fact_type(self):
        """Gets the fact_type of this CreateDomainResponse.  # noqa: E501


        :return: The fact_type of this CreateDomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._fact_type

    @fact_type.setter
    def fact_type(self, fact_type):
        """Sets the fact_type of this CreateDomainResponse.


        :param fact_type: The fact_type of this CreateDomainResponse.  # noqa: E501
        :type: str
        """

        self._fact_type = fact_type

    @property
    def parent_id(self):
        """Gets the parent_id of this CreateDomainResponse.  # noqa: E501


        :return: The parent_id of this CreateDomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CreateDomainResponse.


        :param parent_id: The parent_id of this CreateDomainResponse.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def description(self):
        """Gets the description of this CreateDomainResponse.  # noqa: E501


        :return: The description of this CreateDomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDomainResponse.


        :param description: The description of this CreateDomainResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this CreateDomainResponse.  # noqa: E501


        :return: The name of this CreateDomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDomainResponse.


        :param name: The name of this CreateDomainResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, CreateDomainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
