// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureAD
{
    /// <summary>
    /// Manages a single Group Membership within Azure Active Directory.
    /// 
    /// &gt; **NOTE:** Do not use this resource at the same time as `azuread_group.members`.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using AzureAD = Pulumi.AzureAD;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleUser = Output.Create(AzureAD.GetUser.InvokeAsync(new AzureAD.GetUserArgs
    ///         {
    ///             UserPrincipalName = "jdoe@hashicorp.com",
    ///         }));
    ///         var exampleGroup = new AzureAD.Group("exampleGroup", new AzureAD.GroupArgs
    ///         {
    ///         });
    ///         var exampleGroupMember = new AzureAD.GroupMember("exampleGroupMember", new AzureAD.GroupMemberArgs
    ///         {
    ///             GroupObjectId = exampleGroup.Id,
    ///             MemberObjectId = exampleUser.Apply(exampleUser =&gt; exampleUser.Id),
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class GroupMember : Pulumi.CustomResource
    {
        /// <summary>
        /// The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
        /// </summary>
        [Output("groupObjectId")]
        public Output<string> GroupObjectId { get; private set; } = null!;

        /// <summary>
        /// The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.
        /// </summary>
        [Output("memberObjectId")]
        public Output<string> MemberObjectId { get; private set; } = null!;


        /// <summary>
        /// Create a GroupMember resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public GroupMember(string name, GroupMemberArgs args, CustomResourceOptions? options = null)
            : base("azuread:index/groupMember:GroupMember", name, args ?? new GroupMemberArgs(), MakeResourceOptions(options, ""))
        {
        }

        private GroupMember(string name, Input<string> id, GroupMemberState? state = null, CustomResourceOptions? options = null)
            : base("azuread:index/groupMember:GroupMember", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing GroupMember resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static GroupMember Get(string name, Input<string> id, GroupMemberState? state = null, CustomResourceOptions? options = null)
        {
            return new GroupMember(name, id, state, options);
        }
    }

    public sealed class GroupMemberArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
        /// </summary>
        [Input("groupObjectId", required: true)]
        public Input<string> GroupObjectId { get; set; } = null!;

        /// <summary>
        /// The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.
        /// </summary>
        [Input("memberObjectId", required: true)]
        public Input<string> MemberObjectId { get; set; } = null!;

        public GroupMemberArgs()
        {
        }
    }

    public sealed class GroupMemberState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
        /// </summary>
        [Input("groupObjectId")]
        public Input<string>? GroupObjectId { get; set; }

        /// <summary>
        /// The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.
        /// </summary>
        [Input("memberObjectId")]
        public Input<string>? MemberObjectId { get; set; }

        public GroupMemberState()
        {
        }
    }
}
