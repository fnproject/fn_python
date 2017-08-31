# swagger_client.LogApi

All URIs are relative to *https://127.0.0.1:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_app_calls_call_log_delete**](LogApi.md#apps_app_calls_call_log_delete) | **DELETE** /apps/{app}/calls/{call}/log | Delete call log entry
[**apps_app_calls_call_log_get**](LogApi.md#apps_app_calls_call_log_get) | **GET** /apps/{app}/calls/{call}/log | Get call logs


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
api_instance = swagger_client.LogApi()
call = 'call_example' # str | Call ID.
app = 'app_example' # str | App name.

try: 
    # Delete call log entry
    api_instance.apps_app_calls_call_log_delete(call, app)
except ApiException as e:
    print("Exception when calling LogApi->apps_app_calls_call_log_delete: %s\n" % e)
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
api_instance = swagger_client.LogApi()
app = 'app_example' # str | App Name
call = 'call_example' # str | Call ID.

try: 
    # Get call logs
    api_response = api_instance.apps_app_calls_call_log_get(app, call)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogApi->apps_app_calls_call_log_get: %s\n" % e)
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

