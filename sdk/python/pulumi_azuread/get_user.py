# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables

__all__ = [
    'GetUserResult',
    'AwaitableGetUserResult',
    'get_user',
]

@pulumi.output_type
class GetUserResult:
    """
    A collection of values returned by getUser.
    """
    def __init__(__self__, account_enabled=None, display_name=None, id=None, immutable_id=None, mail=None, mail_nickname=None, object_id=None, onpremises_sam_account_name=None, onpremises_user_principal_name=None, usage_location=None, user_principal_name=None):
        if account_enabled and not isinstance(account_enabled, bool):
            raise TypeError("Expected argument 'account_enabled' to be a bool")
        pulumi.set(__self__, "account_enabled", account_enabled)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if immutable_id and not isinstance(immutable_id, str):
            raise TypeError("Expected argument 'immutable_id' to be a str")
        pulumi.set(__self__, "immutable_id", immutable_id)
        if mail and not isinstance(mail, str):
            raise TypeError("Expected argument 'mail' to be a str")
        pulumi.set(__self__, "mail", mail)
        if mail_nickname and not isinstance(mail_nickname, str):
            raise TypeError("Expected argument 'mail_nickname' to be a str")
        pulumi.set(__self__, "mail_nickname", mail_nickname)
        if object_id and not isinstance(object_id, str):
            raise TypeError("Expected argument 'object_id' to be a str")
        pulumi.set(__self__, "object_id", object_id)
        if onpremises_sam_account_name and not isinstance(onpremises_sam_account_name, str):
            raise TypeError("Expected argument 'onpremises_sam_account_name' to be a str")
        pulumi.set(__self__, "onpremises_sam_account_name", onpremises_sam_account_name)
        if onpremises_user_principal_name and not isinstance(onpremises_user_principal_name, str):
            raise TypeError("Expected argument 'onpremises_user_principal_name' to be a str")
        pulumi.set(__self__, "onpremises_user_principal_name", onpremises_user_principal_name)
        if usage_location and not isinstance(usage_location, str):
            raise TypeError("Expected argument 'usage_location' to be a str")
        pulumi.set(__self__, "usage_location", usage_location)
        if user_principal_name and not isinstance(user_principal_name, str):
            raise TypeError("Expected argument 'user_principal_name' to be a str")
        pulumi.set(__self__, "user_principal_name", user_principal_name)

    @property
    @pulumi.getter(name="accountEnabled")
    def account_enabled(self) -> bool:
        """
        `True` if the account is enabled; otherwise `False`.
        """
        return pulumi.get(self, "account_enabled")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The Display Name of the Azure AD User.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="immutableId")
    def immutable_id(self) -> str:
        """
        The value used to associate an on-premises Active Directory user account with their Azure AD user object.
        """
        return pulumi.get(self, "immutable_id")

    @property
    @pulumi.getter
    def mail(self) -> str:
        """
        The primary email address of the Azure AD User.
        """
        return pulumi.get(self, "mail")

    @property
    @pulumi.getter(name="mailNickname")
    def mail_nickname(self) -> str:
        """
        The email alias of the Azure AD User.
        """
        return pulumi.get(self, "mail_nickname")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> str:
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="onpremisesSamAccountName")
    def onpremises_sam_account_name(self) -> str:
        """
        The on premise sam account name of the Azure AD User.
        """
        return pulumi.get(self, "onpremises_sam_account_name")

    @property
    @pulumi.getter(name="onpremisesUserPrincipalName")
    def onpremises_user_principal_name(self) -> str:
        """
        The on premise user principal name of the Azure AD User.
        """
        return pulumi.get(self, "onpremises_user_principal_name")

    @property
    @pulumi.getter(name="usageLocation")
    def usage_location(self) -> str:
        """
        The usage location of the Azure AD User.
        """
        return pulumi.get(self, "usage_location")

    @property
    @pulumi.getter(name="userPrincipalName")
    def user_principal_name(self) -> str:
        """
        The User Principal Name of the Azure AD User.
        """
        return pulumi.get(self, "user_principal_name")


class AwaitableGetUserResult(GetUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserResult(
            account_enabled=self.account_enabled,
            display_name=self.display_name,
            id=self.id,
            immutable_id=self.immutable_id,
            mail=self.mail,
            mail_nickname=self.mail_nickname,
            object_id=self.object_id,
            onpremises_sam_account_name=self.onpremises_sam_account_name,
            onpremises_user_principal_name=self.onpremises_user_principal_name,
            usage_location=self.usage_location,
            user_principal_name=self.user_principal_name)


def get_user(mail_nickname: Optional[str] = None,
             object_id: Optional[str] = None,
             user_principal_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserResult:
    """
    Gets information about an Azure Active Directory user.

    > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read directory data` within the `Windows Azure Active Directory` API.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azuread as azuread

    example = azuread.get_user(user_principal_name="user@hashicorp.com")
    ```


    :param str mail_nickname: The email alias of the Azure AD User.
    :param str object_id: Specifies the Object ID of the Application within Azure Active Directory.
    :param str user_principal_name: The User Principal Name of the Azure AD User.
    """
    __args__ = dict()
    __args__['mailNickname'] = mail_nickname
    __args__['objectId'] = object_id
    __args__['userPrincipalName'] = user_principal_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azuread:index/getUser:getUser', __args__, opts=opts, typ=GetUserResult).value

    return AwaitableGetUserResult(
        account_enabled=__ret__.account_enabled,
        display_name=__ret__.display_name,
        id=__ret__.id,
        immutable_id=__ret__.immutable_id,
        mail=__ret__.mail,
        mail_nickname=__ret__.mail_nickname,
        object_id=__ret__.object_id,
        onpremises_sam_account_name=__ret__.onpremises_sam_account_name,
        onpremises_user_principal_name=__ret__.onpremises_user_principal_name,
        usage_location=__ret__.usage_location,
        user_principal_name=__ret__.user_principal_name)
