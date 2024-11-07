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
from openapi_client.models.get_linode_types200_response_data_inner_addons import GetLinodeTypes200ResponseDataInnerAddons
from openapi_client.models.get_linode_types200_response_data_inner_price import GetLinodeTypes200ResponseDataInnerPrice
from openapi_client.models.get_linode_types200_response_data_inner_region_prices_inner import GetLinodeTypes200ResponseDataInnerRegionPricesInner
from typing import Optional, Set
from typing_extensions import Self

class GetLinodeTypes200ResponseDataInner(BaseModel):
    """
    Returns collection of Linode types, including pricing and specifications for each type. These are used when [creating](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) or [resizing](https://techdocs.akamai.com/linode-api/reference/post-resize-linode-instance) Linodes.
    """ # noqa: E501
    addons: Optional[GetLinodeTypes200ResponseDataInnerAddons] = None
    var_class: Optional[StrictStr] = Field(default=None, description="The class of the Linode Type.  We currently offer six classes of compute instances:    - `nanode` - Nanode instances are good for low-duty workloads, where performance isn't critical. __Note__. As of June 16th, 2020, Nanodes became 1 GB Linodes in the Cloud Manager, however, the API, the CLI, and billing will continue to refer to these instances as Nanodes.   - `standard` - Standard Shared instances are good for medium-duty workloads and are a good mix of performance, resources, and price. __Note__. As of June 16th, 2020, Standard Linodes in the Cloud Manager became Shared Linodes, however, the API, the CLI, and billing will continue to refer to these instances as Standard Linodes.   - `dedicated` - Dedicated CPU instances are good for full-duty workloads where consistent performance is important.   - `premium` (limited Regions) - In addition to the features of Dedicated instances, Premium instances come equipped with the latest AMD EPYC&trade; CPUs, ensuring your applications are running on the latest hardware with consistently high performance. Only available in [regions](https://techdocs.akamai.com/linode-api/reference/get-regions) with \"Premium Plans\" in their `capabilities`   - `gpu` (limited Regions) - Linodes with dedicated NVIDIA Quadro&reg; RTX 6000 GPUs accelerate highly specialized applications such as machine learning, AI, and video transcoding. Only available in [regions](https://techdocs.akamai.com/linode-api/reference/get-regions) with \"GPU Linodes\" in their `capabilities`   - `highmem` - High Memory instances favor RAM over other resources, and can be good for memory hungry use cases like caching and in-memory databases. All High Memory plans contain dedicated CPU cores.", alias="class")
    disk: Optional[StrictInt] = Field(default=None, description="The Disk size, in MB, of the Linode Type.")
    gpus: Optional[StrictInt] = Field(default=None, description="The number of GPUs this Linode Type offers.")
    id: Optional[StrictStr] = Field(default=None, description="The ID representing the Linode Type.")
    label: Optional[StrictStr] = Field(default=None, description="The Linode Type's label is for display purposes only.")
    memory: Optional[StrictInt] = Field(default=None, description="Amount of RAM included in this Linode Type.")
    network_out: Optional[StrictInt] = Field(default=None, description="The Mbits outbound bandwidth allocation.")
    price: Optional[GetLinodeTypes200ResponseDataInnerPrice] = None
    region_prices: Optional[List[GetLinodeTypes200ResponseDataInnerRegionPricesInner]] = None
    successor: Optional[StrictStr] = Field(default=None, description="The Linode Type that a [mutate](https://techdocs.akamai.com/linode-api/reference/post-mutate-linode-instance) will upgrade to for a Linode of this type.  If `null`, a Linode of this type may not mutate.")
    transfer: Optional[StrictInt] = Field(default=None, description="The monthly outbound transfer amount, in MB.")
    vcpus: Optional[StrictInt] = Field(default=None, description="The number of VCPU cores this Linode Type offers.")
    __properties: ClassVar[List[str]] = ["addons", "class", "disk", "gpus", "id", "label", "memory", "network_out", "price", "region_prices", "successor", "transfer", "vcpus"]

    @field_validator('var_class')
    def var_class_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['nanode', 'standard', 'dedicated', 'premium', 'gpu', 'highmem']):
            raise ValueError("must be one of enum values ('nanode', 'standard', 'dedicated', 'premium', 'gpu', 'highmem')")
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
        """Create an instance of GetLinodeTypes200ResponseDataInner from a JSON string"""
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
            "var_class",
            "disk",
            "gpus",
            "id",
            "label",
            "memory",
            "network_out",
            "successor",
            "transfer",
            "vcpus",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of addons
        if self.addons:
            _dict['addons'] = self.addons.to_dict()
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
        # set to None if successor (nullable) is None
        # and model_fields_set contains the field
        if self.successor is None and "successor" in self.model_fields_set:
            _dict['successor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetLinodeTypes200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addons": GetLinodeTypes200ResponseDataInnerAddons.from_dict(obj["addons"]) if obj.get("addons") is not None else None,
            "class": obj.get("class"),
            "disk": obj.get("disk"),
            "gpus": obj.get("gpus"),
            "id": obj.get("id"),
            "label": obj.get("label"),
            "memory": obj.get("memory"),
            "network_out": obj.get("network_out"),
            "price": GetLinodeTypes200ResponseDataInnerPrice.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "region_prices": [GetLinodeTypes200ResponseDataInnerRegionPricesInner.from_dict(_item) for _item in obj["region_prices"]] if obj.get("region_prices") is not None else None,
            "successor": obj.get("successor"),
            "transfer": obj.get("transfer"),
            "vcpus": obj.get("vcpus")
        })
        return _obj

