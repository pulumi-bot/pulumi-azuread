// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Gets information about an Azure Active Directory user.
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
// 		opt0 := "user@hashicorp.com"
// 		_, err := azuread.LookupUser(ctx, &azuread.LookupUserArgs{
// 			UserPrincipalName: _opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
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
	// Specifies the Object ID of the User within Azure Active Directory.
	ObjectId *string `pulumi:"objectId"`
	// The User Principal Name of the Azure AD User.
	UserPrincipalName *string `pulumi:"userPrincipalName"`
}

// A collection of values returned by getUser.
type LookupUserResult struct {
	// `True` if the account is enabled; otherwise `False`.
	AccountEnabled bool `pulumi:"accountEnabled"`
	// The city in which the user is located.
	City string `pulumi:"city"`
	// The company name which the user is associated. This property can be useful for describing the company that an external user comes from.
	CompanyName string `pulumi:"companyName"`
	// The country/region in which the user is located; for example, “US” or “UK”.
	Country string `pulumi:"country"`
	// The name for the department in which the user works.
	Department string `pulumi:"department"`
	// The Display Name of the Azure AD User.
	DisplayName string `pulumi:"displayName"`
	// The given name (first name) of the user.
	GivenName string `pulumi:"givenName"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The value used to associate an on-premise Active Directory user account with their Azure AD user object.
	ImmutableId string `pulumi:"immutableId"`
	// The user’s job title.
	JobTitle string `pulumi:"jobTitle"`
	// The primary email address of the Azure AD User.
	Mail string `pulumi:"mail"`
	// The email alias of the Azure AD User.
	MailNickname string `pulumi:"mailNickname"`
	// The primary cellular telephone number for the user.
	Mobile   string `pulumi:"mobile"`
	ObjectId string `pulumi:"objectId"`
	// The on-premise SAM account name of the Azure AD User.
	OnpremisesSamAccountName string `pulumi:"onpremisesSamAccountName"`
	// The on-premise user principal name of the Azure AD User.
	OnpremisesUserPrincipalName string `pulumi:"onpremisesUserPrincipalName"`
	// The office location in the user's place of business.
	PhysicalDeliveryOfficeName string `pulumi:"physicalDeliveryOfficeName"`
	// The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code.
	PostalCode string `pulumi:"postalCode"`
	// The state or province in the user's address.
	State string `pulumi:"state"`
	// The street address of the user's place of business.
	StreetAddress string `pulumi:"streetAddress"`
	// The user's surname (family name or last name).
	Surname string `pulumi:"surname"`
	// The usage location of the Azure AD User.
	UsageLocation string `pulumi:"usageLocation"`
	// The User Principal Name of the Azure AD User.
	UserPrincipalName string `pulumi:"userPrincipalName"`
}
