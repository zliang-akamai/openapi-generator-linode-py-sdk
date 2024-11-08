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
from typing import Optional, Set
from typing_extensions import Self

class GetAccount200ResponseActivePromotionsInner(BaseModel):
    """
    Promotions generally offer a set amount of credit that can be used toward your Linode services, and the promotion expires after a specified date. As well, a monthly cap on the promotional offer is set.  Simply put, a promotion offers a certain amount of credit  month, until either the expiration date is passed, or until the total promotional credit is used, whichever comes first.
    """ # noqa: E501
    credit_monthly_cap: Optional[StrictStr] = Field(default=None, description="The amount available to spend per month.")
    credit_remaining: Optional[StrictStr] = Field(default=None, description="The total amount of credit left for this promotion.")
    description: Optional[StrictStr] = Field(default=None, description="A detailed description of this promotion.")
    expire_dt: Optional[StrictStr] = Field(default=None, description="When this promotion's credits expire.")
    image_url: Optional[StrictStr] = Field(default=None, description="The location of an image for this promotion.")
    service_type: Optional[StrictStr] = Field(default=None, description="The service to which this promotion applies.")
    summary: Optional[StrictStr] = Field(default=None, description="Short details of this promotion.")
    this_month_credit_remaining: Optional[StrictStr] = Field(default=None, description="The amount of credit left for this month for this promotion.")
    __properties: ClassVar[List[str]] = ["credit_monthly_cap", "credit_remaining", "description", "expire_dt", "image_url", "service_type", "summary", "this_month_credit_remaining"]

    @field_validator('service_type')
    def service_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['all', 'backup', 'blockstorage', 'db_mysql', 'ip_v4', 'linode', 'linode_disk', 'linode_memory', 'longview', 'managed', 'nodebalancer', 'objectstorage', 'placement_group', 'transfer_tx']):
            raise ValueError("must be one of enum values ('all', 'backup', 'blockstorage', 'db_mysql', 'ip_v4', 'linode', 'linode_disk', 'linode_memory', 'longview', 'managed', 'nodebalancer', 'objectstorage', 'placement_group', 'transfer_tx')")
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
        """Create an instance of GetAccount200ResponseActivePromotionsInner from a JSON string"""
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
        """Create an instance of GetAccount200ResponseActivePromotionsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "credit_monthly_cap": obj.get("credit_monthly_cap"),
            "credit_remaining": obj.get("credit_remaining"),
            "description": obj.get("description"),
            "expire_dt": obj.get("expire_dt"),
            "image_url": obj.get("image_url"),
            "service_type": obj.get("service_type"),
            "summary": obj.get("summary"),
            "this_month_credit_remaining": obj.get("this_month_credit_remaining")
        })
        return _obj


