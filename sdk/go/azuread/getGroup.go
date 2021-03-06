// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Gets information about an Azure Active Directory group.
//
// > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read directory data` within the `Windows Azure Active Directory` API.
func LookupGroup(ctx *pulumi.Context, args *LookupGroupArgs, opts ...pulumi.InvokeOption) (*LookupGroupResult, error) {
	var rv LookupGroupResult
	err := ctx.Invoke("azuread:index/getGroup:getGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getGroup.
type LookupGroupArgs struct {
	// The Name of the AD Group we want to lookup.
	Name *string `pulumi:"name"`
	// Specifies the Object ID of the AD Group within Azure Active Directory.
	ObjectId *string `pulumi:"objectId"`
}

// A collection of values returned by getGroup.
type LookupGroupResult struct {
	// The description of the AD Group.
	Description string `pulumi:"description"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The Object IDs of the Azure AD Group members.
	Members []string `pulumi:"members"`
	// The name of the Azure AD Group.
	Name     string `pulumi:"name"`
	ObjectId string `pulumi:"objectId"`
	// The Object IDs of the Azure AD Group owners.
	Owners []string `pulumi:"owners"`
}
