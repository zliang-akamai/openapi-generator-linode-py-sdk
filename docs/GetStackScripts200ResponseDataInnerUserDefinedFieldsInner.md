# GetStackScripts200ResponseDataInnerUserDefinedFieldsInner

A custom field defined by the User with a special syntax within a StackScript. Derived from the contents of the script.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | The default value.  If not specified, this value will be used. | [optional] [readonly] 
**example** | **str** | An example value for the field. | [readonly] 
**label** | **str** | A human-readable label for the field that will serve as the input prompt for entering the value during deployment. | [readonly] 
**many_of** | **str** | A list of acceptable values for the field in any quantity, combination or order. | [optional] [readonly] 
**name** | **str** | The name of the field. | [readonly] 
**one_of** | **str** | A list of acceptable single values for the field. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_stack_scripts200_response_data_inner_user_defined_fields_inner import GetStackScripts200ResponseDataInnerUserDefinedFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetStackScripts200ResponseDataInnerUserDefinedFieldsInner from a JSON string
get_stack_scripts200_response_data_inner_user_defined_fields_inner_instance = GetStackScripts200ResponseDataInnerUserDefinedFieldsInner.from_json(json)
# print the JSON string representation of the object
print(GetStackScripts200ResponseDataInnerUserDefinedFieldsInner.to_json())

# convert the object into a dict
get_stack_scripts200_response_data_inner_user_defined_fields_inner_dict = get_stack_scripts200_response_data_inner_user_defined_fields_inner_instance.to_dict()
# create an instance of GetStackScripts200ResponseDataInnerUserDefinedFieldsInner from a dict
get_stack_scripts200_response_data_inner_user_defined_fields_inner_from_dict = GetStackScripts200ResponseDataInnerUserDefinedFieldsInner.from_dict(get_stack_scripts200_response_data_inner_user_defined_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


