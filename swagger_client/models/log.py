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


class Log(object):
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
        'call_id': 'str',
        'log': 'str'
    }

    attribute_map = {
        'call_id': 'call_id',
        'log': 'log'
    }

    def __init__(self, call_id=None, log=None):
        """
        Log - a model defined in Swagger
        """

        self._call_id = None
        self._log = None

        if call_id is not None:
          self.call_id = call_id
        if log is not None:
          self.log = log

    @property
    def call_id(self):
        """
        Gets the call_id of this Log.
        Call UUID ID

        :return: The call_id of this Log.
        :rtype: str
        """
        return self._call_id

    @call_id.setter
    def call_id(self, call_id):
        """
        Sets the call_id of this Log.
        Call UUID ID

        :param call_id: The call_id of this Log.
        :type: str
        """

        self._call_id = call_id

    @property
    def log(self):
        """
        Gets the log of this Log.

        :return: The log of this Log.
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """
        Sets the log of this Log.

        :param log: The log of this Log.
        :type: str
        """

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
        if not isinstance(other, Log):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other