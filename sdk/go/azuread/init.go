// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuread

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "azuread:index/application:Application":
		r, err = NewApplication(ctx, name, nil, pulumi.URN_(urn))
	case "azuread:index/applicationAppRole:ApplicationAppRole":
		r, err = NewApplicationAppRole(ctx, name, nil, pulumi.URN_(urn))
	case "azuread:index/applicationCertificate:ApplicationCertificate":
		r, err = NewApplicationCertificate(ctx, name, nil, pulumi.URN_(urn))
	case "azuread:index/applicationOAuth2Permission:ApplicationOAuth2Permission":
		r, err = NewApplicationOAuth2Permission(ctx, name, nil, pulumi.URN_(urn))
	case "azuread:index/applicationPassword:ApplicationPassword":
		r, err = NewApplicationPassword(ctx, name, nil, pulumi.URN_(urn))
	case "azuread:index/group:Group":
		r, err = NewGroup(ctx, name, nil, pulumi.URN_(urn))
	case "azuread:index/groupMember:GroupMember":
		r, err = NewGroupMember(ctx, name, nil, pulumi.URN_(urn))
	case "azuread:index/servicePrincipal:ServicePrincipal":
		r, err = NewServicePrincipal(ctx, name, nil, pulumi.URN_(urn))
	case "azuread:index/servicePrincipalCertificate:ServicePrincipalCertificate":
		r, err = NewServicePrincipalCertificate(ctx, name, nil, pulumi.URN_(urn))
	case "azuread:index/servicePrincipalPassword:ServicePrincipalPassword":
		r, err = NewServicePrincipalPassword(ctx, name, nil, pulumi.URN_(urn))
	case "azuread:index/user:User":
		r, err = NewUser(ctx, name, nil, pulumi.URN_(urn))
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:azuread" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	return NewProvider(ctx, name, nil, pulumi.URN_(urn))
}

func init() {
	version, err := PkgVersion()
	if err != nil {
		fmt.Println("failed to determine package version. defaulting to v1: %v", err)
	}
	pulumi.RegisterResourceModule(
		"azuread",
		"index/application",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azuread",
		"index/applicationAppRole",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azuread",
		"index/applicationCertificate",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azuread",
		"index/applicationOAuth2Permission",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azuread",
		"index/applicationPassword",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azuread",
		"index/group",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azuread",
		"index/groupMember",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azuread",
		"index/servicePrincipal",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azuread",
		"index/servicePrincipalCertificate",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azuread",
		"index/servicePrincipalPassword",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azuread",
		"index/user",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"azuread",
		&pkg{version},
	)
}