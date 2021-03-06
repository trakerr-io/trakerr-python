# coding: utf-8

"""
    Trakerr API

    Get your application events and errors to Trakerr via the *Trakerr API*.

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class StackTraceLine(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, function=None, line=None, file=None):
        """
        StackTraceLine - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'function': 'str',
            'line': 'int',
            'file': 'str'
        }

        self.attribute_map = {
            'function': 'function',
            'line': 'line',
            'file': 'file'
        }

        self._function = function
        self._line = line
        self._file = file

    @property
    def function(self):
        """
        Gets the function of this StackTraceLine.


        :return: The function of this StackTraceLine.
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """
        Sets the function of this StackTraceLine.


        :param function: The function of this StackTraceLine.
        :type: str
        """

        self._function = function

    @property
    def line(self):
        """
        Gets the line of this StackTraceLine.


        :return: The line of this StackTraceLine.
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        """
        Sets the line of this StackTraceLine.


        :param line: The line of this StackTraceLine.
        :type: int
        """

        self._line = line

    @property
    def file(self):
        """
        Gets the file of this StackTraceLine.


        :return: The file of this StackTraceLine.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """
        Sets the file of this StackTraceLine.


        :param file: The file of this StackTraceLine.
        :type: str
        """

        self._file = file

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
