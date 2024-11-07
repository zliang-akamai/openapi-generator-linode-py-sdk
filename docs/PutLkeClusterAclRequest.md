# PutLkeClusterAclRequest

Defines settings for the Kubernetes Control Plane. Allows for the enabling of IP-based Access Control List (ACL) for Control Plane Components. An ACL can only be managed through this endpoint after either the Cluster was created with ACL enabled or after it has been upgraded to use it. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | [**GetLkeClusters200ResponseDataInnerControlPlaneAcl**](GetLkeClusters200ResponseDataInnerControlPlaneAcl.md) |  | [optional] 

## Example

```python
from openapi_client.models.put_lke_cluster_acl_request import PutLkeClusterAclRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutLkeClusterAclRequest from a JSON string
put_lke_cluster_acl_request_instance = PutLkeClusterAclRequest.from_json(json)
# print the JSON string representation of the object
print(PutLkeClusterAclRequest.to_json())

# convert the object into a dict
put_lke_cluster_acl_request_dict = put_lke_cluster_acl_request_instance.to_dict()
# create an instance of PutLkeClusterAclRequest from a dict
put_lke_cluster_acl_request_from_dict = PutLkeClusterAclRequest.from_dict(put_lke_cluster_acl_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


