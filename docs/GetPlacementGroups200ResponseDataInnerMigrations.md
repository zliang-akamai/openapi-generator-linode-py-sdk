# GetPlacementGroups200ResponseDataInnerMigrations

Any compute instances that are being migrated to or from the placement group. Returns an empty object if no migrations are taking place.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbound** | [**List[GetPlacementGroups200ResponseDataInnerMigrationsInboundInner]**](GetPlacementGroups200ResponseDataInnerMigrationsInboundInner.md) |  | [optional] 
**outbound** | [**List[GetPlacementGroups200ResponseDataInnerMigrationsOutboundInner]**](GetPlacementGroups200ResponseDataInnerMigrationsOutboundInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_placement_groups200_response_data_inner_migrations import GetPlacementGroups200ResponseDataInnerMigrations

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlacementGroups200ResponseDataInnerMigrations from a JSON string
get_placement_groups200_response_data_inner_migrations_instance = GetPlacementGroups200ResponseDataInnerMigrations.from_json(json)
# print the JSON string representation of the object
print(GetPlacementGroups200ResponseDataInnerMigrations.to_json())

# convert the object into a dict
get_placement_groups200_response_data_inner_migrations_dict = get_placement_groups200_response_data_inner_migrations_instance.to_dict()
# create an instance of GetPlacementGroups200ResponseDataInnerMigrations from a dict
get_placement_groups200_response_data_inner_migrations_from_dict = GetPlacementGroups200ResponseDataInnerMigrations.from_dict(get_placement_groups200_response_data_inner_migrations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


