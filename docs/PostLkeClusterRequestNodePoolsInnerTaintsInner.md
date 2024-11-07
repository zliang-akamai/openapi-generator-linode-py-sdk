# PostLkeClusterRequestNodePoolsInnerTaintsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | The Kubernetes taint effect. For &#x60;NoSchedule&#x60;, &#x60;PreferNoSchedule&#x60; and &#x60;NoExecute&#x60; descriptions, see [Kubernetes Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/). | 
**key** | **str** | The Kubernetes taint key.  - A key can contain alphanumeric characters, dashes (&#x60;-&#x60;), underscores (&#x60;_&#x60;), or dots (&#x60;.&#x60;). Start and end it with an alphanumeric character.  - If the key begins with a DNS subdomain prefix followed by a single slash, for example &#x60;example.com/my-app&#x60;, the prefix part needs to adhere to [RFC 1123](https://datatracker.ietf.org/doc/html/rfc1123) DNS subdomain restrictions and be a maximum of 253 characters. | 
**value** | **str** | The Kubernetes taint value.  - A key can contain alphanumeric characters, dashes (&#x60;-&#x60;), underscores (&#x60;_&#x60;), or dots (&#x60;.&#x60;). Start and end it with an alphanumeric character.  - Can be specified as an empty string value with &#x60;\&quot;\&quot;&#x60;. | 

## Example

```python
from openapi_client.models.post_lke_cluster_request_node_pools_inner_taints_inner import PostLkeClusterRequestNodePoolsInnerTaintsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostLkeClusterRequestNodePoolsInnerTaintsInner from a JSON string
post_lke_cluster_request_node_pools_inner_taints_inner_instance = PostLkeClusterRequestNodePoolsInnerTaintsInner.from_json(json)
# print the JSON string representation of the object
print(PostLkeClusterRequestNodePoolsInnerTaintsInner.to_json())

# convert the object into a dict
post_lke_cluster_request_node_pools_inner_taints_inner_dict = post_lke_cluster_request_node_pools_inner_taints_inner_instance.to_dict()
# create an instance of PostLkeClusterRequestNodePoolsInnerTaintsInner from a dict
post_lke_cluster_request_node_pools_inner_taints_inner_from_dict = PostLkeClusterRequestNodePoolsInnerTaintsInner.from_dict(post_lke_cluster_request_node_pools_inner_taints_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


