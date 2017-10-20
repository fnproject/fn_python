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


class LogWrapper(object):
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
        'log': 'Log'
    }

    attribute_map = {
        'log': 'log'
    }

    def __init__(self, log=None):
        """
        LogWrapper - a model defined in Swagger
        """

        self._log = None

        self.log = log

    @property
    def log(self):
        """
        Gets the log of this LogWrapper.
        Call log entry.

        :return: The log of this LogWrapper.
        :rtype: Log
        """
        return self._log

    @log.setter
    def log(self, log):
        """
        Sets the log of this LogWrapper.
        Call log entry.

        :param log: The log of this LogWrapper.
        :type: Log
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")

        self._log = log

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
        if not isinstance(other, LogWrapper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
