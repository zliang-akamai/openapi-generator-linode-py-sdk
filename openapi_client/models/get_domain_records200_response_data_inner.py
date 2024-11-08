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
from typing import Optional, Set
from typing_extensions import Self

class GetDomainRecords200ResponseDataInner(BaseModel):
    """
    A single record on a Domain.
    """ # noqa: E501
    created: Optional[datetime] = Field(default=None, description="When this Domain Record was created.")
    id: Optional[StrictInt] = Field(default=None, description="This Record's unique ID.")
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(default=None, description="The name of this Record. For requests, this property's actual usage and whether it is required depends on the type of record this represents:  `A` and `AAAA`: The hostname or FQDN of the Record.  `NS`: The subdomain, if any, to use with the Domain of the Record. Wildcard NS records (`*`) are not supported.  `MX`: The mail subdomain. For example, `sub` for the address `user@sub.example.com` under the `example.com` Domain.  - The left-most subdomain component may be an asterisk (`*`) to designate a wildcard subdomain. - Other subdomain components must only contain letters, digits, and hyphens, start with a letter, end with a letter or digit, and contain less than 64 characters. - Must be an empty string (`\"\"`) for a Null MX Record.  `CNAME`: The hostname. Must be unique. Required.  `TXT`: The hostname.  `SRV`: Unused. Use the `service` property to set the service name for this record.  `CAA`: The subdomain. Omit or enter an empty string (`\"\"`) to apply to the entire Domain.  `PTR`: See our guide on how to [Configure Your Linode for Reverse DNS (rDNS)](https://www.linode.com/docs/guides/configure-rdns/).")
    port: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The port this Record points to. Only valid and required for SRV record requests.")
    priority: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=None, description="The priority of the target host for this Record. Lower values are preferred. Only valid for MX and SRV record requests. Required for SRV record requests.  Defaults to `0` for MX record requests. Must be `0` for Null MX records.")
    protocol: Optional[StrictStr] = Field(default=None, description="The protocol this Record's service communicates with. An underscore (`_`) is prepended automatically to the submitted value for this property. Only valid for SRV record requests.")
    service: Optional[StrictStr] = Field(default=None, description="The name of the service. An underscore (`_`) is prepended and a period (`.`) is appended automatically to the submitted value for this property. Only valid and required for SRV record requests.")
    tag: Optional[StrictStr] = Field(default=None, description="The tag portion of a CAA record. Only valid and required for CAA record requests.")
    target: Optional[Annotated[str, Field(strict=True, max_length=65535)]] = Field(default=None, description="The target for this Record. For requests, this property's actual usage and whether it is required depends on the type of record this represents:  `A` and `AAAA`: The IP address. Use `[remote_addr]` to submit the IPv4 address of the request. Required.  `NS`: The name server. Must be a valid domain. Required.  `MX`: The mail server. Must be a valid domain unless creating a Null MX Record. Required.  - Must have less than 254 total characters. - The left-most domain component may be an asterisk (`*`) to designate a wildcard domain. - Other domain components must only contain letters, digits, and hyphens, start with a letter, end with a letter or digit, and contain less than 64 characters. - To create a [Null MX Record](https://datatracker.ietf.org/doc/html/rfc7505), first [remove](https://techdocs.akamai.com/linode-api/reference/delete-domain-record) any additional MX records, then create an MX record with empty strings (`\"\"`) for the `target` and `name`. If a Domain has a Null MX record, new MX records cannot be created.  `CNAME`: The alias. Must be a valid domain. Required.  `TXT`: The value. Required.  `SRV`: The target domain or subdomain. If a subdomain is entered, it is automatically used with the Domain. To configure for a different domain, enter a valid FQDN. For example, the value `www` with a Domain for `example.com` results in a target set to `www.example.com`, whereas the value `sample.com` results in a target set to `sample.com`. Required.  `CAA`: The value. For `issue` or `issuewild` tags, the domain of your certificate issuer. For the `iodef` tag, a contact or submission URL (domain, http, https, or mailto). Requirements depend on the tag for this record:    - `issue`: The domain of your certificate issuer. Must include a valid domain. May include additional parameters separated with semicolons (`;`), for example: `www.example.com; foo=bar`   - `issuewild`: The domain of your wildcard certificate issuer. Must be a valid domain and must not start with an asterisk (`*`).   - `iodef`: Must be either (1) a valid domain, (2) a valid domain prepended with `http://` or `https://`, or (3) a valid email address prepended with `mailto:`.  `PTR`: Required. See our guide on how to [Configure Your Linode for Reverse DNS (rDNS)](https://www.linode.com/docs/guides/configure-rdns/).  With the exception of A, AAAA, and CAA records, this field accepts a trailing period.")
    ttl_sec: Optional[StrictInt] = Field(default=None, description="\"Time to Live\" - the amount of time in seconds that this Domain's records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.")
    type: Optional[StrictStr] = Field(default=None, description="The type of Record this is in the DNS system. For example, A records associate a domain name with an IPv4 address, and AAAA records associate a domain name with an IPv6 address. For more information, see the guides on [DNS Record Types](https://www.linode.com/docs/products/networking/dns-manager/guides/#dns-record-types).")
    updated: Optional[datetime] = Field(default=None, description="When this Domain Record was last updated.")
    weight: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The relative weight of this Record used in the case of identical priority. Higher values are preferred. Only valid and required for SRV record requests.")
    __properties: ClassVar[List[str]] = ["created", "id", "name", "port", "priority", "protocol", "service", "tag", "target", "ttl_sec", "type", "updated", "weight"]

    @field_validator('tag')
    def tag_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['issue', 'issuewild', 'iodef']):
            raise ValueError("must be one of enum values ('issue', 'issuewild', 'iodef')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['A', 'AAAA', 'NS', 'MX', 'CNAME', 'TXT', 'SRV', 'PTR', 'CAA']):
            raise ValueError("must be one of enum values ('A', 'AAAA', 'NS', 'MX', 'CNAME', 'TXT', 'SRV', 'PTR', 'CAA')")
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
        """Create an instance of GetDomainRecords200ResponseDataInner from a JSON string"""
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
            "created",
            "id",
            "updated",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if protocol (nullable) is None
        # and model_fields_set contains the field
        if self.protocol is None and "protocol" in self.model_fields_set:
            _dict['protocol'] = None

        # set to None if service (nullable) is None
        # and model_fields_set contains the field
        if self.service is None and "service" in self.model_fields_set:
            _dict['service'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetDomainRecords200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created": obj.get("created"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "port": obj.get("port"),
            "priority": obj.get("priority"),
            "protocol": obj.get("protocol"),
            "service": obj.get("service"),
            "tag": obj.get("tag"),
            "target": obj.get("target"),
            "ttl_sec": obj.get("ttl_sec"),
            "type": obj.get("type"),
            "updated": obj.get("updated"),
            "weight": obj.get("weight")
        })
        return _obj


