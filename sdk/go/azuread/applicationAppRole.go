// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages an App Role associated with an Application within Azure Active Directory.
//
// > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
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
// 		exampleApplication, err := azuread.NewApplication(ctx, "exampleApplication", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = azuread.NewApplicationAppRole(ctx, "exampleApplicationAppRole", &azuread.ApplicationAppRoleArgs{
// 			ApplicationObjectId: exampleApplication.ID(),
// 			AllowedMemberTypes: pulumi.StringArray{
// 				pulumi.String("User"),
// 			},
// 			Description: pulumi.String("Admins can manage roles and perform all task actions"),
// 			DisplayName: pulumi.String("Admin"),
// 			IsEnabled:   pulumi.Bool(true),
// 			Value:       pulumi.String("administer"),
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
// App Roles can be imported using the `object id` of an Application and the `id` of the App Role, e.g.
//
// ```sh
//  $ pulumi import azuread:index/applicationAppRole:ApplicationAppRole test 00000000-0000-0000-0000-000000000000/role/11111111-1111-1111-1111-111111111111
// ```
type ApplicationAppRole struct {
	pulumi.CustomResourceState

	// Specifies whether this app role definition can be assigned to users and groups by setting to `User`, or to other applications (that are accessing this application in daemon service scenarios) by setting to `Application`, or to both.
	AllowedMemberTypes pulumi.StringArrayOutput `pulumi:"allowedMemberTypes"`
	// The Object ID of the Application for which this App Role should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId pulumi.StringOutput `pulumi:"applicationObjectId"`
	// Permission help text that appears in the admin app assignment and consent experiences.
	Description pulumi.StringOutput `pulumi:"description"`
	// Display name for the permission that appears in the admin consent and app assignment experiences.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// Determines if the app role is enabled. Defaults to `true`.
	IsEnabled pulumi.BoolPtrOutput `pulumi:"isEnabled"`
	// Specifies a custom UUID for the app role. If omitted, a random UUID will be automatically generated. Changing this field forces a new resource to be created.
	RoleId pulumi.StringOutput `pulumi:"roleId"`
	// Specifies the value of the roles claim that the application should expect in the authentication and access tokens.
	Value pulumi.StringPtrOutput `pulumi:"value"`
}

// NewApplicationAppRole registers a new resource with the given unique name, arguments, and options.
func NewApplicationAppRole(ctx *pulumi.Context,
	name string, args *ApplicationAppRoleArgs, opts ...pulumi.ResourceOption) (*ApplicationAppRole, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AllowedMemberTypes == nil {
		return nil, errors.New("invalid value for required argument 'AllowedMemberTypes'")
	}
	if args.ApplicationObjectId == nil {
		return nil, errors.New("invalid value for required argument 'ApplicationObjectId'")
	}
	if args.Description == nil {
		return nil, errors.New("invalid value for required argument 'Description'")
	}
	if args.DisplayName == nil {
		return nil, errors.New("invalid value for required argument 'DisplayName'")
	}
	var resource ApplicationAppRole
	err := ctx.RegisterResource("azuread:index/applicationAppRole:ApplicationAppRole", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetApplicationAppRole gets an existing ApplicationAppRole resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApplicationAppRole(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ApplicationAppRoleState, opts ...pulumi.ResourceOption) (*ApplicationAppRole, error) {
	var resource ApplicationAppRole
	err := ctx.ReadResource("azuread:index/applicationAppRole:ApplicationAppRole", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ApplicationAppRole resources.
type applicationAppRoleState struct {
	// Specifies whether this app role definition can be assigned to users and groups by setting to `User`, or to other applications (that are accessing this application in daemon service scenarios) by setting to `Application`, or to both.
	AllowedMemberTypes []string `pulumi:"allowedMemberTypes"`
	// The Object ID of the Application for which this App Role should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId *string `pulumi:"applicationObjectId"`
	// Permission help text that appears in the admin app assignment and consent experiences.
	Description *string `pulumi:"description"`
	// Display name for the permission that appears in the admin consent and app assignment experiences.
	DisplayName *string `pulumi:"displayName"`
	// Determines if the app role is enabled. Defaults to `true`.
	IsEnabled *bool `pulumi:"isEnabled"`
	// Specifies a custom UUID for the app role. If omitted, a random UUID will be automatically generated. Changing this field forces a new resource to be created.
	RoleId *string `pulumi:"roleId"`
	// Specifies the value of the roles claim that the application should expect in the authentication and access tokens.
	Value *string `pulumi:"value"`
}

type ApplicationAppRoleState struct {
	// Specifies whether this app role definition can be assigned to users and groups by setting to `User`, or to other applications (that are accessing this application in daemon service scenarios) by setting to `Application`, or to both.
	AllowedMemberTypes pulumi.StringArrayInput
	// The Object ID of the Application for which this App Role should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId pulumi.StringPtrInput
	// Permission help text that appears in the admin app assignment and consent experiences.
	Description pulumi.StringPtrInput
	// Display name for the permission that appears in the admin consent and app assignment experiences.
	DisplayName pulumi.StringPtrInput
	// Determines if the app role is enabled. Defaults to `true`.
	IsEnabled pulumi.BoolPtrInput
	// Specifies a custom UUID for the app role. If omitted, a random UUID will be automatically generated. Changing this field forces a new resource to be created.
	RoleId pulumi.StringPtrInput
	// Specifies the value of the roles claim that the application should expect in the authentication and access tokens.
	Value pulumi.StringPtrInput
}

func (ApplicationAppRoleState) ElementType() reflect.Type {
	return reflect.TypeOf((*applicationAppRoleState)(nil)).Elem()
}

type applicationAppRoleArgs struct {
	// Specifies whether this app role definition can be assigned to users and groups by setting to `User`, or to other applications (that are accessing this application in daemon service scenarios) by setting to `Application`, or to both.
	AllowedMemberTypes []string `pulumi:"allowedMemberTypes"`
	// The Object ID of the Application for which this App Role should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId string `pulumi:"applicationObjectId"`
	// Permission help text that appears in the admin app assignment and consent experiences.
	Description string `pulumi:"description"`
	// Display name for the permission that appears in the admin consent and app assignment experiences.
	DisplayName string `pulumi:"displayName"`
	// Determines if the app role is enabled. Defaults to `true`.
	IsEnabled *bool `pulumi:"isEnabled"`
	// Specifies a custom UUID for the app role. If omitted, a random UUID will be automatically generated. Changing this field forces a new resource to be created.
	RoleId *string `pulumi:"roleId"`
	// Specifies the value of the roles claim that the application should expect in the authentication and access tokens.
	Value *string `pulumi:"value"`
}

// The set of arguments for constructing a ApplicationAppRole resource.
type ApplicationAppRoleArgs struct {
	// Specifies whether this app role definition can be assigned to users and groups by setting to `User`, or to other applications (that are accessing this application in daemon service scenarios) by setting to `Application`, or to both.
	AllowedMemberTypes pulumi.StringArrayInput
	// The Object ID of the Application for which this App Role should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId pulumi.StringInput
	// Permission help text that appears in the admin app assignment and consent experiences.
	Description pulumi.StringInput
	// Display name for the permission that appears in the admin consent and app assignment experiences.
	DisplayName pulumi.StringInput
	// Determines if the app role is enabled. Defaults to `true`.
	IsEnabled pulumi.BoolPtrInput
	// Specifies a custom UUID for the app role. If omitted, a random UUID will be automatically generated. Changing this field forces a new resource to be created.
	RoleId pulumi.StringPtrInput
	// Specifies the value of the roles claim that the application should expect in the authentication and access tokens.
	Value pulumi.StringPtrInput
}

func (ApplicationAppRoleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*applicationAppRoleArgs)(nil)).Elem()
}

type ApplicationAppRoleInput interface {
	pulumi.Input

	ToApplicationAppRoleOutput() ApplicationAppRoleOutput
	ToApplicationAppRoleOutputWithContext(ctx context.Context) ApplicationAppRoleOutput
}

func (*ApplicationAppRole) ElementType() reflect.Type {
	return reflect.TypeOf((*ApplicationAppRole)(nil))
}

func (i *ApplicationAppRole) ToApplicationAppRoleOutput() ApplicationAppRoleOutput {
	return i.ToApplicationAppRoleOutputWithContext(context.Background())
}

func (i *ApplicationAppRole) ToApplicationAppRoleOutputWithContext(ctx context.Context) ApplicationAppRoleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ApplicationAppRoleOutput)
}

type ApplicationAppRoleOutput struct {
	*pulumi.OutputState
}

func (ApplicationAppRoleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ApplicationAppRole)(nil))
}

func (o ApplicationAppRoleOutput) ToApplicationAppRoleOutput() ApplicationAppRoleOutput {
	return o
}

func (o ApplicationAppRoleOutput) ToApplicationAppRoleOutputWithContext(ctx context.Context) ApplicationAppRoleOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ApplicationAppRoleOutput{})
}
