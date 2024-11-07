# GetManagedLinodeSettings200ResponseDataInner

Settings for a specific Linode related to Managed Services. There is one ManagedLinodeSettings object for each Linode on your Account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | The group of the Linode these Settings are for. This is for display purposes only. | [optional] [readonly] 
**id** | **int** | The ID of the Linode these Settings are for. | [optional] [readonly] 
**label** | **str** | The label of the Linode these Settings are for. | [optional] [readonly] 
**ssh** | [**GetManagedLinodeSettings200ResponseDataInnerSsh**](GetManagedLinodeSettings200ResponseDataInnerSsh.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_managed_linode_settings200_response_data_inner import GetManagedLinodeSettings200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedLinodeSettings200ResponseDataInner from a JSON string
get_managed_linode_settings200_response_data_inner_instance = GetManagedLinodeSettings200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetManagedLinodeSettings200ResponseDataInner.to_json())

# convert the object into a dict
get_managed_linode_settings200_response_data_inner_dict = get_managed_linode_settings200_response_data_inner_instance.to_dict()
# create an instance of GetManagedLinodeSettings200ResponseDataInner from a dict
get_managed_linode_settings200_response_data_inner_from_dict = GetManagedLinodeSettings200ResponseDataInner.from_dict(get_managed_linode_settings200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


