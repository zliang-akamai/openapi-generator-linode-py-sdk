# GetLkeClusters200ResponseDataInnerControlPlaneAclAddresses

Supports keys `ipv4` and `ipv6`. Defaults to `{}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | **List[str]** | A list of individual ipv4 addresses or CIDRs to ALLOW. Defaults to &#x60;[]&#x60;. | [optional] 
**ipv6** | **List[str]** | A list of individual ipv6 addresses or CIDRs to ALLOW. Defaults to &#x60;[]&#x60;. | [optional] 

## Example

```python
from openapi_client.models.get_lke_clusters200_response_data_inner_control_plane_acl_addresses import GetLkeClusters200ResponseDataInnerControlPlaneAclAddresses

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusters200ResponseDataInnerControlPlaneAclAddresses from a JSON string
get_lke_clusters200_response_data_inner_control_plane_acl_addresses_instance = GetLkeClusters200ResponseDataInnerControlPlaneAclAddresses.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusters200ResponseDataInnerControlPlaneAclAddresses.to_json())

# convert the object into a dict
get_lke_clusters200_response_data_inner_control_plane_acl_addresses_dict = get_lke_clusters200_response_data_inner_control_plane_acl_addresses_instance.to_dict()
# create an instance of GetLkeClusters200ResponseDataInnerControlPlaneAclAddresses from a dict
get_lke_clusters200_response_data_inner_control_plane_acl_addresses_from_dict = GetLkeClusters200ResponseDataInnerControlPlaneAclAddresses.from_dict(get_lke_clusters200_response_data_inner_control_plane_acl_addresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


