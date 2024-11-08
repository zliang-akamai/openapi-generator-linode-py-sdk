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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.get_tickets200_response_data_inner_entity import GetTickets200ResponseDataInnerEntity
from typing import Optional, Set
from typing_extensions import Self

class GetTickets200ResponseDataInner(BaseModel):
    """
    A Support Ticket opened on your Account.
    """ # noqa: E501
    attachments: Optional[List[StrictStr]] = Field(default=None, description="A list of filenames representing attached files associated with this Ticket.")
    closable: Optional[StrictBool] = Field(default=None, description="Whether the Support Ticket may be closed.")
    closed: Optional[datetime] = Field(default=None, description="The date and time this Ticket was closed.")
    description: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=65000)]] = Field(default=None, description="The full details of the issue or question.")
    entity: Optional[GetTickets200ResponseDataInnerEntity] = None
    gravatar_id: Optional[StrictStr] = Field(default=None, description="The Gravatar ID of the User who opened this Ticket.")
    id: Optional[StrictInt] = Field(default=None, description="The ID of the Support Ticket.")
    opened: Optional[datetime] = Field(default=None, description="The date and time this Ticket was created.")
    opened_by: Optional[StrictStr] = Field(default=None, description="The User who opened this Ticket.")
    status: Optional[StrictStr] = Field(default=None, description="The current status of this Ticket.")
    summary: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=64)]] = Field(default=None, description="The summary or title for this Ticket.")
    updated: Optional[datetime] = Field(default=None, description="The date and time this Ticket was last updated.")
    updated_by: Optional[StrictStr] = Field(default=None, description="The User who last updated this Ticket.")
    __properties: ClassVar[List[str]] = ["attachments", "closable", "closed", "description", "entity", "gravatar_id", "id", "opened", "opened_by", "status", "summary", "updated", "updated_by"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['closed', 'new', 'open']):
            raise ValueError("must be one of enum values ('closed', 'new', 'open')")
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
        """Create an instance of GetTickets200ResponseDataInner from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "attachments",
            "closed",
            "description",
            "gravatar_id",
            "id",
            "opened",
            "opened_by",
            "status",
            "summary",
            "updated",
            "updated_by",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of entity
        if self.entity:
            _dict['entity'] = self.entity.to_dict()
        # set to None if closed (nullable) is None
        # and model_fields_set contains the field
        if self.closed is None and "closed" in self.model_fields_set:
            _dict['closed'] = None

        # set to None if entity (nullable) is None
        # and model_fields_set contains the field
        if self.entity is None and "entity" in self.model_fields_set:
            _dict['entity'] = None

        # set to None if updated_by (nullable) is None
        # and model_fields_set contains the field
        if self.updated_by is None and "updated_by" in self.model_fields_set:
            _dict['updated_by'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetTickets200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attachments": obj.get("attachments"),
            "closable": obj.get("closable"),
            "closed": obj.get("closed"),
            "description": obj.get("description"),
            "entity": GetTickets200ResponseDataInnerEntity.from_dict(obj["entity"]) if obj.get("entity") is not None else None,
            "gravatar_id": obj.get("gravatar_id"),
            "id": obj.get("id"),
            "opened": obj.get("opened"),
            "opened_by": obj.get("opened_by"),
            "status": obj.get("status"),
            "summary": obj.get("summary"),
            "updated": obj.get("updated"),
            "updated_by": obj.get("updated_by")
        })
        return _obj


