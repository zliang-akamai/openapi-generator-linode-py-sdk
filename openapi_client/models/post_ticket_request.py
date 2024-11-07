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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PostTicketRequest(BaseModel):
    """
    An object representing a created Support Ticket - a question or issue and request for help from the Linode support team. Only one of the ID attributes (`linode_id`, `domain_id`, etc.) can be set on a single Support Ticket.
    """ # noqa: E501
    database_id: Optional[StrictInt] = Field(default=None, description="The ID of the Managed Database this ticket is regarding, if relevant.")
    description: Annotated[str, Field(min_length=1, strict=True, max_length=65000)] = Field(description="The full details of the issue or question.")
    domain_id: Optional[StrictInt] = Field(default=None, description="The ID of the Domain this ticket is regarding, if relevant.")
    firewall_id: Optional[StrictInt] = Field(default=None, description="The ID of the Firewall this ticket is regarding, if relevant.")
    linode_id: Optional[StrictInt] = Field(default=None, description="The ID of the Linode this ticket is regarding, if relevant.")
    lkecluster_id: Optional[StrictInt] = Field(default=None, description="The ID of the Kubernetes cluster this ticket is regarding, if relevant.")
    longviewclient_id: Optional[StrictInt] = Field(default=None, description="The ID of the Longview client this ticket is regarding, if relevant.")
    managed_issue: Optional[StrictBool] = Field(default=None, description="Designates if this ticket is related to a [Managed service](https://www.linode.com/products/managed/). If `true`, the following constraints will apply:  - No ID attributes (i.e. `linode_id`, `domain_id`, etc.) should be provided with this request. - Your account must have a managed service [enabled](https://techdocs.akamai.com/linode-api/reference/post-enable-managed-service).")
    nodebalancer_id: Optional[StrictInt] = Field(default=None, description="The ID of the NodeBalancer this ticket is regarding, if relevant.")
    region: Optional[StrictStr] = Field(default=None, description="The [Region](https://techdocs.akamai.com/linode-api/reference/get-regions) ID for the associated VLAN this ticket is regarding.  Only allowed when submitting a VLAN ticket.")
    summary: Annotated[str, Field(min_length=1, strict=True, max_length=64)] = Field(description="The summary or title for this SupportTicket.")
    vlan: Optional[StrictStr] = Field(default=None, description="The label of the VLAN this ticket is regarding, if relevant. To view your VLANs, run the [List VLANs](https://techdocs.akamai.com/linode-api/reference/get-vlans)) operation.  Requires a specified `region` to identify the VLAN.")
    volume_id: Optional[StrictInt] = Field(default=None, description="The ID of the Volume this ticket is regarding, if relevant.")
    vpc_id: Optional[StrictInt] = Field(default=None, description="The ID of the VPC this ticket is regarding, if relevant.")
    __properties: ClassVar[List[str]] = ["database_id", "description", "domain_id", "firewall_id", "linode_id", "lkecluster_id", "longviewclient_id", "managed_issue", "nodebalancer_id", "region", "summary", "vlan", "volume_id", "vpc_id"]

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
        """Create an instance of PostTicketRequest from a JSON string"""
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
        """Create an instance of PostTicketRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "database_id": obj.get("database_id"),
            "description": obj.get("description"),
            "domain_id": obj.get("domain_id"),
            "firewall_id": obj.get("firewall_id"),
            "linode_id": obj.get("linode_id"),
            "lkecluster_id": obj.get("lkecluster_id"),
            "longviewclient_id": obj.get("longviewclient_id"),
            "managed_issue": obj.get("managed_issue"),
            "nodebalancer_id": obj.get("nodebalancer_id"),
            "region": obj.get("region"),
            "summary": obj.get("summary"),
            "vlan": obj.get("vlan"),
            "volume_id": obj.get("volume_id"),
            "vpc_id": obj.get("vpc_id")
        })
        return _obj


