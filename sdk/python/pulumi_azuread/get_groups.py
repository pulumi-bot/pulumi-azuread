# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetGroupsResult:
    """
    A collection of values returned by getGroups.
    """
    def __init__(__self__, id=None, names=None, object_ids=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        __self__.names = names
        """
        The Display Names of the Azure AD Groups.
        """
        if object_ids and not isinstance(object_ids, list):
            raise TypeError("Expected argument 'object_ids' to be a list")
        __self__.object_ids = object_ids
        """
        The Object IDs of the Azure AD Groups.
        """
class AwaitableGetGroupsResult(GetGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupsResult(
            id=self.id,
            names=self.names,
            object_ids=self.object_ids)

def get_groups(names=None,object_ids=None,opts=None):
    """
    Gets Object IDs or Display Names for multiple Azure Active Directory groups.

    > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read directory data` within the `Windows Azure Active Directory` API.

    ## Example Usage



    ```python
    import pulumi
    import pulumi_azuread as azuread

    groups = azuread.get_groups(names=[
        "group-a",
        "group-b",
    ])
    ```


    :param list names: The Display Names of the Azure AD Groups.
    :param list object_ids: The Object IDs of the Azure AD Groups.
    """
    __args__ = dict()


    __args__['names'] = names
    __args__['objectIds'] = object_ids
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azuread:index/getGroups:getGroups', __args__, opts=opts).value

    return AwaitableGetGroupsResult(
        id=__ret__.get('id'),
        names=__ret__.get('names'),
        object_ids=__ret__.get('objectIds'))
