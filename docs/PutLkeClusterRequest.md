# PutLkeClusterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_plane** | [**PutLkeClusterRequestControlPlane**](PutLkeClusterRequestControlPlane.md) |  | [optional] 
**k8s_version** | **str** | The desired Kubernetes version for this Kubernetes cluster in the format of &amp;lt;major&amp;gt;.&amp;lt;minor&amp;gt;. New and recycled Nodes in this cluster will be installed with the latest available patch for the Cluster&#39;s Kubernetes version.  When upgrading the Kubernetes version, only the next latest minor version following the current version can be deployed. For example, a cluster with Kubernetes version 1.19 can be upgraded to version 1.20, but not directly to 1.21.  The Kubernetes version of a cluster can not be downgraded. | [optional] 
**label** | **str** | This Kubernetes cluster&#39;s unique label for display purposes only. Labels have the following constraints:    - UTF-8 characters will be returned by the API using escape sequences of their Unicode code points. For example, the Japanese character _か_ is 3 bytes in UTF-8 (&#x60;0xE382AB&#x60;). Its Unicode code point is 2 bytes (&#x60;0x30AB&#x60;). APIv4 supports this character and the API will return it as the escape sequence using six 1 byte characters which represent 2 bytes of Unicode code point (&#x60;\&quot;\\u30ab\&quot;&#x60;).    - 4 byte UTF-8 characters are not supported.    - If the label is entirely composed of UTF-8 characters, the API response will return the code points using up to 193 1 byte characters. | [optional] 
**tags** | **List[str]** | An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only. To delete a tag, exclude it from your &#x60;tags&#x60; array. | [optional] 

## Example

```python
from openapi_client.models.put_lke_cluster_request import PutLkeClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutLkeClusterRequest from a JSON string
put_lke_cluster_request_instance = PutLkeClusterRequest.from_json(json)
# print the JSON string representation of the object
print(PutLkeClusterRequest.to_json())

# convert the object into a dict
put_lke_cluster_request_dict = put_lke_cluster_request_instance.to_dict()
# create an instance of PutLkeClusterRequest from a dict
put_lke_cluster_request_from_dict = PutLkeClusterRequest.from_dict(put_lke_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


