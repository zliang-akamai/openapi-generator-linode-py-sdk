# PostServiceTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**GetServiceTransfers200ResponseDataInnerEntities**](GetServiceTransfers200ResponseDataInnerEntities.md) |  | 

## Example

```python
from openapi_client.models.post_service_transfer_request import PostServiceTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServiceTransferRequest from a JSON string
post_service_transfer_request_instance = PostServiceTransferRequest.from_json(json)
# print the JSON string representation of the object
print(PostServiceTransferRequest.to_json())

# convert the object into a dict
post_service_transfer_request_dict = post_service_transfer_request_instance.to_dict()
# create an instance of PostServiceTransferRequest from a dict
post_service_transfer_request_from_dict = PostServiceTransferRequest.from_dict(post_service_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


