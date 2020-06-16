// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Certificate associated with an Application within Azure Active Directory.
//
// > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
//
// {{% examples %}}
// {{% /examples %}}
type ApplicationCertificate struct {
	pulumi.CustomResourceState

	// The Object ID of the Application for which this Certificate should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId pulumi.StringOutput `pulumi:"applicationObjectId"`
	// The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
	EndDate pulumi.StringOutput `pulumi:"endDate"`
	// A relative duration for which the Certificate is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
	EndDateRelative pulumi.StringPtrOutput `pulumi:"endDateRelative"`
	// A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.
	KeyId pulumi.StringOutput `pulumi:"keyId"`
	// The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
	StartDate pulumi.StringOutput `pulumi:"startDate"`
	// The type of key/certificate. Must be one of `AsymmetricX509Cert` or `Symmetric`. Changing this fields forces a new resource to be created.
	Type pulumi.StringPtrOutput `pulumi:"type"`
	// The Certificate for this Service Principal.
	Value pulumi.StringOutput `pulumi:"value"`
}

// NewApplicationCertificate registers a new resource with the given unique name, arguments, and options.
func NewApplicationCertificate(ctx *pulumi.Context,
	name string, args *ApplicationCertificateArgs, opts ...pulumi.ResourceOption) (*ApplicationCertificate, error) {
	if args == nil || args.ApplicationObjectId == nil {
		return nil, errors.New("missing required argument 'ApplicationObjectId'")
	}
	if args == nil || args.Value == nil {
		return nil, errors.New("missing required argument 'Value'")
	}
	if args == nil {
		args = &ApplicationCertificateArgs{}
	}
	var resource ApplicationCertificate
	err := ctx.RegisterResource("azuread:index/applicationCertificate:ApplicationCertificate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetApplicationCertificate gets an existing ApplicationCertificate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApplicationCertificate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ApplicationCertificateState, opts ...pulumi.ResourceOption) (*ApplicationCertificate, error) {
	var resource ApplicationCertificate
	err := ctx.ReadResource("azuread:index/applicationCertificate:ApplicationCertificate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ApplicationCertificate resources.
type applicationCertificateState struct {
	// The Object ID of the Application for which this Certificate should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId *string `pulumi:"applicationObjectId"`
	// The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
	EndDate *string `pulumi:"endDate"`
	// A relative duration for which the Certificate is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
	EndDateRelative *string `pulumi:"endDateRelative"`
	// A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.
	KeyId *string `pulumi:"keyId"`
	// The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
	StartDate *string `pulumi:"startDate"`
	// The type of key/certificate. Must be one of `AsymmetricX509Cert` or `Symmetric`. Changing this fields forces a new resource to be created.
	Type *string `pulumi:"type"`
	// The Certificate for this Service Principal.
	Value *string `pulumi:"value"`
}

type ApplicationCertificateState struct {
	// The Object ID of the Application for which this Certificate should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId pulumi.StringPtrInput
	// The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
	EndDate pulumi.StringPtrInput
	// A relative duration for which the Certificate is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
	EndDateRelative pulumi.StringPtrInput
	// A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.
	KeyId pulumi.StringPtrInput
	// The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
	StartDate pulumi.StringPtrInput
	// The type of key/certificate. Must be one of `AsymmetricX509Cert` or `Symmetric`. Changing this fields forces a new resource to be created.
	Type pulumi.StringPtrInput
	// The Certificate for this Service Principal.
	Value pulumi.StringPtrInput
}

func (ApplicationCertificateState) ElementType() reflect.Type {
	return reflect.TypeOf((*applicationCertificateState)(nil)).Elem()
}

type applicationCertificateArgs struct {
	// The Object ID of the Application for which this Certificate should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId string `pulumi:"applicationObjectId"`
	// The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
	EndDate *string `pulumi:"endDate"`
	// A relative duration for which the Certificate is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
	EndDateRelative *string `pulumi:"endDateRelative"`
	// A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.
	KeyId *string `pulumi:"keyId"`
	// The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
	StartDate *string `pulumi:"startDate"`
	// The type of key/certificate. Must be one of `AsymmetricX509Cert` or `Symmetric`. Changing this fields forces a new resource to be created.
	Type *string `pulumi:"type"`
	// The Certificate for this Service Principal.
	Value string `pulumi:"value"`
}

// The set of arguments for constructing a ApplicationCertificate resource.
type ApplicationCertificateArgs struct {
	// The Object ID of the Application for which this Certificate should be created. Changing this field forces a new resource to be created.
	ApplicationObjectId pulumi.StringInput
	// The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
	EndDate pulumi.StringPtrInput
	// A relative duration for which the Certificate is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
	EndDateRelative pulumi.StringPtrInput
	// A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.
	KeyId pulumi.StringPtrInput
	// The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
	StartDate pulumi.StringPtrInput
	// The type of key/certificate. Must be one of `AsymmetricX509Cert` or `Symmetric`. Changing this fields forces a new resource to be created.
	Type pulumi.StringPtrInput
	// The Certificate for this Service Principal.
	Value pulumi.StringInput
}

func (ApplicationCertificateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*applicationCertificateArgs)(nil)).Elem()
}
