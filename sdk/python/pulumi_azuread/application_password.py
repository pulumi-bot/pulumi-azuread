# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['ApplicationPassword']


class ApplicationPassword(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 application_object_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 end_date_relative: Optional[pulumi.Input[str]] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Password associated with an Application within Azure Active Directory. Also can be referred to as Client secrets.

        > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuread as azuread

        example_application = azuread.Application("exampleApplication")
        example_application_password = azuread.ApplicationPassword("exampleApplicationPassword",
            application_object_id=example_application.id,
            description="My managed password",
            value="VT=uSgbTanZhyz@%nL9Hpd+Tfay_MRV#",
            end_date="2099-01-01T01:02:03Z")
        ```

        ## Import

        Passwords can be imported using the `object id` of an Application and the `key id` of the password, e.g. ell

         -> **NOTE:** This ID format is unique to Terraform and is composed of the Application's Object ID, the string "password" and the Password's Key ID in the format `{ObjectId}/password/{PasswordKeyId}`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_object_id: The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
        :param pulumi.Input[str] description: A description for the Password.
        :param pulumi.Input[str] end_date: The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
        :param pulumi.Input[str] end_date_relative: A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
        :param pulumi.Input[str] key_id: A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
        :param pulumi.Input[str] start_date: The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
        :param pulumi.Input[str] value: The Password for this Application.
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

            if application_id is not None:
                warnings.warn("Deprecated in favour of `application_object_id` to prevent confusion", DeprecationWarning)
                pulumi.log.warn("application_id is deprecated: Deprecated in favour of `application_object_id` to prevent confusion")
            __props__['application_id'] = application_id
            __props__['application_object_id'] = application_object_id
            __props__['description'] = description
            __props__['end_date'] = end_date
            __props__['end_date_relative'] = end_date_relative
            __props__['key_id'] = key_id
            __props__['start_date'] = start_date
            if value is None:
                raise TypeError("Missing required property 'value'")
            __props__['value'] = value
        super(ApplicationPassword, __self__).__init__(
            'azuread:index/applicationPassword:ApplicationPassword',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_id: Optional[pulumi.Input[str]] = None,
            application_object_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            end_date: Optional[pulumi.Input[str]] = None,
            end_date_relative: Optional[pulumi.Input[str]] = None,
            key_id: Optional[pulumi.Input[str]] = None,
            start_date: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'ApplicationPassword':
        """
        Get an existing ApplicationPassword resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_object_id: The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
        :param pulumi.Input[str] description: A description for the Password.
        :param pulumi.Input[str] end_date: The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
        :param pulumi.Input[str] end_date_relative: A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
        :param pulumi.Input[str] key_id: A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
        :param pulumi.Input[str] start_date: The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
        :param pulumi.Input[str] value: The Password for this Application.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["application_id"] = application_id
        __props__["application_object_id"] = application_object_id
        __props__["description"] = description
        __props__["end_date"] = end_date
        __props__["end_date_relative"] = end_date_relative
        __props__["key_id"] = key_id
        __props__["start_date"] = start_date
        __props__["value"] = value
        return ApplicationPassword(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="applicationObjectId")
    def application_object_id(self) -> pulumi.Output[str]:
        """
        The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
        """
        return pulumi.get(self, "application_object_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        A description for the Password.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Output[str]:
        """
        The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
        """
        return pulumi.get(self, "end_date")

    @property
    @pulumi.getter(name="endDateRelative")
    def end_date_relative(self) -> pulumi.Output[Optional[str]]:
        """
        A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
        """
        return pulumi.get(self, "end_date_relative")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[str]:
        """
        A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
        """
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[str]:
        """
        The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
        """
        return pulumi.get(self, "start_date")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The Password for this Application.
        """
        return pulumi.get(self, "value")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

