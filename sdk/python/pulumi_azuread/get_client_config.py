# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables


class GetClientConfigResult:
    """
    A collection of values returned by getClientConfig.
    """
    def __init__(__self__, client_id=None, id=None, object_id=None, subscription_id=None, tenant_id=None):
        if client_id and not isinstance(client_id, str):
            raise TypeError("Expected argument 'client_id' to be a str")
        __self__.client_id = client_id
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if object_id and not isinstance(object_id, str):
            raise TypeError("Expected argument 'object_id' to be a str")
        __self__.object_id = object_id
        if subscription_id and not isinstance(subscription_id, str):
            raise TypeError("Expected argument 'subscription_id' to be a str")
        __self__.subscription_id = subscription_id
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        __self__.tenant_id = tenant_id


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


def get_client_config(opts=None):
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
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azuread:index/getClientConfig:getClientConfig', __args__, opts=opts).value

    return AwaitableGetClientConfigResult(
        client_id=__ret__.get('clientId'),
        id=__ret__.get('id'),
        object_id=__ret__.get('objectId'),
        subscription_id=__ret__.get('subscriptionId'),
        tenant_id=__ret__.get('tenantId'))
