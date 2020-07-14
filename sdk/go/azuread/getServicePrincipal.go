// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Gets information about an existing Service Principal associated with an Application within Azure Active Directory.
//
// > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
//
// ## Example Usage
// ### By Application Display Name)
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azuread/sdk/v2/go/azuread"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "my-awesome-application"
// 		_, err := azuread.LookupServicePrincipal(ctx, "azuread::getServicePrincipal", &azuread.LookupServicePrincipalArgs{
// 			DisplayName: &opt0,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### By Application ID)
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azuread/sdk/v2/go/azuread"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "00000000-0000-0000-0000-000000000000"
// 		_, err := azuread.LookupServicePrincipal(ctx, "azuread::getServicePrincipal", &azuread.LookupServicePrincipalArgs{
// 			ApplicationId: &opt0,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### By Object ID)
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azuread/sdk/v2/go/azuread"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "00000000-0000-0000-0000-000000000000"
// 		_, err := azuread.LookupServicePrincipal(ctx, "azuread::getServicePrincipal", &azuread.LookupServicePrincipalArgs{
// 			ObjectId: &opt0,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupServicePrincipal(ctx *pulumi.Context, args *LookupServicePrincipalArgs, opts ...pulumi.InvokeOption) (*LookupServicePrincipalResult, error) {
	var rv LookupServicePrincipalResult
	err := ctx.Invoke("azuread:index/getServicePrincipal:getServicePrincipal", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getServicePrincipal.
type LookupServicePrincipalArgs struct {
	// The ID of the Azure AD Application.
	ApplicationId *string `pulumi:"applicationId"`
	// The Display Name of the Azure AD Application associated with this Service Principal.
	DisplayName *string `pulumi:"displayName"`
	// A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a `oauth2Permission` block as documented below.
	Oauth2Permissions []GetServicePrincipalOauth2Permission `pulumi:"oauth2Permissions"`
	// The ID of the Azure AD Service Principal.
	ObjectId *string `pulumi:"objectId"`
}

// A collection of values returned by getServicePrincipal.
type LookupServicePrincipalResult struct {
	AppRoles      []GetServicePrincipalAppRole `pulumi:"appRoles"`
	ApplicationId string                       `pulumi:"applicationId"`
	// Display name for the permission that appears in the admin consent and app assignment experiences.
	DisplayName string `pulumi:"displayName"`
	// The provider-assigned unique ID for this managed resource.
	Id                string                                `pulumi:"id"`
	Oauth2Permissions []GetServicePrincipalOauth2Permission `pulumi:"oauth2Permissions"`
	ObjectId          string                                `pulumi:"objectId"`
}
