# GetManagedSshKey200Response

A unique SSH public key that allows Linode's special forces to access a Managed server to respond to Issues.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh_key** | **str** | The unique SSH public key assigned to your Linode account&#39;s Managed service. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_managed_ssh_key200_response import GetManagedSshKey200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedSshKey200Response from a JSON string
get_managed_ssh_key200_response_instance = GetManagedSshKey200Response.from_json(json)
# print the JSON string representation of the object
print(GetManagedSshKey200Response.to_json())

# convert the object into a dict
get_managed_ssh_key200_response_dict = get_managed_ssh_key200_response_instance.to_dict()
# create an instance of GetManagedSshKey200Response from a dict
get_managed_ssh_key200_response_from_dict = GetManagedSshKey200Response.from_dict(get_managed_ssh_key200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


