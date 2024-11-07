# coding: utf-8

"""
    Linode API

    [Read the API documentation](https://techdocs.akamai.com/linode-api/reference/api).

    The version of the OpenAPI document: 4.189.2
    Contact: support@linode.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.get_managed_contacts200_response_data_inner_phone import GetManagedContacts200ResponseDataInnerPhone
from typing import Optional, Set
from typing_extensions import Self

class GetManagedContacts200ResponseDataInner(BaseModel):
    """
    Information about someone Linode's special forces may contact in case an issue is detected with a manager service.
    """ # noqa: E501
    email: Optional[StrictStr] = Field(default=None, description="The address to email this Contact to alert them of issues.")
    group: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=50)]] = Field(default=None, description="A grouping for this Contact. This is for display purposes only.")
    id: Optional[StrictInt] = Field(default=None, description="This Contact's unique ID.")
    name: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=64)]] = Field(default=None, description="The name of this Contact.")
    phone: Optional[GetManagedContacts200ResponseDataInnerPhone] = None
    updated: Optional[datetime] = Field(default=None, description="When this Contact was last updated.")
    __properties: ClassVar[List[str]] = ["email", "group", "id", "name", "phone", "updated"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-zA-Z0-9-_ ]{2,64}", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z0-9-_ ]{2,64}/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GetManagedContacts200ResponseDataInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "updated",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of phone
        if self.phone:
            _dict['phone'] = self.phone.to_dict()
        # set to None if group (nullable) is None
        # and model_fields_set contains the field
        if self.group is None and "group" in self.model_fields_set:
            _dict['group'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetManagedContacts200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "group": obj.get("group"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "phone": GetManagedContacts200ResponseDataInnerPhone.from_dict(obj["phone"]) if obj.get("phone") is not None else None,
            "updated": obj.get("updated")
        })
        return _obj

