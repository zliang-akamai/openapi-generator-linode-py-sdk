# PostIpv6Range200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | **str** | The IPv6 network range, including subnet and prefix length. | [optional] 
**route_target** | **str** | The route target IPV6 SLAAC address for this range. Does not include the prefix length. | [optional] 

## Example

```python
from openapi_client.models.post_ipv6_range200_response import PostIpv6Range200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostIpv6Range200Response from a JSON string
post_ipv6_range200_response_instance = PostIpv6Range200Response.from_json(json)
# print the JSON string representation of the object
print(PostIpv6Range200Response.to_json())

# convert the object into a dict
post_ipv6_range200_response_dict = post_ipv6_range200_response_instance.to_dict()
# create an instance of PostIpv6Range200Response from a dict
post_ipv6_range200_response_from_dict = PostIpv6Range200Response.from_dict(post_ipv6_range200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


