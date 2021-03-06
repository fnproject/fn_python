# coding: utf-8

"""
    fn

    The open source serverless platform.

    OpenAPI spec version: 0.2.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AppWrapper(object):
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
        'app': 'App',
        'error': 'ErrorBody'
    }

    attribute_map = {
        'app': 'app',
        'error': 'error'
    }

    def __init__(self, app=None, error=None):
        """
        AppWrapper - a model defined in Swagger
        """

        self._app = None
        self._error = None

        self.app = app
        if error is not None:
          self.error = error

    @property
    def app(self):
        """
        Gets the app of this AppWrapper.

        :return: The app of this AppWrapper.
        :rtype: App
        """
        return self._app

    @app.setter
    def app(self, app):
        """
        Sets the app of this AppWrapper.

        :param app: The app of this AppWrapper.
        :type: App
        """
        if app is None:
            raise ValueError("Invalid value for `app`, must not be `None`")

        self._app = app

    @property
    def error(self):
        """
        Gets the error of this AppWrapper.

        :return: The error of this AppWrapper.
        :rtype: ErrorBody
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this AppWrapper.

        :param error: The error of this AppWrapper.
        :type: ErrorBody
        """

        self._error = error

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
        if not isinstance(other, AppWrapper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
