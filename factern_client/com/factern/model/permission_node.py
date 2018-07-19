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


class PermissionNode(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'policy': 'PermissionPolicyDocument',
        'target_node_id': 'str',
        'permission_interface_id': 'str'
    }

    attribute_map = {
        'policy': 'policy',
        'target_node_id': 'targetNodeId',
        'permission_interface_id': 'permissionInterfaceId'
    }

    def __init__(self, policy=None, target_node_id=None, permission_interface_id=None):  # noqa: E501
        """PermissionNode - a model defined in Swagger"""  # noqa: E501

        self._policy = None
        self._target_node_id = None
        self._permission_interface_id = None
        self.discriminator = None

        if policy is not None:
            self.policy = policy
        if target_node_id is not None:
            self.target_node_id = target_node_id
        if permission_interface_id is not None:
            self.permission_interface_id = permission_interface_id

    @property
    def policy(self):
        """Gets the policy of this PermissionNode.  # noqa: E501


        :return: The policy of this PermissionNode.  # noqa: E501
        :rtype: PermissionPolicyDocument
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this PermissionNode.


        :param policy: The policy of this PermissionNode.  # noqa: E501
        :type: PermissionPolicyDocument
        """

        self._policy = policy

    @property
    def target_node_id(self):
        """Gets the target_node_id of this PermissionNode.  # noqa: E501


        :return: The target_node_id of this PermissionNode.  # noqa: E501
        :rtype: str
        """
        return self._target_node_id

    @target_node_id.setter
    def target_node_id(self, target_node_id):
        """Sets the target_node_id of this PermissionNode.


        :param target_node_id: The target_node_id of this PermissionNode.  # noqa: E501
        :type: str
        """

        self._target_node_id = target_node_id

    @property
    def permission_interface_id(self):
        """Gets the permission_interface_id of this PermissionNode.  # noqa: E501


        :return: The permission_interface_id of this PermissionNode.  # noqa: E501
        :rtype: str
        """
        return self._permission_interface_id

    @permission_interface_id.setter
    def permission_interface_id(self, permission_interface_id):
        """Sets the permission_interface_id of this PermissionNode.


        :param permission_interface_id: The permission_interface_id of this PermissionNode.  # noqa: E501
        :type: str
        """

        self._permission_interface_id = permission_interface_id

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
        if not isinstance(other, PermissionNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
