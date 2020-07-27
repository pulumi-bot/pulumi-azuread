# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import _utilities, _tables


class ServicePrincipal(pulumi.CustomResource):
    app_role_assignment_required: pulumi.Output[bool]
    """
    Does this Service Principal require an AppRoleAssignment to a user or group before Azure AD will issue a user or access token to the application? Defaults to `false`.
    """
    application_id: pulumi.Output[str]
    """
    The ID of the Azure AD Application for which to create a Service Principal.
    """
    display_name: pulumi.Output[str]
    """
    The Display Name of the Azure Active Directory Application associated with this Service Principal.
    """
    oauth2_permissions: pulumi.Output[list]
    """
    A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a `oauth2_permission` block as documented below.

      * `adminConsentDescription` (`str`) - The description of the admin consent.
      * `adminConsentDisplayName` (`str`) - The display name of the admin consent.
      * `id` (`str`) - The unique identifier for one of the `OAuth2Permission`.
      * `isEnabled` (`bool`) - Is this permission enabled?
      * `type` (`str`) - The type of the permission.
      * `userConsentDescription` (`str`) - The description of the user consent.
      * `userConsentDisplayName` (`str`) - The display name of the user consent.
      * `value` (`str`) - The name of this permission.
    """
    object_id: pulumi.Output[str]
    """
    The Service Principal's Object ID.
    """
    tags: pulumi.Output[list]
    """
    A list of tags to apply to the Service Principal.
    """
    def __init__(__self__, resource_name, opts=None, app_role_assignment_required=None, application_id=None, oauth2_permissions=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Service Principal associated with an Application within Azure Active Directory.

        > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API. Please see The Granting a Service Principal permission to manage AAD for the required steps.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuread as azuread

        example_application = azuread.Application("exampleApplication",
            homepage="http://homepage",
            identifier_uris=["http://uri"],
            reply_urls=["http://replyurl"],
            available_to_other_tenants=False,
            oauth2_allow_implicit_flow=True)
        example_service_principal = azuread.ServicePrincipal("exampleServicePrincipal",
            application_id=example_application.application_id,
            app_role_assignment_required=False,
            tags=[
                "example",
                "tags",
                "here",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] app_role_assignment_required: Does this Service Principal require an AppRoleAssignment to a user or group before Azure AD will issue a user or access token to the application? Defaults to `false`.
        :param pulumi.Input[str] application_id: The ID of the Azure AD Application for which to create a Service Principal.
        :param pulumi.Input[list] oauth2_permissions: A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a `oauth2_permission` block as documented below.
        :param pulumi.Input[list] tags: A list of tags to apply to the Service Principal.

        The **oauth2_permissions** object supports the following:

          * `adminConsentDescription` (`pulumi.Input[str]`) - The description of the admin consent.
          * `adminConsentDisplayName` (`pulumi.Input[str]`) - The display name of the admin consent.
          * `id` (`pulumi.Input[str]`) - The unique identifier for one of the `OAuth2Permission`.
          * `isEnabled` (`pulumi.Input[bool]`) - Is this permission enabled?
          * `type` (`pulumi.Input[str]`) - The type of the permission.
          * `userConsentDescription` (`pulumi.Input[str]`) - The description of the user consent.
          * `userConsentDisplayName` (`pulumi.Input[str]`) - The display name of the user consent.
          * `value` (`pulumi.Input[str]`) - The name of this permission.
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

            __props__['app_role_assignment_required'] = app_role_assignment_required
            if application_id is None:
                raise TypeError("Missing required property 'application_id'")
            __props__['application_id'] = application_id
            __props__['oauth2_permissions'] = oauth2_permissions
            __props__['tags'] = tags
            __props__['display_name'] = None
            __props__['object_id'] = None
        super(ServicePrincipal, __self__).__init__(
            'azuread:index/servicePrincipal:ServicePrincipal',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, app_role_assignment_required=None, application_id=None, display_name=None, oauth2_permissions=None, object_id=None, tags=None):
        """
        Get an existing ServicePrincipal resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] app_role_assignment_required: Does this Service Principal require an AppRoleAssignment to a user or group before Azure AD will issue a user or access token to the application? Defaults to `false`.
        :param pulumi.Input[str] application_id: The ID of the Azure AD Application for which to create a Service Principal.
        :param pulumi.Input[str] display_name: The Display Name of the Azure Active Directory Application associated with this Service Principal.
        :param pulumi.Input[list] oauth2_permissions: A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a `oauth2_permission` block as documented below.
        :param pulumi.Input[str] object_id: The Service Principal's Object ID.
        :param pulumi.Input[list] tags: A list of tags to apply to the Service Principal.

        The **oauth2_permissions** object supports the following:

          * `adminConsentDescription` (`pulumi.Input[str]`) - The description of the admin consent.
          * `adminConsentDisplayName` (`pulumi.Input[str]`) - The display name of the admin consent.
          * `id` (`pulumi.Input[str]`) - The unique identifier for one of the `OAuth2Permission`.
          * `isEnabled` (`pulumi.Input[bool]`) - Is this permission enabled?
          * `type` (`pulumi.Input[str]`) - The type of the permission.
          * `userConsentDescription` (`pulumi.Input[str]`) - The description of the user consent.
          * `userConsentDisplayName` (`pulumi.Input[str]`) - The display name of the user consent.
          * `value` (`pulumi.Input[str]`) - The name of this permission.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["app_role_assignment_required"] = app_role_assignment_required
        __props__["application_id"] = application_id
        __props__["display_name"] = display_name
        __props__["oauth2_permissions"] = oauth2_permissions
        __props__["object_id"] = object_id
        __props__["tags"] = tags
        return ServicePrincipal(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
