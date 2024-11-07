# GetServiceTransfers200ResponseDataInner

An object representing a Service Transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When this transfer was created. | [optional] 
**entities** | [**GetServiceTransfers200ResponseDataInnerEntities**](GetServiceTransfers200ResponseDataInnerEntities.md) |  | [optional] 
**expiry** | **datetime** | When this transfer expires. Transfers will automatically expire 24 hours after creation. | [optional] 
**is_sender** | **bool** | If the requesting account created this transfer. | [optional] 
**status** | **str** | The status of the transfer request.  &#x60;accepted&#x60;: The transfer has been accepted by another user and is currently in progress. Transfers can take up to 3 hours to complete.  &#x60;canceled&#x60;: The transfer has been canceled by the sender.  &#x60;completed&#x60;: The transfer has completed successfully.  &#x60;failed&#x60;: The transfer has failed after initiation.  &#x60;pending&#x60;: The transfer is ready to be accepted.  &#x60;stale&#x60;: The transfer has exceeded its expiration date. It can no longer be accepted or canceled. | [optional] 
**token** | **str** | The token used to identify and accept or cancel this transfer. | [optional] 
**updated** | **datetime** | When this transfer was last updated. | [optional] 

## Example

```python
from openapi_client.models.get_service_transfers200_response_data_inner import GetServiceTransfers200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetServiceTransfers200ResponseDataInner from a JSON string
get_service_transfers200_response_data_inner_instance = GetServiceTransfers200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetServiceTransfers200ResponseDataInner.to_json())

# convert the object into a dict
get_service_transfers200_response_data_inner_dict = get_service_transfers200_response_data_inner_instance.to_dict()
# create an instance of GetServiceTransfers200ResponseDataInner from a dict
get_service_transfers200_response_data_inner_from_dict = GetServiceTransfers200ResponseDataInner.from_dict(get_service_transfers200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


