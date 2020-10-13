// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Runtime.Serialization;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureAD.Inputs
{

    public sealed class ApplicationAppRoleGetArgs : Pulumi.ResourceArgs
    {
        [Input("allowedMemberTypes", required: true)]
        private InputList<string>? _allowedMemberTypes;

        /// <summary>
        /// Specifies whether this app role definition can be assigned to users and groups by setting to `User`, or to other applications (that are accessing this application in daemon service scenarios) by setting to `Application`, or to both.
        /// </summary>
        public InputList<string> AllowedMemberTypes
        {
            get => _allowedMemberTypes ?? (_allowedMemberTypes = new InputList<string>());
            set => _allowedMemberTypes = value;
        }

        /// <summary>
        /// Permission help text that appears in the admin app assignment and consent experiences.
        /// </summary>
        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        /// <summary>
        /// Display name for the permission that appears in the admin consent and app assignment experiences.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        /// <summary>
        /// The unique identifier of the `app_role`.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Determines if the permission is enabled: defaults to `true`.
        /// </summary>
        [Input("isEnabled")]
        public Input<bool>? IsEnabled { get; set; }

        /// <summary>
        /// The value of the scope claim that the resource application should expect in the OAuth 2.0 access token.
        /// </summary>
        [Input("value")]
        public Input<string>? Value { get; set; }

        public ApplicationAppRoleGetArgs()
        {
        }
    }
}
