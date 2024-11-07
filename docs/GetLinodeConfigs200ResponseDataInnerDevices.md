# GetLinodeConfigs200ResponseDataInnerDevices

A dictionary of device disks to use as a device map in a Linode's configuration profile.  - An empty device disk dictionary or a dictionary with empty values for device slots is allowed. - If no devices are specified, booting from this configuration will hold until a device exists that allows the boot process to start.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sda** | [**GetLinodeConfigs200ResponseDataInnerDevicesSda**](GetLinodeConfigs200ResponseDataInnerDevicesSda.md) |  | [optional] 
**sdb** | [**GetLinodeConfigs200ResponseDataInnerDevicesSda**](GetLinodeConfigs200ResponseDataInnerDevicesSda.md) |  | [optional] 
**sdc** | [**GetLinodeConfigs200ResponseDataInnerDevicesSda**](GetLinodeConfigs200ResponseDataInnerDevicesSda.md) |  | [optional] 
**sdd** | [**GetLinodeConfigs200ResponseDataInnerDevicesSda**](GetLinodeConfigs200ResponseDataInnerDevicesSda.md) |  | [optional] 
**sde** | [**GetLinodeConfigs200ResponseDataInnerDevicesSda**](GetLinodeConfigs200ResponseDataInnerDevicesSda.md) |  | [optional] 
**sdf** | [**GetLinodeConfigs200ResponseDataInnerDevicesSda**](GetLinodeConfigs200ResponseDataInnerDevicesSda.md) |  | [optional] 
**sdg** | [**GetLinodeConfigs200ResponseDataInnerDevicesSda**](GetLinodeConfigs200ResponseDataInnerDevicesSda.md) |  | [optional] 
**sdh** | [**GetLinodeConfigs200ResponseDataInnerDevicesSda**](GetLinodeConfigs200ResponseDataInnerDevicesSda.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_linode_configs200_response_data_inner_devices import GetLinodeConfigs200ResponseDataInnerDevices

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeConfigs200ResponseDataInnerDevices from a JSON string
get_linode_configs200_response_data_inner_devices_instance = GetLinodeConfigs200ResponseDataInnerDevices.from_json(json)
# print the JSON string representation of the object
print(GetLinodeConfigs200ResponseDataInnerDevices.to_json())

# convert the object into a dict
get_linode_configs200_response_data_inner_devices_dict = get_linode_configs200_response_data_inner_devices_instance.to_dict()
# create an instance of GetLinodeConfigs200ResponseDataInnerDevices from a dict
get_linode_configs200_response_data_inner_devices_from_dict = GetLinodeConfigs200ResponseDataInnerDevices.from_dict(get_linode_configs200_response_data_inner_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


