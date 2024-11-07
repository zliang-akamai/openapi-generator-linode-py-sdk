# PostIpv6RangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linode_id** | **int** | The ID of the Linode to assign this range to. The SLAAC address for the provided Linode is used as the range&#39;s &#x60;route_target&#x60;.  - __Required__ if &#x60;route_target&#x60; is omitted from the request.  - Mutually exclusive with &#x60;route_target&#x60;. Submitting values for both properties in a request results in an error. | [optional] 
**prefix_length** | **int** | The prefix length of the IPv6 range. | 
**route_target** | **str** | The IPv6 SLAAC address to assign this range to.  - __Required__ if &#x60;linode_id&#x60; is omitted from the request.  - Mutually exclusive with &#x60;linode_id&#x60;. Submitting values for both properties in a request results in an error.  - __Note__. Omit the &#x60;/128&#x60; prefix length of the SLAAC address when using this property. | [optional] 

## Example

```python
from openapi_client.models.post_ipv6_range_request import PostIpv6RangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostIpv6RangeRequest from a JSON string
post_ipv6_range_request_instance = PostIpv6RangeRequest.from_json(json)
# print the JSON string representation of the object
print(PostIpv6RangeRequest.to_json())

# convert the object into a dict
post_ipv6_range_request_dict = post_ipv6_range_request_instance.to_dict()
# create an instance of PostIpv6RangeRequest from a dict
post_ipv6_range_request_from_dict = PostIpv6RangeRequest.from_dict(post_ipv6_range_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


