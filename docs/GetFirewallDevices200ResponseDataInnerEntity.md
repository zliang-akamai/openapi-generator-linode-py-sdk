# GetFirewallDevices200ResponseDataInnerEntity

The compute service that this Firewall has been applied to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The entity&#39;s ID. | [optional] 
**label** | **str** | The entity&#39;s label. | [optional] [readonly] 
**type** | **str** | The entity&#39;s type. | [optional] 
**url** | **str** | The API URL path you can use to access this entity. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_firewall_devices200_response_data_inner_entity import GetFirewallDevices200ResponseDataInnerEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GetFirewallDevices200ResponseDataInnerEntity from a JSON string
get_firewall_devices200_response_data_inner_entity_instance = GetFirewallDevices200ResponseDataInnerEntity.from_json(json)
# print the JSON string representation of the object
print(GetFirewallDevices200ResponseDataInnerEntity.to_json())

# convert the object into a dict
get_firewall_devices200_response_data_inner_entity_dict = get_firewall_devices200_response_data_inner_entity_instance.to_dict()
# create an instance of GetFirewallDevices200ResponseDataInnerEntity from a dict
get_firewall_devices200_response_data_inner_entity_from_dict = GetFirewallDevices200ResponseDataInnerEntity.from_dict(get_firewall_devices200_response_data_inner_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


