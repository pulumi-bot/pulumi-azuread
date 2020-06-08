// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureAD.Inputs
{

    public sealed class ApplicationOptionalClaimsGetArgs : Pulumi.ResourceArgs
    {
        [Input("accessTokens")]
        private InputList<Inputs.ApplicationOptionalClaimsAccessTokenGetArgs>? _accessTokens;
        public InputList<Inputs.ApplicationOptionalClaimsAccessTokenGetArgs> AccessTokens
        {
            get => _accessTokens ?? (_accessTokens = new InputList<Inputs.ApplicationOptionalClaimsAccessTokenGetArgs>());
            set => _accessTokens = value;
        }

        [Input("idTokens")]
        private InputList<Inputs.ApplicationOptionalClaimsIdTokenGetArgs>? _idTokens;
        public InputList<Inputs.ApplicationOptionalClaimsIdTokenGetArgs> IdTokens
        {
            get => _idTokens ?? (_idTokens = new InputList<Inputs.ApplicationOptionalClaimsIdTokenGetArgs>());
            set => _idTokens = value;
        }

        public ApplicationOptionalClaimsGetArgs()
        {
        }
    }
}