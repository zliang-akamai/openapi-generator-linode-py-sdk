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
from openapi_client.models.get_linode_firewalls200_response_data_inner_rules_inbound_inner import GetLinodeFirewalls200ResponseDataInnerRulesInboundInner
from typing import Optional, Set
from typing_extensions import Self

class GetLinodeFirewalls200ResponseDataInnerRules(BaseModel):
    """
    The inbound and outbound access rules to apply to the Firewall.  A Firewall may have up to 25 rules across its inbound and outbound rulesets.  Multiple rules are applied in order. If two rules conflict, the first rule takes precedence. For example, if the first rule accepts inbound traffic from an address, and the second rule drops inbound traffic the same address, the first rule applies and inbound traffic from that address is accepted.
    """ # noqa: E501
    fingerprint: Optional[StrictStr] = Field(default=None, description="The fingerprint is a 32-bit hash. It represents the firewall rules as an 8 character hex string. You can use `fingerprint` to compare rule versions.")
    inbound: Optional[List[GetLinodeFirewalls200ResponseDataInnerRulesInboundInner]] = Field(default=None, description="The inbound rules for the firewall, as a JSON array.")
    inbound_policy: Optional[StrictStr] = Field(default=None, description="The default behavior for inbound traffic. This setting can be overridden by [updating](https://techdocs.akamai.com/linode-api/reference/put-firewall-rules) the `inbound.action` property of the Firewall Rule.")
    outbound: Optional[List[GetLinodeFirewalls200ResponseDataInnerRulesInboundInner]] = Field(default=None, description="The outbound rules for the firewall, as a JSON array.")
    outbound_policy: Optional[StrictStr] = Field(default=None, description="The default behavior for outbound traffic. This setting can be overridden by [updating](https://techdocs.akamai.com/linode-api/reference/put-firewall-rules) the `outbound.action` property of the Firewall Rule.")
    version: Optional[StrictInt] = Field(default=None, description="The firewall's rule version. The first version is `1`. The version number is incremented when the firewall's rules change.")
    __properties: ClassVar[List[str]] = ["fingerprint", "inbound", "inbound_policy", "outbound", "outbound_policy", "version"]

    @field_validator('inbound_policy')
    def inbound_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACCEPT', 'DROP']):
            raise ValueError("must be one of enum values ('ACCEPT', 'DROP')")
        return value

    @field_validator('outbound_policy')
    def outbound_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACCEPT', 'DROP']):
            raise ValueError("must be one of enum values ('ACCEPT', 'DROP')")
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
        """Create an instance of GetLinodeFirewalls200ResponseDataInnerRules from a JSON string"""
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
            "fingerprint",
            "version",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in inbound (list)
        _items = []
        if self.inbound:
            for _item_inbound in self.inbound:
                if _item_inbound:
                    _items.append(_item_inbound.to_dict())
            _dict['inbound'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in outbound (list)
        _items = []
        if self.outbound:
            for _item_outbound in self.outbound:
                if _item_outbound:
                    _items.append(_item_outbound.to_dict())
            _dict['outbound'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetLinodeFirewalls200ResponseDataInnerRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fingerprint": obj.get("fingerprint"),
            "inbound": [GetLinodeFirewalls200ResponseDataInnerRulesInboundInner.from_dict(_item) for _item in obj["inbound"]] if obj.get("inbound") is not None else None,
            "inbound_policy": obj.get("inbound_policy"),
            "outbound": [GetLinodeFirewalls200ResponseDataInnerRulesInboundInner.from_dict(_item) for _item in obj["outbound"]] if obj.get("outbound") is not None else None,
            "outbound_policy": obj.get("outbound_policy"),
            "version": obj.get("version")
        })
        return _obj

