// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access the configuration of the AzureRM provider.
//
// {{% examples %}}
// {{% /examples %}}
func GetClientConfig(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetClientConfigResult, error) {
	var rv GetClientConfigResult
	err := ctx.Invoke("azuread:index/getClientConfig:getClientConfig", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getClientConfig.
type GetClientConfigResult struct {
	ClientId string `pulumi:"clientId"`
	// The provider-assigned unique ID for this managed resource.
	Id             string `pulumi:"id"`
	ObjectId       string `pulumi:"objectId"`
	SubscriptionId string `pulumi:"subscriptionId"`
	TenantId       string `pulumi:"tenantId"`
}
