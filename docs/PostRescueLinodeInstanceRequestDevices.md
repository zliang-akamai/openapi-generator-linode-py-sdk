# PostRescueLinodeInstanceRequestDevices


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

## Example

```python
from openapi_client.models.post_rescue_linode_instance_request_devices import PostRescueLinodeInstanceRequestDevices

# TODO update the JSON string below
json = "{}"
# create an instance of PostRescueLinodeInstanceRequestDevices from a JSON string
post_rescue_linode_instance_request_devices_instance = PostRescueLinodeInstanceRequestDevices.from_json(json)
# print the JSON string representation of the object
print(PostRescueLinodeInstanceRequestDevices.to_json())

# convert the object into a dict
post_rescue_linode_instance_request_devices_dict = post_rescue_linode_instance_request_devices_instance.to_dict()
# create an instance of PostRescueLinodeInstanceRequestDevices from a dict
post_rescue_linode_instance_request_devices_from_dict = PostRescueLinodeInstanceRequestDevices.from_dict(post_rescue_linode_instance_request_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


