# GetLkeClusters200ResponseDataInnerControlPlane

Defines settings for the Kubernetes Control Plane, including High Availability (HA) and IP-based Access Control List (ACL) for Control Plane Components. Enabling of either of these for LKE is an __irreversible__ change.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | [**GetLkeClusters200ResponseDataInnerControlPlaneAcl**](GetLkeClusters200ResponseDataInnerControlPlaneAcl.md) |  | [optional] 
**high_availability** | **bool** | Enables High Availability for the Control Plane Components of the cluster. Defaults to &#x60;false&#x60;. Enabling High Availability for LKE is an __irreversible__ change. | [optional] [default to False]

## Example

```python
from openapi_client.models.get_lke_clusters200_response_data_inner_control_plane import GetLkeClusters200ResponseDataInnerControlPlane

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusters200ResponseDataInnerControlPlane from a JSON string
get_lke_clusters200_response_data_inner_control_plane_instance = GetLkeClusters200ResponseDataInnerControlPlane.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusters200ResponseDataInnerControlPlane.to_json())

# convert the object into a dict
get_lke_clusters200_response_data_inner_control_plane_dict = get_lke_clusters200_response_data_inner_control_plane_instance.to_dict()
# create an instance of GetLkeClusters200ResponseDataInnerControlPlane from a dict
get_lke_clusters200_response_data_inner_control_plane_from_dict = GetLkeClusters200ResponseDataInnerControlPlane.from_dict(get_lke_clusters200_response_data_inner_control_plane_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


