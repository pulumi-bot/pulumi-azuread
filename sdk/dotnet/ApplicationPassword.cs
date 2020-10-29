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
    /// Manages a Password associated with an Application within Azure Active Directory. Also can be referred to as Client secrets.
    /// 
    /// &gt; **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
    /// </summary>
    public partial class ApplicationPassword : Pulumi.CustomResource
    {
        [Output("applicationId")]
        public Output<string> ApplicationId { get; private set; } = null!;

        /// <summary>
        /// The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
        /// </summary>
        [Output("applicationObjectId")]
        public Output<string> ApplicationObjectId { get; private set; } = null!;

        /// <summary>
        /// A description for the Password.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
        /// </summary>
        [Output("endDate")]
        public Output<string> EndDate { get; private set; } = null!;

        /// <summary>
        /// A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
        /// </summary>
        [Output("endDateRelative")]
        public Output<string?> EndDateRelative { get; private set; } = null!;

        /// <summary>
        /// A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
        /// </summary>
        [Output("keyId")]
        public Output<string> KeyId { get; private set; } = null!;

        /// <summary>
        /// The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
        /// </summary>
        [Output("startDate")]
        public Output<string> StartDate { get; private set; } = null!;

        /// <summary>
        /// The Password for this Application.
        /// </summary>
        [Output("value")]
        public Output<string> Value { get; private set; } = null!;


        /// <summary>
        /// Create a ApplicationPassword resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ApplicationPassword(string name, ApplicationPasswordArgs args, CustomResourceOptions? options = null)
            : base("azuread:index/applicationPassword:ApplicationPassword", name, args ?? new ApplicationPasswordArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ApplicationPassword(string name, Input<string> id, ApplicationPasswordState? state = null, CustomResourceOptions? options = null)
            : base("azuread:index/applicationPassword:ApplicationPassword", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ApplicationPassword resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ApplicationPassword Get(string name, Input<string> id, ApplicationPasswordState? state = null, CustomResourceOptions? options = null)
        {
            return new ApplicationPassword(name, id, state, options);
        }
    }

    public sealed class ApplicationPasswordArgs : Pulumi.ResourceArgs
    {
        [Input("applicationId")]
        public Input<string>? ApplicationId { get; set; }

        /// <summary>
        /// The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
        /// </summary>
        [Input("applicationObjectId")]
        public Input<string>? ApplicationObjectId { get; set; }

        /// <summary>
        /// A description for the Password.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
        /// </summary>
        [Input("endDate")]
        public Input<string>? EndDate { get; set; }

        /// <summary>
        /// A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
        /// </summary>
        [Input("endDateRelative")]
        public Input<string>? EndDateRelative { get; set; }

        /// <summary>
        /// A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
        /// </summary>
        [Input("keyId")]
        public Input<string>? KeyId { get; set; }

        /// <summary>
        /// The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
        /// </summary>
        [Input("startDate")]
        public Input<string>? StartDate { get; set; }

        /// <summary>
        /// The Password for this Application.
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public ApplicationPasswordArgs()
        {
        }
    }

    public sealed class ApplicationPasswordState : Pulumi.ResourceArgs
    {
        [Input("applicationId")]
        public Input<string>? ApplicationId { get; set; }

        /// <summary>
        /// The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
        /// </summary>
        [Input("applicationObjectId")]
        public Input<string>? ApplicationObjectId { get; set; }

        /// <summary>
        /// A description for the Password.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
        /// </summary>
        [Input("endDate")]
        public Input<string>? EndDate { get; set; }

        /// <summary>
        /// A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
        /// </summary>
        [Input("endDateRelative")]
        public Input<string>? EndDateRelative { get; set; }

        /// <summary>
        /// A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
        /// </summary>
        [Input("keyId")]
        public Input<string>? KeyId { get; set; }

        /// <summary>
        /// The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
        /// </summary>
        [Input("startDate")]
        public Input<string>? StartDate { get; set; }

        /// <summary>
        /// The Password for this Application.
        /// </summary>
        [Input("value")]
        public Input<string>? Value { get; set; }

        public ApplicationPasswordState()
        {
        }
    }
}
