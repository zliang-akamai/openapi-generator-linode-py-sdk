# PostShareIpsRequest

A request object IP Addresses Share (POST /networking/ips/share).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **List[str]** | A list of secondary Linode IPs to share with the primary Linode.  - Can include both IPv4 addresses and IPv6 ranges (omit /56 and /64 prefix lengths) - Can include both private and public IPv4 addresses. - You must have access to all of these addresses and they must be in the same Region as the primary Linode. - Enter an empty array to remove all shared IP addresses. | 
**linode_id** | **int** | The ID of the primary Linode that the addresses will be shared with. | 

## Example

```python
from openapi_client.models.post_share_ips_request import PostShareIpsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostShareIpsRequest from a JSON string
post_share_ips_request_instance = PostShareIpsRequest.from_json(json)
# print the JSON string representation of the object
print(PostShareIpsRequest.to_json())

# convert the object into a dict
post_share_ips_request_dict = post_share_ips_request_instance.to_dict()
# create an instance of PostShareIpsRequest from a dict
post_share_ips_request_from_dict = PostShareIpsRequest.from_dict(post_share_ips_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


