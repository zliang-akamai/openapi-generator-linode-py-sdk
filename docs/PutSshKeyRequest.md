# PutSshKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | A label for the SSH Key. | [optional] 

## Example

```python
from openapi_client.models.put_ssh_key_request import PutSshKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutSshKeyRequest from a JSON string
put_ssh_key_request_instance = PutSshKeyRequest.from_json(json)
# print the JSON string representation of the object
print(PutSshKeyRequest.to_json())

# convert the object into a dict
put_ssh_key_request_dict = put_ssh_key_request_instance.to_dict()
# create an instance of PutSshKeyRequest from a dict
put_ssh_key_request_from_dict = PutSshKeyRequest.from_dict(put_ssh_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


