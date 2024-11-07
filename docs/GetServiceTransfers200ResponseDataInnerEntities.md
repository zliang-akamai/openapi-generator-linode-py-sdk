# GetServiceTransfers200ResponseDataInnerEntities

A collection of the services to include in this transfer request, separated by type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linodes** | **List[int]** | An array containing the IDs of each of the Linodes included in this transfer. | [optional] 

## Example

```python
from openapi_client.models.get_service_transfers200_response_data_inner_entities import GetServiceTransfers200ResponseDataInnerEntities

# TODO update the JSON string below
json = "{}"
# create an instance of GetServiceTransfers200ResponseDataInnerEntities from a JSON string
get_service_transfers200_response_data_inner_entities_instance = GetServiceTransfers200ResponseDataInnerEntities.from_json(json)
# print the JSON string representation of the object
print(GetServiceTransfers200ResponseDataInnerEntities.to_json())

# convert the object into a dict
get_service_transfers200_response_data_inner_entities_dict = get_service_transfers200_response_data_inner_entities_instance.to_dict()
# create an instance of GetServiceTransfers200ResponseDataInnerEntities from a dict
get_service_transfers200_response_data_inner_entities_from_dict = GetServiceTransfers200ResponseDataInnerEntities.from_dict(get_service_transfers200_response_data_inner_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


