// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Password associated with an Application within Azure Active Directory. Also can be referred to as Client secrets.
//
// > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"fmt"
//
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
// 		_, err = azuread.NewApplicationPassword(ctx, "exampleApplicationPassword", &azuread.ApplicationPasswordArgs{
// 			ApplicationObjectId: exampleApplication.ID(),
// 			Description:         pulumi.String("My managed password"),
// 			Value:               pulumi.String(fmt.Sprintf("%v%v%v", "VT=uSgbTanZhyz@", "%", "nL9Hpd+Tfay_MRV#")),
// 			EndDate:             pulumi.String("2099-01-01T01:02:03Z"),
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
// Passwords can be imported using the `object id` of an Application and the `key id` of the password, e.g.
//
// ```sh
//  $ pulumi import azuread:index/applicationPassword:ApplicationPassword test 00000000-0000-0000-0000-000000000000/password/11111111-1111-1111-1111-111111111111
// ```
type ApplicationPassword struct {
	pulumi.CustomResourceState

	// The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId pulumi.StringOutput `pulumi:"applicationObjectId"`
	// A description for the Password.
	Description pulumi.StringOutput `pulumi:"description"`
	// The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
	EndDate pulumi.StringOutput `pulumi:"endDate"`
	// A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
	EndDateRelative pulumi.StringPtrOutput `pulumi:"endDateRelative"`
	// A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
	KeyId pulumi.StringOutput `pulumi:"keyId"`
	// The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
	StartDate pulumi.StringOutput `pulumi:"startDate"`
	// The Password for this Application.
	Value pulumi.StringOutput `pulumi:"value"`
}

// NewApplicationPassword registers a new resource with the given unique name, arguments, and options.
func NewApplicationPassword(ctx *pulumi.Context,
	name string, args *ApplicationPasswordArgs, opts ...pulumi.ResourceOption) (*ApplicationPassword, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApplicationObjectId == nil {
		return nil, errors.New("invalid value for required argument 'ApplicationObjectId'")
	}
	if args.Value == nil {
		return nil, errors.New("invalid value for required argument 'Value'")
	}
	var resource ApplicationPassword
	err := ctx.RegisterResource("azuread:index/applicationPassword:ApplicationPassword", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetApplicationPassword gets an existing ApplicationPassword resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApplicationPassword(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ApplicationPasswordState, opts ...pulumi.ResourceOption) (*ApplicationPassword, error) {
	var resource ApplicationPassword
	err := ctx.ReadResource("azuread:index/applicationPassword:ApplicationPassword", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ApplicationPassword resources.
type applicationPasswordState struct {
	// The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId *string `pulumi:"applicationObjectId"`
	// A description for the Password.
	Description *string `pulumi:"description"`
	// The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
	EndDate *string `pulumi:"endDate"`
	// A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
	EndDateRelative *string `pulumi:"endDateRelative"`
	// A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
	KeyId *string `pulumi:"keyId"`
	// The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
	StartDate *string `pulumi:"startDate"`
	// The Password for this Application.
	Value *string `pulumi:"value"`
}

type ApplicationPasswordState struct {
	// The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId pulumi.StringPtrInput
	// A description for the Password.
	Description pulumi.StringPtrInput
	// The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
	EndDate pulumi.StringPtrInput
	// A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
	EndDateRelative pulumi.StringPtrInput
	// A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
	KeyId pulumi.StringPtrInput
	// The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
	StartDate pulumi.StringPtrInput
	// The Password for this Application.
	Value pulumi.StringPtrInput
}

func (ApplicationPasswordState) ElementType() reflect.Type {
	return reflect.TypeOf((*applicationPasswordState)(nil)).Elem()
}

type applicationPasswordArgs struct {
	// The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId string `pulumi:"applicationObjectId"`
	// A description for the Password.
	Description *string `pulumi:"description"`
	// The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
	EndDate *string `pulumi:"endDate"`
	// A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
	EndDateRelative *string `pulumi:"endDateRelative"`
	// A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
	KeyId *string `pulumi:"keyId"`
	// The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
	StartDate *string `pulumi:"startDate"`
	// The Password for this Application.
	Value string `pulumi:"value"`
}

// The set of arguments for constructing a ApplicationPassword resource.
type ApplicationPasswordArgs struct {
	// The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId pulumi.StringInput
	// A description for the Password.
	Description pulumi.StringPtrInput
	// The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
	EndDate pulumi.StringPtrInput
	// A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
	EndDateRelative pulumi.StringPtrInput
	// A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
	KeyId pulumi.StringPtrInput
	// The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
	StartDate pulumi.StringPtrInput
	// The Password for this Application.
	Value pulumi.StringInput
}

func (ApplicationPasswordArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*applicationPasswordArgs)(nil)).Elem()
}

type ApplicationPasswordInput interface {
	pulumi.Input

	ToApplicationPasswordOutput() ApplicationPasswordOutput
	ToApplicationPasswordOutputWithContext(ctx context.Context) ApplicationPasswordOutput
}

type ApplicationPasswordPtrInput interface {
	pulumi.Input

	ToApplicationPasswordPtrOutput() ApplicationPasswordPtrOutput
	ToApplicationPasswordPtrOutputWithContext(ctx context.Context) ApplicationPasswordPtrOutput
}

func (ApplicationPassword) ElementType() reflect.Type {
	return reflect.TypeOf((*ApplicationPassword)(nil)).Elem()
}

func (i ApplicationPassword) ToApplicationPasswordOutput() ApplicationPasswordOutput {
	return i.ToApplicationPasswordOutputWithContext(context.Background())
}

func (i ApplicationPassword) ToApplicationPasswordOutputWithContext(ctx context.Context) ApplicationPasswordOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ApplicationPasswordOutput)
}

func (i ApplicationPassword) ToApplicationPasswordPtrOutput() ApplicationPasswordPtrOutput {
	return i.ToApplicationPasswordPtrOutputWithContext(context.Background())
}

func (i ApplicationPassword) ToApplicationPasswordPtrOutputWithContext(ctx context.Context) ApplicationPasswordPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ApplicationPasswordPtrOutput)
}

type ApplicationPasswordOutput struct {
	*pulumi.OutputState
}

func (ApplicationPasswordOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ApplicationPasswordOutput)(nil)).Elem()
}

func (o ApplicationPasswordOutput) ToApplicationPasswordOutput() ApplicationPasswordOutput {
	return o
}

func (o ApplicationPasswordOutput) ToApplicationPasswordOutputWithContext(ctx context.Context) ApplicationPasswordOutput {
	return o
}

type ApplicationPasswordPtrOutput struct {
	*pulumi.OutputState
}

func (ApplicationPasswordPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ApplicationPassword)(nil)).Elem()
}

func (o ApplicationPasswordPtrOutput) ToApplicationPasswordPtrOutput() ApplicationPasswordPtrOutput {
	return o
}

func (o ApplicationPasswordPtrOutput) ToApplicationPasswordPtrOutputWithContext(ctx context.Context) ApplicationPasswordPtrOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ApplicationPasswordOutput{})
	pulumi.RegisterOutputType(ApplicationPasswordPtrOutput{})
}
