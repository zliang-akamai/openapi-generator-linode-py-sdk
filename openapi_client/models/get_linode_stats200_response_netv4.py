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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class GetLinodeStats200ResponseNetv4(BaseModel):
    """
    IPv4 statistics.
    """ # noqa: E501
    var_in: Optional[List[List[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Input stats for IPv4, measured in bits/s (bits/second).", alias="in")
    out: Optional[List[List[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Output stats for IPv4, measured in bits/s (bits/second).")
    private_in: Optional[List[List[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Private IPv4 input statistics, measured in bits/s (bits/second).")
    private_out: Optional[List[List[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Private IPv4 output statistics, measured in bits/s (bits/second).")
    __properties: ClassVar[List[str]] = ["in", "out", "private_in", "private_out"]

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
        """Create an instance of GetLinodeStats200ResponseNetv4 from a JSON string"""
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
        """Create an instance of GetLinodeStats200ResponseNetv4 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "in": obj.get("in"),
            "out": obj.get("out"),
            "private_in": obj.get("private_in"),
            "private_out": obj.get("private_out")
        })
        return _obj


