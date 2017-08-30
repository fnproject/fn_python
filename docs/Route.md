# Route

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | URL path that will be matched to this route | [optional] 
**image** | **str** | Name of Docker image to use in this route. You should include the image tag, which should be a version number, to be more accurate. Can be overridden on a per route basis with route.image. | [optional] 
**headers** | **dict(str, list[str])** | Map of http headers that will be sent with the response | [optional] 
**memory** | **int** | Max usable memory for this route (MiB). | [optional] 
**type** | **str** | Route type | [optional] 
**format** | **str** | Payload format sent into function. | [optional] 
**max_concurrency** | **int** | Maximum number of hot functions concurrency | [optional] 
**config** | **dict(str, str)** | Route configuration - overrides application configuration | [optional] 
**timeout** | **int** | Timeout for executions of this route. Value in Seconds | [optional] 
**idle_timeout** | **int** | Hot functions idle timeout before termination. Value in Seconds | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


