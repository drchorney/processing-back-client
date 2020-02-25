# coding: utf-8

"""
    Processing Project

    This is the api for the processing project backend.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.model_configurations_api import ModelConfigurationsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestModelConfigurationsApi(unittest.TestCase):
    """ModelConfigurationsApi unit test stubs"""

    def setUp(self):
        self.api = api.model_configurations_api.ModelConfigurationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_configuration_id_download_get(self):
        """Test case for configuration_id_download_get

        Retreive signed url to download binary  # noqa: E501
        """
        pass

    def test_configuration_id_get(self):
        """Test case for configuration_id_get

        Returns a model configuration  # noqa: E501
        """
        pass

    def test_configuration_id_patch(self):
        """Test case for configuration_id_patch

        Launch a configuration to one of the workers to be processed.  # noqa: E501
        """
        pass

    def test_configuration_id_put(self):
        """Test case for configuration_id_put

        Update and replace a model configuration  # noqa: E501
        """
        pass

    def test_configuration_post(self):
        """Test case for configuration_post

        Creates a model configuration.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
