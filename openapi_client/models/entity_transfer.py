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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.get_entity_transfers200_response_all_of_data_inner_entities import GetEntityTransfers200ResponseAllOfDataInnerEntities
from typing import Optional, Set
from typing_extensions import Self

class EntityTransfer(BaseModel):
    """
    An object representing an Entity Transfer.
    """ # noqa: E501
    created: Optional[datetime] = Field(default=None, description="When this transfer was created.")
    entities: Optional[GetEntityTransfers200ResponseAllOfDataInnerEntities] = None
    expiry: Optional[datetime] = Field(default=None, description="When this transfer expires. Transfers will automatically expire 24 hours after creation.")
    is_sender: Optional[StrictBool] = Field(default=None, description="If the requesting account created this transfer.")
    status: Optional[StrictStr] = Field(default=None, description="The status of the transfer request:  `accepted`: The transfer has been accepted by another user and is currently in progress. Transfers can take up to 3 hours to complete. `canceled`: The transfer has been canceled by the sender. `completed`: The transfer has completed successfully. `failed`: The transfer has failed after initiation. `pending`: The transfer is ready to be accepted. `stale`: The transfer has exceeded its expiration date. It can no longer be accepted or canceled.")
    token: Optional[StrictStr] = Field(default=None, description="The token used to identify and accept or cancel this transfer.")
    updated: Optional[datetime] = Field(default=None, description="When this transfer was last updated.")
    __properties: ClassVar[List[str]] = ["created", "entities", "expiry", "is_sender", "status", "token", "updated"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['accepted', 'canceled', 'completed', 'failed', 'pending', 'stale']):
            raise ValueError("must be one of enum values ('accepted', 'canceled', 'completed', 'failed', 'pending', 'stale')")
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
        """Create an instance of EntityTransfer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of entities
        if self.entities:
            _dict['entities'] = self.entities.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EntityTransfer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created": obj.get("created"),
            "entities": GetEntityTransfers200ResponseAllOfDataInnerEntities.from_dict(obj["entities"]) if obj.get("entities") is not None else None,
            "expiry": obj.get("expiry"),
            "is_sender": obj.get("is_sender"),
            "status": obj.get("status"),
            "token": obj.get("token"),
            "updated": obj.get("updated")
        })
        return _obj


