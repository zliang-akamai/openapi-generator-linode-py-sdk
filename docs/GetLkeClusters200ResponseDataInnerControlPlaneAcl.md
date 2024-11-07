# GetLkeClusters200ResponseDataInnerControlPlaneAcl

When a cluster is equipped with an ACL, the apiserver and dashboard endpoints get mapped to a NodeBalancer address where all traffic is protected through a Cloud Firewall. This object supports required keys `enabled` and `addresses`. Also supports the optional key `revision-id`. If omitted, at discretion of the platform, the cluster may or may not be equipped with ACL support. The Default Policy shall be set to ALLOW (i.e., access controls are disabled). If set to `{}`, default elements are set. __NOTE: Control Plane ACLs may not currently be available to all users.__

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**GetLkeClusters200ResponseDataInnerControlPlaneAclAddresses**](GetLkeClusters200ResponseDataInnerControlPlaneAclAddresses.md) |  | [optional] 
**enabled** | **bool** | Defines Default Policy.  A value of true results in a default policy of DENY.  A value of false results in a default policy of ALLOW (i.e., access controls are disabled). Defaults to &#x60;true&#x60;. Creating a cluster with ACL (or upgrading a cluster to use ACL for LKE) is an __irreversible__ change: once upgraded, access controls can only be toggled through this property. | [optional] 
**revision_id** | **str** | Enables clients to track events related to ACL update requests and enforcements. Optional field. If omitted, defaults to a randomly generated string. | [optional] 

## Example

```python
from openapi_client.models.get_lke_clusters200_response_data_inner_control_plane_acl import GetLkeClusters200ResponseDataInnerControlPlaneAcl

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusters200ResponseDataInnerControlPlaneAcl from a JSON string
get_lke_clusters200_response_data_inner_control_plane_acl_instance = GetLkeClusters200ResponseDataInnerControlPlaneAcl.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusters200ResponseDataInnerControlPlaneAcl.to_json())

# convert the object into a dict
get_lke_clusters200_response_data_inner_control_plane_acl_dict = get_lke_clusters200_response_data_inner_control_plane_acl_instance.to_dict()
# create an instance of GetLkeClusters200ResponseDataInnerControlPlaneAcl from a dict
get_lke_clusters200_response_data_inner_control_plane_acl_from_dict = GetLkeClusters200ResponseDataInnerControlPlaneAcl.from_dict(get_lke_clusters200_response_data_inner_control_plane_acl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


