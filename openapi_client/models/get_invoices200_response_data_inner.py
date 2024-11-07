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
from openapi_client.models.get_invoices200_response_data_inner_tax_summary_inner import GetInvoices200ResponseDataInnerTaxSummaryInner
from typing import Optional, Set
from typing_extensions import Self

class GetInvoices200ResponseDataInner(BaseModel):
    """
    Account Invoice object.
    """ # noqa: E501
    billing_source: Optional[StrictStr] = Field(default=None, description="`akamai`: This Invoice was generated according to the terms of an agreement between the customer and Akamai.  `linode`: This Invoice was generated according to the default terms, prices, and discounts.")
    var_date: Optional[datetime] = Field(default=None, description="When this Invoice was generated.", alias="date")
    id: Optional[StrictInt] = Field(default=None, description="The Invoice's unique ID.")
    label: Optional[StrictStr] = Field(default=None, description="The Invoice's display label.")
    subtotal: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of the Invoice before taxes in US Dollars.")
    tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of tax levied on the Invoice in US Dollars.")
    tax_summary: Optional[List[GetInvoices200ResponseDataInnerTaxSummaryInner]] = Field(default=None, description="The amount of tax broken down into subtotals by source.")
    total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of the Invoice after taxes in US Dollars.")
    __properties: ClassVar[List[str]] = ["billing_source", "date", "id", "label", "subtotal", "tax", "tax_summary", "total"]

    @field_validator('billing_source')
    def billing_source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['akamai', 'linode']):
            raise ValueError("must be one of enum values ('akamai', 'linode')")
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
        """Create an instance of GetInvoices200ResponseDataInner from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "billing_source",
            "var_date",
            "id",
            "label",
            "subtotal",
            "tax",
            "tax_summary",
            "total",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in tax_summary (list)
        _items = []
        if self.tax_summary:
            for _item_tax_summary in self.tax_summary:
                if _item_tax_summary:
                    _items.append(_item_tax_summary.to_dict())
            _dict['tax_summary'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetInvoices200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "billing_source": obj.get("billing_source"),
            "date": obj.get("date"),
            "id": obj.get("id"),
            "label": obj.get("label"),
            "subtotal": obj.get("subtotal"),
            "tax": obj.get("tax"),
            "tax_summary": [GetInvoices200ResponseDataInnerTaxSummaryInner.from_dict(_item) for _item in obj["tax_summary"]] if obj.get("tax_summary") is not None else None,
            "total": obj.get("total")
        })
        return _obj


