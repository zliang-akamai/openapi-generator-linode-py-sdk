# PostDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**axfr_ips** | **List[str]** | The list of IPs that may perform a zone transfer for this Domain. The total combined length of all data within this array cannot exceed 1000 characters.  __Note__. This is potentially dangerous, and should be set to an empty list unless you intend to use it. | [optional] 
**description** | **str** | A description for this Domain. This is for display purposes only. | [optional] 
**domain** | **str** | The domain this Domain represents. Domain labels cannot be longer than 63 characters and must conform to [RFC1035](https://tools.ietf.org/html/rfc1035). Domains must be unique on Linode&#39;s platform, including across different Linode accounts; there cannot be two Domains representing the same domain. | 
**expire_sec** | **int** | The amount of time in seconds that may pass before this Domain is no longer authoritative.  - Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  - Any other value is rounded up to the nearest valid value.  - A value of 0 is equivalent to the default value of 1209600. | [optional] [default to 0]
**group** | **str** | The group this Domain belongs to.  This is for display purposes only. | [optional] 
**id** | **int** | This Domain&#39;s unique ID. | [optional] [readonly] 
**master_ips** | **List[str]** | The IP addresses representing the master DNS for this Domain. At least one value is required for &#x60;type&#x60; slave Domains. The total combined length of all data within this array cannot exceed 1000 characters. | [optional] 
**refresh_sec** | **int** | The amount of time in seconds before this Domain should be refreshed.  - Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  - Any other value is rounded up to the nearest valid value.  - A value of 0 is equivalent to the default value of 14400. | [optional] [default to 0]
**retry_sec** | **int** | The interval, in seconds, at which a failed refresh should be retried.  - Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  - Any other value is rounded up to the nearest valid value.  - A value of 0 is equivalent to the default value of 14400. | [optional] [default to 0]
**soa_email** | **str** | Start of Authority email address. This is required for &#x60;type&#x60; master Domains. | [optional] 
**status** | **str** | Used to control whether this Domain is currently being rendered. | [optional] [default to 'active']
**tags** | **List[str]** | An array of tags applied to this object.  Tags are for organizational purposes only. | [optional] 
**ttl_sec** | **int** | \&quot;Time to Live\&quot; - the amount of time in seconds that this Domain&#39;s records may be cached by resolvers or other domain servers.  - Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200. - Any other value is rounded up to the nearest valid value. - A value of 0 is equivalent to the default value of 86400. | [optional] [default to 0]
**type** | **str** | Whether this Domain represents the authoritative source of information for the domain it describes (&#x60;master&#x60;), or whether it is a read-only copy of a master (&#x60;slave&#x60;). | 

## Example

```python
from openapi_client.models.post_domain_request import PostDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDomainRequest from a JSON string
post_domain_request_instance = PostDomainRequest.from_json(json)
# print the JSON string representation of the object
print(PostDomainRequest.to_json())

# convert the object into a dict
post_domain_request_dict = post_domain_request_instance.to_dict()
# create an instance of PostDomainRequest from a dict
post_domain_request_from_dict = PostDomainRequest.from_dict(post_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


