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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class GetInvoiceItems200ResponseDataInner(BaseModel):
    """
    An InvoiceItem object.
    """ # noqa: E501
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The price, in US dollars, of the Invoice Item. Equal to the unit price multiplied by quantity.")
    var_from: Optional[datetime] = Field(default=None, description="The date the Invoice Item started, based on month.", alias="from")
    label: Optional[StrictStr] = Field(default=None, description="The Invoice Item's display label.")
    quantity: Optional[StrictInt] = Field(default=None, description="The quantity of this Item for the specified Invoice.")
    region: Optional[StrictStr] = Field(default=None, description="The ID of the applicable Region associated with this Invoice Item.  `null` if there is no applicable Region.")
    tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of tax levied on this Item in US Dollars.")
    to: Optional[datetime] = Field(default=None, description="The date the Invoice Item ended, based on month.")
    total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The price of this Item after taxes in US Dollars.")
    type: Optional[StrictStr] = Field(default=None, description="The type of service, ether `hourly` or `misc`.")
    unit_price: Optional[StrictStr] = Field(default=None, description="The monthly service fee in US Dollars for this Item.")
    __properties: ClassVar[List[str]] = ["amount", "from", "label", "quantity", "region", "tax", "to", "total", "type", "unit_price"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['hourly', 'misc']):
            raise ValueError("must be one of enum values ('hourly', 'misc')")
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
        """Create an instance of GetInvoiceItems200ResponseDataInner from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "amount",
            "var_from",
            "label",
            "quantity",
            "region",
            "tax",
            "to",
            "total",
            "type",
            "unit_price",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if region (nullable) is None
        # and model_fields_set contains the field
        if self.region is None and "region" in self.model_fields_set:
            _dict['region'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetInvoiceItems200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "from": obj.get("from"),
            "label": obj.get("label"),
            "quantity": obj.get("quantity"),
            "region": obj.get("region"),
            "tax": obj.get("tax"),
            "to": obj.get("to"),
            "total": obj.get("total"),
            "type": obj.get("type"),
            "unit_price": obj.get("unit_price")
        })
        return _obj

