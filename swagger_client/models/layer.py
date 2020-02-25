# coding: utf-8

"""
    Processing Project

    This is the api for the processing project backend.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Layer(object):
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
        'thickness': 'float',
        'p_vel': 'float',
        's_vel': 'float'
    }

    attribute_map = {
        'thickness': 'thickness',
        'p_vel': 'pVel',
        's_vel': 'sVel'
    }

    def __init__(self, thickness=None, p_vel=None, s_vel=None):  # noqa: E501
        """Layer - a model defined in Swagger"""  # noqa: E501
        self._thickness = None
        self._p_vel = None
        self._s_vel = None
        self.discriminator = None
        self.thickness = thickness
        self.p_vel = p_vel
        if s_vel is not None:
            self.s_vel = s_vel

    @property
    def thickness(self):
        """Gets the thickness of this Layer.  # noqa: E501


        :return: The thickness of this Layer.  # noqa: E501
        :rtype: float
        """
        return self._thickness

    @thickness.setter
    def thickness(self, thickness):
        """Sets the thickness of this Layer.


        :param thickness: The thickness of this Layer.  # noqa: E501
        :type: float
        """
        if thickness is None:
            raise ValueError("Invalid value for `thickness`, must not be `None`")  # noqa: E501

        self._thickness = thickness

    @property
    def p_vel(self):
        """Gets the p_vel of this Layer.  # noqa: E501


        :return: The p_vel of this Layer.  # noqa: E501
        :rtype: float
        """
        return self._p_vel

    @p_vel.setter
    def p_vel(self, p_vel):
        """Sets the p_vel of this Layer.


        :param p_vel: The p_vel of this Layer.  # noqa: E501
        :type: float
        """
        if p_vel is None:
            raise ValueError("Invalid value for `p_vel`, must not be `None`")  # noqa: E501

        self._p_vel = p_vel

    @property
    def s_vel(self):
        """Gets the s_vel of this Layer.  # noqa: E501


        :return: The s_vel of this Layer.  # noqa: E501
        :rtype: float
        """
        return self._s_vel

    @s_vel.setter
    def s_vel(self, s_vel):
        """Sets the s_vel of this Layer.


        :param s_vel: The s_vel of this Layer.  # noqa: E501
        :type: float
        """

        self._s_vel = s_vel

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
        if issubclass(Layer, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Layer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other