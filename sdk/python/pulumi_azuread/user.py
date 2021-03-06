# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class User(pulumi.CustomResource):
    account_enabled: pulumi.Output[bool]
    """
    `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
    """
    display_name: pulumi.Output[str]
    """
    The name to display in the address book for the user.
    """
    force_password_change: pulumi.Output[bool]
    """
    `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
    """
    immutable_id: pulumi.Output[str]
    """
    The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account. 
    """
    mail: pulumi.Output[str]
    """
    The primary email address of the Azure AD User.
    """
    mail_nickname: pulumi.Output[str]
    """
    The mail alias for the user. Defaults to the user name part of the User Principal Name.
    """
    object_id: pulumi.Output[str]
    """
    The Object ID of the Azure AD User.
    """
    onpremises_sam_account_name: pulumi.Output[str]
    """
    The on premise sam account name of the Azure AD User.
    """
    onpremises_user_principal_name: pulumi.Output[str]
    """
    The on premise user principal name of the Azure AD User.
    """
    password: pulumi.Output[str]
    """
    The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
    """
    usage_location: pulumi.Output[str]
    """
    The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set. 
    """
    user_principal_name: pulumi.Output[str]
    """
    The User Principal Name of the Azure AD User.
    """
    def __init__(__self__, resource_name, opts=None, account_enabled=None, display_name=None, force_password_change=None, immutable_id=None, mail_nickname=None, password=None, usage_location=None, user_principal_name=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a User within Azure Active Directory.

        > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Directory.ReadWrite.All` within the `Windows Azure Active Directory` API.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] account_enabled: `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
        :param pulumi.Input[str] display_name: The name to display in the address book for the user.
        :param pulumi.Input[bool] force_password_change: `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
        :param pulumi.Input[str] immutable_id: The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account. 
        :param pulumi.Input[str] mail_nickname: The mail alias for the user. Defaults to the user name part of the User Principal Name.
        :param pulumi.Input[str] password: The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
        :param pulumi.Input[str] usage_location: The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set. 
        :param pulumi.Input[str] user_principal_name: The User Principal Name of the Azure AD User.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['account_enabled'] = account_enabled
            if display_name is None:
                raise TypeError("Missing required property 'display_name'")
            __props__['display_name'] = display_name
            __props__['force_password_change'] = force_password_change
            __props__['immutable_id'] = immutable_id
            __props__['mail_nickname'] = mail_nickname
            if password is None:
                raise TypeError("Missing required property 'password'")
            __props__['password'] = password
            __props__['usage_location'] = usage_location
            if user_principal_name is None:
                raise TypeError("Missing required property 'user_principal_name'")
            __props__['user_principal_name'] = user_principal_name
            __props__['mail'] = None
            __props__['object_id'] = None
            __props__['onpremises_sam_account_name'] = None
            __props__['onpremises_user_principal_name'] = None
        super(User, __self__).__init__(
            'azuread:index/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, account_enabled=None, display_name=None, force_password_change=None, immutable_id=None, mail=None, mail_nickname=None, object_id=None, onpremises_sam_account_name=None, onpremises_user_principal_name=None, password=None, usage_location=None, user_principal_name=None):
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] account_enabled: `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
        :param pulumi.Input[str] display_name: The name to display in the address book for the user.
        :param pulumi.Input[bool] force_password_change: `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
        :param pulumi.Input[str] immutable_id: The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account. 
        :param pulumi.Input[str] mail: The primary email address of the Azure AD User.
        :param pulumi.Input[str] mail_nickname: The mail alias for the user. Defaults to the user name part of the User Principal Name.
        :param pulumi.Input[str] object_id: The Object ID of the Azure AD User.
        :param pulumi.Input[str] onpremises_sam_account_name: The on premise sam account name of the Azure AD User.
        :param pulumi.Input[str] onpremises_user_principal_name: The on premise user principal name of the Azure AD User.
        :param pulumi.Input[str] password: The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
        :param pulumi.Input[str] usage_location: The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set. 
        :param pulumi.Input[str] user_principal_name: The User Principal Name of the Azure AD User.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_enabled"] = account_enabled
        __props__["display_name"] = display_name
        __props__["force_password_change"] = force_password_change
        __props__["immutable_id"] = immutable_id
        __props__["mail"] = mail
        __props__["mail_nickname"] = mail_nickname
        __props__["object_id"] = object_id
        __props__["onpremises_sam_account_name"] = onpremises_sam_account_name
        __props__["onpremises_user_principal_name"] = onpremises_user_principal_name
        __props__["password"] = password
        __props__["usage_location"] = usage_location
        __props__["user_principal_name"] = user_principal_name
        return User(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

