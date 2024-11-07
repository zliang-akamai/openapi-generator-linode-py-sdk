# GetSshKeys200ResponseDataInner

A credential object for authenticating a User's secure shell connection to a Linode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The date this key was added. | [optional] [readonly] 
**id** | **int** | The unique identifier of an SSH Key object. | [optional] [readonly] 
**label** | **str** | A label for the SSH Key. | [optional] 
**ssh_key** | **str** | The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.  Accepted formats:  - ssh-dss - ssh-rsa - ecdsa-sha2-nistp - ssh-ed25519 - sk-ecdsa-sha2-nistp256 (Akamai-specific) | [optional] 

## Example

```python
from openapi_client.models.get_ssh_keys200_response_data_inner import GetSshKeys200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSshKeys200ResponseDataInner from a JSON string
get_ssh_keys200_response_data_inner_instance = GetSshKeys200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetSshKeys200ResponseDataInner.to_json())

# convert the object into a dict
get_ssh_keys200_response_data_inner_dict = get_ssh_keys200_response_data_inner_instance.to_dict()
# create an instance of GetSshKeys200ResponseDataInner from a dict
get_ssh_keys200_response_data_inner_from_dict = GetSshKeys200ResponseDataInner.from_dict(get_ssh_keys200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


