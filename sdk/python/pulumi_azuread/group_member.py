# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GroupMember(pulumi.CustomResource):
    group_object_id: pulumi.Output[str]
    """
    The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
    """
    member_object_id: pulumi.Output[str]
    """
    The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.
    """
    def __init__(__self__, resource_name, opts=None, group_object_id=None, member_object_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a single Group Membership within Azure Active Directory.

        > **NOTE:** Do not use this resource at the same time as `azuread_group.members`.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_azuread as azuread

        example_user = azuread.get_user(user_principal_name="jdoe@hashicorp.com")
        example_group = azuread.Group("exampleGroup")
        example_group_member = azuread.GroupMember("exampleGroupMember",
            group_object_id=example_group.id,
            member_object_id=example_user.id)
        ```

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/r/group_member.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_object_id: The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
        :param pulumi.Input[str] member_object_id: The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.
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

            if group_object_id is None:
                raise TypeError("Missing required property 'group_object_id'")
            __props__['group_object_id'] = group_object_id
            if member_object_id is None:
                raise TypeError("Missing required property 'member_object_id'")
            __props__['member_object_id'] = member_object_id
        super(GroupMember, __self__).__init__(
            'azuread:index/groupMember:GroupMember',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, group_object_id=None, member_object_id=None):
        """
        Get an existing GroupMember resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_object_id: The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
        :param pulumi.Input[str] member_object_id: The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["group_object_id"] = group_object_id
        __props__["member_object_id"] = member_object_id
        return GroupMember(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

