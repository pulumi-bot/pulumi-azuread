# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['ServicePrincipalCertificate']


class ServicePrincipalCertificate(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 end_date_relative: Optional[pulumi.Input[str]] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 service_principal_id: Optional[pulumi.Input[str]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Certificate associated with a Service Principal within Azure Active Directory.

        > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuread as azuread

        example_application = azuread.Application("exampleApplication")
        example_service_principal = azuread.ServicePrincipal("exampleServicePrincipal", application_id=example_application.application_id)
        example_service_principal_certificate = azuread.ServicePrincipalCertificate("exampleServicePrincipalCertificate",
            service_principal_id=example_service_principal.id,
            type="AsymmetricX509Cert",
            value=(lambda path: open(path).read())("cert.pem"),
            end_date="2021-05-01T01:02:03Z")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] end_date: The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
        :param pulumi.Input[str] end_date_relative: A relative duration for which the Certificate is valid until, for example `240h` (10 days) or `2400h30m`. Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". Changing this field forces a new resource to be created.
        :param pulumi.Input[str] key_id: A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.
        :param pulumi.Input[str] service_principal_id: The ID of the Service Principal for which this certificate should be created. Changing this field forces a new resource to be created.
        :param pulumi.Input[str] start_date: The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
        :param pulumi.Input[str] type: The type of key/certificate. Must be one of `AsymmetricX509Cert` or `Symmetric`. Changing this fields forces a new resource to be created.
        :param pulumi.Input[str] value: The Certificate for this Service Principal.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['end_date'] = end_date
            __props__['end_date_relative'] = end_date_relative
            __props__['key_id'] = key_id
            if service_principal_id is None:
                raise TypeError("Missing required property 'service_principal_id'")
            __props__['service_principal_id'] = service_principal_id
            __props__['start_date'] = start_date
            __props__['type'] = type
            if value is None:
                raise TypeError("Missing required property 'value'")
            __props__['value'] = value
        super(ServicePrincipalCertificate, __self__).__init__(
            'azuread:index/servicePrincipalCertificate:ServicePrincipalCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            end_date: Optional[pulumi.Input[str]] = None,
            end_date_relative: Optional[pulumi.Input[str]] = None,
            key_id: Optional[pulumi.Input[str]] = None,
            service_principal_id: Optional[pulumi.Input[str]] = None,
            start_date: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'ServicePrincipalCertificate':
        """
        Get an existing ServicePrincipalCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] end_date: The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
        :param pulumi.Input[str] end_date_relative: A relative duration for which the Certificate is valid until, for example `240h` (10 days) or `2400h30m`. Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". Changing this field forces a new resource to be created.
        :param pulumi.Input[str] key_id: A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.
        :param pulumi.Input[str] service_principal_id: The ID of the Service Principal for which this certificate should be created. Changing this field forces a new resource to be created.
        :param pulumi.Input[str] start_date: The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
        :param pulumi.Input[str] type: The type of key/certificate. Must be one of `AsymmetricX509Cert` or `Symmetric`. Changing this fields forces a new resource to be created.
        :param pulumi.Input[str] value: The Certificate for this Service Principal.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["end_date"] = end_date
        __props__["end_date_relative"] = end_date_relative
        __props__["key_id"] = key_id
        __props__["service_principal_id"] = service_principal_id
        __props__["start_date"] = start_date
        __props__["type"] = type
        __props__["value"] = value
        return ServicePrincipalCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Output[str]:
        """
        The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
        """
        return pulumi.get(self, "end_date")

    @property
    @pulumi.getter(name="endDateRelative")
    def end_date_relative(self) -> pulumi.Output[Optional[str]]:
        """
        A relative duration for which the Certificate is valid until, for example `240h` (10 days) or `2400h30m`. Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". Changing this field forces a new resource to be created.
        """
        return pulumi.get(self, "end_date_relative")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[str]:
        """
        A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.
        """
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter(name="servicePrincipalId")
    def service_principal_id(self) -> pulumi.Output[str]:
        """
        The ID of the Service Principal for which this certificate should be created. Changing this field forces a new resource to be created.
        """
        return pulumi.get(self, "service_principal_id")

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[str]:
        """
        The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
        """
        return pulumi.get(self, "start_date")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of key/certificate. Must be one of `AsymmetricX509Cert` or `Symmetric`. Changing this fields forces a new resource to be created.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The Certificate for this Service Principal.
        """
        return pulumi.get(self, "value")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

