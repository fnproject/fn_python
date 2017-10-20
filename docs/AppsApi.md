# swagger_client.AppsApi

All URIs are relative to *https://127.0.0.1:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_app_delete**](AppsApi.md#apps_app_delete) | **DELETE** /apps/{app} | Delete an app.
[**apps_app_get**](AppsApi.md#apps_app_get) | **GET** /apps/{app} | Get information for a app.
[**apps_app_patch**](AppsApi.md#apps_app_patch) | **PATCH** /apps/{app} | Updates an app.
[**apps_get**](AppsApi.md#apps_get) | **GET** /apps | Get all app names.
[**apps_post**](AppsApi.md#apps_post) | **POST** /apps | Post new app


# **apps_app_delete**
> apps_app_delete(app)

Delete an app.

Delete an app.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppsApi()
app = 'app_example' # str | Name of the app.

try: 
    # Delete an app.
    api_instance.apps_app_delete(app)
except ApiException as e:
    print("Exception when calling AppsApi->apps_app_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| Name of the app. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_app_get**
> AppWrapper apps_app_get(app)

Get information for a app.

This gives more details about a app, such as statistics.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppsApi()
app = 'app_example' # str | name of the app.

try: 
    # Get information for a app.
    api_response = api_instance.apps_app_get(app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_app_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| name of the app. | 

### Return type

[**AppWrapper**](AppWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_app_patch**
> AppWrapper apps_app_patch(app, body)

Updates an app.

You can set app level settings here. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppsApi()
app = 'app_example' # str | name of the app.
body = swagger_client.AppWrapper() # AppWrapper | App to post.

try: 
    # Updates an app.
    api_response = api_instance.apps_app_patch(app, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_app_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| name of the app. | 
 **body** | [**AppWrapper**](AppWrapper.md)| App to post. | 

### Return type

[**AppWrapper**](AppWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get**
> AppsWrapper apps_get(cursor=cursor, per_page=per_page)

Get all app names.

Get a list of all the apps in the system, returned in alphabetical order.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppsApi()
cursor = 'cursor_example' # str | Cursor from previous response.next_cursor to begin results after, if any. (optional)
per_page = 56 # int | Number of results to return, defaults to 30. Max of 100. (optional)

try: 
    # Get all app names.
    api_response = api_instance.apps_get(cursor=cursor, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Cursor from previous response.next_cursor to begin results after, if any. | [optional] 
 **per_page** | **int**| Number of results to return, defaults to 30. Max of 100. | [optional] 

### Return type

[**AppsWrapper**](AppsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_post**
> AppWrapper apps_post(body)

Post new app

Insert a new app

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppsApi()
body = swagger_client.AppWrapper() # AppWrapper | App to post.

try: 
    # Post new app
    api_response = api_instance.apps_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppWrapper**](AppWrapper.md)| App to post. | 

### Return type

[**AppWrapper**](AppWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

