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


class ApiEndpoint(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'body': 'str',
        'url': 'str',
        'response_transform': 'list[TransformElement]',
        'headers': 'list[HttpHeader]',
        'type': 'str',
        'method': 'str'
    }

    attribute_map = {
        'body': 'body',
        'url': 'url',
        'response_transform': 'responseTransform',
        'headers': 'headers',
        'type': 'type',
        'method': 'method'
    }

    def __init__(self, body=None, url=None, response_transform=None, headers=None, type=None, method=None):  # noqa: E501
        """ApiEndpoint - a model defined in Swagger"""  # noqa: E501

        self._body = None
        self._url = None
        self._response_transform = None
        self._headers = None
        self._type = None
        self._method = None
        self.discriminator = None

        if body is not None:
            self.body = body
        self.url = url
        if response_transform is not None:
            self.response_transform = response_transform
        if headers is not None:
            self.headers = headers
        if type is not None:
            self.type = type
        if method is not None:
            self.method = method

    @property
    def body(self):
        """Gets the body of this ApiEndpoint.  # noqa: E501


        :return: The body of this ApiEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ApiEndpoint.


        :param body: The body of this ApiEndpoint.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def url(self):
        """Gets the url of this ApiEndpoint.  # noqa: E501


        :return: The url of this ApiEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ApiEndpoint.


        :param url: The url of this ApiEndpoint.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def response_transform(self):
        """Gets the response_transform of this ApiEndpoint.  # noqa: E501


        :return: The response_transform of this ApiEndpoint.  # noqa: E501
        :rtype: list[TransformElement]
        """
        return self._response_transform

    @response_transform.setter
    def response_transform(self, response_transform):
        """Sets the response_transform of this ApiEndpoint.


        :param response_transform: The response_transform of this ApiEndpoint.  # noqa: E501
        :type: list[TransformElement]
        """

        self._response_transform = response_transform

    @property
    def headers(self):
        """Gets the headers of this ApiEndpoint.  # noqa: E501


        :return: The headers of this ApiEndpoint.  # noqa: E501
        :rtype: list[HttpHeader]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this ApiEndpoint.


        :param headers: The headers of this ApiEndpoint.  # noqa: E501
        :type: list[HttpHeader]
        """

        self._headers = headers

    @property
    def type(self):
        """Gets the type of this ApiEndpoint.  # noqa: E501


        :return: The type of this ApiEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApiEndpoint.


        :param type: The type of this ApiEndpoint.  # noqa: E501
        :type: str
        """
        allowed_values = ["Direct", "Indirect"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def method(self):
        """Gets the method of this ApiEndpoint.  # noqa: E501


        :return: The method of this ApiEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ApiEndpoint.


        :param method: The method of this ApiEndpoint.  # noqa: E501
        :type: str
        """
        allowed_values = ["GET", "POST", "PUT"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

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
        if not isinstance(other, ApiEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
