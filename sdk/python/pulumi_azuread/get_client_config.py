# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'GetClientConfigResult',
    'AwaitableGetClientConfigResult',
    'get_client_config',
]

@pulumi.output_type
class GetClientConfigResult:
    """
    A collection of values returned by getClientConfig.
    """
    def __init__(__self__, client_id=None, id=None, object_id=None, subscription_id=None, tenant_id=None):
        if client_id and not isinstance(client_id, str):
            raise TypeError("Expected argument 'client_id' to be a str")
        pulumi.set(__self__, "client_id", client_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if object_id and not isinstance(object_id, str):
            raise TypeError("Expected argument 'object_id' to be a str")
        pulumi.set(__self__, "object_id", object_id)
        if subscription_id and not isinstance(subscription_id, str):
            raise TypeError("Expected argument 'subscription_id' to be a str")
        if subscription_id is not None:
            warnings.warn("The \"subscription_id\" attribute will be removed in version 1.0 of the provider. If you are using this attribute, you should instead use the \"azurerm_client_config\" data source from the AzureRM provider", DeprecationWarning)
            pulumi.log.warn("subscription_id is deprecated: The \"subscription_id\" attribute will be removed in version 1.0 of the provider. If you are using this attribute, you should instead use the \"azurerm_client_config\" data source from the AzureRM provider")

        pulumi.set(__self__, "subscription_id", subscription_id)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> str:
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        return pulumi.get(self, "tenant_id")


class AwaitableGetClientConfigResult(GetClientConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClientConfigResult(
            client_id=self.client_id,
            id=self.id,
            object_id=self.object_id,
            subscription_id=self.subscription_id,
            tenant_id=self.tenant_id)


def get_client_config(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClientConfigResult:
    """
    Use this data source to access the configuration of the AzureRM provider.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azuread as azuread

    current = azuread.get_client_config()
    pulumi.export("accountId", current.client_id)
    ```
    """
    __args__ = dict()
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azuread:index/getClientConfig:getClientConfig', __args__, opts=opts, typ=GetClientConfigResult).value

    return AwaitableGetClientConfigResult(
        client_id=__ret__.client_id,
        id=__ret__.id,
        object_id=__ret__.object_id,
        subscription_id=__ret__.subscription_id,
        tenant_id=__ret__.tenant_id)
