# GetLongviewClients200ResponseDataInner

A LongviewClient is a single monitor set up to track statistics about one of your servers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | The API key for this Client, used when configuring the Longview Client application on your Linode.  Returns as &#x60;[REDACTED]&#x60; if you do not have read-write access to this client. | [optional] [readonly] 
**apps** | [**GetLongviewClients200ResponseDataInnerApps**](GetLongviewClients200ResponseDataInnerApps.md) |  | [optional] 
**created** | **datetime** | When this Longview Client was created. | [optional] [readonly] 
**id** | **int** | This Client&#39;s unique ID. | [optional] [readonly] 
**install_code** | **str** | The install code for this Client, used when configuring the Longview Client application on your Linode.  Returns as &#x60;[REDACTED]&#x60; if you do not have read-write access to this client. | [optional] [readonly] 
**label** | **str** | This Client&#39;s unique label. This is for display purposes only. | [optional] 
**updated** | **datetime** | When this Longview Client was last updated. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_longview_clients200_response_data_inner import GetLongviewClients200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLongviewClients200ResponseDataInner from a JSON string
get_longview_clients200_response_data_inner_instance = GetLongviewClients200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetLongviewClients200ResponseDataInner.to_json())

# convert the object into a dict
get_longview_clients200_response_data_inner_dict = get_longview_clients200_response_data_inner_instance.to_dict()
# create an instance of GetLongviewClients200ResponseDataInner from a dict
get_longview_clients200_response_data_inner_from_dict = GetLongviewClients200ResponseDataInner.from_dict(get_longview_clients200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


