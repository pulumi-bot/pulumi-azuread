# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables


class Group(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    The description for the Group.  Changing this forces a new resource to be created.
    """
    members: pulumi.Output[list]
    """
    A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.
    """
    name: pulumi.Output[str]
    """
    The display name for the Group. Changing this forces a new resource to be created.
    """
    object_id: pulumi.Output[str]
    owners: pulumi.Output[list]
    """
    A set of owners who own this Group. Supported Object types are Users or Service Principals.
    """
    prevent_duplicate_names: pulumi.Output[bool]
    """
    If `true`, will return an error when an existing Group is found with the same name. Defaults to `false`.
    """
    def __init__(__self__, resource_name, opts=None, description=None, members=None, name=None, owners=None, prevent_duplicate_names=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Group within Azure Active Directory.

        > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read and write all groups` within the `Windows Azure Active Directory` API. In addition it must also have either the `Company Administrator` or `User Account Administrator` Azure Active Directory roles assigned in order to be able to delete groups. You can assign one of the required Azure Active Directory Roles with the **AzureAD PowerShell Module**, which is available for Windows PowerShell or in the Azure Cloud Shell. Please refer to [this documentation](https://docs.microsoft.com/en-us/powershell/module/azuread/add-azureaddirectoryrolemember) for more details.

        ## Example Usage

        *Basic example*

        ```python
        import pulumi
        import pulumi_azuread as azuread

        example = azuread.Group("example")
        ```

        *A group with members*

        ```python
        import pulumi
        import pulumi_azuread as azuread

        example_user = azuread.User("exampleUser",
            display_name="J Doe",
            password="notSecure123",
            user_principal_name="jdoe@hashicorp.com")
        example_group = azuread.Group("exampleGroup", members=[example_user.object_id])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description for the Group.  Changing this forces a new resource to be created.
        :param pulumi.Input[list] members: A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.
        :param pulumi.Input[str] name: The display name for the Group. Changing this forces a new resource to be created.
        :param pulumi.Input[list] owners: A set of owners who own this Group. Supported Object types are Users or Service Principals.
        :param pulumi.Input[bool] prevent_duplicate_names: If `true`, will return an error when an existing Group is found with the same name. Defaults to `false`.
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

            __props__['description'] = description
            __props__['members'] = members
            __props__['name'] = name
            __props__['owners'] = owners
            __props__['prevent_duplicate_names'] = prevent_duplicate_names
            __props__['object_id'] = None
        super(Group, __self__).__init__(
            'azuread:index/group:Group',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, description=None, members=None, name=None, object_id=None, owners=None, prevent_duplicate_names=None):
        """
        Get an existing Group resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description for the Group.  Changing this forces a new resource to be created.
        :param pulumi.Input[list] members: A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.
        :param pulumi.Input[str] name: The display name for the Group. Changing this forces a new resource to be created.
        :param pulumi.Input[list] owners: A set of owners who own this Group. Supported Object types are Users or Service Principals.
        :param pulumi.Input[bool] prevent_duplicate_names: If `true`, will return an error when an existing Group is found with the same name. Defaults to `false`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["members"] = members
        __props__["name"] = name
        __props__["object_id"] = object_id
        __props__["owners"] = owners
        __props__["prevent_duplicate_names"] = prevent_duplicate_names
        return Group(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
