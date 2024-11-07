# LinodeSpecs

Information about the resources available to this Linode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk** | **int** | The amount of storage space, in MB, this Linode has access to. A typical Linode divides this space between a primary disk with an &#x60;image&#x60; deployed to it, and a swap disk, usually 512 MB. This is the default configuration created when deploying a Linode with an &#x60;image&#x60; through [Create a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance). While this configuration is suitable for 99% of use cases, if you need finer control over your Linode&#39;s disks, see the [List disks](https://techdocs.akamai.com/linode-api/reference/get-linode-disks) operations. | [optional] [readonly] 
**gpus** | **int** | The number of GPUs this Linode has access to. | [optional] [readonly] 
**memory** | **int** | The amount of RAM, in MB, this Linode has access to.  Typically, a Linode boots with all of its available RAM, but this can be configured in a config profile. See the [List config profiles](https://techdocs.akamai.com/linode-api/reference/get-linode-configs) operation for more information. | [optional] [readonly] 
**transfer** | **int** | The amount of network transfer this Linode is allotted each month. | [optional] [readonly] 
**vcpus** | **int** | The number of VCPUs this Linode has access to. | [optional] [readonly] 

## Example

```python
from openapi_client.models.linode_specs import LinodeSpecs

# TODO update the JSON string below
json = "{}"
# create an instance of LinodeSpecs from a JSON string
linode_specs_instance = LinodeSpecs.from_json(json)
# print the JSON string representation of the object
print(LinodeSpecs.to_json())

# convert the object into a dict
linode_specs_dict = linode_specs_instance.to_dict()
# create an instance of LinodeSpecs from a dict
linode_specs_from_dict = LinodeSpecs.from_dict(linode_specs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


