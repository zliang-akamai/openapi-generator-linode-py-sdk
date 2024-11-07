# PutLinodeIpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rdns** | **str** | The reverse DNS assigned to this address. For public IPv4 addresses, this will be set to a default value provided by Linode if not explicitly set. | 

## Example

```python
from openapi_client.models.put_linode_ip_request import PutLinodeIpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutLinodeIpRequest from a JSON string
put_linode_ip_request_instance = PutLinodeIpRequest.from_json(json)
# print the JSON string representation of the object
print(PutLinodeIpRequest.to_json())

# convert the object into a dict
put_linode_ip_request_dict = put_linode_ip_request_instance.to_dict()
# create an instance of PutLinodeIpRequest from a dict
put_linode_ip_request_from_dict = PutLinodeIpRequest.from_dict(put_linode_ip_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


