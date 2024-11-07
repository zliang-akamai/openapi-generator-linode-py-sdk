# PostImportDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain to import. | 
**remote_nameserver** | **str** | The remote nameserver that allows zone transfers (AXFR). | 

## Example

```python
from openapi_client.models.post_import_domain_request import PostImportDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostImportDomainRequest from a JSON string
post_import_domain_request_instance = PostImportDomainRequest.from_json(json)
# print the JSON string representation of the object
print(PostImportDomainRequest.to_json())

# convert the object into a dict
post_import_domain_request_dict = post_import_domain_request_instance.to_dict()
# create an instance of PostImportDomainRequest from a dict
post_import_domain_request_from_dict = PostImportDomainRequest.from_dict(post_import_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


