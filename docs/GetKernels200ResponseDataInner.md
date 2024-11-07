# GetKernels200ResponseDataInner

Linux kernel object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | The architecture of this Kernel. | [optional] [readonly] 
**built** | **datetime** | The date on which this Kernel was built. | [optional] [readonly] 
**deprecated** | **bool** | If this Kernel is marked as deprecated, this field has a value of true; otherwise, this field is false. | [optional] [readonly] 
**id** | **str** | The unique ID of this Kernel. | [optional] [readonly] 
**kvm** | **bool** | If this Kernel is suitable for KVM Linodes. | [optional] [readonly] 
**label** | **str** | The friendly name of this Kernel. | [optional] [readonly] 
**pvops** | **bool** | If this Kernel is suitable for paravirtualized operations. | [optional] [readonly] 
**version** | **str** | Linux Kernel version. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_kernels200_response_data_inner import GetKernels200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetKernels200ResponseDataInner from a JSON string
get_kernels200_response_data_inner_instance = GetKernels200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetKernels200ResponseDataInner.to_json())

# convert the object into a dict
get_kernels200_response_data_inner_dict = get_kernels200_response_data_inner_instance.to_dict()
# create an instance of GetKernels200ResponseDataInner from a dict
get_kernels200_response_data_inner_from_dict = GetKernels200ResponseDataInner.from_dict(get_kernels200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


