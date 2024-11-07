# GetPlacementGroups200ResponseDataInnerMigrationsOutboundInner

The individual compute instances the system is migrating out of the placement group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linode_id** | **int** | The unique identifier for a compute instance being migrated out of the placement group. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_placement_groups200_response_data_inner_migrations_outbound_inner import GetPlacementGroups200ResponseDataInnerMigrationsOutboundInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlacementGroups200ResponseDataInnerMigrationsOutboundInner from a JSON string
get_placement_groups200_response_data_inner_migrations_outbound_inner_instance = GetPlacementGroups200ResponseDataInnerMigrationsOutboundInner.from_json(json)
# print the JSON string representation of the object
print(GetPlacementGroups200ResponseDataInnerMigrationsOutboundInner.to_json())

# convert the object into a dict
get_placement_groups200_response_data_inner_migrations_outbound_inner_dict = get_placement_groups200_response_data_inner_migrations_outbound_inner_instance.to_dict()
# create an instance of GetPlacementGroups200ResponseDataInnerMigrationsOutboundInner from a dict
get_placement_groups200_response_data_inner_migrations_outbound_inner_from_dict = GetPlacementGroups200ResponseDataInnerMigrationsOutboundInner.from_dict(get_placement_groups200_response_data_inner_migrations_outbound_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


