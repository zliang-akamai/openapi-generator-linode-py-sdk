# GetDevices200ResponseDataInner

A trusted device object represents an active Remember Me session with [login.linode.com](https://login.linode.com).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When this Remember Me session was started.  This corresponds to the time of login with the \&quot;Remember Me\&quot; box checked. | [optional] [readonly] 
**expiry** | **datetime** | When this TrustedDevice session expires.  Sessions typically last 30 days. | [optional] [readonly] 
**id** | **int** | The unique ID for this TrustedDevice. | [optional] [readonly] 
**last_authenticated** | **datetime** | The last time this TrustedDevice was successfully used to authenticate to [login.linode.com](https://login.linode.com). | [optional] [readonly] 
**last_remote_addr** | **str** | The last IP Address to successfully authenticate with this TrustedDevice. | [optional] [readonly] 
**user_agent** | **str** | The User Agent of the browser that created this TrustedDevice session. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_devices200_response_data_inner import GetDevices200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDevices200ResponseDataInner from a JSON string
get_devices200_response_data_inner_instance = GetDevices200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetDevices200ResponseDataInner.to_json())

# convert the object into a dict
get_devices200_response_data_inner_dict = get_devices200_response_data_inner_instance.to_dict()
# create an instance of GetDevices200ResponseDataInner from a dict
get_devices200_response_data_inner_from_dict = GetDevices200ResponseDataInner.from_dict(get_devices200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


