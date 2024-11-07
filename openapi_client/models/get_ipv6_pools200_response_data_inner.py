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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetIpv6Pools200ResponseDataInner(BaseModel):
    """
    An object representing an IPv6 pool.
    """ # noqa: E501
    prefix: Optional[StrictInt] = Field(default=None, description="The prefix length of the address. The total number of addresses that can be assigned from this range is calculated as 2<sup>(128 - prefix length)</sup>.")
    range: Optional[StrictStr] = Field(default=None, description="The IPv6 range of addresses in this pool.")
    region: Optional[StrictStr] = Field(default=None, description="The region for this pool of IPv6 addresses.")
    route_target: Optional[StrictStr] = Field(default=None, description="The last address in this block of IPv6 addresses.")
    __properties: ClassVar[List[str]] = ["prefix", "range", "region", "route_target"]

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
        """Create an instance of GetIpv6Pools200ResponseDataInner from a JSON string"""
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
            "range",
            "region",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if route_target (nullable) is None
        # and model_fields_set contains the field
        if self.route_target is None and "route_target" in self.model_fields_set:
            _dict['route_target'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetIpv6Pools200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "prefix": obj.get("prefix"),
            "range": obj.get("range"),
            "region": obj.get("region"),
            "route_target": obj.get("route_target")
        })
        return _obj


