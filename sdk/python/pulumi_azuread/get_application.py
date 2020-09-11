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

__all__ = [
    'GetApplicationResult',
    'AwaitableGetApplicationResult',
    'get_application',
]

@pulumi.output_type
class GetApplicationResult:
    """
    A collection of values returned by getApplication.
    """
    def __init__(__self__, app_roles=None, application_id=None, available_to_other_tenants=None, group_membership_claims=None, homepage=None, id=None, identifier_uris=None, logout_url=None, name=None, oauth2_allow_implicit_flow=None, oauth2_permissions=None, object_id=None, optional_claims=None, owners=None, reply_urls=None, required_resource_accesses=None, type=None):
        if app_roles and not isinstance(app_roles, list):
            raise TypeError("Expected argument 'app_roles' to be a list")
        pulumi.set(__self__, "app_roles", app_roles)
        if application_id and not isinstance(application_id, str):
            raise TypeError("Expected argument 'application_id' to be a str")
        pulumi.set(__self__, "application_id", application_id)
        if available_to_other_tenants and not isinstance(available_to_other_tenants, bool):
            raise TypeError("Expected argument 'available_to_other_tenants' to be a bool")
        pulumi.set(__self__, "available_to_other_tenants", available_to_other_tenants)
        if group_membership_claims and not isinstance(group_membership_claims, str):
            raise TypeError("Expected argument 'group_membership_claims' to be a str")
        pulumi.set(__self__, "group_membership_claims", group_membership_claims)
        if homepage and not isinstance(homepage, str):
            raise TypeError("Expected argument 'homepage' to be a str")
        pulumi.set(__self__, "homepage", homepage)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identifier_uris and not isinstance(identifier_uris, list):
            raise TypeError("Expected argument 'identifier_uris' to be a list")
        pulumi.set(__self__, "identifier_uris", identifier_uris)
        if logout_url and not isinstance(logout_url, str):
            raise TypeError("Expected argument 'logout_url' to be a str")
        pulumi.set(__self__, "logout_url", logout_url)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if oauth2_allow_implicit_flow and not isinstance(oauth2_allow_implicit_flow, bool):
            raise TypeError("Expected argument 'oauth2_allow_implicit_flow' to be a bool")
        pulumi.set(__self__, "oauth2_allow_implicit_flow", oauth2_allow_implicit_flow)
        if oauth2_permissions and not isinstance(oauth2_permissions, list):
            raise TypeError("Expected argument 'oauth2_permissions' to be a list")
        pulumi.set(__self__, "oauth2_permissions", oauth2_permissions)
        if object_id and not isinstance(object_id, str):
            raise TypeError("Expected argument 'object_id' to be a str")
        pulumi.set(__self__, "object_id", object_id)
        if optional_claims and not isinstance(optional_claims, dict):
            raise TypeError("Expected argument 'optional_claims' to be a dict")
        pulumi.set(__self__, "optional_claims", optional_claims)
        if owners and not isinstance(owners, list):
            raise TypeError("Expected argument 'owners' to be a list")
        pulumi.set(__self__, "owners", owners)
        if reply_urls and not isinstance(reply_urls, list):
            raise TypeError("Expected argument 'reply_urls' to be a list")
        pulumi.set(__self__, "reply_urls", reply_urls)
        if required_resource_accesses and not isinstance(required_resource_accesses, list):
            raise TypeError("Expected argument 'required_resource_accesses' to be a list")
        pulumi.set(__self__, "required_resource_accesses", required_resource_accesses)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="appRoles")
    def app_roles(self) -> Sequence['outputs.GetApplicationAppRoleResult']:
        """
        A collection of `app_role` blocks as documented below. For more information https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles
        """
        return pulumi.get(self, "app_roles")

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> str:
        """
        the Application ID of the Azure Active Directory Application.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="availableToOtherTenants")
    def available_to_other_tenants(self) -> bool:
        """
        Is this Azure AD Application available to other tenants?
        """
        return pulumi.get(self, "available_to_other_tenants")

    @property
    @pulumi.getter(name="groupMembershipClaims")
    def group_membership_claims(self) -> str:
        """
        The `groups` claim issued in a user or OAuth 2.0 access token that the app expects.
        """
        return pulumi.get(self, "group_membership_claims")

    @property
    @pulumi.getter
    def homepage(self) -> str:
        return pulumi.get(self, "homepage")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="identifierUris")
    def identifier_uris(self) -> Sequence[str]:
        """
        A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
        """
        return pulumi.get(self, "identifier_uris")

    @property
    @pulumi.getter(name="logoutUrl")
    def logout_url(self) -> str:
        """
        The URL of the logout page.
        """
        return pulumi.get(self, "logout_url")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the optional claim.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oauth2AllowImplicitFlow")
    def oauth2_allow_implicit_flow(self) -> bool:
        """
        Does this Azure AD Application allow OAuth2.0 implicit flow tokens?
        """
        return pulumi.get(self, "oauth2_allow_implicit_flow")

    @property
    @pulumi.getter(name="oauth2Permissions")
    def oauth2_permissions(self) -> Sequence['outputs.GetApplicationOauth2PermissionResult']:
        """
        A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a `oauth2_permission` block as documented below.
        """
        return pulumi.get(self, "oauth2_permissions")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> str:
        """
        the Object ID of the Azure Active Directory Application.
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="optionalClaims")
    def optional_claims(self) -> Optional['outputs.GetApplicationOptionalClaimsResult']:
        """
        A collection of `access_token` or `id_token` blocks as documented below which list the optional claims configured for each token type. For more information see https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims
        """
        return pulumi.get(self, "optional_claims")

    @property
    @pulumi.getter
    def owners(self) -> Sequence[str]:
        """
        A list of User Object IDs that are assigned ownership of the application registration.
        """
        return pulumi.get(self, "owners")

    @property
    @pulumi.getter(name="replyUrls")
    def reply_urls(self) -> Sequence[str]:
        """
        A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.
        """
        return pulumi.get(self, "reply_urls")

    @property
    @pulumi.getter(name="requiredResourceAccesses")
    def required_resource_accesses(self) -> Sequence['outputs.GetApplicationRequiredResourceAccessResult']:
        """
        A collection of `required_resource_access` blocks as documented below.
        """
        return pulumi.get(self, "required_resource_accesses")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the permission
        """
        return pulumi.get(self, "type")


class AwaitableGetApplicationResult(GetApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationResult(
            app_roles=self.app_roles,
            application_id=self.application_id,
            available_to_other_tenants=self.available_to_other_tenants,
            group_membership_claims=self.group_membership_claims,
            homepage=self.homepage,
            id=self.id,
            identifier_uris=self.identifier_uris,
            logout_url=self.logout_url,
            name=self.name,
            oauth2_allow_implicit_flow=self.oauth2_allow_implicit_flow,
            oauth2_permissions=self.oauth2_permissions,
            object_id=self.object_id,
            optional_claims=self.optional_claims,
            owners=self.owners,
            reply_urls=self.reply_urls,
            required_resource_accesses=self.required_resource_accesses,
            type=self.type)


def get_application(application_id: Optional[str] = None,
                    name: Optional[str] = None,
                    oauth2_permissions: Optional[Sequence[pulumi.InputType['GetApplicationOauth2PermissionArgs']]] = None,
                    object_id: Optional[str] = None,
                    optional_claims: Optional[pulumi.InputType['GetApplicationOptionalClaimsArgs']] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationResult:
    """
    Use this data source to access information about an existing Application within Azure Active Directory.

    > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all (or owned by) applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azuread as azuread

    example = azuread.get_application(name="My First AzureAD Application")
    pulumi.export("azureAdObjectId", example.id)
    ```


    :param str application_id: Specifies the Application ID of the Azure Active Directory Application.
    :param str name: Specifies the name of the Application within Azure Active Directory.
    :param Sequence[pulumi.InputType['GetApplicationOauth2PermissionArgs']] oauth2_permissions: A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a `oauth2_permission` block as documented below.
    :param str object_id: Specifies the Object ID of the Application within Azure Active Directory.
    :param pulumi.InputType['GetApplicationOptionalClaimsArgs'] optional_claims: A collection of `access_token` or `id_token` blocks as documented below which list the optional claims configured for each token type. For more information see https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims
    """
    __args__ = dict()
    __args__['applicationId'] = application_id
    __args__['name'] = name
    __args__['oauth2Permissions'] = oauth2_permissions
    __args__['objectId'] = object_id
    __args__['optionalClaims'] = optional_claims
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azuread:index/getApplication:getApplication', __args__, opts=opts, typ=GetApplicationResult).value

    return AwaitableGetApplicationResult(
        app_roles=__ret__.app_roles,
        application_id=__ret__.application_id,
        available_to_other_tenants=__ret__.available_to_other_tenants,
        group_membership_claims=__ret__.group_membership_claims,
        homepage=__ret__.homepage,
        id=__ret__.id,
        identifier_uris=__ret__.identifier_uris,
        logout_url=__ret__.logout_url,
        name=__ret__.name,
        oauth2_allow_implicit_flow=__ret__.oauth2_allow_implicit_flow,
        oauth2_permissions=__ret__.oauth2_permissions,
        object_id=__ret__.object_id,
        optional_claims=__ret__.optional_claims,
        owners=__ret__.owners,
        reply_urls=__ret__.reply_urls,
        required_resource_accesses=__ret__.required_resource_accesses,
        type=__ret__.type)
