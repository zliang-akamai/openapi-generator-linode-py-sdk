# Login

An object representing a previous successful login for a User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datetime** | **datetime** | When the login was initiated. | [optional] [readonly] 
**id** | **int** | The unique ID of this login object. | [optional] [readonly] 
**ip** | **str** | The remote IP address that requested the login. | [optional] [readonly] 
**restricted** | **bool** | True if the User that attempted the login was a restricted User, false otherwise. | [optional] [readonly] 
**status** | **str** | Whether the login attempt succeeded or failed. | [optional] [readonly] 
**username** | **str** | The username of the User that attempted the login. | [optional] [readonly] 

## Example

```python
from openapi_client.models.login import Login

# TODO update the JSON string below
json = "{}"
# create an instance of Login from a JSON string
login_instance = Login.from_json(json)
# print the JSON string representation of the object
print(Login.to_json())

# convert the object into a dict
login_dict = login_instance.to_dict()
# create an instance of Login from a dict
login_from_dict = Login.from_dict(login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


