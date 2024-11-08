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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.node_balancer_transfer import NodeBalancerTransfer
from typing import Optional, Set
from typing_extensions import Self

class NodeBalancer1(BaseModel):
    """
    Linode's load balancing solution.  Can handle multiple ports, SSL termination, and any number of backends.  NodeBalancer ports are configured with NodeBalancer Configs, and each config is given one or more NodeBalancer Node that accepts traffic.  The traffic should be routed to the  NodeBalancer's ip address, the NodeBalancer will handle routing individual requests to backends.
    """ # noqa: E501
    client_conn_throttle: Optional[Annotated[int, Field(le=20, strict=True, ge=0)]] = Field(default=None, description="Throttle connections per second.  Set to 0 (zero) to disable throttling.")
    created: Optional[datetime] = Field(default=None, description="When this NodeBalancer was created.")
    hostname: Optional[StrictStr] = Field(default=None, description="This NodeBalancer's hostname, beginning with its IP address and ending with _.ip.linodeusercontent.com_.")
    id: Optional[StrictInt] = Field(default=None, description="This NodeBalancer's unique ID.")
    ipv4: Optional[StrictStr] = Field(default=None, description="This NodeBalancer's public IPv4 address.")
    ipv6: Optional[StrictStr] = Field(default=None, description="This NodeBalancer's public IPv6 address.")
    label: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=32)]] = Field(default=None, description="This NodeBalancer's label. These must be unique on your Account.")
    region: Optional[StrictStr] = Field(default=None, description="The Region where this NodeBalancer is located. NodeBalancers only support backends in the same Region.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="An array of Tags applied to this object.  Tags are for organizational purposes only.")
    transfer: Optional[NodeBalancerTransfer] = None
    updated: Optional[datetime] = Field(default=None, description="When this NodeBalancer was last updated.")
    __properties: ClassVar[List[str]] = ["client_conn_throttle", "created", "hostname", "id", "ipv4", "ipv6", "label", "region", "tags", "transfer", "updated"]

    @field_validator('label')
    def label_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-zA-Z0-9-_]{3,32}", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z0-9-_]{3,32}/")
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
        """Create an instance of NodeBalancer1 from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created",
            "hostname",
            "id",
            "ipv4",
            "ipv6",
            "region",
            "updated",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of transfer
        if self.transfer:
            _dict['transfer'] = self.transfer.to_dict()
        # set to None if ipv6 (nullable) is None
        # and model_fields_set contains the field
        if self.ipv6 is None and "ipv6" in self.model_fields_set:
            _dict['ipv6'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodeBalancer1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "client_conn_throttle": obj.get("client_conn_throttle"),
            "created": obj.get("created"),
            "hostname": obj.get("hostname"),
            "id": obj.get("id"),
            "ipv4": obj.get("ipv4"),
            "ipv6": obj.get("ipv6"),
            "label": obj.get("label"),
            "region": obj.get("region"),
            "tags": obj.get("tags"),
            "transfer": NodeBalancerTransfer.from_dict(obj["transfer"]) if obj.get("transfer") is not None else None,
            "updated": obj.get("updated")
        })
        return _obj


