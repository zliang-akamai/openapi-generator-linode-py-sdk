# PostObjectStorageSslRequest

Upload a TLS/SSL certificate and private key to be served when you visit your Object Storage bucket via HTTPS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | Your Base64 encoded and PEM formatted SSL certificate.  Line breaks must be represented as &#x60;\\n&#x60; in the string for requests (but not when using the Linode CLI) | 
**private_key** | **str** | The private key associated with this TLS/SSL certificate.  Line breaks must be represented as &#x60;\\n&#x60; in the string for requests (but not when using the Linode CLI) | 

## Example

```python
from openapi_client.models.post_object_storage_ssl_request import PostObjectStorageSslRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostObjectStorageSslRequest from a JSON string
post_object_storage_ssl_request_instance = PostObjectStorageSslRequest.from_json(json)
# print the JSON string representation of the object
print(PostObjectStorageSslRequest.to_json())

# convert the object into a dict
post_object_storage_ssl_request_dict = post_object_storage_ssl_request_instance.to_dict()
# create an instance of PostObjectStorageSslRequest from a dict
post_object_storage_ssl_request_from_dict = PostObjectStorageSslRequest.from_dict(post_object_storage_ssl_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


