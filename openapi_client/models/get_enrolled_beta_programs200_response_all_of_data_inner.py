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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetEnrolledBetaPrograms200ResponseAllOfDataInner(BaseModel):
    """
    An object representing an enrolled Beta Program for the Account.
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Additional details regarding the Beta Program.")
    ended: Optional[datetime] = Field(default=None, description="The date-time that the Beta Program ended.  `null` indicates that the Beta Program is ongoing.")
    enrolled: Optional[datetime] = Field(default=None, description="The date-time of Account enrollment to the Beta Program.")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the Beta Program.")
    label: Optional[StrictStr] = Field(default=None, description="The name of the Beta Program.")
    started: Optional[datetime] = Field(default=None, description="The start date-time of the Beta Program.")
    __properties: ClassVar[List[str]] = ["description", "ended", "enrolled", "id", "label", "started"]

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
        """Create an instance of GetEnrolledBetaPrograms200ResponseAllOfDataInner from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "description",
            "ended",
            "enrolled",
            "label",
            "started",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if ended (nullable) is None
        # and model_fields_set contains the field
        if self.ended is None and "ended" in self.model_fields_set:
            _dict['ended'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetEnrolledBetaPrograms200ResponseAllOfDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "ended": obj.get("ended"),
            "enrolled": obj.get("enrolled"),
            "id": obj.get("id"),
            "label": obj.get("label"),
            "started": obj.get("started")
        })
        return _obj


