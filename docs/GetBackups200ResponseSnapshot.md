# GetBackups200ResponseSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | [**GetBackups200ResponseSnapshotCurrent**](GetBackups200ResponseSnapshotCurrent.md) |  | [optional] 
**in_progress** | [**GetBackups200ResponseSnapshotCurrent**](GetBackups200ResponseSnapshotCurrent.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_backups200_response_snapshot import GetBackups200ResponseSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of GetBackups200ResponseSnapshot from a JSON string
get_backups200_response_snapshot_instance = GetBackups200ResponseSnapshot.from_json(json)
# print the JSON string representation of the object
print(GetBackups200ResponseSnapshot.to_json())

# convert the object into a dict
get_backups200_response_snapshot_dict = get_backups200_response_snapshot_instance.to_dict()
# create an instance of GetBackups200ResponseSnapshot from a dict
get_backups200_response_snapshot_from_dict = GetBackups200ResponseSnapshot.from_dict(get_backups200_response_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


