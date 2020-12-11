// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a User within Azure Active Directory.
//
// > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Directory.ReadWrite.All` within the `Windows Azure Active Directory` API.
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
// 		_, err := azuread.NewUser(ctx, "example", &azuread.UserArgs{
// 			DisplayName:       pulumi.String("J. Doe"),
// 			MailNickname:      pulumi.String("jdoe"),
// 			Password:          pulumi.String("SecretP@sswd99!"),
// 			UserPrincipalName: pulumi.String("jdoe@hashicorp.com"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// Azure Active Directory Users can be imported using the `object id`, e.g.
//
// ```sh
//  $ pulumi import azuread:index/user:User my_user 00000000-0000-0000-0000-000000000000
// ```
type User struct {
	pulumi.CustomResourceState

	// `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
	AccountEnabled pulumi.BoolPtrOutput `pulumi:"accountEnabled"`
	// The city in which the user is located.
	City pulumi.StringOutput `pulumi:"city"`
	// The company name which the user is associated. This property can be useful for describing the company that an external user comes from.
	CompanyName pulumi.StringOutput `pulumi:"companyName"`
	// The country/region in which the user is located; for example, “US” or “UK”.
	Country pulumi.StringOutput `pulumi:"country"`
	// The name for the department in which the user works.
	Department pulumi.StringOutput `pulumi:"department"`
	// The name to display in the address book for the user.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
	ForcePasswordChange pulumi.BoolPtrOutput `pulumi:"forcePasswordChange"`
	// The given name (first name) of the user.
	GivenName pulumi.StringOutput `pulumi:"givenName"`
	// The value used to associate an on-premise Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
	ImmutableId pulumi.StringOutput `pulumi:"immutableId"`
	// The user’s job title.
	JobTitle pulumi.StringOutput `pulumi:"jobTitle"`
	// The primary email address of the Azure AD User.
	Mail pulumi.StringOutput `pulumi:"mail"`
	// The mail alias for the user. Defaults to the user name part of the User Principal Name.
	MailNickname pulumi.StringOutput `pulumi:"mailNickname"`
	// The primary cellular telephone number for the user.
	Mobile pulumi.StringOutput `pulumi:"mobile"`
	// The Object ID of the Azure AD User.
	ObjectId pulumi.StringOutput `pulumi:"objectId"`
	// The on-premise SAM account name of the Azure AD User.
	OnpremisesSamAccountName pulumi.StringOutput `pulumi:"onpremisesSamAccountName"`
	// The on-premise user principal name of the Azure AD User.
	OnpremisesUserPrincipalName pulumi.StringOutput `pulumi:"onpremisesUserPrincipalName"`
	// The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
	Password pulumi.StringOutput `pulumi:"password"`
	// The office location in the user's place of business.
	PhysicalDeliveryOfficeName pulumi.StringOutput `pulumi:"physicalDeliveryOfficeName"`
	// The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code.
	PostalCode pulumi.StringOutput `pulumi:"postalCode"`
	// The state or province in the user's address.
	State pulumi.StringOutput `pulumi:"state"`
	// The street address of the user's place of business.
	StreetAddress pulumi.StringOutput `pulumi:"streetAddress"`
	// The user's surname (family name or last name).
	Surname pulumi.StringOutput `pulumi:"surname"`
	// The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set.
	UsageLocation pulumi.StringOutput `pulumi:"usageLocation"`
	// The User Principal Name of the Azure AD User.
	UserPrincipalName pulumi.StringOutput `pulumi:"userPrincipalName"`
}

// NewUser registers a new resource with the given unique name, arguments, and options.
func NewUser(ctx *pulumi.Context,
	name string, args *UserArgs, opts ...pulumi.ResourceOption) (*User, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DisplayName == nil {
		return nil, errors.New("invalid value for required argument 'DisplayName'")
	}
	if args.Password == nil {
		return nil, errors.New("invalid value for required argument 'Password'")
	}
	if args.UserPrincipalName == nil {
		return nil, errors.New("invalid value for required argument 'UserPrincipalName'")
	}
	var resource User
	err := ctx.RegisterResource("azuread:index/user:User", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUser gets an existing User resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUser(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserState, opts ...pulumi.ResourceOption) (*User, error) {
	var resource User
	err := ctx.ReadResource("azuread:index/user:User", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering User resources.
type userState struct {
	// `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
	AccountEnabled *bool `pulumi:"accountEnabled"`
	// The city in which the user is located.
	City *string `pulumi:"city"`
	// The company name which the user is associated. This property can be useful for describing the company that an external user comes from.
	CompanyName *string `pulumi:"companyName"`
	// The country/region in which the user is located; for example, “US” or “UK”.
	Country *string `pulumi:"country"`
	// The name for the department in which the user works.
	Department *string `pulumi:"department"`
	// The name to display in the address book for the user.
	DisplayName *string `pulumi:"displayName"`
	// `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
	ForcePasswordChange *bool `pulumi:"forcePasswordChange"`
	// The given name (first name) of the user.
	GivenName *string `pulumi:"givenName"`
	// The value used to associate an on-premise Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
	ImmutableId *string `pulumi:"immutableId"`
	// The user’s job title.
	JobTitle *string `pulumi:"jobTitle"`
	// The primary email address of the Azure AD User.
	Mail *string `pulumi:"mail"`
	// The mail alias for the user. Defaults to the user name part of the User Principal Name.
	MailNickname *string `pulumi:"mailNickname"`
	// The primary cellular telephone number for the user.
	Mobile *string `pulumi:"mobile"`
	// The Object ID of the Azure AD User.
	ObjectId *string `pulumi:"objectId"`
	// The on-premise SAM account name of the Azure AD User.
	OnpremisesSamAccountName *string `pulumi:"onpremisesSamAccountName"`
	// The on-premise user principal name of the Azure AD User.
	OnpremisesUserPrincipalName *string `pulumi:"onpremisesUserPrincipalName"`
	// The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
	Password *string `pulumi:"password"`
	// The office location in the user's place of business.
	PhysicalDeliveryOfficeName *string `pulumi:"physicalDeliveryOfficeName"`
	// The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code.
	PostalCode *string `pulumi:"postalCode"`
	// The state or province in the user's address.
	State *string `pulumi:"state"`
	// The street address of the user's place of business.
	StreetAddress *string `pulumi:"streetAddress"`
	// The user's surname (family name or last name).
	Surname *string `pulumi:"surname"`
	// The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set.
	UsageLocation *string `pulumi:"usageLocation"`
	// The User Principal Name of the Azure AD User.
	UserPrincipalName *string `pulumi:"userPrincipalName"`
}

type UserState struct {
	// `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
	AccountEnabled pulumi.BoolPtrInput
	// The city in which the user is located.
	City pulumi.StringPtrInput
	// The company name which the user is associated. This property can be useful for describing the company that an external user comes from.
	CompanyName pulumi.StringPtrInput
	// The country/region in which the user is located; for example, “US” or “UK”.
	Country pulumi.StringPtrInput
	// The name for the department in which the user works.
	Department pulumi.StringPtrInput
	// The name to display in the address book for the user.
	DisplayName pulumi.StringPtrInput
	// `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
	ForcePasswordChange pulumi.BoolPtrInput
	// The given name (first name) of the user.
	GivenName pulumi.StringPtrInput
	// The value used to associate an on-premise Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
	ImmutableId pulumi.StringPtrInput
	// The user’s job title.
	JobTitle pulumi.StringPtrInput
	// The primary email address of the Azure AD User.
	Mail pulumi.StringPtrInput
	// The mail alias for the user. Defaults to the user name part of the User Principal Name.
	MailNickname pulumi.StringPtrInput
	// The primary cellular telephone number for the user.
	Mobile pulumi.StringPtrInput
	// The Object ID of the Azure AD User.
	ObjectId pulumi.StringPtrInput
	// The on-premise SAM account name of the Azure AD User.
	OnpremisesSamAccountName pulumi.StringPtrInput
	// The on-premise user principal name of the Azure AD User.
	OnpremisesUserPrincipalName pulumi.StringPtrInput
	// The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
	Password pulumi.StringPtrInput
	// The office location in the user's place of business.
	PhysicalDeliveryOfficeName pulumi.StringPtrInput
	// The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code.
	PostalCode pulumi.StringPtrInput
	// The state or province in the user's address.
	State pulumi.StringPtrInput
	// The street address of the user's place of business.
	StreetAddress pulumi.StringPtrInput
	// The user's surname (family name or last name).
	Surname pulumi.StringPtrInput
	// The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set.
	UsageLocation pulumi.StringPtrInput
	// The User Principal Name of the Azure AD User.
	UserPrincipalName pulumi.StringPtrInput
}

func (UserState) ElementType() reflect.Type {
	return reflect.TypeOf((*userState)(nil)).Elem()
}

type userArgs struct {
	// `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
	AccountEnabled *bool `pulumi:"accountEnabled"`
	// The city in which the user is located.
	City *string `pulumi:"city"`
	// The company name which the user is associated. This property can be useful for describing the company that an external user comes from.
	CompanyName *string `pulumi:"companyName"`
	// The country/region in which the user is located; for example, “US” or “UK”.
	Country *string `pulumi:"country"`
	// The name for the department in which the user works.
	Department *string `pulumi:"department"`
	// The name to display in the address book for the user.
	DisplayName string `pulumi:"displayName"`
	// `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
	ForcePasswordChange *bool `pulumi:"forcePasswordChange"`
	// The given name (first name) of the user.
	GivenName *string `pulumi:"givenName"`
	// The value used to associate an on-premise Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
	ImmutableId *string `pulumi:"immutableId"`
	// The user’s job title.
	JobTitle *string `pulumi:"jobTitle"`
	// The mail alias for the user. Defaults to the user name part of the User Principal Name.
	MailNickname *string `pulumi:"mailNickname"`
	// The primary cellular telephone number for the user.
	Mobile *string `pulumi:"mobile"`
	// The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
	Password string `pulumi:"password"`
	// The office location in the user's place of business.
	PhysicalDeliveryOfficeName *string `pulumi:"physicalDeliveryOfficeName"`
	// The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code.
	PostalCode *string `pulumi:"postalCode"`
	// The state or province in the user's address.
	State *string `pulumi:"state"`
	// The street address of the user's place of business.
	StreetAddress *string `pulumi:"streetAddress"`
	// The user's surname (family name or last name).
	Surname *string `pulumi:"surname"`
	// The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set.
	UsageLocation *string `pulumi:"usageLocation"`
	// The User Principal Name of the Azure AD User.
	UserPrincipalName string `pulumi:"userPrincipalName"`
}

// The set of arguments for constructing a User resource.
type UserArgs struct {
	// `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
	AccountEnabled pulumi.BoolPtrInput
	// The city in which the user is located.
	City pulumi.StringPtrInput
	// The company name which the user is associated. This property can be useful for describing the company that an external user comes from.
	CompanyName pulumi.StringPtrInput
	// The country/region in which the user is located; for example, “US” or “UK”.
	Country pulumi.StringPtrInput
	// The name for the department in which the user works.
	Department pulumi.StringPtrInput
	// The name to display in the address book for the user.
	DisplayName pulumi.StringInput
	// `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
	ForcePasswordChange pulumi.BoolPtrInput
	// The given name (first name) of the user.
	GivenName pulumi.StringPtrInput
	// The value used to associate an on-premise Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
	ImmutableId pulumi.StringPtrInput
	// The user’s job title.
	JobTitle pulumi.StringPtrInput
	// The mail alias for the user. Defaults to the user name part of the User Principal Name.
	MailNickname pulumi.StringPtrInput
	// The primary cellular telephone number for the user.
	Mobile pulumi.StringPtrInput
	// The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
	Password pulumi.StringInput
	// The office location in the user's place of business.
	PhysicalDeliveryOfficeName pulumi.StringPtrInput
	// The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code.
	PostalCode pulumi.StringPtrInput
	// The state or province in the user's address.
	State pulumi.StringPtrInput
	// The street address of the user's place of business.
	StreetAddress pulumi.StringPtrInput
	// The user's surname (family name or last name).
	Surname pulumi.StringPtrInput
	// The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set.
	UsageLocation pulumi.StringPtrInput
	// The User Principal Name of the Azure AD User.
	UserPrincipalName pulumi.StringInput
}

func (UserArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userArgs)(nil)).Elem()
}

type UserInput interface {
	pulumi.Input

	ToUserOutput() UserOutput
	ToUserOutputWithContext(ctx context.Context) UserOutput
}

type UserPtrInput interface {
	pulumi.Input

	ToUserPtrOutput() UserPtrOutput
	ToUserPtrOutputWithContext(ctx context.Context) UserPtrOutput
}

func (User) ElementType() reflect.Type {
	return reflect.TypeOf((*User)(nil)).Elem()
}

func (i User) ToUserOutput() UserOutput {
	return i.ToUserOutputWithContext(context.Background())
}

func (i User) ToUserOutputWithContext(ctx context.Context) UserOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserOutput)
}

func (i User) ToUserPtrOutput() UserPtrOutput {
	return i.ToUserPtrOutputWithContext(context.Background())
}

func (i User) ToUserPtrOutputWithContext(ctx context.Context) UserPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserPtrOutput)
}

type UserOutput struct {
	*pulumi.OutputState
}

func (UserOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*UserOutput)(nil)).Elem()
}

func (o UserOutput) ToUserOutput() UserOutput {
	return o
}

func (o UserOutput) ToUserOutputWithContext(ctx context.Context) UserOutput {
	return o
}

type UserPtrOutput struct {
	*pulumi.OutputState
}

func (UserPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**User)(nil)).Elem()
}

func (o UserPtrOutput) ToUserPtrOutput() UserPtrOutput {
	return o
}

func (o UserPtrOutput) ToUserPtrOutputWithContext(ctx context.Context) UserPtrOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(UserOutput{})
	pulumi.RegisterOutputType(UserPtrOutput{})
}
