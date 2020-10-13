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
    public sealed class GetUsersUserResult
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
        private GetUsersUserResult(
            bool accountEnabled,

            string displayName,

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
