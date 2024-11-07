# GetLinodeConfigs200ResponseDataInnerHelpers

Helpers enabled when booting to this Linode Config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devtmpfs_automount** | **bool** | Populates the /dev directory early during boot without udev.  Defaults to false. | [optional] 
**distro** | **bool** | Helps maintain correct inittab/upstart console device. | [optional] 
**modules_dep** | **bool** | Creates a modules dependency file for the Kernel you run. | [optional] 
**network** | **bool** | Automatically configures static networking. | [optional] 
**updatedb_disabled** | **bool** | Disables updatedb cron job to avoid disk thrashing. | [optional] 

## Example

```python
from openapi_client.models.get_linode_configs200_response_data_inner_helpers import GetLinodeConfigs200ResponseDataInnerHelpers

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeConfigs200ResponseDataInnerHelpers from a JSON string
get_linode_configs200_response_data_inner_helpers_instance = GetLinodeConfigs200ResponseDataInnerHelpers.from_json(json)
# print the JSON string representation of the object
print(GetLinodeConfigs200ResponseDataInnerHelpers.to_json())

# convert the object into a dict
get_linode_configs200_response_data_inner_helpers_dict = get_linode_configs200_response_data_inner_helpers_instance.to_dict()
# create an instance of GetLinodeConfigs200ResponseDataInnerHelpers from a dict
get_linode_configs200_response_data_inner_helpers_from_dict = GetLinodeConfigs200ResponseDataInnerHelpers.from_dict(get_linode_configs200_response_data_inner_helpers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


