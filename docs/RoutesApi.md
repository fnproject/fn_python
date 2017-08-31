# swagger_client.RoutesApi

All URIs are relative to *https://127.0.0.1:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_app_routes_get**](RoutesApi.md#apps_app_routes_get) | **GET** /apps/{app}/routes | Get route list by app name.
[**apps_app_routes_post**](RoutesApi.md#apps_app_routes_post) | **POST** /apps/{app}/routes | Create new Route
[**apps_app_routes_route_delete**](RoutesApi.md#apps_app_routes_route_delete) | **DELETE** /apps/{app}/routes/{route} | Deletes the route
[**apps_app_routes_route_get**](RoutesApi.md#apps_app_routes_route_get) | **GET** /apps/{app}/routes/{route} | Gets route by name
[**apps_app_routes_route_patch**](RoutesApi.md#apps_app_routes_route_patch) | **PATCH** /apps/{app}/routes/{route} | Update a Route, Fails if the route or app does not exist. Accepts partial updates / skips validation of zero values.
[**apps_app_routes_route_put**](RoutesApi.md#apps_app_routes_route_put) | **PUT** /apps/{app}/routes/{route} | Create a Route if it does not exist. Update if it does. Will also create app if it does not exist. Put does not skip validation of zero values


# **apps_app_routes_get**
> RoutesWrapper apps_app_routes_get(app)

Get route list by app name.

This will list routes for a particular app.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutesApi()
app = 'app_example' # str | Name of app for this set of routes.

try: 
    # Get route list by app name.
    api_response = api_instance.apps_app_routes_get(app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->apps_app_routes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| Name of app for this set of routes. | 

### Return type

[**RoutesWrapper**](RoutesWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_app_routes_post**
> RouteWrapper apps_app_routes_post(app, body)

Create new Route

Create a new route in an app, if app doesn't exists, it creates the app. Post does not skip validation of zero values.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutesApi()
app = 'app_example' # str | name of the app.
body = swagger_client.RouteWrapper() # RouteWrapper | One route to post.

try: 
    # Create new Route
    api_response = api_instance.apps_app_routes_post(app, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->apps_app_routes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| name of the app. | 
 **body** | [**RouteWrapper**](RouteWrapper.md)| One route to post. | 

### Return type

[**RouteWrapper**](RouteWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_app_routes_route_delete**
> apps_app_routes_route_delete(app, route)

Deletes the route

Deletes the route.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutesApi()
app = 'app_example' # str | Name of app for this set of routes.
route = 'route_example' # str | Route name

try: 
    # Deletes the route
    api_instance.apps_app_routes_route_delete(app, route)
except ApiException as e:
    print("Exception when calling RoutesApi->apps_app_routes_route_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| Name of app for this set of routes. | 
 **route** | **str**| Route name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_app_routes_route_get**
> RouteWrapper apps_app_routes_route_get(app, route)

Gets route by name

Gets a route by name.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutesApi()
app = 'app_example' # str | Name of app for this set of routes.
route = 'route_example' # str | Route name

try: 
    # Gets route by name
    api_response = api_instance.apps_app_routes_route_get(app, route)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->apps_app_routes_route_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| Name of app for this set of routes. | 
 **route** | **str**| Route name | 

### Return type

[**RouteWrapper**](RouteWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_app_routes_route_patch**
> RouteWrapper apps_app_routes_route_patch(app, route, body)

Update a Route, Fails if the route or app does not exist. Accepts partial updates / skips validation of zero values.

Update a route

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutesApi()
app = 'app_example' # str | name of the app.
route = 'route_example' # str | route path.
body = swagger_client.RouteWrapper() # RouteWrapper | One route to post.

try: 
    # Update a Route, Fails if the route or app does not exist. Accepts partial updates / skips validation of zero values.
    api_response = api_instance.apps_app_routes_route_patch(app, route, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->apps_app_routes_route_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| name of the app. | 
 **route** | **str**| route path. | 
 **body** | [**RouteWrapper**](RouteWrapper.md)| One route to post. | 

### Return type

[**RouteWrapper**](RouteWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_app_routes_route_put**
> RouteWrapper apps_app_routes_route_put(app, route, body)

Create a Route if it does not exist. Update if it does. Will also create app if it does not exist. Put does not skip validation of zero values

Update or Create a route

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutesApi()
app = 'app_example' # str | name of the app.
route = 'route_example' # str | route path.
body = swagger_client.RouteWrapper() # RouteWrapper | One route to post.

try: 
    # Create a Route if it does not exist. Update if it does. Will also create app if it does not exist. Put does not skip validation of zero values
    api_response = api_instance.apps_app_routes_route_put(app, route, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->apps_app_routes_route_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| name of the app. | 
 **route** | **str**| route path. | 
 **body** | [**RouteWrapper**](RouteWrapper.md)| One route to post. | 

### Return type

[**RouteWrapper**](RouteWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

