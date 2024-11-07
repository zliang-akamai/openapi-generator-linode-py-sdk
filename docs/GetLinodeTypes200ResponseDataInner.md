# GetLinodeTypes200ResponseDataInner

Returns collection of Linode types, including pricing and specifications for each type. These are used when [creating](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) or [resizing](https://techdocs.akamai.com/linode-api/reference/post-resize-linode-instance) Linodes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | [**GetLinodeTypes200ResponseDataInnerAddons**](GetLinodeTypes200ResponseDataInnerAddons.md) |  | [optional] 
**var_class** | **str** | The class of the Linode Type.  We currently offer six classes of compute instances:    - &#x60;nanode&#x60; - Nanode instances are good for low-duty workloads, where performance isn&#39;t critical. __Note__. As of June 16th, 2020, Nanodes became 1 GB Linodes in the Cloud Manager, however, the API, the CLI, and billing will continue to refer to these instances as Nanodes.   - &#x60;standard&#x60; - Standard Shared instances are good for medium-duty workloads and are a good mix of performance, resources, and price. __Note__. As of June 16th, 2020, Standard Linodes in the Cloud Manager became Shared Linodes, however, the API, the CLI, and billing will continue to refer to these instances as Standard Linodes.   - &#x60;dedicated&#x60; - Dedicated CPU instances are good for full-duty workloads where consistent performance is important.   - &#x60;premium&#x60; (limited Regions) - In addition to the features of Dedicated instances, Premium instances come equipped with the latest AMD EPYC&amp;trade; CPUs, ensuring your applications are running on the latest hardware with consistently high performance. Only available in [regions](https://techdocs.akamai.com/linode-api/reference/get-regions) with \&quot;Premium Plans\&quot; in their &#x60;capabilities&#x60;   - &#x60;gpu&#x60; (limited Regions) - Linodes with dedicated NVIDIA Quadro&amp;reg; RTX 6000 GPUs accelerate highly specialized applications such as machine learning, AI, and video transcoding. Only available in [regions](https://techdocs.akamai.com/linode-api/reference/get-regions) with \&quot;GPU Linodes\&quot; in their &#x60;capabilities&#x60;   - &#x60;highmem&#x60; - High Memory instances favor RAM over other resources, and can be good for memory hungry use cases like caching and in-memory databases. All High Memory plans contain dedicated CPU cores. | [optional] [readonly] 
**disk** | **int** | The Disk size, in MB, of the Linode Type. | [optional] [readonly] 
**gpus** | **int** | The number of GPUs this Linode Type offers. | [optional] [readonly] 
**id** | **str** | The ID representing the Linode Type. | [optional] [readonly] 
**label** | **str** | The Linode Type&#39;s label is for display purposes only. | [optional] [readonly] 
**memory** | **int** | Amount of RAM included in this Linode Type. | [optional] [readonly] 
**network_out** | **int** | The Mbits outbound bandwidth allocation. | [optional] [readonly] 
**price** | [**GetLinodeTypes200ResponseDataInnerPrice**](GetLinodeTypes200ResponseDataInnerPrice.md) |  | [optional] 
**region_prices** | [**List[GetLinodeTypes200ResponseDataInnerRegionPricesInner]**](GetLinodeTypes200ResponseDataInnerRegionPricesInner.md) |  | [optional] 
**successor** | **str** | The Linode Type that a [mutate](https://techdocs.akamai.com/linode-api/reference/post-mutate-linode-instance) will upgrade to for a Linode of this type.  If &#x60;null&#x60;, a Linode of this type may not mutate. | [optional] [readonly] 
**transfer** | **int** | The monthly outbound transfer amount, in MB. | [optional] [readonly] 
**vcpus** | **int** | The number of VCPU cores this Linode Type offers. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_linode_types200_response_data_inner import GetLinodeTypes200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeTypes200ResponseDataInner from a JSON string
get_linode_types200_response_data_inner_instance = GetLinodeTypes200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetLinodeTypes200ResponseDataInner.to_json())

# convert the object into a dict
get_linode_types200_response_data_inner_dict = get_linode_types200_response_data_inner_instance.to_dict()
# create an instance of GetLinodeTypes200ResponseDataInner from a dict
get_linode_types200_response_data_inner_from_dict = GetLinodeTypes200ResponseDataInner.from_dict(get_linode_types200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


