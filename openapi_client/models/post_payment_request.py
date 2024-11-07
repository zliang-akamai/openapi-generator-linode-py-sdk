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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PostPaymentRequest(BaseModel):
    """
    PostPaymentRequest
    """ # noqa: E501
    payment_method_id: Optional[StrictInt] = Field(default=None, description="The ID of the Payment Method to apply to the Payment.")
    usd: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The amount in US Dollars of the Payment.  - Can begin with or without `$`. - Commas (`,`) are not accepted. - Must end with a decimal expression, such as `.00` or `.99`. - Minimum: `$5.00` or the Account balance, whichever is lower. - Maximum: `$2000.00` or the Account balance up to `$50000.00`, whichever is greater.")
    __properties: ClassVar[List[str]] = ["payment_method_id", "usd"]

    @field_validator('usd')
    def usd_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\$?\d+\.\d{2}$", value):
            raise ValueError(r"must validate the regular expression /^\$?\d+\.\d{2}$/")
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
        """Create an instance of PostPaymentRequest from a JSON string"""
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
        """Create an instance of PostPaymentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "payment_method_id": obj.get("payment_method_id"),
            "usd": obj.get("usd")
        })
        return _obj


