# swagger_client.CallApi

All URIs are relative to *https://127.0.0.1:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_app_calls_call_get**](CallApi.md#apps_app_calls_call_get) | **GET** /apps/{app}/calls/{call} | Get call information
[**apps_app_calls_call_log_delete**](CallApi.md#apps_app_calls_call_log_delete) | **DELETE** /apps/{app}/calls/{call}/log | Delete call log entry
[**apps_app_calls_call_log_get**](CallApi.md#apps_app_calls_call_log_get) | **GET** /apps/{app}/calls/{call}/log | Get call logs
[**apps_app_calls_get**](CallApi.md#apps_app_calls_get) | **GET** /apps/{app}/calls | Get app-bound calls.


# **apps_app_calls_call_get**
> CallWrapper apps_app_calls_call_get(app, call)

Get call information

Get call information

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CallApi()
app = 'app_example' # str | app name
call = 'call_example' # str | Call ID.

try: 
    # Get call information
    api_response = api_instance.apps_app_calls_call_get(app, call)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallApi->apps_app_calls_call_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| app name | 
 **call** | **str**| Call ID. | 

### Return type

[**CallWrapper**](CallWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_app_calls_call_log_delete**
> apps_app_calls_call_log_delete(call, app)

Delete call log entry

Delete call log entry

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CallApi()
call = 'call_example' # str | Call ID.
app = 'app_example' # str | App name.

try: 
    # Delete call log entry
    api_instance.apps_app_calls_call_log_delete(call, app)
except ApiException as e:
    print("Exception when calling CallApi->apps_app_calls_call_log_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call** | **str**| Call ID. | 
 **app** | **str**| App name. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_app_calls_call_log_get**
> LogWrapper apps_app_calls_call_log_get(app, call)

Get call logs

Get call logs

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CallApi()
app = 'app_example' # str | App Name
call = 'call_example' # str | Call ID.

try: 
    # Get call logs
    api_response = api_instance.apps_app_calls_call_log_get(app, call)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallApi->apps_app_calls_call_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| App Name | 
 **call** | **str**| Call ID. | 

### Return type

[**LogWrapper**](LogWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_app_calls_get**
> CallsWrapper apps_app_calls_get(app, path=path, cursor=cursor, per_page=per_page, from_time=from_time, to_time=to_time)

Get app-bound calls.

Get app-bound calls can filter to route-bound calls, results returned in created_at, descending order (newest first).

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CallApi()
app = 'app_example' # str | App name.
path = 'path_example' # str | Route path to match, exact. (optional)
cursor = 'cursor_example' # str | Cursor from previous response.next_cursor to begin results after, if any. (optional)
per_page = 56 # int | Number of results to return, defaults to 30. Max of 100. (optional)
from_time = 56 # int | Unix timestamp in seconds, of call.created_at to begin the results at, default 0. (optional)
to_time = 56 # int | Unix timestamp in seconds, of call.created_at to end the results at, defaults to latest. (optional)

try: 
    # Get app-bound calls.
    api_response = api_instance.apps_app_calls_get(app, path=path, cursor=cursor, per_page=per_page, from_time=from_time, to_time=to_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallApi->apps_app_calls_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| App name. | 
 **path** | **str**| Route path to match, exact. | [optional] 
 **cursor** | **str**| Cursor from previous response.next_cursor to begin results after, if any. | [optional] 
 **per_page** | **int**| Number of results to return, defaults to 30. Max of 100. | [optional] 
 **from_time** | **int**| Unix timestamp in seconds, of call.created_at to begin the results at, default 0. | [optional] 
 **to_time** | **int**| Unix timestamp in seconds, of call.created_at to end the results at, defaults to latest. | [optional] 

### Return type

[**CallsWrapper**](CallsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

