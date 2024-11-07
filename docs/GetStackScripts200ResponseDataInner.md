# GetStackScripts200ResponseDataInner

A StackScript enables you to quickly deploy a fully configured application in an automated manner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The date this StackScript was created. | [optional] [readonly] 
**deployments_active** | **int** | Count of currently active, deployed Linodes created from this StackScript. | [optional] [readonly] 
**deployments_total** | **int** | The total number of times this StackScript has been deployed. | [optional] [readonly] 
**description** | **str** | A description for the StackScript. | [optional] 
**id** | **int** | The unique ID of this StackScript. | [optional] [readonly] 
**images** | **List[str]** | An array of Image IDs. These are the Images that can be deployed with this StackScript.  &#x60;any/all&#x60; indicates that all available Images, including private Images, are accepted. | [optional] 
**is_public** | **bool** | This determines whether other users can use your StackScript. __Once a StackScript is made public, it cannot be made private.__ | [optional] 
**label** | **str** | The StackScript&#39;s label is for display purposes only. | [optional] 
**mine** | **bool** | Returns &#x60;true&#x60; if this StackScript is owned by the account of the user making the request, and the user making the request is unrestricted or has access to this StackScript. | [optional] [readonly] 
**rev_note** | **str** | This field allows you to add notes for the set of revisions made to this StackScript. | [optional] 
**script** | **str** | The script to execute when provisioning a new Linode with this StackScript. | [optional] 
**updated** | **datetime** | The date this StackScript was last updated. | [optional] [readonly] 
**user_defined_fields** | [**List[GetStackScripts200ResponseDataInnerUserDefinedFieldsInner]**](GetStackScripts200ResponseDataInnerUserDefinedFieldsInner.md) | This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized parameters during deployment. See [Declare User-Defined Fields (UDFs)](https://www.linode.com/docs/products/tools/stackscripts/guides/write-a-custom-script/#declare-user-defined-fields-udfs) for more information. | [optional] [readonly] 
**user_gravatar_id** | **str** | The Gravatar ID for the User who created the StackScript. | [optional] [readonly] 
**username** | **str** | The User who created the StackScript. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_stack_scripts200_response_data_inner import GetStackScripts200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetStackScripts200ResponseDataInner from a JSON string
get_stack_scripts200_response_data_inner_instance = GetStackScripts200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetStackScripts200ResponseDataInner.to_json())

# convert the object into a dict
get_stack_scripts200_response_data_inner_dict = get_stack_scripts200_response_data_inner_instance.to_dict()
# create an instance of GetStackScripts200ResponseDataInner from a dict
get_stack_scripts200_response_data_inner_from_dict = GetStackScripts200ResponseDataInner.from_dict(get_stack_scripts200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


