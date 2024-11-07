# PostCloneDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The new domain for the clone. Domain labels cannot be longer than 63 characters and must conform to [RFC1035](https://tools.ietf.org/html/rfc1035). Domains must be unique on Linode&#39;s platform, including across different Linode accounts; there cannot be two Domains representing the same domain. | 

## Example

```python
from openapi_client.models.post_clone_domain_request import PostCloneDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCloneDomainRequest from a JSON string
post_clone_domain_request_instance = PostCloneDomainRequest.from_json(json)
# print the JSON string representation of the object
print(PostCloneDomainRequest.to_json())

# convert the object into a dict
post_clone_domain_request_dict = post_clone_domain_request_instance.to_dict()
# create an instance of PostCloneDomainRequest from a dict
post_clone_domain_request_from_dict = PostCloneDomainRequest.from_dict(post_clone_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


