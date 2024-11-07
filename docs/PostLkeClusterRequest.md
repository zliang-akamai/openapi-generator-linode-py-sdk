# PostLkeClusterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_plane** | [**GetLkeClusters200ResponseDataInnerControlPlane**](GetLkeClusters200ResponseDataInnerControlPlane.md) |  | [optional] 
**k8s_version** | **str** | The desired Kubernetes version for this Kubernetes cluster in the format of &amp;lt;major&amp;gt;.&amp;lt;minor&amp;gt;, and the latest supported patch version will be deployed. | 
**label** | **str** | This Kubernetes cluster&#39;s unique label for display purposes only. Labels have the following constraints:    - UTF-8 characters will be returned by the API using escape sequences of their Unicode code points. For example, the Japanese character _か_ is 3 bytes in UTF-8 (&#x60;0xE382AB&#x60;). Its Unicode code point is 2 bytes (&#x60;0x30AB&#x60;). APIv4 supports this character and the API will return it as the escape sequence using six 1 byte characters which represent 2 bytes of Unicode code point (&#x60;\&quot;\\u30ab\&quot;&#x60;).    - 4 byte UTF-8 characters are not supported.    - If the label is entirely composed of UTF-8 characters, the API response will return the code points using up to 193 1 byte characters. | 
**node_pools** | [**List[PostLkeClusterRequestNodePoolsInner]**](PostLkeClusterRequestNodePoolsInner.md) |  | 
**region** | **str** | This Kubernetes cluster&#39;s location. | 
**tags** | **List[str]** | An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only. | [optional] 

## Example

```python
from openapi_client.models.post_lke_cluster_request import PostLkeClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostLkeClusterRequest from a JSON string
post_lke_cluster_request_instance = PostLkeClusterRequest.from_json(json)
# print the JSON string representation of the object
print(PostLkeClusterRequest.to_json())

# convert the object into a dict
post_lke_cluster_request_dict = post_lke_cluster_request_instance.to_dict()
# create an instance of PostLkeClusterRequest from a dict
post_lke_cluster_request_from_dict = PostLkeClusterRequest.from_dict(post_lke_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


