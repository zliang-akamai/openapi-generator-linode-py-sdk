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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.get_regions200_response_data_inner_placement_group_limits import GetRegions200ResponseDataInnerPlacementGroupLimits
from openapi_client.models.get_regions200_response_data_inner_resolvers import GetRegions200ResponseDataInnerResolvers
from typing import Optional, Set
from typing_extensions import Self

class GetRegions200ResponseDataInner(BaseModel):
    """
    An area where Linode services are available.
    """ # noqa: E501
    capabilities: Optional[List[StrictStr]] = Field(default=None, description="A list of capabilities of this region.")
    country: Optional[StrictStr] = Field(default=None, description="The country where this Region resides.")
    id: Optional[StrictStr] = Field(default=None, description="The unique ID of this Region.")
    label: Optional[StrictStr] = Field(default=None, description="Detailed location information for this Region, including city, state or region, and country.")
    placement_group_limits: Optional[GetRegions200ResponseDataInnerPlacementGroupLimits] = None
    resolvers: Optional[GetRegions200ResponseDataInnerResolvers] = None
    site_type: Optional[StrictStr] = Field(default=None, description="This region's site type. A `core` region indicates a traditional cloud computing [region](https://www.linode.com/docs/products/platform/get-started/guides/choose-a-data-center/#product-availability) that offers all compute services. A `distributed` region indicates sites that are globally dispersed to be closer to end users and workloads. These regions offer limited services.")
    status: Optional[StrictStr] = Field(default=None, description="This region's current operational status.")
    __properties: ClassVar[List[str]] = ["capabilities", "country", "id", "label", "placement_group_limits", "resolvers", "site_type", "status"]

    @field_validator('site_type')
    def site_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['core', 'distributed']):
            raise ValueError("must be one of enum values ('core', 'distributed')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ok', 'outage']):
            raise ValueError("must be one of enum values ('ok', 'outage')")
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
        """Create an instance of GetRegions200ResponseDataInner from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "capabilities",
            "country",
            "id",
            "label",
            "site_type",
            "status",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of placement_group_limits
        if self.placement_group_limits:
            _dict['placement_group_limits'] = self.placement_group_limits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resolvers
        if self.resolvers:
            _dict['resolvers'] = self.resolvers.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetRegions200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "capabilities": obj.get("capabilities"),
            "country": obj.get("country"),
            "id": obj.get("id"),
            "label": obj.get("label"),
            "placement_group_limits": GetRegions200ResponseDataInnerPlacementGroupLimits.from_dict(obj["placement_group_limits"]) if obj.get("placement_group_limits") is not None else None,
            "resolvers": GetRegions200ResponseDataInnerResolvers.from_dict(obj["resolvers"]) if obj.get("resolvers") is not None else None,
            "site_type": obj.get("site_type"),
            "status": obj.get("status")
        })
        return _obj

