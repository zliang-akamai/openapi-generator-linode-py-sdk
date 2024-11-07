# GetRegions200ResponseDataInnerPlacementGroupLimits

The limits for [placement groups](https://www.linode.com/docs/products/compute/compute-instances/guides/placement-groups/) in this region.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_linodes_per_pg** | **int** | The maximum number of compute instances you can include in a single placement group in this region. | [optional] [readonly] 
**maximum_pgs_per_customer** | **int** | The maximum number of placement groups you can have in this region. Displayed as &#x60;null&#x60; if you don&#39;t have a limit. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_regions200_response_data_inner_placement_group_limits import GetRegions200ResponseDataInnerPlacementGroupLimits

# TODO update the JSON string below
json = "{}"
# create an instance of GetRegions200ResponseDataInnerPlacementGroupLimits from a JSON string
get_regions200_response_data_inner_placement_group_limits_instance = GetRegions200ResponseDataInnerPlacementGroupLimits.from_json(json)
# print the JSON string representation of the object
print(GetRegions200ResponseDataInnerPlacementGroupLimits.to_json())

# convert the object into a dict
get_regions200_response_data_inner_placement_group_limits_dict = get_regions200_response_data_inner_placement_group_limits_instance.to_dict()
# create an instance of GetRegions200ResponseDataInnerPlacementGroupLimits from a dict
get_regions200_response_data_inner_placement_group_limits_from_dict = GetRegions200ResponseDataInnerPlacementGroupLimits.from_dict(get_regions200_response_data_inner_placement_group_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


