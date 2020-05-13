# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetGroupResult:
    """
    A collection of values returned by getGroup.
    """
    def __init__(__self__, description=None, id=None, members=None, name=None, object_id=None, owners=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The description of the AD Group.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if members and not isinstance(members, list):
            raise TypeError("Expected argument 'members' to be a list")
        __self__.members = members
        """
        The Object IDs of the Azure AD Group members.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The name of the Azure AD Group.
        """
        if object_id and not isinstance(object_id, str):
            raise TypeError("Expected argument 'object_id' to be a str")
        __self__.object_id = object_id
        if owners and not isinstance(owners, list):
            raise TypeError("Expected argument 'owners' to be a list")
        __self__.owners = owners
        """
        The Object IDs of the Azure AD Group owners.
        """
class AwaitableGetGroupResult(GetGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupResult(
            description=self.description,
            id=self.id,
            members=self.members,
            name=self.name,
            object_id=self.object_id,
            owners=self.owners)

def get_group(name=None,object_id=None,opts=None):
    """
    Gets information about an Azure Active Directory group.

    > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read directory data` within the `Windows Azure Active Directory` API.

    ## Example Usage (by Group Display Name)

    ```python
    import pulumi
    import pulumi_azuread as azuread

    example = azuread.get_group(name="A-AD-Group")
    ```
    > This content is derived from https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/group.html.markdown.


    :param str name: The Name of the AD Group we want to lookup.
    :param str object_id: Specifies the Object ID of the AD Group within Azure Active Directory.
    """
    __args__ = dict()


    __args__['name'] = name
    __args__['objectId'] = object_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azuread:index/getGroup:getGroup', __args__, opts=opts).value

    return AwaitableGetGroupResult(
        description=__ret__.get('description'),
        id=__ret__.get('id'),
        members=__ret__.get('members'),
        name=__ret__.get('name'),
        object_id=__ret__.get('objectId'),
        owners=__ret__.get('owners'))
