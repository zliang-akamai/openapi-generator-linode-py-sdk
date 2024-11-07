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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class GetNetworkTransferPrices200ResponseDataInnerRegionPricesInner(BaseModel):
    """
    GetNetworkTransferPrices200ResponseDataInnerRegionPricesInner
    """ # noqa: E501
    hourly: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Cost per hour for this region, in US dollars.")
    id: Optional[StrictStr] = Field(default=None, description="The Region ID for these prices.")
    monthly: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Cost per month for this region, in US dollars.")
    __properties: ClassVar[List[str]] = ["hourly", "id", "monthly"]

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
        """Create an instance of GetNetworkTransferPrices200ResponseDataInnerRegionPricesInner from a JSON string"""
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
        # set to None if monthly (nullable) is None
        # and model_fields_set contains the field
        if self.monthly is None and "monthly" in self.model_fields_set:
            _dict['monthly'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetNetworkTransferPrices200ResponseDataInnerRegionPricesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hourly": obj.get("hourly"),
            "id": obj.get("id"),
            "monthly": obj.get("monthly")
        })
        return _obj


