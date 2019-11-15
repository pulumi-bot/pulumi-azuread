// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a User within Azure Active Directory.
// 
// > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Directory.ReadWrite.All` within the `Windows Azure Active Directory` API.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/user.html.markdown.
type User struct {
	s *pulumi.ResourceState
}

// NewUser registers a new resource with the given unique name, arguments, and options.
func NewUser(ctx *pulumi.Context,
	name string, args *UserArgs, opts ...pulumi.ResourceOpt) (*User, error) {
	if args == nil || args.DisplayName == nil {
		return nil, errors.New("missing required argument 'DisplayName'")
	}
	if args == nil || args.Password == nil {
		return nil, errors.New("missing required argument 'Password'")
	}
	if args == nil || args.UserPrincipalName == nil {
		return nil, errors.New("missing required argument 'UserPrincipalName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["accountEnabled"] = nil
		inputs["displayName"] = nil
		inputs["forcePasswordChange"] = nil
		inputs["mailNickname"] = nil
		inputs["password"] = nil
		inputs["usageLocation"] = nil
		inputs["userPrincipalName"] = nil
	} else {
		inputs["accountEnabled"] = args.AccountEnabled
		inputs["displayName"] = args.DisplayName
		inputs["forcePasswordChange"] = args.ForcePasswordChange
		inputs["mailNickname"] = args.MailNickname
		inputs["password"] = args.Password
		inputs["usageLocation"] = args.UsageLocation
		inputs["userPrincipalName"] = args.UserPrincipalName
	}
	inputs["mail"] = nil
	inputs["objectId"] = nil
	s, err := ctx.RegisterResource("azuread:index/user:User", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &User{s: s}, nil
}

// GetUser gets an existing User resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUser(ctx *pulumi.Context,
	name string, id pulumi.ID, state *UserState, opts ...pulumi.ResourceOpt) (*User, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["accountEnabled"] = state.AccountEnabled
		inputs["displayName"] = state.DisplayName
		inputs["forcePasswordChange"] = state.ForcePasswordChange
		inputs["mail"] = state.Mail
		inputs["mailNickname"] = state.MailNickname
		inputs["objectId"] = state.ObjectId
		inputs["password"] = state.Password
		inputs["usageLocation"] = state.UsageLocation
		inputs["userPrincipalName"] = state.UserPrincipalName
	}
	s, err := ctx.ReadResource("azuread:index/user:User", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &User{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *User) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *User) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
// * `mailNickname`- (Optional) The mail alias for the user. Defaults to the user name part of the User Principal Name.
func (r *User) AccountEnabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["accountEnabled"])
}

// The name to display in the address book for the user.
func (r *User) DisplayName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["displayName"])
}

// `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
func (r *User) ForcePasswordChange() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["forcePasswordChange"])
}

// The primary email address of the Azure AD User.
func (r *User) Mail() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["mail"])
}

func (r *User) MailNickname() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["mailNickname"])
}

// The Object ID of the Azure AD User.
func (r *User) ObjectId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["objectId"])
}

// The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
func (r *User) Password() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["password"])
}

// The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set. 
func (r *User) UsageLocation() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["usageLocation"])
}

// The User Principal Name of the Azure AD User.
func (r *User) UserPrincipalName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["userPrincipalName"])
}

// Input properties used for looking up and filtering User resources.
type UserState struct {
	// `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
	// * `mailNickname`- (Optional) The mail alias for the user. Defaults to the user name part of the User Principal Name.
	AccountEnabled interface{}
	// The name to display in the address book for the user.
	DisplayName interface{}
	// `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
	ForcePasswordChange interface{}
	// The primary email address of the Azure AD User.
	Mail interface{}
	MailNickname interface{}
	// The Object ID of the Azure AD User.
	ObjectId interface{}
	// The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
	Password interface{}
	// The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set. 
	UsageLocation interface{}
	// The User Principal Name of the Azure AD User.
	UserPrincipalName interface{}
}

// The set of arguments for constructing a User resource.
type UserArgs struct {
	// `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
	// * `mailNickname`- (Optional) The mail alias for the user. Defaults to the user name part of the User Principal Name.
	AccountEnabled interface{}
	// The name to display in the address book for the user.
	DisplayName interface{}
	// `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
	ForcePasswordChange interface{}
	MailNickname interface{}
	// The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
	Password interface{}
	// The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set. 
	UsageLocation interface{}
	// The User Principal Name of the Azure AD User.
	UserPrincipalName interface{}
}
