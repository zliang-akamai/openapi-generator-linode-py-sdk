# PostLinodeInstanceRequestAllOfInterfacesInnerIpv4

IPv4 addresses configured for this Interface. Only allowed for `vpc` type Interfaces. Returns `null` if no `vpc` Interface is assigned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nat_1_1** | **str** | The 1:1 NAT IPv4 address, used to associate a public IPv4 address with the VPC Subnet IPv4 address assigned to this Interface.  - Only allowed for &#x60;vpc&#x60; type Interfaces. - Returns &#x60;null&#x60; if no 1:1 NAT is set for a &#x60;vpc&#x60; type Interface. - Returns an empty string (&#x60;\&quot;\&quot;&#x60;) for non-&#x60;vpc&#x60; type Interfaces.  For requests:  - Setting this value to &#x60;any&#x60; enables the Linode&#39;s assigned public IPv4 address on this Interface and establishes a 1:1 NAT between the public IPv4 and VPC Subnet IPv4 addresses. - Setting the value to a specific public IPv4 address that is assigned to the Linode enables a 1:1 NAT between that address and the VPC Subnet IPv4 address. - The public IPv4 address can&#39;t be shared with another Linode. - If omitted, set to &#x60;null&#x60;, or set to an empty string (&#x60;\&quot;\&quot;&#x60;), no 1:1 NAT is established.  &gt; 📘 &gt; &gt; When creating a new compute instance, you can&#39;t set this to a specific IPv4 address. When a new compute instance is created, the network establishes a public IPv4 address for it. Since this address doesn&#39;t exist yet, you can&#39;t include a custom IPv4 address to change it. Once your compute instance is created, you can [update your configuration profile interface](https://www.linode.com/docs/api/linode-instances/#configuration-profile-interface-update) to change the &#x60;nat_1_1&#x60; address. | [optional] 
**vpc** | **str** | The VPC Subnet IPv4 address for this Interface.  - Only allowed for &#x60;vpc&#x60; type Interfaces. - Returns an empty string (&#x60;\&quot;\&quot;&#x60;) for non-&#x60;vpc&#x60; type Interfaces.  For requests:  - Must not already be actively assigned as an address or within a range to any Linodes. - Must not be the first two or last two addresses in the Subnet IPv4 Range. - If omitted, a valid address within the Subnet IPv4 range is automatically assigned. | [optional] 

## Example

```python
from openapi_client.models.post_linode_instance_request_all_of_interfaces_inner_ipv4 import PostLinodeInstanceRequestAllOfInterfacesInnerIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of PostLinodeInstanceRequestAllOfInterfacesInnerIpv4 from a JSON string
post_linode_instance_request_all_of_interfaces_inner_ipv4_instance = PostLinodeInstanceRequestAllOfInterfacesInnerIpv4.from_json(json)
# print the JSON string representation of the object
print(PostLinodeInstanceRequestAllOfInterfacesInnerIpv4.to_json())

# convert the object into a dict
post_linode_instance_request_all_of_interfaces_inner_ipv4_dict = post_linode_instance_request_all_of_interfaces_inner_ipv4_instance.to_dict()
# create an instance of PostLinodeInstanceRequestAllOfInterfacesInnerIpv4 from a dict
post_linode_instance_request_all_of_interfaces_inner_ipv4_from_dict = PostLinodeInstanceRequestAllOfInterfacesInnerIpv4.from_dict(post_linode_instance_request_all_of_interfaces_inner_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


