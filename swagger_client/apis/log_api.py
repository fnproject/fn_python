# coding: utf-8

"""
    fn

    The open source serverless platform.

    OpenAPI spec version: 0.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class LogApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def apps_app_calls_call_log_delete(self, call, app, **kwargs):
        """
        Delete call log entry
        Delete call log entry
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_calls_call_log_delete(call, app, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call: Call ID. (required)
        :param str app: App name. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apps_app_calls_call_log_delete_with_http_info(call, app, **kwargs)
        else:
            (data) = self.apps_app_calls_call_log_delete_with_http_info(call, app, **kwargs)
            return data

    def apps_app_calls_call_log_delete_with_http_info(self, call, app, **kwargs):
        """
        Delete call log entry
        Delete call log entry
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_calls_call_log_delete_with_http_info(call, app, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call: Call ID. (required)
        :param str app: App name. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['call', 'app']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apps_app_calls_call_log_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'call' is set
        if ('call' not in params) or (params['call'] is None):
            raise ValueError("Missing the required parameter `call` when calling `apps_app_calls_call_log_delete`")
        # verify the required parameter 'app' is set
        if ('app' not in params) or (params['app'] is None):
            raise ValueError("Missing the required parameter `app` when calling `apps_app_calls_call_log_delete`")


        collection_formats = {}

        path_params = {}
        if 'call' in params:
            path_params['call'] = params['call']
        if 'app' in params:
            path_params['app'] = params['app']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/apps/{app}/calls/{call}/log', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def apps_app_calls_call_log_get(self, app, call, **kwargs):
        """
        Get call logs
        Get call logs
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_calls_call_log_get(app, call, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app: App Name (required)
        :param str call: Call ID. (required)
        :return: LogWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apps_app_calls_call_log_get_with_http_info(app, call, **kwargs)
        else:
            (data) = self.apps_app_calls_call_log_get_with_http_info(app, call, **kwargs)
            return data

    def apps_app_calls_call_log_get_with_http_info(self, app, call, **kwargs):
        """
        Get call logs
        Get call logs
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_calls_call_log_get_with_http_info(app, call, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app: App Name (required)
        :param str call: Call ID. (required)
        :return: LogWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app', 'call']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apps_app_calls_call_log_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app' is set
        if ('app' not in params) or (params['app'] is None):
            raise ValueError("Missing the required parameter `app` when calling `apps_app_calls_call_log_get`")
        # verify the required parameter 'call' is set
        if ('call' not in params) or (params['call'] is None):
            raise ValueError("Missing the required parameter `call` when calling `apps_app_calls_call_log_get`")


        collection_formats = {}

        path_params = {}
        if 'app' in params:
            path_params['app'] = params['app']
        if 'call' in params:
            path_params['call'] = params['call']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/apps/{app}/calls/{call}/log', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='LogWrapper',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
