# Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | Name of Docker image to use. This is optional and can be used to override the image defined at the group level. | 
**payload** | **str** | Payload for the task. This is what you pass into each task to make it do something. | [optional] 
**group_name** | **str** | Group this task belongs to. | [optional] 
**error** | **str** | The error message, if status is &#39;error&#39;. This is errors due to things outside the task itself. Errors from user code will be found in the log. | [optional] 
**reason** | **str** | Machine usable reason for task being in this state. Valid values for error status are &#x60;timeout | killed | bad_exit&#x60;. Valid values for cancelled status are &#x60;client_request&#x60;. For everything else, this is undefined.  | [optional] 
**created_at** | **datetime** | Time when task was submitted. Always in UTC. | [optional] 
**started_at** | **datetime** | Time when task started execution. Always in UTC. | [optional] 
**completed_at** | **datetime** | Time when task completed, whether it was successul or failed. Always in UTC. | [optional] 
**retry_of** | **str** | If this field is set, then this task is a retry of the ID in this field. | [optional] 
**retry_at** | **str** | If this field is set, then this task was retried by the task referenced in this field. | [optional] 
**env_vars** | **dict(str, str)** | Env vars for the task. Comes from the ones set on the Group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


