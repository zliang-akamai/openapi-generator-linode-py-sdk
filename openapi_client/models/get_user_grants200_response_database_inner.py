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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetUserGrants200ResponseDatabaseInner(BaseModel):
    """
    Represents the level of access a restricted User has to a specific resource on the Account.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The ID of the entity this grant applies to.")
    label: Optional[StrictStr] = Field(default=None, description="The current label of the entity this grant applies to, for display purposes.")
    permissions: Optional[StrictStr] = Field(default=None, description="The level of access this User has to this entity.  If null, this User has no access.")
    __properties: ClassVar[List[str]] = ["id", "label", "permissions"]

    @field_validator('permissions')
    def permissions_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['read_only', 'read_write']):
            raise ValueError("must be one of enum values ('read_only', 'read_write')")
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
        """Create an instance of GetUserGrants200ResponseDatabaseInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "label",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if permissions (nullable) is None
        # and model_fields_set contains the field
        if self.permissions is None and "permissions" in self.model_fields_set:
            _dict['permissions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetUserGrants200ResponseDatabaseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "label": obj.get("label"),
            "permissions": obj.get("permissions")
        })
        return _obj


