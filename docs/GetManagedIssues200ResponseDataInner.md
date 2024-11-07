# GetManagedIssues200ResponseDataInner

An Issue that was detected with a service Linode is managing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When this Issue was created. Issues are created in response to issues detected with Managed Services, so this is also when the Issue was detected. | [optional] [readonly] 
**entity** | [**GetManagedIssues200ResponseDataInnerEntity**](GetManagedIssues200ResponseDataInnerEntity.md) |  | [optional] 
**id** | **int** | This Issue&#39;s unique ID. | [optional] [readonly] 
**services** | **List[int]** | An array of Managed Service IDs that were affected by this Issue. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_managed_issues200_response_data_inner import GetManagedIssues200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedIssues200ResponseDataInner from a JSON string
get_managed_issues200_response_data_inner_instance = GetManagedIssues200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetManagedIssues200ResponseDataInner.to_json())

# convert the object into a dict
get_managed_issues200_response_data_inner_dict = get_managed_issues200_response_data_inner_instance.to_dict()
# create an instance of GetManagedIssues200ResponseDataInner from a dict
get_managed_issues200_response_data_inner_from_dict = GetManagedIssues200ResponseDataInner.from_dict(get_managed_issues200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


