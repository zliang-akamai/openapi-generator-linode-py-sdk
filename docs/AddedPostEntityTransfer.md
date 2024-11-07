# AddedPostEntityTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**GetEntityTransfers200ResponseAllOfDataInnerEntities**](GetEntityTransfers200ResponseAllOfDataInnerEntities.md) |  | 

## Example

```python
from openapi_client.models.added_post_entity_transfer import AddedPostEntityTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of AddedPostEntityTransfer from a JSON string
added_post_entity_transfer_instance = AddedPostEntityTransfer.from_json(json)
# print the JSON string representation of the object
print(AddedPostEntityTransfer.to_json())

# convert the object into a dict
added_post_entity_transfer_dict = added_post_entity_transfer_instance.to_dict()
# create an instance of AddedPostEntityTransfer from a dict
added_post_entity_transfer_from_dict = AddedPostEntityTransfer.from_dict(added_post_entity_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


