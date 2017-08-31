# coding: utf-8

"""
    fn

    The open source serverless platform.

    OpenAPI spec version: 0.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class App(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'name': 'str',
        'config': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'config': 'config'
    }

    def __init__(self, name=None, config=None):
        """
        App - a model defined in Swagger
        """

        self._name = None
        self._config = None

        if name is not None:
          self.name = name
        if config is not None:
          self.config = config

    @property
    def name(self):
        """
        Gets the name of this App.
        Name of this app. Must be different than the image name. Can ony contain alphanumeric, -, and _.

        :return: The name of this App.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this App.
        Name of this app. Must be different than the image name. Can ony contain alphanumeric, -, and _.

        :param name: The name of this App.
        :type: str
        """

        self._name = name

    @property
    def config(self):
        """
        Gets the config of this App.
        Application configuration

        :return: The config of this App.
        :rtype: dict(str, str)
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this App.
        Application configuration

        :param config: The config of this App.
        :type: dict(str, str)
        """

        self._config = config

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, App):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
