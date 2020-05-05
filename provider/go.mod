module github.com/pulumi/pulumi-azuread/provider/v2

go 1.13

require (
	github.com/hashicorp/terraform-plugin-sdk v1.7.0
	github.com/pulumi/pulumi-terraform-bridge/v2 v2.2.0
	github.com/pulumi/pulumi/sdk/v2 v2.1.1-0.20200505193935-7b446d6c55ad
	github.com/terraform-providers/terraform-provider-azuread v0.8.0
)

replace (
	github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
	github.com/hashicorp/vault => github.com/hashicorp/vault v1.2.0
)

replace github.com/pulumi/pulumi-terraform-bridge/v2 => ../../pulumi-terraform-bridge
