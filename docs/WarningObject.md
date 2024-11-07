# WarningObject

An object for describing a single warning associated with a response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **str** | Specific information related to the warning. | [optional] 
**title** | **str** | The general warning message. | [optional] 

## Example

```python
from openapi_client.models.warning_object import WarningObject

# TODO update the JSON string below
json = "{}"
# create an instance of WarningObject from a JSON string
warning_object_instance = WarningObject.from_json(json)
# print the JSON string representation of the object
print(WarningObject.to_json())

# convert the object into a dict
warning_object_dict = warning_object_instance.to_dict()
# create an instance of WarningObject from a dict
warning_object_from_dict = WarningObject.from_dict(warning_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


