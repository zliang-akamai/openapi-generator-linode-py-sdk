# GetRegions200ResponseDataInnerResolvers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | **str** | The IPv4 addresses for this region&#39;s DNS resolvers, separated by commas. | [optional] [readonly] 
**ipv6** | **str** | The IPv6 addresses for this region&#39;s DNS resolvers, separated by commas. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_regions200_response_data_inner_resolvers import GetRegions200ResponseDataInnerResolvers

# TODO update the JSON string below
json = "{}"
# create an instance of GetRegions200ResponseDataInnerResolvers from a JSON string
get_regions200_response_data_inner_resolvers_instance = GetRegions200ResponseDataInnerResolvers.from_json(json)
# print the JSON string representation of the object
print(GetRegions200ResponseDataInnerResolvers.to_json())

# convert the object into a dict
get_regions200_response_data_inner_resolvers_dict = get_regions200_response_data_inner_resolvers_instance.to_dict()
# create an instance of GetRegions200ResponseDataInnerResolvers from a dict
get_regions200_response_data_inner_resolvers_from_dict = GetRegions200ResponseDataInnerResolvers.from_dict(get_regions200_response_data_inner_resolvers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


