// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Gets Object IDs or Display Names for multiple Azure Active Directory groups.
//
// > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read directory data` within the `Windows Azure Active Directory` API.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azuread/sdk/v3/go/azuread"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := azuread.GetGroups(ctx, &azuread.GetGroupsArgs{
// 			Names: []string{
// 				"group-a",
// 				"group-b",
// 			},
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetGroups(ctx *pulumi.Context, args *GetGroupsArgs, opts ...pulumi.InvokeOption) (*GetGroupsResult, error) {
	var rv GetGroupsResult
	err := ctx.Invoke("azuread:index/getGroups:getGroups", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getGroups.
type GetGroupsArgs struct {
	DisplayNames []string `pulumi:"displayNames"`
	// The Display Names of the Azure AD Groups.
	//
	// Deprecated: This property has been renamed to `display_names` and will be removed in v2.0 of this provider.
	Names []string `pulumi:"names"`
	// The Object IDs of the Azure AD Groups.
	ObjectIds []string `pulumi:"objectIds"`
}

// A collection of values returned by getGroups.
type GetGroupsResult struct {
	DisplayNames []string `pulumi:"displayNames"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The Display Names of the Azure AD Groups.
	//
	// Deprecated: This property has been renamed to `display_names` and will be removed in v2.0 of this provider.
	Names []string `pulumi:"names"`
	// The Object IDs of the Azure AD Groups.
	ObjectIds []string `pulumi:"objectIds"`
}
