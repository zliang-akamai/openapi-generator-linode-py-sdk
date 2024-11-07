# GetLongviewClients200ResponseDataInnerApps

The apps this Client is monitoring on your Linode. This is configured when you install the Longview Client application, and is present here for information purposes only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apache** | **bool** | If True, the Apache Longview Client module is monitoring Apache on your server. | [optional] [readonly] 
**mysql** | **bool** | If True, the MySQL Longview Client modules is monitoring MySQL on your server. | [optional] [readonly] 
**nginx** | **bool** | If True, the Nginx Longview Client module is monitoring Nginx on your server. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_longview_clients200_response_data_inner_apps import GetLongviewClients200ResponseDataInnerApps

# TODO update the JSON string below
json = "{}"
# create an instance of GetLongviewClients200ResponseDataInnerApps from a JSON string
get_longview_clients200_response_data_inner_apps_instance = GetLongviewClients200ResponseDataInnerApps.from_json(json)
# print the JSON string representation of the object
print(GetLongviewClients200ResponseDataInnerApps.to_json())

# convert the object into a dict
get_longview_clients200_response_data_inner_apps_dict = get_longview_clients200_response_data_inner_apps_instance.to_dict()
# create an instance of GetLongviewClients200ResponseDataInnerApps from a dict
get_longview_clients200_response_data_inner_apps_from_dict = GetLongviewClients200ResponseDataInnerApps.from_dict(get_longview_clients200_response_data_inner_apps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


