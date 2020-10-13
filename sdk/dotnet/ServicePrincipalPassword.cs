// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Runtime.Serialization;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureAD
{
    /// <summary>
    /// Manages a Password associated with a Service Principal within Azure Active Directory.
    /// 
    /// &gt; **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
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
    ///         var exampleApplication = new AzureAD.Application("exampleApplication", new AzureAD.ApplicationArgs
    ///         {
    ///         });
    ///         var exampleServicePrincipal = new AzureAD.ServicePrincipal("exampleServicePrincipal", new AzureAD.ServicePrincipalArgs
    ///         {
    ///             ApplicationId = exampleApplication.ApplicationId,
    ///         });
    ///         var exampleServicePrincipalPassword = new AzureAD.ServicePrincipalPassword("exampleServicePrincipalPassword", new AzureAD.ServicePrincipalPasswordArgs
    ///         {
    ///             ServicePrincipalId = exampleServicePrincipal.Id,
    ///             Description = "My managed password",
    ///             Value = "VT=uSgbTanZhyz@%nL9Hpd+Tfay_MRV#",
    ///             EndDate = "2099-01-01T01:02:03Z",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class ServicePrincipalPassword : Pulumi.CustomResource
    {
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
        /// A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". Changing this field forces a new resource to be created.
        /// </summary>
        [Output("endDateRelative")]
        public Output<string?> EndDateRelative { get; private set; } = null!;

        /// <summary>
        /// A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.
        /// </summary>
        [Output("keyId")]
        public Output<string> KeyId { get; private set; } = null!;

        /// <summary>
        /// The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.
        /// </summary>
        [Output("servicePrincipalId")]
        public Output<string> ServicePrincipalId { get; private set; } = null!;

        /// <summary>
        /// The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
        /// </summary>
        [Output("startDate")]
        public Output<string> StartDate { get; private set; } = null!;

        /// <summary>
        /// The Password for this Service Principal.
        /// </summary>
        [Output("value")]
        public Output<string> Value { get; private set; } = null!;


        /// <summary>
        /// Create a ServicePrincipalPassword resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServicePrincipalPassword(string name, ServicePrincipalPasswordArgs args, CustomResourceOptions? options = null)
            : base("azuread:index/servicePrincipalPassword:ServicePrincipalPassword", name, args ?? new ServicePrincipalPasswordArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ServicePrincipalPassword(string name, Input<string> id, ServicePrincipalPasswordState? state = null, CustomResourceOptions? options = null)
            : base("azuread:index/servicePrincipalPassword:ServicePrincipalPassword", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ServicePrincipalPassword resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ServicePrincipalPassword Get(string name, Input<string> id, ServicePrincipalPasswordState? state = null, CustomResourceOptions? options = null)
        {
            return new ServicePrincipalPassword(name, id, state, options);
        }
    }

    public sealed class ServicePrincipalPasswordArgs : Pulumi.ResourceArgs
    {
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
        /// A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". Changing this field forces a new resource to be created.
        /// </summary>
        [Input("endDateRelative")]
        public Input<string>? EndDateRelative { get; set; }

        /// <summary>
        /// A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.
        /// </summary>
        [Input("keyId")]
        public Input<string>? KeyId { get; set; }

        /// <summary>
        /// The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.
        /// </summary>
        [Input("servicePrincipalId", required: true)]
        public Input<string> ServicePrincipalId { get; set; } = null!;

        /// <summary>
        /// The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
        /// </summary>
        [Input("startDate")]
        public Input<string>? StartDate { get; set; }

        /// <summary>
        /// The Password for this Service Principal.
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public ServicePrincipalPasswordArgs()
        {
        }
    }

    public sealed class ServicePrincipalPasswordState : Pulumi.ResourceArgs
    {
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
        /// A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". Changing this field forces a new resource to be created.
        /// </summary>
        [Input("endDateRelative")]
        public Input<string>? EndDateRelative { get; set; }

        /// <summary>
        /// A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.
        /// </summary>
        [Input("keyId")]
        public Input<string>? KeyId { get; set; }

        /// <summary>
        /// The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.
        /// </summary>
        [Input("servicePrincipalId")]
        public Input<string>? ServicePrincipalId { get; set; }

        /// <summary>
        /// The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
        /// </summary>
        [Input("startDate")]
        public Input<string>? StartDate { get; set; }

        /// <summary>
        /// The Password for this Service Principal.
        /// </summary>
        [Input("value")]
        public Input<string>? Value { get; set; }

        public ServicePrincipalPasswordState()
        {
        }
    }
}
