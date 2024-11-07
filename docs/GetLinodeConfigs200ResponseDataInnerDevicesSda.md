# GetLinodeConfigs200ResponseDataInnerDevicesSda

Device can be either a Disk or Volume identified by `disk_id` or `volume_id`. Only one type per slot allowed. Can be null. Devices mapped from _sde_ through _sdh_ are unavailable in `fullvirt` virt_mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | **int** | The Disk ID, or &#x60;null&#x60; if a Volume is assigned to this slot. | [optional] 
**volume_id** | **int** | The Volume ID, or &#x60;null&#x60; if a Disk is assigned to this slot. | [optional] 

## Example

```python
from openapi_client.models.get_linode_configs200_response_data_inner_devices_sda import GetLinodeConfigs200ResponseDataInnerDevicesSda

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeConfigs200ResponseDataInnerDevicesSda from a JSON string
get_linode_configs200_response_data_inner_devices_sda_instance = GetLinodeConfigs200ResponseDataInnerDevicesSda.from_json(json)
# print the JSON string representation of the object
print(GetLinodeConfigs200ResponseDataInnerDevicesSda.to_json())

# convert the object into a dict
get_linode_configs200_response_data_inner_devices_sda_dict = get_linode_configs200_response_data_inner_devices_sda_instance.to_dict()
# create an instance of GetLinodeConfigs200ResponseDataInnerDevicesSda from a dict
get_linode_configs200_response_data_inner_devices_sda_from_dict = GetLinodeConfigs200ResponseDataInnerDevicesSda.from_dict(get_linode_configs200_response_data_inner_devices_sda_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


