// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Gets information about an Azure Active Directory user.
//
// > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read directory data` within the `Windows Azure Active Directory` API.
func LookupUser(ctx *pulumi.Context, args *LookupUserArgs, opts ...pulumi.InvokeOption) (*LookupUserResult, error) {
	var rv LookupUserResult
	err := ctx.Invoke("azuread:index/getUser:getUser", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getUser.
type LookupUserArgs struct {
	// The email alias of the Azure AD User.
	MailNickname *string `pulumi:"mailNickname"`
	// Specifies the Object ID of the Application within Azure Active Directory.
	ObjectId *string `pulumi:"objectId"`
	// The User Principal Name of the Azure AD User.
	UserPrincipalName *string `pulumi:"userPrincipalName"`
}

// A collection of values returned by getUser.
type LookupUserResult struct {
	// `True` if the account is enabled; otherwise `False`.
	AccountEnabled bool `pulumi:"accountEnabled"`
	// The Display Name of the Azure AD User.
	DisplayName string `pulumi:"displayName"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The value used to associate an on-premises Active Directory user account with their Azure AD user object.
	ImmutableId string `pulumi:"immutableId"`
	// The primary email address of the Azure AD User.
	Mail string `pulumi:"mail"`
	// The email alias of the Azure AD User.
	MailNickname string `pulumi:"mailNickname"`
	ObjectId     string `pulumi:"objectId"`
	// The on premise sam account name of the Azure AD User.
	OnpremisesSamAccountName string `pulumi:"onpremisesSamAccountName"`
	// The on premise user principal name of the Azure AD User.
	OnpremisesUserPrincipalName string `pulumi:"onpremisesUserPrincipalName"`
	// The usage location of the Azure AD User.
	UsageLocation string `pulumi:"usageLocation"`
	// The User Principal Name of the Azure AD User.
	UserPrincipalName string `pulumi:"userPrincipalName"`
}
