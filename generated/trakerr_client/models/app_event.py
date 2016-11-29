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


class AppEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_key=None, classification=None, event_type=None, event_message=None, event_time=None, event_stacktrace=None, event_user=None, event_session=None, context_app_version=None, context_env_name=None, context_env_version=None, context_env_hostname=None, context_app_browser=None, context_app_browser_version=None, context_app_os=None, context_app_os_version=None, context_data_center=None, context_data_center_region=None, custom_properties=None, custom_segments=None):
        """
        AppEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_key': 'str',
            'classification': 'str',
            'event_type': 'str',
            'event_message': 'str',
            'event_time': 'int',
            'event_stacktrace': 'Stacktrace',
            'event_user': 'str',
            'event_session': 'str',
            'context_app_version': 'str',
            'context_env_name': 'str',
            'context_env_version': 'str',
            'context_env_hostname': 'str',
            'context_app_browser': 'str',
            'context_app_browser_version': 'str',
            'context_app_os': 'str',
            'context_app_os_version': 'str',
            'context_data_center': 'str',
            'context_data_center_region': 'str',
            'custom_properties': 'CustomData',
            'custom_segments': 'CustomData'
        }

        self.attribute_map = {
            'api_key': 'apiKey',
            'classification': 'classification',
            'event_type': 'eventType',
            'event_message': 'eventMessage',
            'event_time': 'eventTime',
            'event_stacktrace': 'eventStacktrace',
            'event_user': 'eventUser',
            'event_session': 'eventSession',
            'context_app_version': 'contextAppVersion',
            'context_env_name': 'contextEnvName',
            'context_env_version': 'contextEnvVersion',
            'context_env_hostname': 'contextEnvHostname',
            'context_app_browser': 'contextAppBrowser',
            'context_app_browser_version': 'contextAppBrowserVersion',
            'context_app_os': 'contextAppOS',
            'context_app_os_version': 'contextAppOSVersion',
            'context_data_center': 'contextDataCenter',
            'context_data_center_region': 'contextDataCenterRegion',
            'custom_properties': 'customProperties',
            'custom_segments': 'customSegments'
        }

        self._api_key = api_key
        self._classification = classification
        self._event_type = event_type
        self._event_message = event_message
        self._event_time = event_time
        self._event_stacktrace = event_stacktrace
        self._event_user = event_user
        self._event_session = event_session
        self._context_app_version = context_app_version
        self._context_env_name = context_env_name
        self._context_env_version = context_env_version
        self._context_env_hostname = context_env_hostname
        self._context_app_browser = context_app_browser
        self._context_app_browser_version = context_app_browser_version
        self._context_app_os = context_app_os
        self._context_app_os_version = context_app_os_version
        self._context_data_center = context_data_center
        self._context_data_center_region = context_data_center_region
        self._custom_properties = custom_properties
        self._custom_segments = custom_segments

    @property
    def api_key(self):
        """
        Gets the api_key of this AppEvent.
        API key generated for the application

        :return: The api_key of this AppEvent.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """
        Sets the api_key of this AppEvent.
        API key generated for the application

        :param api_key: The api_key of this AppEvent.
        :type: str
        """

        self._api_key = api_key

    @property
    def classification(self):
        """
        Gets the classification of this AppEvent.
        one of 'debug','info','warning','error' or a custom string

        :return: The classification of this AppEvent.
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """
        Sets the classification of this AppEvent.
        one of 'debug','info','warning','error' or a custom string

        :param classification: The classification of this AppEvent.
        :type: str
        """

        self._classification = classification

    @property
    def event_type(self):
        """
        Gets the event_type of this AppEvent.
        type or event or error (eg. NullPointerException)

        :return: The event_type of this AppEvent.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this AppEvent.
        type or event or error (eg. NullPointerException)

        :param event_type: The event_type of this AppEvent.
        :type: str
        """

        self._event_type = event_type

    @property
    def event_message(self):
        """
        Gets the event_message of this AppEvent.
        message containing details of the event or error

        :return: The event_message of this AppEvent.
        :rtype: str
        """
        return self._event_message

    @event_message.setter
    def event_message(self, event_message):
        """
        Sets the event_message of this AppEvent.
        message containing details of the event or error

        :param event_message: The event_message of this AppEvent.
        :type: str
        """

        self._event_message = event_message

    @property
    def event_time(self):
        """
        Gets the event_time of this AppEvent.
        (optional) event time in ms since epoch

        :return: The event_time of this AppEvent.
        :rtype: int
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """
        Sets the event_time of this AppEvent.
        (optional) event time in ms since epoch

        :param event_time: The event_time of this AppEvent.
        :type: int
        """

        self._event_time = event_time

    @property
    def event_stacktrace(self):
        """
        Gets the event_stacktrace of this AppEvent.


        :return: The event_stacktrace of this AppEvent.
        :rtype: Stacktrace
        """
        return self._event_stacktrace

    @event_stacktrace.setter
    def event_stacktrace(self, event_stacktrace):
        """
        Sets the event_stacktrace of this AppEvent.


        :param event_stacktrace: The event_stacktrace of this AppEvent.
        :type: Stacktrace
        """

        self._event_stacktrace = event_stacktrace

    @property
    def event_user(self):
        """
        Gets the event_user of this AppEvent.
        (optional) event user identifying a user

        :return: The event_user of this AppEvent.
        :rtype: str
        """
        return self._event_user

    @event_user.setter
    def event_user(self, event_user):
        """
        Sets the event_user of this AppEvent.
        (optional) event user identifying a user

        :param event_user: The event_user of this AppEvent.
        :type: str
        """

        self._event_user = event_user

    @property
    def event_session(self):
        """
        Gets the event_session of this AppEvent.
        (optional) session identification

        :return: The event_session of this AppEvent.
        :rtype: str
        """
        return self._event_session

    @event_session.setter
    def event_session(self, event_session):
        """
        Sets the event_session of this AppEvent.
        (optional) session identification

        :param event_session: The event_session of this AppEvent.
        :type: str
        """

        self._event_session = event_session

    @property
    def context_app_version(self):
        """
        Gets the context_app_version of this AppEvent.
        (optional) application version information

        :return: The context_app_version of this AppEvent.
        :rtype: str
        """
        return self._context_app_version

    @context_app_version.setter
    def context_app_version(self, context_app_version):
        """
        Sets the context_app_version of this AppEvent.
        (optional) application version information

        :param context_app_version: The context_app_version of this AppEvent.
        :type: str
        """

        self._context_app_version = context_app_version

    @property
    def context_env_name(self):
        """
        Gets the context_env_name of this AppEvent.
        (optional) one of 'development','staging','production' or a custom string

        :return: The context_env_name of this AppEvent.
        :rtype: str
        """
        return self._context_env_name

    @context_env_name.setter
    def context_env_name(self, context_env_name):
        """
        Sets the context_env_name of this AppEvent.
        (optional) one of 'development','staging','production' or a custom string

        :param context_env_name: The context_env_name of this AppEvent.
        :type: str
        """

        self._context_env_name = context_env_name

    @property
    def context_env_version(self):
        """
        Gets the context_env_version of this AppEvent.
        (optional) version of environment

        :return: The context_env_version of this AppEvent.
        :rtype: str
        """
        return self._context_env_version

    @context_env_version.setter
    def context_env_version(self, context_env_version):
        """
        Sets the context_env_version of this AppEvent.
        (optional) version of environment

        :param context_env_version: The context_env_version of this AppEvent.
        :type: str
        """

        self._context_env_version = context_env_version

    @property
    def context_env_hostname(self):
        """
        Gets the context_env_hostname of this AppEvent.
        (optional) hostname or ID of environment

        :return: The context_env_hostname of this AppEvent.
        :rtype: str
        """
        return self._context_env_hostname

    @context_env_hostname.setter
    def context_env_hostname(self, context_env_hostname):
        """
        Sets the context_env_hostname of this AppEvent.
        (optional) hostname or ID of environment

        :param context_env_hostname: The context_env_hostname of this AppEvent.
        :type: str
        """

        self._context_env_hostname = context_env_hostname

    @property
    def context_app_browser(self):
        """
        Gets the context_app_browser of this AppEvent.
        (optional) browser name if running in a browser (eg. Chrome)

        :return: The context_app_browser of this AppEvent.
        :rtype: str
        """
        return self._context_app_browser

    @context_app_browser.setter
    def context_app_browser(self, context_app_browser):
        """
        Sets the context_app_browser of this AppEvent.
        (optional) browser name if running in a browser (eg. Chrome)

        :param context_app_browser: The context_app_browser of this AppEvent.
        :type: str
        """

        self._context_app_browser = context_app_browser

    @property
    def context_app_browser_version(self):
        """
        Gets the context_app_browser_version of this AppEvent.
        (optional) browser version if running in a browser

        :return: The context_app_browser_version of this AppEvent.
        :rtype: str
        """
        return self._context_app_browser_version

    @context_app_browser_version.setter
    def context_app_browser_version(self, context_app_browser_version):
        """
        Sets the context_app_browser_version of this AppEvent.
        (optional) browser version if running in a browser

        :param context_app_browser_version: The context_app_browser_version of this AppEvent.
        :type: str
        """

        self._context_app_browser_version = context_app_browser_version

    @property
    def context_app_os(self):
        """
        Gets the context_app_os of this AppEvent.
        (optional) OS the application is running on

        :return: The context_app_os of this AppEvent.
        :rtype: str
        """
        return self._context_app_os

    @context_app_os.setter
    def context_app_os(self, context_app_os):
        """
        Sets the context_app_os of this AppEvent.
        (optional) OS the application is running on

        :param context_app_os: The context_app_os of this AppEvent.
        :type: str
        """

        self._context_app_os = context_app_os

    @property
    def context_app_os_version(self):
        """
        Gets the context_app_os_version of this AppEvent.
        (optional) OS version the application is running on

        :return: The context_app_os_version of this AppEvent.
        :rtype: str
        """
        return self._context_app_os_version

    @context_app_os_version.setter
    def context_app_os_version(self, context_app_os_version):
        """
        Sets the context_app_os_version of this AppEvent.
        (optional) OS version the application is running on

        :param context_app_os_version: The context_app_os_version of this AppEvent.
        :type: str
        """

        self._context_app_os_version = context_app_os_version

    @property
    def context_data_center(self):
        """
        Gets the context_data_center of this AppEvent.
        (optional) Data center the application is running on or connected to

        :return: The context_data_center of this AppEvent.
        :rtype: str
        """
        return self._context_data_center

    @context_data_center.setter
    def context_data_center(self, context_data_center):
        """
        Sets the context_data_center of this AppEvent.
        (optional) Data center the application is running on or connected to

        :param context_data_center: The context_data_center of this AppEvent.
        :type: str
        """

        self._context_data_center = context_data_center

    @property
    def context_data_center_region(self):
        """
        Gets the context_data_center_region of this AppEvent.
        (optional) Data center region

        :return: The context_data_center_region of this AppEvent.
        :rtype: str
        """
        return self._context_data_center_region

    @context_data_center_region.setter
    def context_data_center_region(self, context_data_center_region):
        """
        Sets the context_data_center_region of this AppEvent.
        (optional) Data center region

        :param context_data_center_region: The context_data_center_region of this AppEvent.
        :type: str
        """

        self._context_data_center_region = context_data_center_region

    @property
    def custom_properties(self):
        """
        Gets the custom_properties of this AppEvent.


        :return: The custom_properties of this AppEvent.
        :rtype: CustomData
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """
        Sets the custom_properties of this AppEvent.


        :param custom_properties: The custom_properties of this AppEvent.
        :type: CustomData
        """

        self._custom_properties = custom_properties

    @property
    def custom_segments(self):
        """
        Gets the custom_segments of this AppEvent.


        :return: The custom_segments of this AppEvent.
        :rtype: CustomData
        """
        return self._custom_segments

    @custom_segments.setter
    def custom_segments(self, custom_segments):
        """
        Sets the custom_segments of this AppEvent.


        :param custom_segments: The custom_segments of this AppEvent.
        :type: CustomData
        """

        self._custom_segments = custom_segments

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
