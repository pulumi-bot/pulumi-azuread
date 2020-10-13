// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Runtime.Serialization;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureAD.Outputs
{

    [OutputType]
    public sealed class GetDomainsDomainResult
    {
        /// <summary>
        /// The authentication type of the domain (Managed or Federated).
        /// </summary>
        public readonly string AuthenticationType;
        /// <summary>
        /// The name of the domain.
        /// </summary>
        public readonly string DomainName;
        /// <summary>
        /// `True` if this is the default domain that is used for user creation.
        /// </summary>
        public readonly bool IsDefault;
        /// <summary>
        /// `True` if this is the initial domain created by Azure Activie Directory.
        /// </summary>
        public readonly bool IsInitial;
        /// <summary>
        /// `True` if the domain has completed domain ownership verification.
        /// </summary>
        public readonly bool IsVerified;

        [OutputConstructor]
        private GetDomainsDomainResult(
            string authenticationType,

            string domainName,

            bool isDefault,

            bool isInitial,

            bool isVerified)
        {
            AuthenticationType = authenticationType;
            DomainName = domainName;
            IsDefault = isDefault;
            IsInitial = isInitial;
            IsVerified = isVerified;
        }
    }
}
