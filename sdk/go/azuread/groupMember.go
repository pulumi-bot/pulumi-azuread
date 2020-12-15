// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a single Group Membership within Azure Active Directory.
//
// > **NOTE:** Do not use this resource at the same time as `azuread_group.members`.
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
// 		opt0 := "jdoe@hashicorp.com"
// 		exampleUser, err := azuread.LookupUser(ctx, &azuread.LookupUserArgs{
// 			UserPrincipalName: _opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		exampleGroup, err := azuread.NewGroup(ctx, "exampleGroup", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = azuread.NewGroupMember(ctx, "exampleGroupMember", &azuread.GroupMemberArgs{
// 			GroupObjectId:  exampleGroup.ID(),
// 			MemberObjectId: pulumi.String(exampleUser.Id),
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
// Azure Active Directory Group Members can be imported using the `object id`, e.g.
//
// ```sh
//  $ pulumi import azuread:index/groupMember:GroupMember test 00000000-0000-0000-0000-000000000000/member/11111111-1111-1111-1111-111111111111
// ```
type GroupMember struct {
	pulumi.CustomResourceState

	// The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
	GroupObjectId pulumi.StringOutput `pulumi:"groupObjectId"`
	// The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.
	MemberObjectId pulumi.StringOutput `pulumi:"memberObjectId"`
}

// NewGroupMember registers a new resource with the given unique name, arguments, and options.
func NewGroupMember(ctx *pulumi.Context,
	name string, args *GroupMemberArgs, opts ...pulumi.ResourceOption) (*GroupMember, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.GroupObjectId == nil {
		return nil, errors.New("invalid value for required argument 'GroupObjectId'")
	}
	if args.MemberObjectId == nil {
		return nil, errors.New("invalid value for required argument 'MemberObjectId'")
	}
	var resource GroupMember
	err := ctx.RegisterResource("azuread:index/groupMember:GroupMember", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGroupMember gets an existing GroupMember resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGroupMember(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GroupMemberState, opts ...pulumi.ResourceOption) (*GroupMember, error) {
	var resource GroupMember
	err := ctx.ReadResource("azuread:index/groupMember:GroupMember", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GroupMember resources.
type groupMemberState struct {
	// The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
	GroupObjectId *string `pulumi:"groupObjectId"`
	// The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.
	MemberObjectId *string `pulumi:"memberObjectId"`
}

type GroupMemberState struct {
	// The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
	GroupObjectId pulumi.StringPtrInput
	// The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.
	MemberObjectId pulumi.StringPtrInput
}

func (GroupMemberState) ElementType() reflect.Type {
	return reflect.TypeOf((*groupMemberState)(nil)).Elem()
}

type groupMemberArgs struct {
	// The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
	GroupObjectId string `pulumi:"groupObjectId"`
	// The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.
	MemberObjectId string `pulumi:"memberObjectId"`
}

// The set of arguments for constructing a GroupMember resource.
type GroupMemberArgs struct {
	// The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
	GroupObjectId pulumi.StringInput
	// The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.
	MemberObjectId pulumi.StringInput
}

func (GroupMemberArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*groupMemberArgs)(nil)).Elem()
}

type GroupMemberInput interface {
	pulumi.Input

	ToGroupMemberOutput() GroupMemberOutput
	ToGroupMemberOutputWithContext(ctx context.Context) GroupMemberOutput
}

func (*GroupMember) ElementType() reflect.Type {
	return reflect.TypeOf((*GroupMember)(nil))
}

func (i *GroupMember) ToGroupMemberOutput() GroupMemberOutput {
	return i.ToGroupMemberOutputWithContext(context.Background())
}

func (i *GroupMember) ToGroupMemberOutputWithContext(ctx context.Context) GroupMemberOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupMemberOutput)
}

type GroupMemberOutput struct {
	*pulumi.OutputState
}

func (GroupMemberOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GroupMember)(nil))
}

func (o GroupMemberOutput) ToGroupMemberOutput() GroupMemberOutput {
	return o
}

func (o GroupMemberOutput) ToGroupMemberOutputWithContext(ctx context.Context) GroupMemberOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(GroupMemberOutput{})
}
