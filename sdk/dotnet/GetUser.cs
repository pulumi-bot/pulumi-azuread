// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureAD
{
    public static class GetUser
    {
        /// <summary>
        /// Gets information about an Azure Active Directory user.
        /// 
        /// &gt; **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read directory data` within the `Windows Azure Active Directory` API.
        /// 
        /// {{% examples %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetUserResult> InvokeAsync(GetUserArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetUserResult>("azuread:index/getUser:getUser", args ?? new GetUserArgs(), options.WithVersion());
    }


    public sealed class GetUserArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The email alias of the Azure AD User.
        /// </summary>
        [Input("mailNickname")]
        public string? MailNickname { get; set; }

        /// <summary>
        /// Specifies the Object ID of the Application within Azure Active Directory.
        /// </summary>
        [Input("objectId")]
        public string? ObjectId { get; set; }

        /// <summary>
        /// The User Principal Name of the Azure AD User.
        /// </summary>
        [Input("userPrincipalName")]
        public string? UserPrincipalName { get; set; }

        public GetUserArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetUserResult
    {
        /// <summary>
        /// `True` if the account is enabled; otherwise `False`.
        /// </summary>
        public readonly bool AccountEnabled;
        /// <summary>
        /// The Display Name of the Azure AD User.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The value used to associate an on-premises Active Directory user account with their Azure AD user object.
        /// </summary>
        public readonly string ImmutableId;
        /// <summary>
        /// The primary email address of the Azure AD User.
        /// </summary>
        public readonly string Mail;
        /// <summary>
        /// The email alias of the Azure AD User.
        /// </summary>
        public readonly string MailNickname;
        public readonly string ObjectId;
        /// <summary>
        /// The on premise sam account name of the Azure AD User.
        /// </summary>
        public readonly string OnpremisesSamAccountName;
        /// <summary>
        /// The on premise user principal name of the Azure AD User.
        /// </summary>
        public readonly string OnpremisesUserPrincipalName;
        /// <summary>
        /// The usage location of the Azure AD User.
        /// </summary>
        public readonly string UsageLocation;
        /// <summary>
        /// The User Principal Name of the Azure AD User.
        /// </summary>
        public readonly string UserPrincipalName;

        [OutputConstructor]
        private GetUserResult(
            bool accountEnabled,

            string displayName,

            string id,

            string immutableId,

            string mail,

            string mailNickname,

            string objectId,

            string onpremisesSamAccountName,

            string onpremisesUserPrincipalName,

            string usageLocation,

            string userPrincipalName)
        {
            AccountEnabled = accountEnabled;
            DisplayName = displayName;
            Id = id;
            ImmutableId = immutableId;
            Mail = mail;
            MailNickname = mailNickname;
            ObjectId = objectId;
            OnpremisesSamAccountName = onpremisesSamAccountName;
            OnpremisesUserPrincipalName = onpremisesUserPrincipalName;
            UsageLocation = usageLocation;
            UserPrincipalName = userPrincipalName;
        }
    }
}
