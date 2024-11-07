# GetObjectStorageSsl200Response

If this Object Storage bucket has a corresponding TLS/SSL Certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssl** | **bool** | A boolean indicating if this Bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_object_storage_ssl200_response import GetObjectStorageSsl200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectStorageSsl200Response from a JSON string
get_object_storage_ssl200_response_instance = GetObjectStorageSsl200Response.from_json(json)
# print the JSON string representation of the object
print(GetObjectStorageSsl200Response.to_json())

# convert the object into a dict
get_object_storage_ssl200_response_dict = get_object_storage_ssl200_response_instance.to_dict()
# create an instance of GetObjectStorageSsl200Response from a dict
get_object_storage_ssl200_response_from_dict = GetObjectStorageSsl200Response.from_dict(get_object_storage_ssl200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


