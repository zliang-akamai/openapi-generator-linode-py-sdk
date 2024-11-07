# PostEntityTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**GetEntityTransfers200ResponseAllOfDataInnerEntities**](GetEntityTransfers200ResponseAllOfDataInnerEntities.md) |  | 

## Example

```python
from openapi_client.models.post_entity_transfer_request import PostEntityTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostEntityTransferRequest from a JSON string
post_entity_transfer_request_instance = PostEntityTransferRequest.from_json(json)
# print the JSON string representation of the object
print(PostEntityTransferRequest.to_json())

# convert the object into a dict
post_entity_transfer_request_dict = post_entity_transfer_request_instance.to_dict()
# create an instance of PostEntityTransferRequest from a dict
post_entity_transfer_request_from_dict = PostEntityTransferRequest.from_dict(post_entity_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


