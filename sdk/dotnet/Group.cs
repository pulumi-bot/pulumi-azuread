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
    /// Manages a Group within Azure Active Directory.
    /// 
    /// &gt; **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read and write all groups` within the `Windows Azure Active Directory` API. In addition it must also have either the `Company Administrator` or `User Account Administrator` Azure Active Directory roles assigned in order to be able to delete groups. You can assign one of the required Azure Active Directory Roles with the **AzureAD PowerShell Module**, which is available for Windows PowerShell or in the Azure Cloud Shell. Please refer to [this documentation](https://docs.microsoft.com/en-us/powershell/module/azuread/add-azureaddirectoryrolemember) for more details.
    /// 
    /// ## Example Usage
    /// 
    /// *Basic example*
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using AzureAD = Pulumi.AzureAD;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new AzureAD.Group("example", new AzureAD.GroupArgs
    ///         {
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// *A group with members*
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using AzureAD = Pulumi.AzureAD;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleUser = new AzureAD.User("exampleUser", new AzureAD.UserArgs
    ///         {
    ///             DisplayName = "J Doe",
    ///             Password = "notSecure123",
    ///             UserPrincipalName = "jdoe@hashicorp.com",
    ///         });
    ///         var exampleGroup = new AzureAD.Group("exampleGroup", new AzureAD.GroupArgs
    ///         {
    ///             Members = 
    ///             {
    ///                 exampleUser.ObjectId,
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Azure Active Directory Groups can be imported using the `object id`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import azuread:index/group:Group my_group 00000000-0000-0000-0000-000000000000
    /// ```
    /// </summary>
    [AzureADResourceType("azuread:index/group:Group")]
    public partial class Group : Pulumi.CustomResource
    {
        /// <summary>
        /// The description for the Group.  Changing this forces a new resource to be created.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.
        /// </summary>
        [Output("members")]
        public Output<ImmutableArray<string>> Members { get; private set; } = null!;

        /// <summary>
        /// The display name for the Group. Changing this forces a new resource to be created.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("objectId")]
        public Output<string> ObjectId { get; private set; } = null!;

        /// <summary>
        /// A set of owners who own this Group. Supported Object types are Users or Service Principals.
        /// </summary>
        [Output("owners")]
        public Output<ImmutableArray<string>> Owners { get; private set; } = null!;

        /// <summary>
        /// If `true`, will return an error when an existing Group is found with the same name. Defaults to `false`.
        /// </summary>
        [Output("preventDuplicateNames")]
        public Output<bool?> PreventDuplicateNames { get; private set; } = null!;


        /// <summary>
        /// Create a Group resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Group(string name, GroupArgs? args = null, CustomResourceOptions? options = null)
            : base("azuread:index/group:Group", name, args ?? new GroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Group(string name, Input<string> id, GroupState? state = null, CustomResourceOptions? options = null)
            : base("azuread:index/group:Group", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Group resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Group Get(string name, Input<string> id, GroupState? state = null, CustomResourceOptions? options = null)
        {
            return new Group(name, id, state, options);
        }
    }

    public sealed class GroupArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description for the Group.  Changing this forces a new resource to be created.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("members")]
        private InputList<string>? _members;

        /// <summary>
        /// A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.
        /// </summary>
        public InputList<string> Members
        {
            get => _members ?? (_members = new InputList<string>());
            set => _members = value;
        }

        /// <summary>
        /// The display name for the Group. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("owners")]
        private InputList<string>? _owners;

        /// <summary>
        /// A set of owners who own this Group. Supported Object types are Users or Service Principals.
        /// </summary>
        public InputList<string> Owners
        {
            get => _owners ?? (_owners = new InputList<string>());
            set => _owners = value;
        }

        /// <summary>
        /// If `true`, will return an error when an existing Group is found with the same name. Defaults to `false`.
        /// </summary>
        [Input("preventDuplicateNames")]
        public Input<bool>? PreventDuplicateNames { get; set; }

        public GroupArgs()
        {
        }
    }

    public sealed class GroupState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description for the Group.  Changing this forces a new resource to be created.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("members")]
        private InputList<string>? _members;

        /// <summary>
        /// A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.
        /// </summary>
        public InputList<string> Members
        {
            get => _members ?? (_members = new InputList<string>());
            set => _members = value;
        }

        /// <summary>
        /// The display name for the Group. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("objectId")]
        public Input<string>? ObjectId { get; set; }

        [Input("owners")]
        private InputList<string>? _owners;

        /// <summary>
        /// A set of owners who own this Group. Supported Object types are Users or Service Principals.
        /// </summary>
        public InputList<string> Owners
        {
            get => _owners ?? (_owners = new InputList<string>());
            set => _owners = value;
        }

        /// <summary>
        /// If `true`, will return an error when an existing Group is found with the same name. Defaults to `false`.
        /// </summary>
        [Input("preventDuplicateNames")]
        public Input<bool>? PreventDuplicateNames { get; set; }

        public GroupState()
        {
        }
    }
}
