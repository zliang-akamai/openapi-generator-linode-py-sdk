# GetLinodeStats200ResponseIo

Input/Output statistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**io** | **List[List[float]]** | Block/s written. | [optional] 
**swap** | **List[List[float]]** | Block/s written. | [optional] 

## Example

```python
from openapi_client.models.get_linode_stats200_response_io import GetLinodeStats200ResponseIo

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeStats200ResponseIo from a JSON string
get_linode_stats200_response_io_instance = GetLinodeStats200ResponseIo.from_json(json)
# print the JSON string representation of the object
print(GetLinodeStats200ResponseIo.to_json())

# convert the object into a dict
get_linode_stats200_response_io_dict = get_linode_stats200_response_io_instance.to_dict()
# create an instance of GetLinodeStats200ResponseIo from a dict
get_linode_stats200_response_io_from_dict = GetLinodeStats200ResponseIo.from_dict(get_linode_stats200_response_io_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


