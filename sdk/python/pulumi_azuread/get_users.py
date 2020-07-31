# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from . import _utilities, _tables
from . import outputs

__all__ = [
    'GetUsersResult',
    'AwaitableGetUsersResult',
    'get_users',
]


class GetUsersResult:
    """
    A collection of values returned by getUsers.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, id=None, ignore_missing=None, mail_nicknames=None, object_ids=None, user_principal_names=None, users=None) -> None:
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if ignore_missing and not isinstance(ignore_missing, bool):
            raise TypeError("Expected argument 'ignore_missing' to be a bool")
        __self__.ignore_missing = ignore_missing
        if mail_nicknames and not isinstance(mail_nicknames, list):
            raise TypeError("Expected argument 'mail_nicknames' to be a list")
        __self__.mail_nicknames = mail_nicknames
        """
        The email aliases of the Azure AD Users.
        """
        if object_ids and not isinstance(object_ids, list):
            raise TypeError("Expected argument 'object_ids' to be a list")
        __self__.object_ids = object_ids
        """
        The Object IDs of the Azure AD Users.
        """
        if user_principal_names and not isinstance(user_principal_names, list):
            raise TypeError("Expected argument 'user_principal_names' to be a list")
        __self__.user_principal_names = user_principal_names
        """
        The User Principal Names of the Azure AD Users.
        """
        if users and not isinstance(users, list):
            raise TypeError("Expected argument 'users' to be a list")
        __self__.users = users
        """
        An Array of Azure AD Users. Each `user` object consists of the fields documented below.
        """


class AwaitableGetUsersResult(GetUsersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUsersResult(
            id=self.id,
            ignore_missing=self.ignore_missing,
            mail_nicknames=self.mail_nicknames,
            object_ids=self.object_ids,
            user_principal_names=self.user_principal_names,
            users=self.users)


def get_users(ignore_missing: Optional[bool] = None, mail_nicknames: Optional[List[str]] = None, object_ids: Optional[List[str]] = None, user_principal_names: Optional[List[str]] = None, opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUsersResult:
    """
    Gets Object IDs or UPNs for multiple Azure Active Directory users.

    > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read directory data` within the `Windows Azure Active Directory` API.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azuread as azuread

    users = azuread.get_users(user_principal_names=[
        "kat@hashicorp.com",
        "byte@hashicorp.com",
    ])
    ```


    :param bool ignore_missing: Ignore missing users and return users that were found. The data source will still fail if no users are found. Defaults to false.
    :param List[str] mail_nicknames: The email aliases of the Azure AD Users.
    :param List[str] object_ids: The Object IDs of the Azure AD Users.
    :param List[str] user_principal_names: The User Principal Names of the Azure AD Users.
    """
    __args__ = dict()
    __args__['ignoreMissing'] = ignore_missing
    __args__['mailNicknames'] = mail_nicknames
    __args__['objectIds'] = object_ids
    __args__['userPrincipalNames'] = user_principal_names
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azuread:index/getUsers:getUsers', __args__, opts=opts).value

    return AwaitableGetUsersResult(
        id=__ret__.get('id'),
        ignore_missing=__ret__.get('ignoreMissing'),
        mail_nicknames=__ret__.get('mailNicknames'),
        object_ids=__ret__.get('objectIds'),
        user_principal_names=__ret__.get('userPrincipalNames'),
        users=__ret__.get('users'))
