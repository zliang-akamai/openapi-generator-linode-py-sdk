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

class Linode1PlacementGroup(BaseModel):
    """
    Details on the [placement group](https://www.linode.com/docs/products/compute/compute-instances/guides/placement-groups/) that this Linode belongs to. Empty if the Linode isn't in a placement group.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The placement group's ID. You need to provide it for all operations that affect it.")
    label: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The unique name set for the placement group. A label has these constraints:  - It needs to begin and end with an alphanumeric character. - It can only consist of alphanumeric characters, hyphens (`-`), underscores (`_`) or periods (`.`).")
    placement_group_policy: Optional[StrictStr] = Field(default=None, description="How requests to add future compute instances to your placement group are handled, and whether it remains compliant:  - `strict`. Don't assign a new compute instance if it breaks the grouped-together or spread-apart model set by the `placement_group_type`. Use this to ensure the placement group stays compliant (`is_compliant: true`). - `flexible`. Assign a new compute instance, even if it breaks the grouped-together or spread-apart model set by the `placement_group_type`. This makes the group non-compliant (`is_compliant: false`). You need to wait for Akamai to move the offending compute instance to make it compliant again, once the necessary capacity is available in the region. Offers flexibility to add future compute instances if compliance isn't an immediate concern.  <<LB>>  > 📘 > > In rare cases, non-compliance can occur with a `strict` placement group if Akamai needs to failover or migrate your compute instances for maintenance. Fixing non-compliance for a `strict` placement group is prioritized over a `flexible` group.")
    placement_group_type: Optional[StrictStr] = Field(default=None, description="How compute instances are distributed in your placement group. A `placement_group_type` using anti-affinity (`anti-affinity:local`) places compute instances in separate hosts, but still in the same region. This best supports the spread-apart model for high availability. A `placement_group_type` using affinity places compute instances physically close together, possibly on the same host. This supports the grouped-together model for low-latency.  > 📘 > > Currently, only `anti_affinity:local` is available for `placement_group_type`.")
    __properties: ClassVar[List[str]] = ["id", "label", "placement_group_policy", "placement_group_type"]

    @field_validator('placement_group_policy')
    def placement_group_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['strict', 'flexible']):
            raise ValueError("must be one of enum values ('strict', 'flexible')")
        return value

    @field_validator('placement_group_type')
    def placement_group_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['anti_affinity:local']):
            raise ValueError("must be one of enum values ('anti_affinity:local')")
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
        """Create an instance of Linode1PlacementGroup from a JSON string"""
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
            "placement_group_type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Linode1PlacementGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "label": obj.get("label"),
            "placement_group_policy": obj.get("placement_group_policy"),
            "placement_group_type": obj.get("placement_group_type")
        })
        return _obj


