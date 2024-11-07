# PutDiskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The name of the disk. This is for display purposes only. | [optional] 

## Example

```python
from openapi_client.models.put_disk_request import PutDiskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutDiskRequest from a JSON string
put_disk_request_instance = PutDiskRequest.from_json(json)
# print the JSON string representation of the object
print(PutDiskRequest.to_json())

# convert the object into a dict
put_disk_request_dict = put_disk_request_instance.to_dict()
# create an instance of PutDiskRequest from a dict
put_disk_request_from_dict = PutDiskRequest.from_dict(put_disk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


