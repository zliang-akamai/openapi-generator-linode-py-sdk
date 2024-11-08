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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PostRebuildNodeBalancerConfigRequestAllOfNodesInner(BaseModel):
    """
    NodeBalancer Node request object including ID.
    """ # noqa: E501
    address: Optional[StrictStr] = Field(default=None, description="The private IP Address where this backend can be reached. This _must_ be a private IP address.")
    id: Optional[StrictInt] = Field(default=None, description="The unique ID of the Node to update.")
    label: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=32)]] = Field(default=None, description="The label for this node.  This is for display purposes only.")
    mode: Optional[StrictStr] = Field(default=None, description="The mode this NodeBalancer should use when sending traffic to this backend.  - If set to `accept` this backend is accepting traffic. - If set to `reject` this backend will not receive traffic. - If set to `drain` this backend will not receive _new_ traffic, but connections already pinned to it will continue to be routed to it. - If set to `backup`, this backend will only receive traffic if all `accept` nodes are down.")
    weight: Optional[Annotated[int, Field(le=255, strict=True, ge=1)]] = Field(default=None, description="Used when picking a backend to serve a request and is not pinned to a single backend yet.  Nodes with a higher weight will receive more traffic.")
    __properties: ClassVar[List[str]] = ["address", "id", "label", "mode", "weight"]

    @field_validator('label')
    def label_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-zA-Z0-9-_.]{3,32}", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z0-9-_.]{3,32}/")
        return value

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['accept', 'reject', 'drain', 'backup']):
            raise ValueError("must be one of enum values ('accept', 'reject', 'drain', 'backup')")
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
        """Create an instance of PostRebuildNodeBalancerConfigRequestAllOfNodesInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostRebuildNodeBalancerConfigRequestAllOfNodesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "id": obj.get("id"),
            "label": obj.get("label"),
            "mode": obj.get("mode"),
            "weight": obj.get("weight")
        })
        return _obj


