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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.get_lke_types200_response_data_inner_price import GetLkeTypes200ResponseDataInnerPrice
from openapi_client.models.get_lke_types200_response_data_inner_region_prices_inner import GetLkeTypes200ResponseDataInnerRegionPricesInner
from typing import Optional, Set
from typing_extensions import Self

class GetLkeTypes200ResponseDataInner(BaseModel):
    """
    Returns collection of Kubernetes types and prices, including any region-specific rates.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The ID representing the Kubernetes type.")
    label: Optional[StrictStr] = Field(default=None, description="The Kubernetes type label is for display purposes only.")
    price: Optional[GetLkeTypes200ResponseDataInnerPrice] = None
    region_prices: Optional[List[GetLkeTypes200ResponseDataInnerRegionPricesInner]] = None
    transfer: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The monthly outbound transfer amount, in MB.")
    __properties: ClassVar[List[str]] = ["id", "label", "price", "region_prices", "transfer"]

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
        """Create an instance of GetLkeTypes200ResponseDataInner from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "label",
            "transfer",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in region_prices (list)
        _items = []
        if self.region_prices:
            for _item_region_prices in self.region_prices:
                if _item_region_prices:
                    _items.append(_item_region_prices.to_dict())
            _dict['region_prices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetLkeTypes200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "label": obj.get("label"),
            "price": GetLkeTypes200ResponseDataInnerPrice.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "region_prices": [GetLkeTypes200ResponseDataInnerRegionPricesInner.from_dict(_item) for _item in obj["region_prices"]] if obj.get("region_prices") is not None else None,
            "transfer": obj.get("transfer")
        })
        return _obj


