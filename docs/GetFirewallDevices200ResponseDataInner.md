# GetFirewallDevices200ResponseDataInner

Associates a Firewall with a Linode or NodeBalancer service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When this Device was created. | [optional] [readonly] 
**entity** | [**GetFirewallDevices200ResponseDataInnerEntity**](GetFirewallDevices200ResponseDataInnerEntity.md) |  | [optional] 
**id** | **int** | The Device&#39;s unique ID. | [optional] 
**updated** | **datetime** | When this Device was last updated. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_firewall_devices200_response_data_inner import GetFirewallDevices200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetFirewallDevices200ResponseDataInner from a JSON string
get_firewall_devices200_response_data_inner_instance = GetFirewallDevices200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetFirewallDevices200ResponseDataInner.to_json())

# convert the object into a dict
get_firewall_devices200_response_data_inner_dict = get_firewall_devices200_response_data_inner_instance.to_dict()
# create an instance of GetFirewallDevices200ResponseDataInner from a dict
get_firewall_devices200_response_data_inner_from_dict = GetFirewallDevices200ResponseDataInner.from_dict(get_firewall_devices200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


