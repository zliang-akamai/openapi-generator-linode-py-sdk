# GetManagedCredentials200ResponseDataInner

A securely stored Credential that allows Linode's special forces to access a Managed server to respond to Issues.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | This Credential&#39;s unique ID. | [optional] [readonly] 
**label** | **str** | The unique label for this Credential. This is for display purposes only. | [optional] 
**last_decrypted** | **datetime** | The date this Credential was last decrypted by a member of Linode special forces. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_managed_credentials200_response_data_inner import GetManagedCredentials200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedCredentials200ResponseDataInner from a JSON string
get_managed_credentials200_response_data_inner_instance = GetManagedCredentials200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetManagedCredentials200ResponseDataInner.to_json())

# convert the object into a dict
get_managed_credentials200_response_data_inner_dict = get_managed_credentials200_response_data_inner_instance.to_dict()
# create an instance of GetManagedCredentials200ResponseDataInner from a dict
get_managed_credentials200_response_data_inner_from_dict = GetManagedCredentials200ResponseDataInner.from_dict(get_managed_credentials200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


