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

class GetProfile200ResponseReferrals(BaseModel):
    """
    Information about your status in our referral program.  This information becomes accessible after this Profile's Account has established at least $25.00 USD of total payments.
    """ # noqa: E501
    code: Optional[StrictStr] = Field(default=None, description="Your referral code.  If others use this when signing up for Linode, you will receive account credit.")
    completed: Optional[StrictInt] = Field(default=None, description="The number of completed signups with your referral code.")
    credit: Optional[StrictInt] = Field(default=None, description="The amount of account credit in US Dollars issued to you through the referral program.")
    pending: Optional[StrictInt] = Field(default=None, description="The number of pending signups with your referral code.  You will not receive credit for these signups until they are completed.")
    total: Optional[StrictInt] = Field(default=None, description="The number of users who have signed up with your referral code.")
    url: Optional[StrictStr] = Field(default=None, description="Your referral url, used to direct others to sign up for Linode with your referral code.")
    __properties: ClassVar[List[str]] = ["code", "completed", "credit", "pending", "total", "url"]

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
        """Create an instance of GetProfile200ResponseReferrals from a JSON string"""
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
            "code",
            "completed",
            "credit",
            "pending",
            "total",
            "url",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetProfile200ResponseReferrals from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "completed": obj.get("completed"),
            "credit": obj.get("credit"),
            "pending": obj.get("pending"),
            "total": obj.get("total"),
            "url": obj.get("url")
        })
        return _obj


