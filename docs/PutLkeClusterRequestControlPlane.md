# PutLkeClusterRequestControlPlane

Defines settings for the Kubernetes Control Plane. Allows for the enabling of High Availability (HA) and IP-based Access Control List (ACL) for Control Plane Components. Enabling of either of these for LKE is an __irreversible__ change.  When upgrading pre-existing LKE clusters to use the HA Control Plane, the following changes will additionally occur:  - All nodes will be deleted and new nodes will be created to replace them.  - Any local storage (such as `hostPath` volumes) will be erased.  - The upgrade process may take several minutes to complete, as nodes will be replaced on a rolling basis.  When upgrading pre-existing LKE clusters to use the ACL Control Plane, the following changes will additionally occur:  - All control plane access will go through a Cloud Firewall. There will be a period on which the FQDN DNS record needs to be propagated. Due to TTL and DNS caching, it could take several hours for external clients to switch over to the new mappings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | [**GetLkeClusters200ResponseDataInnerControlPlaneAcl**](GetLkeClusters200ResponseDataInnerControlPlaneAcl.md) |  | [optional] 
**high_availability** | **bool** | Enables High Availability for the Control Plane Components of the cluster. Defaults to &#x60;false&#x60;. Enabling High Availability for LKE is an __irreversible__ change. | [optional] [default to False]

## Example

```python
from openapi_client.models.put_lke_cluster_request_control_plane import PutLkeClusterRequestControlPlane

# TODO update the JSON string below
json = "{}"
# create an instance of PutLkeClusterRequestControlPlane from a JSON string
put_lke_cluster_request_control_plane_instance = PutLkeClusterRequestControlPlane.from_json(json)
# print the JSON string representation of the object
print(PutLkeClusterRequestControlPlane.to_json())

# convert the object into a dict
put_lke_cluster_request_control_plane_dict = put_lke_cluster_request_control_plane_instance.to_dict()
# create an instance of PutLkeClusterRequestControlPlane from a dict
put_lke_cluster_request_control_plane_from_dict = PutLkeClusterRequestControlPlane.from_dict(put_lke_cluster_request_control_plane_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


