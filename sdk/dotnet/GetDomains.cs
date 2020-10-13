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
    public static class GetDomains
    {
        /// <summary>
        /// Use this data source to access information about an existing Domains within Azure Active Directory.
        /// 
        /// &gt; **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Directory.Read.All` within the `Windows Azure Active Directory` API.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using AzureAD = Pulumi.AzureAD;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var aadDomains = Output.Create(AzureAD.GetDomains.InvokeAsync());
        ///         this.Domains = aadDomains.Apply(aadDomains =&gt; aadDomains.Domains);
        ///     }
        /// 
        ///     [Output("domains")]
        ///     public Output&lt;string&gt; Domains { get; set; }
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetDomainsResult> InvokeAsync(GetDomainsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetDomainsResult>("azuread:index/getDomains:getDomains", args ?? new GetDomainsArgs(), options.WithVersion());
    }


    public sealed class GetDomainsArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Set to `true` if unverified Azure AD Domains should be included. Defaults to `false`.
        /// </summary>
        [Input("includeUnverified")]
        public bool? IncludeUnverified { get; set; }

        /// <summary>
        /// Set to `true` to only return the default domain.
        /// </summary>
        [Input("onlyDefault")]
        public bool? OnlyDefault { get; set; }

        /// <summary>
        /// Set to `true` to only return the initial domain, which is your primary Azure Active Directory tenant domain. Defaults to `false`.
        /// </summary>
        [Input("onlyInitial")]
        public bool? OnlyInitial { get; set; }

        public GetDomainsArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetDomainsResult
    {
        /// <summary>
        /// One or more `domain` blocks as defined below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetDomainsDomainResult> Domains;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly bool? IncludeUnverified;
        public readonly bool? OnlyDefault;
        public readonly bool? OnlyInitial;

        [OutputConstructor]
        private GetDomainsResult(
            ImmutableArray<Outputs.GetDomainsDomainResult> domains,

            string id,

            bool? includeUnverified,

            bool? onlyDefault,

            bool? onlyInitial)
        {
            Domains = domains;
            Id = id;
            IncludeUnverified = includeUnverified;
            OnlyDefault = onlyDefault;
            OnlyInitial = onlyInitial;
        }
    }
}
