# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Application']


class Application(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_roles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationAppRoleArgs']]]]] = None,
                 available_to_other_tenants: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 group_membership_claims: Optional[pulumi.Input[str]] = None,
                 homepage: Optional[pulumi.Input[str]] = None,
                 identifier_uris: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 logout_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 oauth2_allow_implicit_flow: Optional[pulumi.Input[bool]] = None,
                 oauth2_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationOauth2PermissionArgs']]]]] = None,
                 optional_claims: Optional[pulumi.Input[pulumi.InputType['ApplicationOptionalClaimsArgs']]] = None,
                 owners: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 prevent_duplicate_names: Optional[pulumi.Input[bool]] = None,
                 public_client: Optional[pulumi.Input[bool]] = None,
                 reply_urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 required_resource_accesses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationRequiredResourceAccessArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an Application within Azure Active Directory.

        > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write owned by applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuread as azuread

        example = azuread.Application("example",
            app_roles=[azuread.ApplicationAppRoleArgs(
                allowed_member_types=[
                    "User",
                    "Application",
                ],
                description="Admins can manage roles and perform all task actions",
                display_name="Admin",
                is_enabled=True,
                value="Admin",
            )],
            available_to_other_tenants=False,
            display_name="example",
            homepage="https://homepage",
            identifier_uris=["https://uri"],
            oauth2_allow_implicit_flow=True,
            oauth2_permissions=[
                azuread.ApplicationOauth2PermissionArgs(
                    admin_consent_description="Allow the application to access example on behalf of the signed-in user.",
                    admin_consent_display_name="Access example",
                    is_enabled=True,
                    type="User",
                    user_consent_description="Allow the application to access example on your behalf.",
                    user_consent_display_name="Access example",
                    value="user_impersonation",
                ),
                azuread.ApplicationOauth2PermissionArgs(
                    admin_consent_description="Administer the example application",
                    admin_consent_display_name="Administer",
                    is_enabled=True,
                    type="Admin",
                    value="administer",
                ),
            ],
            optional_claims=azuread.ApplicationOptionalClaimsArgs(
                access_tokens=[
                    azuread.ApplicationOptionalClaimsAccessTokenArgs(
                        name="myclaim",
                    ),
                    azuread.ApplicationOptionalClaimsAccessTokenArgs(
                        name="otherclaim",
                    ),
                ],
                id_tokens=[azuread.ApplicationOptionalClaimsIdTokenArgs(
                    additional_properties=["emit_as_roles"],
                    essential=True,
                    name="userclaim",
                    source="user",
                )],
            ),
            owners=["00000004-0000-0000-c000-000000000000"],
            reply_urls=["https://replyurl"],
            required_resource_accesses=[
                azuread.ApplicationRequiredResourceAccessArgs(
                    resource_accesses=[
                        azuread.ApplicationRequiredResourceAccessResourceAccessArgs(
                            id="...",
                            type="Role",
                        ),
                        azuread.ApplicationRequiredResourceAccessResourceAccessArgs(
                            id="...",
                            type="Scope",
                        ),
                        azuread.ApplicationRequiredResourceAccessResourceAccessArgs(
                            id="...",
                            type="Scope",
                        ),
                    ],
                    resource_app_id="00000003-0000-0000-c000-000000000000",
                ),
                azuread.ApplicationRequiredResourceAccessArgs(
                    resource_accesses=[azuread.ApplicationRequiredResourceAccessResourceAccessArgs(
                        id="...",
                        type="Scope",
                    )],
                    resource_app_id="00000002-0000-0000-c000-000000000000",
                ),
            ],
            type="webapp/api")
        ```

        ## Import

        Azure Active Directory Applications can be imported using the `object id`, e.g.

        ```sh
         $ pulumi import azuread:index/application:Application test 00000000-0000-0000-0000-000000000000
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationAppRoleArgs']]]] app_roles: A collection of `app_role` blocks as documented below. For more information https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles
        :param pulumi.Input[bool] available_to_other_tenants: Is this Azure AD Application available to other tenants? Defaults to `false`.
        :param pulumi.Input[str] display_name: The display name for the application.
        :param pulumi.Input[str] group_membership_claims: Configures the `groups` claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to `SecurityGroup`. Possible values are `None`, `SecurityGroup`, `DirectoryRole`, `ApplicationGroup` or `All`.
        :param pulumi.Input[str] homepage: The URL to the application's home page.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] identifier_uris: A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
        :param pulumi.Input[str] logout_url: The URL of the logout page.
        :param pulumi.Input[str] name: The name of the optional claim.
        :param pulumi.Input[bool] oauth2_allow_implicit_flow: Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationOauth2PermissionArgs']]]] oauth2_permissions: A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by `oauth2_permissions` blocks as documented below.
        :param pulumi.Input[pulumi.InputType['ApplicationOptionalClaimsArgs']] optional_claims: A collection of `access_token` or `id_token` blocks as documented below which list the optional claims configured for each token type. For more information see https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims
        :param pulumi.Input[Sequence[pulumi.Input[str]]] owners: A list of Azure AD Object IDs that will be granted ownership of the application. Defaults to the Object ID of the caller creating the application. If a list is specified the caller Object ID will no longer be included unless explicitly added to the list.
        :param pulumi.Input[bool] prevent_duplicate_names: If `true`, will return an error when an existing Application is found with the same name. Defaults to `false`.
        :param pulumi.Input[bool] public_client: Is this Azure AD Application a public client? Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] reply_urls: A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationRequiredResourceAccessArgs']]]] required_resource_accesses: A collection of `required_resource_access` blocks as documented below.
        :param pulumi.Input[str] type: Type of an application: `webapp/api` or `native`. Defaults to `webapp/api`. For `native` apps type `identifier_uris` property can not not be set.
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

            __props__['app_roles'] = app_roles
            __props__['available_to_other_tenants'] = available_to_other_tenants
            __props__['display_name'] = display_name
            __props__['group_membership_claims'] = group_membership_claims
            __props__['homepage'] = homepage
            __props__['identifier_uris'] = identifier_uris
            __props__['logout_url'] = logout_url
            if name is not None and not opts.urn:
                warnings.warn("""This property has been renamed to `display_name` and will be removed in version 2.0 of this provider.""", DeprecationWarning)
                pulumi.log.warn("""name is deprecated: This property has been renamed to `display_name` and will be removed in version 2.0 of this provider.""")
            __props__['name'] = name
            __props__['oauth2_allow_implicit_flow'] = oauth2_allow_implicit_flow
            __props__['oauth2_permissions'] = oauth2_permissions
            __props__['optional_claims'] = optional_claims
            __props__['owners'] = owners
            __props__['prevent_duplicate_names'] = prevent_duplicate_names
            __props__['public_client'] = public_client
            __props__['reply_urls'] = reply_urls
            __props__['required_resource_accesses'] = required_resource_accesses
            if type is not None and not opts.urn:
                warnings.warn("""This property is deprecated and will be removed in version 2.0 of this provider.""", DeprecationWarning)
                pulumi.log.warn("""type is deprecated: This property is deprecated and will be removed in version 2.0 of this provider.""")
            __props__['type'] = type
            __props__['application_id'] = None
            __props__['object_id'] = None
        super(Application, __self__).__init__(
            'azuread:index/application:Application',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_roles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationAppRoleArgs']]]]] = None,
            application_id: Optional[pulumi.Input[str]] = None,
            available_to_other_tenants: Optional[pulumi.Input[bool]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            group_membership_claims: Optional[pulumi.Input[str]] = None,
            homepage: Optional[pulumi.Input[str]] = None,
            identifier_uris: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            logout_url: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            oauth2_allow_implicit_flow: Optional[pulumi.Input[bool]] = None,
            oauth2_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationOauth2PermissionArgs']]]]] = None,
            object_id: Optional[pulumi.Input[str]] = None,
            optional_claims: Optional[pulumi.Input[pulumi.InputType['ApplicationOptionalClaimsArgs']]] = None,
            owners: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            prevent_duplicate_names: Optional[pulumi.Input[bool]] = None,
            public_client: Optional[pulumi.Input[bool]] = None,
            reply_urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            required_resource_accesses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationRequiredResourceAccessArgs']]]]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Application':
        """
        Get an existing Application resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationAppRoleArgs']]]] app_roles: A collection of `app_role` blocks as documented below. For more information https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles
        :param pulumi.Input[str] application_id: The Application ID (Client ID).
        :param pulumi.Input[bool] available_to_other_tenants: Is this Azure AD Application available to other tenants? Defaults to `false`.
        :param pulumi.Input[str] display_name: The display name for the application.
        :param pulumi.Input[str] group_membership_claims: Configures the `groups` claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to `SecurityGroup`. Possible values are `None`, `SecurityGroup`, `DirectoryRole`, `ApplicationGroup` or `All`.
        :param pulumi.Input[str] homepage: The URL to the application's home page.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] identifier_uris: A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
        :param pulumi.Input[str] logout_url: The URL of the logout page.
        :param pulumi.Input[str] name: The name of the optional claim.
        :param pulumi.Input[bool] oauth2_allow_implicit_flow: Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationOauth2PermissionArgs']]]] oauth2_permissions: A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by `oauth2_permissions` blocks as documented below.
        :param pulumi.Input[str] object_id: The Application's Object ID.
        :param pulumi.Input[pulumi.InputType['ApplicationOptionalClaimsArgs']] optional_claims: A collection of `access_token` or `id_token` blocks as documented below which list the optional claims configured for each token type. For more information see https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims
        :param pulumi.Input[Sequence[pulumi.Input[str]]] owners: A list of Azure AD Object IDs that will be granted ownership of the application. Defaults to the Object ID of the caller creating the application. If a list is specified the caller Object ID will no longer be included unless explicitly added to the list.
        :param pulumi.Input[bool] prevent_duplicate_names: If `true`, will return an error when an existing Application is found with the same name. Defaults to `false`.
        :param pulumi.Input[bool] public_client: Is this Azure AD Application a public client? Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] reply_urls: A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationRequiredResourceAccessArgs']]]] required_resource_accesses: A collection of `required_resource_access` blocks as documented below.
        :param pulumi.Input[str] type: Type of an application: `webapp/api` or `native`. Defaults to `webapp/api`. For `native` apps type `identifier_uris` property can not not be set.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["app_roles"] = app_roles
        __props__["application_id"] = application_id
        __props__["available_to_other_tenants"] = available_to_other_tenants
        __props__["display_name"] = display_name
        __props__["group_membership_claims"] = group_membership_claims
        __props__["homepage"] = homepage
        __props__["identifier_uris"] = identifier_uris
        __props__["logout_url"] = logout_url
        __props__["name"] = name
        __props__["oauth2_allow_implicit_flow"] = oauth2_allow_implicit_flow
        __props__["oauth2_permissions"] = oauth2_permissions
        __props__["object_id"] = object_id
        __props__["optional_claims"] = optional_claims
        __props__["owners"] = owners
        __props__["prevent_duplicate_names"] = prevent_duplicate_names
        __props__["public_client"] = public_client
        __props__["reply_urls"] = reply_urls
        __props__["required_resource_accesses"] = required_resource_accesses
        __props__["type"] = type
        return Application(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appRoles")
    def app_roles(self) -> pulumi.Output[Sequence['outputs.ApplicationAppRole']]:
        """
        A collection of `app_role` blocks as documented below. For more information https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles
        """
        return pulumi.get(self, "app_roles")

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        """
        The Application ID (Client ID).
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="availableToOtherTenants")
    def available_to_other_tenants(self) -> pulumi.Output[Optional[bool]]:
        """
        Is this Azure AD Application available to other tenants? Defaults to `false`.
        """
        return pulumi.get(self, "available_to_other_tenants")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name for the application.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="groupMembershipClaims")
    def group_membership_claims(self) -> pulumi.Output[Optional[str]]:
        """
        Configures the `groups` claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to `SecurityGroup`. Possible values are `None`, `SecurityGroup`, `DirectoryRole`, `ApplicationGroup` or `All`.
        """
        return pulumi.get(self, "group_membership_claims")

    @property
    @pulumi.getter
    def homepage(self) -> pulumi.Output[str]:
        """
        The URL to the application's home page.
        """
        return pulumi.get(self, "homepage")

    @property
    @pulumi.getter(name="identifierUris")
    def identifier_uris(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
        """
        return pulumi.get(self, "identifier_uris")

    @property
    @pulumi.getter(name="logoutUrl")
    def logout_url(self) -> pulumi.Output[Optional[str]]:
        """
        The URL of the logout page.
        """
        return pulumi.get(self, "logout_url")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the optional claim.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oauth2AllowImplicitFlow")
    def oauth2_allow_implicit_flow(self) -> pulumi.Output[Optional[bool]]:
        """
        Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.
        """
        return pulumi.get(self, "oauth2_allow_implicit_flow")

    @property
    @pulumi.getter(name="oauth2Permissions")
    def oauth2_permissions(self) -> pulumi.Output[Sequence['outputs.ApplicationOauth2Permission']]:
        """
        A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by `oauth2_permissions` blocks as documented below.
        """
        return pulumi.get(self, "oauth2_permissions")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[str]:
        """
        The Application's Object ID.
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="optionalClaims")
    def optional_claims(self) -> pulumi.Output[Optional['outputs.ApplicationOptionalClaims']]:
        """
        A collection of `access_token` or `id_token` blocks as documented below which list the optional claims configured for each token type. For more information see https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims
        """
        return pulumi.get(self, "optional_claims")

    @property
    @pulumi.getter
    def owners(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of Azure AD Object IDs that will be granted ownership of the application. Defaults to the Object ID of the caller creating the application. If a list is specified the caller Object ID will no longer be included unless explicitly added to the list.
        """
        return pulumi.get(self, "owners")

    @property
    @pulumi.getter(name="preventDuplicateNames")
    def prevent_duplicate_names(self) -> pulumi.Output[Optional[bool]]:
        """
        If `true`, will return an error when an existing Application is found with the same name. Defaults to `false`.
        """
        return pulumi.get(self, "prevent_duplicate_names")

    @property
    @pulumi.getter(name="publicClient")
    def public_client(self) -> pulumi.Output[bool]:
        """
        Is this Azure AD Application a public client? Defaults to `false`.
        """
        return pulumi.get(self, "public_client")

    @property
    @pulumi.getter(name="replyUrls")
    def reply_urls(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.
        """
        return pulumi.get(self, "reply_urls")

    @property
    @pulumi.getter(name="requiredResourceAccesses")
    def required_resource_accesses(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationRequiredResourceAccess']]]:
        """
        A collection of `required_resource_access` blocks as documented below.
        """
        return pulumi.get(self, "required_resource_accesses")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of an application: `webapp/api` or `native`. Defaults to `webapp/api`. For `native` apps type `identifier_uris` property can not not be set.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

