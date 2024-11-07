# GetProfileApps200ResponseDataInner

An application you have authorized access to your Account through OAuth.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When this app was authorized. | [optional] [readonly] 
**expiry** | **datetime** | When the app&#39;s access to your account expires. If &#x60;null&#x60;, the app&#39;s access must be revoked manually. | [optional] [readonly] 
**id** | **int** | This authorization&#39;s ID, used for revoking access. | [optional] [readonly] 
**label** | **str** | The name of the application you&#39;ve authorized. | [optional] [readonly] 
**scopes** | **str** | The OAuth scopes this app was authorized with.  This defines what parts of your Account the app is allowed to access. | [optional] [readonly] 
**thumbnail_url** | **str** | The URL at which this app&#39;s thumbnail may be accessed. | [optional] [readonly] 
**website** | **str** | The website where you can get more information about this app. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_profile_apps200_response_data_inner import GetProfileApps200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProfileApps200ResponseDataInner from a JSON string
get_profile_apps200_response_data_inner_instance = GetProfileApps200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetProfileApps200ResponseDataInner.to_json())

# convert the object into a dict
get_profile_apps200_response_data_inner_dict = get_profile_apps200_response_data_inner_instance.to_dict()
# create an instance of GetProfileApps200ResponseDataInner from a dict
get_profile_apps200_response_data_inner_from_dict = GetProfileApps200ResponseDataInner.from_dict(get_profile_apps200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


