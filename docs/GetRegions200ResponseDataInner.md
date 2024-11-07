# GetRegions200ResponseDataInner

An area where Linode services are available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **List[str]** | A list of capabilities of this region. | [optional] [readonly] 
**country** | **str** | The country where this Region resides. | [optional] [readonly] 
**id** | **str** | The unique ID of this Region. | [optional] [readonly] 
**label** | **str** | Detailed location information for this Region, including city, state or region, and country. | [optional] [readonly] 
**placement_group_limits** | [**GetRegions200ResponseDataInnerPlacementGroupLimits**](GetRegions200ResponseDataInnerPlacementGroupLimits.md) |  | [optional] 
**resolvers** | [**GetRegions200ResponseDataInnerResolvers**](GetRegions200ResponseDataInnerResolvers.md) |  | [optional] 
**site_type** | **str** | This region&#39;s site type. A &#x60;core&#x60; region indicates a traditional cloud computing [region](https://www.linode.com/docs/products/platform/get-started/guides/choose-a-data-center/#product-availability) that offers all compute services. A &#x60;distributed&#x60; region indicates sites that are globally dispersed to be closer to end users and workloads. These regions offer limited services. | [optional] [readonly] 
**status** | **str** | This region&#39;s current operational status. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_regions200_response_data_inner import GetRegions200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRegions200ResponseDataInner from a JSON string
get_regions200_response_data_inner_instance = GetRegions200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetRegions200ResponseDataInner.to_json())

# convert the object into a dict
get_regions200_response_data_inner_dict = get_regions200_response_data_inner_instance.to_dict()
# create an instance of GetRegions200ResponseDataInner from a dict
get_regions200_response_data_inner_from_dict = GetRegions200ResponseDataInner.from_dict(get_regions200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


