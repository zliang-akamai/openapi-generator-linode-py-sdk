# AddedGetEntityTransfers200AllOfData

An object representing an Entity Transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When this transfer was created. | [optional] 
**entities** | [**AddedGetEntityTransfers200AllOfEntities**](AddedGetEntityTransfers200AllOfEntities.md) |  | [optional] 
**expiry** | **datetime** | When this transfer expires. Transfers will automatically expire 24 hours after creation. | [optional] 
**is_sender** | **bool** | If the requesting account created this transfer. | [optional] 
**status** | **str** | The status of the transfer request:  &#x60;accepted&#x60;: The transfer has been accepted by another user and is currently in progress. Transfers can take up to 3 hours to complete. &#x60;canceled&#x60;: The transfer has been canceled by the sender. &#x60;completed&#x60;: The transfer has completed successfully. &#x60;failed&#x60;: The transfer has failed after initiation. &#x60;pending&#x60;: The transfer is ready to be accepted. &#x60;stale&#x60;: The transfer has exceeded its expiration date. It can no longer be accepted or canceled. | [optional] 
**token** | **str** | The token used to identify and accept or cancel this transfer. | [optional] 
**updated** | **datetime** | When this transfer was last updated. | [optional] 

## Example

```python
from openapi_client.models.added_get_entity_transfers200_all_of_data import AddedGetEntityTransfers200AllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of AddedGetEntityTransfers200AllOfData from a JSON string
added_get_entity_transfers200_all_of_data_instance = AddedGetEntityTransfers200AllOfData.from_json(json)
# print the JSON string representation of the object
print(AddedGetEntityTransfers200AllOfData.to_json())

# convert the object into a dict
added_get_entity_transfers200_all_of_data_dict = added_get_entity_transfers200_all_of_data_instance.to_dict()
# create an instance of AddedGetEntityTransfers200AllOfData from a dict
added_get_entity_transfers200_all_of_data_from_dict = AddedGetEntityTransfers200AllOfData.from_dict(added_get_entity_transfers200_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


