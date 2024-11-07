# GetLinodeTransfer200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable** | **int** | The amount of network transfer this Linode has used, in GB, past your monthly quota. | [optional] [readonly] 
**quota** | **int** | The amount of network transfer this Linode adds to your transfer pool, in GB, for the current month&#39;s billing cycle. | [optional] [readonly] 
**used** | **int** | The amount of network transfer used by this Linode, in bytes, for the current month&#39;s billing cycle. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_linode_transfer200_response import GetLinodeTransfer200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeTransfer200Response from a JSON string
get_linode_transfer200_response_instance = GetLinodeTransfer200Response.from_json(json)
# print the JSON string representation of the object
print(GetLinodeTransfer200Response.to_json())

# convert the object into a dict
get_linode_transfer200_response_dict = get_linode_transfer200_response_instance.to_dict()
# create an instance of GetLinodeTransfer200Response from a dict
get_linode_transfer200_response_from_dict = GetLinodeTransfer200Response.from_dict(get_linode_transfer200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


