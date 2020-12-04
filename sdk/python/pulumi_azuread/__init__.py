# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .application import *
from .application_certificate import *
from .application_password import *
from .get_application import *
from .get_client_config import *
from .get_domains import *
from .get_group import *
from .get_groups import *
from .get_service_principal import *
from .get_user import *
from .get_users import *
from .group import *
from .group_member import *
from .provider import *
from .service_principal import *
from .service_principal_certificate import *
from .service_principal_password import *
from .user import *
from ._inputs import *
from . import outputs

# Make subpackages available:
from . import (
    config,
)

def _register_module():
    import pulumi
    from . import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azuread:index/application:Application":
                return Application(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azuread:index/applicationCertificate:ApplicationCertificate":
                return ApplicationCertificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azuread:index/applicationPassword:ApplicationPassword":
                return ApplicationPassword(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azuread:index/group:Group":
                return Group(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azuread:index/groupMember:GroupMember":
                return GroupMember(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azuread:index/servicePrincipal:ServicePrincipal":
                return ServicePrincipal(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azuread:index/servicePrincipalCertificate:ServicePrincipalCertificate":
                return ServicePrincipalCertificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azuread:index/servicePrincipalPassword:ServicePrincipalPassword":
                return ServicePrincipalPassword(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azuread:index/user:User":
                return User(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azuread", "index/application", _module_instance)
    pulumi.runtime.register_resource_module("azuread", "index/applicationCertificate", _module_instance)
    pulumi.runtime.register_resource_module("azuread", "index/applicationPassword", _module_instance)
    pulumi.runtime.register_resource_module("azuread", "index/group", _module_instance)
    pulumi.runtime.register_resource_module("azuread", "index/groupMember", _module_instance)
    pulumi.runtime.register_resource_module("azuread", "index/servicePrincipal", _module_instance)
    pulumi.runtime.register_resource_module("azuread", "index/servicePrincipalCertificate", _module_instance)
    pulumi.runtime.register_resource_module("azuread", "index/servicePrincipalPassword", _module_instance)
    pulumi.runtime.register_resource_module("azuread", "index/user", _module_instance)


    class Package(pulumi.runtime.ResourcePackage):
        _version = _utilities.get_semver_version()

        def version(self):
            return Package._version

        def construct_provider(self, name: str, typ: str, urn: str) -> pulumi.ProviderResource:
            if typ != "pulumi:providers:azuread":
                raise Exception(f"unknown provider type {typ}")
            return Provider(name, pulumi.ResourceOptions(urn=urn))


    pulumi.runtime.register_resource_package("azuread", Package())

_register_module()
