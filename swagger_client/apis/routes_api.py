# coding: utf-8

"""
    fn

    The open source serverless platform.

    OpenAPI spec version: 0.2.1
    
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


class RoutesApi(object):
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

    def apps_app_routes_get(self, app, **kwargs):
        """
        Get route list by app name.
        This will list routes for a particular app, returned in alphabetical order.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_routes_get(app, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app: Name of app for this set of routes. (required)
        :param str image: Route image to match, exact.
        :param str cursor: Cursor from previous response.next_cursor to begin results after, if any.
        :param int per_page: Number of results to return, defaults to 30. Max of 100.
        :return: RoutesWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apps_app_routes_get_with_http_info(app, **kwargs)
        else:
            (data) = self.apps_app_routes_get_with_http_info(app, **kwargs)
            return data

    def apps_app_routes_get_with_http_info(self, app, **kwargs):
        """
        Get route list by app name.
        This will list routes for a particular app, returned in alphabetical order.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_routes_get_with_http_info(app, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app: Name of app for this set of routes. (required)
        :param str image: Route image to match, exact.
        :param str cursor: Cursor from previous response.next_cursor to begin results after, if any.
        :param int per_page: Number of results to return, defaults to 30. Max of 100.
        :return: RoutesWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app', 'image', 'cursor', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apps_app_routes_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app' is set
        if ('app' not in params) or (params['app'] is None):
            raise ValueError("Missing the required parameter `app` when calling `apps_app_routes_get`")


        collection_formats = {}

        path_params = {}
        if 'app' in params:
            path_params['app'] = params['app']

        query_params = []
        if 'image' in params:
            query_params.append(('image', params['image']))
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))

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

        return self.api_client.call_api('/apps/{app}/routes', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RoutesWrapper',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def apps_app_routes_post(self, app, body, **kwargs):
        """
        Create new Route
        Create a new route in an app, if app doesn't exists, it creates the app. Post does not skip validation of zero values.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_routes_post(app, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app: name of the app. (required)
        :param RouteWrapper body: One route to post. (required)
        :return: RouteWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apps_app_routes_post_with_http_info(app, body, **kwargs)
        else:
            (data) = self.apps_app_routes_post_with_http_info(app, body, **kwargs)
            return data

    def apps_app_routes_post_with_http_info(self, app, body, **kwargs):
        """
        Create new Route
        Create a new route in an app, if app doesn't exists, it creates the app. Post does not skip validation of zero values.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_routes_post_with_http_info(app, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app: name of the app. (required)
        :param RouteWrapper body: One route to post. (required)
        :return: RouteWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apps_app_routes_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app' is set
        if ('app' not in params) or (params['app'] is None):
            raise ValueError("Missing the required parameter `app` when calling `apps_app_routes_post`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `apps_app_routes_post`")


        collection_formats = {}

        path_params = {}
        if 'app' in params:
            path_params['app'] = params['app']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/apps/{app}/routes', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RouteWrapper',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def apps_app_routes_route_delete(self, app, route, **kwargs):
        """
        Deletes the route
        Deletes the route.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_routes_route_delete(app, route, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app: Name of app for this set of routes. (required)
        :param str route: Route name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apps_app_routes_route_delete_with_http_info(app, route, **kwargs)
        else:
            (data) = self.apps_app_routes_route_delete_with_http_info(app, route, **kwargs)
            return data

    def apps_app_routes_route_delete_with_http_info(self, app, route, **kwargs):
        """
        Deletes the route
        Deletes the route.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_routes_route_delete_with_http_info(app, route, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app: Name of app for this set of routes. (required)
        :param str route: Route name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app', 'route']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apps_app_routes_route_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app' is set
        if ('app' not in params) or (params['app'] is None):
            raise ValueError("Missing the required parameter `app` when calling `apps_app_routes_route_delete`")
        # verify the required parameter 'route' is set
        if ('route' not in params) or (params['route'] is None):
            raise ValueError("Missing the required parameter `route` when calling `apps_app_routes_route_delete`")


        collection_formats = {}

        path_params = {}
        if 'app' in params:
            path_params['app'] = params['app']
        if 'route' in params:
            path_params['route'] = params['route']

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

        return self.api_client.call_api('/apps/{app}/routes/{route}', 'DELETE',
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

    def apps_app_routes_route_get(self, app, route, **kwargs):
        """
        Gets route by name
        Gets a route by name.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_routes_route_get(app, route, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app: Name of app for this set of routes. (required)
        :param str route: Route name (required)
        :return: RouteWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apps_app_routes_route_get_with_http_info(app, route, **kwargs)
        else:
            (data) = self.apps_app_routes_route_get_with_http_info(app, route, **kwargs)
            return data

    def apps_app_routes_route_get_with_http_info(self, app, route, **kwargs):
        """
        Gets route by name
        Gets a route by name.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_routes_route_get_with_http_info(app, route, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app: Name of app for this set of routes. (required)
        :param str route: Route name (required)
        :return: RouteWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app', 'route']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apps_app_routes_route_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app' is set
        if ('app' not in params) or (params['app'] is None):
            raise ValueError("Missing the required parameter `app` when calling `apps_app_routes_route_get`")
        # verify the required parameter 'route' is set
        if ('route' not in params) or (params['route'] is None):
            raise ValueError("Missing the required parameter `route` when calling `apps_app_routes_route_get`")


        collection_formats = {}

        path_params = {}
        if 'app' in params:
            path_params['app'] = params['app']
        if 'route' in params:
            path_params['route'] = params['route']

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

        return self.api_client.call_api('/apps/{app}/routes/{route}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RouteWrapper',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def apps_app_routes_route_patch(self, app, route, body, **kwargs):
        """
        Update a Route, Fails if the route or app does not exist. Accepts partial updates / skips validation of zero values.
        Update a route
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_routes_route_patch(app, route, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app: name of the app. (required)
        :param str route: route path. (required)
        :param RouteWrapper body: One route to post. (required)
        :return: RouteWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apps_app_routes_route_patch_with_http_info(app, route, body, **kwargs)
        else:
            (data) = self.apps_app_routes_route_patch_with_http_info(app, route, body, **kwargs)
            return data

    def apps_app_routes_route_patch_with_http_info(self, app, route, body, **kwargs):
        """
        Update a Route, Fails if the route or app does not exist. Accepts partial updates / skips validation of zero values.
        Update a route
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_routes_route_patch_with_http_info(app, route, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app: name of the app. (required)
        :param str route: route path. (required)
        :param RouteWrapper body: One route to post. (required)
        :return: RouteWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app', 'route', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apps_app_routes_route_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app' is set
        if ('app' not in params) or (params['app'] is None):
            raise ValueError("Missing the required parameter `app` when calling `apps_app_routes_route_patch`")
        # verify the required parameter 'route' is set
        if ('route' not in params) or (params['route'] is None):
            raise ValueError("Missing the required parameter `route` when calling `apps_app_routes_route_patch`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `apps_app_routes_route_patch`")


        collection_formats = {}

        path_params = {}
        if 'app' in params:
            path_params['app'] = params['app']
        if 'route' in params:
            path_params['route'] = params['route']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/apps/{app}/routes/{route}', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RouteWrapper',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def apps_app_routes_route_put(self, app, route, body, **kwargs):
        """
        Create a Route if it does not exist. Update if it does. Will also create app if it does not exist. Put does not skip validation of zero values
        Update or Create a route
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_routes_route_put(app, route, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app: name of the app. (required)
        :param str route: route path. (required)
        :param RouteWrapper body: One route to post. (required)
        :return: RouteWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apps_app_routes_route_put_with_http_info(app, route, body, **kwargs)
        else:
            (data) = self.apps_app_routes_route_put_with_http_info(app, route, body, **kwargs)
            return data

    def apps_app_routes_route_put_with_http_info(self, app, route, body, **kwargs):
        """
        Create a Route if it does not exist. Update if it does. Will also create app if it does not exist. Put does not skip validation of zero values
        Update or Create a route
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_app_routes_route_put_with_http_info(app, route, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app: name of the app. (required)
        :param str route: route path. (required)
        :param RouteWrapper body: One route to post. (required)
        :return: RouteWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app', 'route', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apps_app_routes_route_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app' is set
        if ('app' not in params) or (params['app'] is None):
            raise ValueError("Missing the required parameter `app` when calling `apps_app_routes_route_put`")
        # verify the required parameter 'route' is set
        if ('route' not in params) or (params['route'] is None):
            raise ValueError("Missing the required parameter `route` when calling `apps_app_routes_route_put`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `apps_app_routes_route_put`")


        collection_formats = {}

        path_params = {}
        if 'app' in params:
            path_params['app'] = params['app']
        if 'route' in params:
            path_params['route'] = params['route']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/apps/{app}/routes/{route}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RouteWrapper',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
