// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
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
// 	"github.com/pulumi/pulumi-azuread/sdk/v2/go/azuread"
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
// Azure Active Directory Users can be imported using the `object id`, e.g. shell
type User struct {
	pulumi.CustomResourceState

	// `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
	AccountEnabled pulumi.BoolPtrOutput `pulumi:"accountEnabled"`
	// The name to display in the address book for the user.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
	ForcePasswordChange pulumi.BoolPtrOutput `pulumi:"forcePasswordChange"`
	// The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
	ImmutableId pulumi.StringOutput `pulumi:"immutableId"`
	// The primary email address of the Azure AD User.
	Mail pulumi.StringOutput `pulumi:"mail"`
	// The mail alias for the user. Defaults to the user name part of the User Principal Name.
	MailNickname pulumi.StringOutput `pulumi:"mailNickname"`
	// The Object ID of the Azure AD User.
	ObjectId pulumi.StringOutput `pulumi:"objectId"`
	// The on premise sam account name of the Azure AD User.
	OnpremisesSamAccountName pulumi.StringOutput `pulumi:"onpremisesSamAccountName"`
	// The on premise user principal name of the Azure AD User.
	OnpremisesUserPrincipalName pulumi.StringOutput `pulumi:"onpremisesUserPrincipalName"`
	// The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
	Password pulumi.StringOutput `pulumi:"password"`
	// The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set.
	UsageLocation pulumi.StringOutput `pulumi:"usageLocation"`
	// The User Principal Name of the Azure AD User.
	UserPrincipalName pulumi.StringOutput `pulumi:"userPrincipalName"`
}

// NewUser registers a new resource with the given unique name, arguments, and options.
func NewUser(ctx *pulumi.Context,
	name string, args *UserArgs, opts ...pulumi.ResourceOption) (*User, error) {
	if args == nil || args.DisplayName == nil {
		return nil, errors.New("missing required argument 'DisplayName'")
	}
	if args == nil || args.Password == nil {
		return nil, errors.New("missing required argument 'Password'")
	}
	if args == nil || args.UserPrincipalName == nil {
		return nil, errors.New("missing required argument 'UserPrincipalName'")
	}
	if args == nil {
		args = &UserArgs{}
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
	// The name to display in the address book for the user.
	DisplayName *string `pulumi:"displayName"`
	// `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
	ForcePasswordChange *bool `pulumi:"forcePasswordChange"`
	// The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
	ImmutableId *string `pulumi:"immutableId"`
	// The primary email address of the Azure AD User.
	Mail *string `pulumi:"mail"`
	// The mail alias for the user. Defaults to the user name part of the User Principal Name.
	MailNickname *string `pulumi:"mailNickname"`
	// The Object ID of the Azure AD User.
	ObjectId *string `pulumi:"objectId"`
	// The on premise sam account name of the Azure AD User.
	OnpremisesSamAccountName *string `pulumi:"onpremisesSamAccountName"`
	// The on premise user principal name of the Azure AD User.
	OnpremisesUserPrincipalName *string `pulumi:"onpremisesUserPrincipalName"`
	// The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
	Password *string `pulumi:"password"`
	// The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set.
	UsageLocation *string `pulumi:"usageLocation"`
	// The User Principal Name of the Azure AD User.
	UserPrincipalName *string `pulumi:"userPrincipalName"`
}

type UserState struct {
	// `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
	AccountEnabled pulumi.BoolPtrInput
	// The name to display in the address book for the user.
	DisplayName pulumi.StringPtrInput
	// `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
	ForcePasswordChange pulumi.BoolPtrInput
	// The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
	ImmutableId pulumi.StringPtrInput
	// The primary email address of the Azure AD User.
	Mail pulumi.StringPtrInput
	// The mail alias for the user. Defaults to the user name part of the User Principal Name.
	MailNickname pulumi.StringPtrInput
	// The Object ID of the Azure AD User.
	ObjectId pulumi.StringPtrInput
	// The on premise sam account name of the Azure AD User.
	OnpremisesSamAccountName pulumi.StringPtrInput
	// The on premise user principal name of the Azure AD User.
	OnpremisesUserPrincipalName pulumi.StringPtrInput
	// The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
	Password pulumi.StringPtrInput
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
	// The name to display in the address book for the user.
	DisplayName string `pulumi:"displayName"`
	// `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
	ForcePasswordChange *bool `pulumi:"forcePasswordChange"`
	// The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
	ImmutableId *string `pulumi:"immutableId"`
	// The mail alias for the user. Defaults to the user name part of the User Principal Name.
	MailNickname *string `pulumi:"mailNickname"`
	// The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
	Password string `pulumi:"password"`
	// The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set.
	UsageLocation *string `pulumi:"usageLocation"`
	// The User Principal Name of the Azure AD User.
	UserPrincipalName string `pulumi:"userPrincipalName"`
}

// The set of arguments for constructing a User resource.
type UserArgs struct {
	// `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
	AccountEnabled pulumi.BoolPtrInput
	// The name to display in the address book for the user.
	DisplayName pulumi.StringInput
	// `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
	ForcePasswordChange pulumi.BoolPtrInput
	// The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
	ImmutableId pulumi.StringPtrInput
	// The mail alias for the user. Defaults to the user name part of the User Principal Name.
	MailNickname pulumi.StringPtrInput
	// The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
	Password pulumi.StringInput
	// The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set.
	UsageLocation pulumi.StringPtrInput
	// The User Principal Name of the Azure AD User.
	UserPrincipalName pulumi.StringInput
}

func (UserArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userArgs)(nil)).Elem()
}
