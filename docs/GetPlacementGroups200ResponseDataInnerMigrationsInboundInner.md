# GetPlacementGroups200ResponseDataInnerMigrationsInboundInner

The individual compute instances the system is migrating into the placement group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linode_id** | **int** | The unique identifier for a compute instance being migrated into the placement group. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_placement_groups200_response_data_inner_migrations_inbound_inner import GetPlacementGroups200ResponseDataInnerMigrationsInboundInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlacementGroups200ResponseDataInnerMigrationsInboundInner from a JSON string
get_placement_groups200_response_data_inner_migrations_inbound_inner_instance = GetPlacementGroups200ResponseDataInnerMigrationsInboundInner.from_json(json)
# print the JSON string representation of the object
print(GetPlacementGroups200ResponseDataInnerMigrationsInboundInner.to_json())

# convert the object into a dict
get_placement_groups200_response_data_inner_migrations_inbound_inner_dict = get_placement_groups200_response_data_inner_migrations_inbound_inner_instance.to_dict()
# create an instance of GetPlacementGroups200ResponseDataInnerMigrationsInboundInner from a dict
get_placement_groups200_response_data_inner_migrations_inbound_inner_from_dict = GetPlacementGroups200ResponseDataInnerMigrationsInboundInner.from_dict(get_placement_groups200_response_data_inner_migrations_inbound_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


