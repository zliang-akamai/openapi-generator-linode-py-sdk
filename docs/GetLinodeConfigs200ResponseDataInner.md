# GetLinodeConfigs200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Optional field for arbitrary User comments on this Config. | [optional] 
**devices** | [**GetLinodeConfigs200ResponseDataInnerDevices**](GetLinodeConfigs200ResponseDataInnerDevices.md) |  | [optional] 
**helpers** | [**GetLinodeConfigs200ResponseDataInnerHelpers**](GetLinodeConfigs200ResponseDataInnerHelpers.md) |  | [optional] 
**id** | **int** | The ID of this Config. | [optional] [readonly] 
**interfaces** | [**List[PostLinodeInstanceRequestAllOfInterfacesInner]**](PostLinodeInstanceRequestAllOfInterfacesInner.md) | An array of Network Interfaces to add to this Linode&#39;s Configuration Profile. At least one and up to three Interface objects can exist in this array. The position in the array determines which of the Linode&#39;s network Interfaces is configured:  - First [0]:  eth0 - Second [1]: eth1 - Third [2]:  eth2  When updating a Linode&#39;s Interfaces, _each Interface must be redefined_. An empty &#x60;interfaces&#x60; array results in a default &#x60;public&#x60; type Interface configuration only.  If no public Interface is configured, public IP addresses are still assigned to the Linode but will not be usable without manual configuration.  __Note__. Changes to Linode Interface configurations can be enabled by rebooting the Linode.  &#x60;vpc&#x60; details  See the [VPC documentation](https://www.linode.com/docs/products/networking/vpc/#technical-specifications) guide for its specifications and limitations.  &#x60;vlan&#x60; details  - Only Next Generation Network (NGN) data centers support VLANs. Run the [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions) operation to view the capabilities of data center regions. If a VLAN is attached to your Linode and you attempt to migrate or clone it to a non-NGN data center, the migration or cloning will not initiate. If a Linode cannot be migrated or cloned because of an incompatibility, you will be prompted to select a different data center or contact support. - See the [VLANs Overview](https://www.linode.com/docs/products/networking/vlans/#technical-specifications) guide to view additional specifications and limitations. | [optional] 
**kernel** | **str** | A Kernel ID to boot a Linode with. Here are examples of commonly used kernels:  - &#x60;linode/latest-64bit&#x60; (default): Our latest kernel at the time of instance boot/reboot. - &#x60;linode/grub2&#x60;: The upstream distribution-supplied kernel that is installed on the primary disk, or a custom kernel if installed. - &#x60;linode/direct-disk&#x60;: The MBR (Master Boot Record) of the primary disk/root device, used instead of a Linux kernel.  For a complete list of options, run the [List kernels](https://techdocs.akamai.com/linode-api/reference/get-kernels) operation. | [optional] [default to 'linode/latest-64bit']
**label** | **str** | The Config&#39;s label is for display purposes only. | [optional] 
**memory_limit** | **int** | Defaults to the total RAM of the Linode. | [optional] 
**root_device** | **str** | The root device to boot.  - If no value or an invalid value is provided, root device will default to &#x60;/dev/sda&#x60;. - If the device specified at the root device location is not mounted, the Linode will not boot until a device is mounted. | [optional] 
**run_level** | **str** | Defines the state of your Linode after booting. Defaults to &#x60;default&#x60;. | [optional] 
**virt_mode** | **str** | Controls the virtualization mode. Defaults to &#x60;paravirt&#x60;.  - &#x60;paravirt&#x60; is suitable for most cases. Linodes running in paravirt mode share some qualities with the host, ultimately making it run faster since there is less transition between it and the host. - &#x60;fullvirt&#x60; affords more customization, but is slower because 100% of the VM is virtualized. | [optional] 

## Example

```python
from openapi_client.models.get_linode_configs200_response_data_inner import GetLinodeConfigs200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinodeConfigs200ResponseDataInner from a JSON string
get_linode_configs200_response_data_inner_instance = GetLinodeConfigs200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetLinodeConfigs200ResponseDataInner.to_json())

# convert the object into a dict
get_linode_configs200_response_data_inner_dict = get_linode_configs200_response_data_inner_instance.to_dict()
# create an instance of GetLinodeConfigs200ResponseDataInner from a dict
get_linode_configs200_response_data_inner_from_dict = GetLinodeConfigs200ResponseDataInner.from_dict(get_linode_configs200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


