# GetBackups200ResponseAutomaticInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | Whether this Backup is available for restoration.  Backups undergoing maintenance are not available for restoration. | [optional] [readonly] 
**configs** | **List[str]** | A list of the labels of the Configuration profiles that are part of the Backup. | [optional] [readonly] 
**created** | **datetime** | The date the Backup was taken. | [optional] [readonly] 
**disks** | [**List[GetBackups200ResponseAutomaticInnerAllOfDisksInner]**](GetBackups200ResponseAutomaticInnerAllOfDisksInner.md) | A list of the disks that are part of the Backup. | [optional] [readonly] 
**finished** | **datetime** | The date the Backup completed. | [optional] [readonly] 
**id** | **int** | The unique ID of this Backup. | [optional] [readonly] 
**label** | **str** | A label for Backups that are of type &#x60;snapshot&#x60;. | [optional] 
**status** | **str** | The current state of a specific Backup. | [optional] [readonly] 
**type** | **str** |  | [optional] 
**updated** | **datetime** | The date the Backup was most recently updated. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_backups200_response_automatic_inner import GetBackups200ResponseAutomaticInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBackups200ResponseAutomaticInner from a JSON string
get_backups200_response_automatic_inner_instance = GetBackups200ResponseAutomaticInner.from_json(json)
# print the JSON string representation of the object
print(GetBackups200ResponseAutomaticInner.to_json())

# convert the object into a dict
get_backups200_response_automatic_inner_dict = get_backups200_response_automatic_inner_instance.to_dict()
# create an instance of GetBackups200ResponseAutomaticInner from a dict
get_backups200_response_automatic_inner_from_dict = GetBackups200ResponseAutomaticInner.from_dict(get_backups200_response_automatic_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


