// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access information about an existing Application within Azure Active Directory.
//
// > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all (or owned by) applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
func LookupApplication(ctx *pulumi.Context, args *LookupApplicationArgs, opts ...pulumi.InvokeOption) (*LookupApplicationResult, error) {
	var rv LookupApplicationResult
	err := ctx.Invoke("azuread:index/getApplication:getApplication", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getApplication.
type LookupApplicationArgs struct {
	// Specifies the Application ID of the Azure Active Directory Application.
	ApplicationId *string `pulumi:"applicationId"`
	// Specifies the name of the Application within Azure Active Directory.
	Name *string `pulumi:"name"`
	// A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a `oauth2Permission` block as documented below.
	Oauth2Permissions []GetApplicationOauth2Permission `pulumi:"oauth2Permissions"`
	// Specifies the Object ID of the Application within Azure Active Directory.
	ObjectId *string `pulumi:"objectId"`
	// A collection of `accessToken` or `idToken` blocks as documented below which list the optional claims configured for each token type. For more information see https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims
	OptionalClaims *GetApplicationOptionalClaims `pulumi:"optionalClaims"`
}

// A collection of values returned by getApplication.
type LookupApplicationResult struct {
	// A collection of `appRole` blocks as documented below. For more information https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles
	AppRoles []GetApplicationAppRole `pulumi:"appRoles"`
	// the Application ID of the Azure Active Directory Application.
	ApplicationId string `pulumi:"applicationId"`
	// Is this Azure AD Application available to other tenants?
	AvailableToOtherTenants bool `pulumi:"availableToOtherTenants"`
	// The `groups` claim issued in a user or OAuth 2.0 access token that the app expects.
	GroupMembershipClaims string `pulumi:"groupMembershipClaims"`
	Homepage              string `pulumi:"homepage"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
	IdentifierUris []string `pulumi:"identifierUris"`
	// The URL of the logout page.
	LogoutUrl string `pulumi:"logoutUrl"`
	// The name of the optional claim.
	Name string `pulumi:"name"`
	// Does this Azure AD Application allow OAuth2.0 implicit flow tokens?
	Oauth2AllowImplicitFlow bool `pulumi:"oauth2AllowImplicitFlow"`
	// A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a `oauth2Permission` block as documented below.
	Oauth2Permissions []GetApplicationOauth2Permission `pulumi:"oauth2Permissions"`
	// the Object ID of the Azure Active Directory Application.
	ObjectId string `pulumi:"objectId"`
	// A collection of `accessToken` or `idToken` blocks as documented below which list the optional claims configured for each token type. For more information see https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims
	OptionalClaims *GetApplicationOptionalClaims `pulumi:"optionalClaims"`
	// A list of User Object IDs that are assigned ownership of the application registration.
	Owners []string `pulumi:"owners"`
	// A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.
	ReplyUrls []string `pulumi:"replyUrls"`
	// A collection of `requiredResourceAccess` blocks as documented below.
	RequiredResourceAccesses []GetApplicationRequiredResourceAccess `pulumi:"requiredResourceAccesses"`
	// The type of the permission
	Type string `pulumi:"type"`
}
