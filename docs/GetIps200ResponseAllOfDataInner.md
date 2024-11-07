# GetIps200ResponseAllOfDataInner

An IP address that exists in Linode's system, either IPv4 or IPv6, specific to the response for the [List IP addresses](https://techdocs.akamai.com/linode-api/reference/get-ips) operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IP address. | [optional] [readonly] 
**gateway** | **str** | The default gateway for this address. | [optional] [readonly] 
**linode_id** | **int** | The ID of the Linode this address currently belongs to. For IPv4 addresses, this defaults to the Linode that this address was assigned to on creation. IPv4 addresses may be moved using the [Assign IPv4s to Linodes](https://techdocs.akamai.com/linode-api/reference/post-assign-ipv4s) operation. For SLAAC and link-local addresses, this value may not be changed. | [optional] [readonly] 
**prefix** | **int** | The number of bits set in the subnet mask. | [optional] [readonly] 
**public** | **bool** | Whether this is a public or private IP address. | [optional] [readonly] 
**rdns** | **str** | The reverse DNS assigned to this address. For public IPv4 addresses, this will be set to a default value provided by Linode if not explicitly set. | [optional] 
**region** | **str** | The Region this IP address resides in. | [optional] [readonly] 
**subnet_mask** | **str** | The mask that separates host bits from network bits for this address. | [optional] [readonly] 
**type** | **str** | The type of address this is. | [optional] [readonly] 
**vpc_nat_1_1** | [**GetIps200ResponseAllOfDataInnerVpcNat11**](GetIps200ResponseAllOfDataInnerVpcNat11.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_ips200_response_all_of_data_inner import GetIps200ResponseAllOfDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIps200ResponseAllOfDataInner from a JSON string
get_ips200_response_all_of_data_inner_instance = GetIps200ResponseAllOfDataInner.from_json(json)
# print the JSON string representation of the object
print(GetIps200ResponseAllOfDataInner.to_json())

# convert the object into a dict
get_ips200_response_all_of_data_inner_dict = get_ips200_response_all_of_data_inner_instance.to_dict()
# create an instance of GetIps200ResponseAllOfDataInner from a dict
get_ips200_response_all_of_data_inner_from_dict = GetIps200ResponseAllOfDataInner.from_dict(get_ips200_response_all_of_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


