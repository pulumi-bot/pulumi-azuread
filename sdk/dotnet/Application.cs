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
    /// Manages an Application within Azure Active Directory.
    /// 
    /// &gt; **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write owned by applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
    /// 
    /// ## Example Usage
    /// 
    /// 
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using AzureAD = Pulumi.AzureAD;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new AzureAD.Application("example", new AzureAD.ApplicationArgs
    ///         {
    ///             AppRoles = 
    ///             {
    ///                 new AzureAD.Inputs.ApplicationAppRoleArgs
    ///                 {
    ///                     AllowedMemberTypes = 
    ///                     {
    ///                         "User",
    ///                         "Application",
    ///                     },
    ///                     Description = "Admins can manage roles and perform all task actions",
    ///                     DisplayName = "Admin",
    ///                     IsEnabled = true,
    ///                     Value = "Admin",
    ///                 },
    ///             },
    ///             AvailableToOtherTenants = false,
    ///             Homepage = "https://homepage",
    ///             IdentifierUris = 
    ///             {
    ///                 "https://uri",
    ///             },
    ///             Oauth2AllowImplicitFlow = true,
    ///             Oauth2Permissions = 
    ///             {
    ///                 new AzureAD.Inputs.ApplicationOauth2PermissionArgs
    ///                 {
    ///                     AdminConsentDescription = "Allow the application to access example on behalf of the signed-in user.",
    ///                     AdminConsentDisplayName = "Access example",
    ///                     IsEnabled = true,
    ///                     Type = "User",
    ///                     UserConsentDescription = "Allow the application to access example on your behalf.",
    ///                     UserConsentDisplayName = "Access example",
    ///                     Value = "user_impersonation",
    ///                 },
    ///                 new AzureAD.Inputs.ApplicationOauth2PermissionArgs
    ///                 {
    ///                     AdminConsentDescription = "Administer the example application",
    ///                     AdminConsentDisplayName = "Administer",
    ///                     IsEnabled = true,
    ///                     Type = "Admin",
    ///                     Value = "administer",
    ///                 },
    ///             },
    ///             OptionalClaims = new AzureAD.Inputs.ApplicationOptionalClaimsArgs
    ///             {
    ///                 AccessToken = 
    ///                 {
    ///                     
    ///                     {
    ///                         { "name", "myclaim" },
    ///                     },
    ///                     
    ///                     {
    ///                         { "name", "otherclaim" },
    ///                     },
    ///                 },
    ///                 IdToken = 
    ///                 {
    ///                     
    ///                     {
    ///                         { "additionalProperties", 
    ///                         {
    ///                             "emit_as_roles",
    ///                         } },
    ///                         { "essential", true },
    ///                         { "name", "userclaim" },
    ///                         { "source", "user" },
    ///                     },
    ///                 },
    ///             },
    ///             Owners = 
    ///             {
    ///                 "00000004-0000-0000-c000-000000000000",
    ///             },
    ///             ReplyUrls = 
    ///             {
    ///                 "https://replyurl",
    ///             },
    ///             RequiredResourceAccesses = 
    ///             {
    ///                 new AzureAD.Inputs.ApplicationRequiredResourceAccessArgs
    ///                 {
    ///                     ResourceAccess = 
    ///                     {
    ///                         
    ///                         {
    ///                             { "id", "..." },
    ///                             { "type", "Role" },
    ///                         },
    ///                         
    ///                         {
    ///                             { "id", "..." },
    ///                             { "type", "Scope" },
    ///                         },
    ///                         
    ///                         {
    ///                             { "id", "..." },
    ///                             { "type", "Scope" },
    ///                         },
    ///                     },
    ///                     ResourceAppId = "00000003-0000-0000-c000-000000000000",
    ///                 },
    ///                 new AzureAD.Inputs.ApplicationRequiredResourceAccessArgs
    ///                 {
    ///                     ResourceAccess = 
    ///                     {
    ///                         
    ///                         {
    ///                             { "id", "..." },
    ///                             { "type", "Scope" },
    ///                         },
    ///                     },
    ///                     ResourceAppId = "00000002-0000-0000-c000-000000000000",
    ///                 },
    ///             },
    ///             Type = "webapp/api",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class Application : Pulumi.CustomResource
    {
        /// <summary>
        /// A collection of `app_role` blocks as documented below. For more information https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles
        /// </summary>
        [Output("appRoles")]
        public Output<ImmutableArray<Outputs.ApplicationAppRole>> AppRoles { get; private set; } = null!;

        /// <summary>
        /// The Application ID.
        /// </summary>
        [Output("applicationId")]
        public Output<string> ApplicationId { get; private set; } = null!;

        /// <summary>
        /// Is this Azure AD Application available to other tenants? Defaults to `false`.
        /// </summary>
        [Output("availableToOtherTenants")]
        public Output<bool?> AvailableToOtherTenants { get; private set; } = null!;

        /// <summary>
        /// Configures the `groups` claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to `SecurityGroup`. Possible values are `None`, `SecurityGroup`, `DirectoryRole`, `ApplicationGroup` or `All`.
        /// </summary>
        [Output("groupMembershipClaims")]
        public Output<string?> GroupMembershipClaims { get; private set; } = null!;

        /// <summary>
        /// The URL to the application's home page. If no homepage is specified this defaults to `https://{name}`.
        /// </summary>
        [Output("homepage")]
        public Output<string> Homepage { get; private set; } = null!;

        /// <summary>
        /// A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
        /// </summary>
        [Output("identifierUris")]
        public Output<ImmutableArray<string>> IdentifierUris { get; private set; } = null!;

        /// <summary>
        /// The URL of the logout page.
        /// </summary>
        [Output("logoutUrl")]
        public Output<string?> LogoutUrl { get; private set; } = null!;

        /// <summary>
        /// The display name for the application.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.
        /// </summary>
        [Output("oauth2AllowImplicitFlow")]
        public Output<bool?> Oauth2AllowImplicitFlow { get; private set; } = null!;

        /// <summary>
        /// A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by `oauth2_permissions` blocks as documented below.
        /// </summary>
        [Output("oauth2Permissions")]
        public Output<ImmutableArray<Outputs.ApplicationOauth2Permission>> Oauth2Permissions { get; private set; } = null!;

        /// <summary>
        /// The Application's Object ID.
        /// </summary>
        [Output("objectId")]
        public Output<string> ObjectId { get; private set; } = null!;

        /// <summary>
        /// A collection of `access_token` or `id_token` blocks as documented below which list the optional claims configured for each token type. For more information see https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims
        /// </summary>
        [Output("optionalClaims")]
        public Output<Outputs.ApplicationOptionalClaims?> OptionalClaims { get; private set; } = null!;

        /// <summary>
        /// A list of Azure AD Object IDs that will be granted ownership of the application. Defaults to the Object ID of the caller creating the application. If a list is specified the caller Object ID will no longer be included unless explicitly added to the list.
        /// </summary>
        [Output("owners")]
        public Output<ImmutableArray<string>> Owners { get; private set; } = null!;

        /// <summary>
        /// Is this Azure AD Application a public client? Defaults to `false`.
        /// </summary>
        [Output("publicClient")]
        public Output<bool> PublicClient { get; private set; } = null!;

        /// <summary>
        /// A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.
        /// </summary>
        [Output("replyUrls")]
        public Output<ImmutableArray<string>> ReplyUrls { get; private set; } = null!;

        /// <summary>
        /// A collection of `required_resource_access` blocks as documented below.
        /// </summary>
        [Output("requiredResourceAccesses")]
        public Output<ImmutableArray<Outputs.ApplicationRequiredResourceAccess>> RequiredResourceAccesses { get; private set; } = null!;

        /// <summary>
        /// Type of an application: `webapp/api` or `native`. Defaults to `webapp/api`. For `native` apps type `identifier_uris` property can not not be set.
        /// </summary>
        [Output("type")]
        public Output<string?> Type { get; private set; } = null!;


        /// <summary>
        /// Create a Application resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Application(string name, ApplicationArgs? args = null, CustomResourceOptions? options = null)
            : base("azuread:index/application:Application", name, args ?? new ApplicationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Application(string name, Input<string> id, ApplicationState? state = null, CustomResourceOptions? options = null)
            : base("azuread:index/application:Application", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Application resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Application Get(string name, Input<string> id, ApplicationState? state = null, CustomResourceOptions? options = null)
        {
            return new Application(name, id, state, options);
        }
    }

    public sealed class ApplicationArgs : Pulumi.ResourceArgs
    {
        [Input("appRoles")]
        private InputList<Inputs.ApplicationAppRoleArgs>? _appRoles;

        /// <summary>
        /// A collection of `app_role` blocks as documented below. For more information https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles
        /// </summary>
        public InputList<Inputs.ApplicationAppRoleArgs> AppRoles
        {
            get => _appRoles ?? (_appRoles = new InputList<Inputs.ApplicationAppRoleArgs>());
            set => _appRoles = value;
        }

        /// <summary>
        /// Is this Azure AD Application available to other tenants? Defaults to `false`.
        /// </summary>
        [Input("availableToOtherTenants")]
        public Input<bool>? AvailableToOtherTenants { get; set; }

        /// <summary>
        /// Configures the `groups` claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to `SecurityGroup`. Possible values are `None`, `SecurityGroup`, `DirectoryRole`, `ApplicationGroup` or `All`.
        /// </summary>
        [Input("groupMembershipClaims")]
        public Input<string>? GroupMembershipClaims { get; set; }

        /// <summary>
        /// The URL to the application's home page. If no homepage is specified this defaults to `https://{name}`.
        /// </summary>
        [Input("homepage")]
        public Input<string>? Homepage { get; set; }

        [Input("identifierUris")]
        private InputList<string>? _identifierUris;

        /// <summary>
        /// A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
        /// </summary>
        public InputList<string> IdentifierUris
        {
            get => _identifierUris ?? (_identifierUris = new InputList<string>());
            set => _identifierUris = value;
        }

        /// <summary>
        /// The URL of the logout page.
        /// </summary>
        [Input("logoutUrl")]
        public Input<string>? LogoutUrl { get; set; }

        /// <summary>
        /// The display name for the application.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.
        /// </summary>
        [Input("oauth2AllowImplicitFlow")]
        public Input<bool>? Oauth2AllowImplicitFlow { get; set; }

        [Input("oauth2Permissions")]
        private InputList<Inputs.ApplicationOauth2PermissionArgs>? _oauth2Permissions;

        /// <summary>
        /// A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by `oauth2_permissions` blocks as documented below.
        /// </summary>
        public InputList<Inputs.ApplicationOauth2PermissionArgs> Oauth2Permissions
        {
            get => _oauth2Permissions ?? (_oauth2Permissions = new InputList<Inputs.ApplicationOauth2PermissionArgs>());
            set => _oauth2Permissions = value;
        }

        /// <summary>
        /// A collection of `access_token` or `id_token` blocks as documented below which list the optional claims configured for each token type. For more information see https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims
        /// </summary>
        [Input("optionalClaims")]
        public Input<Inputs.ApplicationOptionalClaimsArgs>? OptionalClaims { get; set; }

        [Input("owners")]
        private InputList<string>? _owners;

        /// <summary>
        /// A list of Azure AD Object IDs that will be granted ownership of the application. Defaults to the Object ID of the caller creating the application. If a list is specified the caller Object ID will no longer be included unless explicitly added to the list.
        /// </summary>
        public InputList<string> Owners
        {
            get => _owners ?? (_owners = new InputList<string>());
            set => _owners = value;
        }

        /// <summary>
        /// Is this Azure AD Application a public client? Defaults to `false`.
        /// </summary>
        [Input("publicClient")]
        public Input<bool>? PublicClient { get; set; }

        [Input("replyUrls")]
        private InputList<string>? _replyUrls;

        /// <summary>
        /// A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.
        /// </summary>
        public InputList<string> ReplyUrls
        {
            get => _replyUrls ?? (_replyUrls = new InputList<string>());
            set => _replyUrls = value;
        }

        [Input("requiredResourceAccesses")]
        private InputList<Inputs.ApplicationRequiredResourceAccessArgs>? _requiredResourceAccesses;

        /// <summary>
        /// A collection of `required_resource_access` blocks as documented below.
        /// </summary>
        public InputList<Inputs.ApplicationRequiredResourceAccessArgs> RequiredResourceAccesses
        {
            get => _requiredResourceAccesses ?? (_requiredResourceAccesses = new InputList<Inputs.ApplicationRequiredResourceAccessArgs>());
            set => _requiredResourceAccesses = value;
        }

        /// <summary>
        /// Type of an application: `webapp/api` or `native`. Defaults to `webapp/api`. For `native` apps type `identifier_uris` property can not not be set.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public ApplicationArgs()
        {
        }
    }

    public sealed class ApplicationState : Pulumi.ResourceArgs
    {
        [Input("appRoles")]
        private InputList<Inputs.ApplicationAppRoleGetArgs>? _appRoles;

        /// <summary>
        /// A collection of `app_role` blocks as documented below. For more information https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles
        /// </summary>
        public InputList<Inputs.ApplicationAppRoleGetArgs> AppRoles
        {
            get => _appRoles ?? (_appRoles = new InputList<Inputs.ApplicationAppRoleGetArgs>());
            set => _appRoles = value;
        }

        /// <summary>
        /// The Application ID.
        /// </summary>
        [Input("applicationId")]
        public Input<string>? ApplicationId { get; set; }

        /// <summary>
        /// Is this Azure AD Application available to other tenants? Defaults to `false`.
        /// </summary>
        [Input("availableToOtherTenants")]
        public Input<bool>? AvailableToOtherTenants { get; set; }

        /// <summary>
        /// Configures the `groups` claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to `SecurityGroup`. Possible values are `None`, `SecurityGroup`, `DirectoryRole`, `ApplicationGroup` or `All`.
        /// </summary>
        [Input("groupMembershipClaims")]
        public Input<string>? GroupMembershipClaims { get; set; }

        /// <summary>
        /// The URL to the application's home page. If no homepage is specified this defaults to `https://{name}`.
        /// </summary>
        [Input("homepage")]
        public Input<string>? Homepage { get; set; }

        [Input("identifierUris")]
        private InputList<string>? _identifierUris;

        /// <summary>
        /// A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
        /// </summary>
        public InputList<string> IdentifierUris
        {
            get => _identifierUris ?? (_identifierUris = new InputList<string>());
            set => _identifierUris = value;
        }

        /// <summary>
        /// The URL of the logout page.
        /// </summary>
        [Input("logoutUrl")]
        public Input<string>? LogoutUrl { get; set; }

        /// <summary>
        /// The display name for the application.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.
        /// </summary>
        [Input("oauth2AllowImplicitFlow")]
        public Input<bool>? Oauth2AllowImplicitFlow { get; set; }

        [Input("oauth2Permissions")]
        private InputList<Inputs.ApplicationOauth2PermissionGetArgs>? _oauth2Permissions;

        /// <summary>
        /// A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by `oauth2_permissions` blocks as documented below.
        /// </summary>
        public InputList<Inputs.ApplicationOauth2PermissionGetArgs> Oauth2Permissions
        {
            get => _oauth2Permissions ?? (_oauth2Permissions = new InputList<Inputs.ApplicationOauth2PermissionGetArgs>());
            set => _oauth2Permissions = value;
        }

        /// <summary>
        /// The Application's Object ID.
        /// </summary>
        [Input("objectId")]
        public Input<string>? ObjectId { get; set; }

        /// <summary>
        /// A collection of `access_token` or `id_token` blocks as documented below which list the optional claims configured for each token type. For more information see https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims
        /// </summary>
        [Input("optionalClaims")]
        public Input<Inputs.ApplicationOptionalClaimsGetArgs>? OptionalClaims { get; set; }

        [Input("owners")]
        private InputList<string>? _owners;

        /// <summary>
        /// A list of Azure AD Object IDs that will be granted ownership of the application. Defaults to the Object ID of the caller creating the application. If a list is specified the caller Object ID will no longer be included unless explicitly added to the list.
        /// </summary>
        public InputList<string> Owners
        {
            get => _owners ?? (_owners = new InputList<string>());
            set => _owners = value;
        }

        /// <summary>
        /// Is this Azure AD Application a public client? Defaults to `false`.
        /// </summary>
        [Input("publicClient")]
        public Input<bool>? PublicClient { get; set; }

        [Input("replyUrls")]
        private InputList<string>? _replyUrls;

        /// <summary>
        /// A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.
        /// </summary>
        public InputList<string> ReplyUrls
        {
            get => _replyUrls ?? (_replyUrls = new InputList<string>());
            set => _replyUrls = value;
        }

        [Input("requiredResourceAccesses")]
        private InputList<Inputs.ApplicationRequiredResourceAccessGetArgs>? _requiredResourceAccesses;

        /// <summary>
        /// A collection of `required_resource_access` blocks as documented below.
        /// </summary>
        public InputList<Inputs.ApplicationRequiredResourceAccessGetArgs> RequiredResourceAccesses
        {
            get => _requiredResourceAccesses ?? (_requiredResourceAccesses = new InputList<Inputs.ApplicationRequiredResourceAccessGetArgs>());
            set => _requiredResourceAccesses = value;
        }

        /// <summary>
        /// Type of an application: `webapp/api` or `native`. Defaults to `webapp/api`. For `native` apps type `identifier_uris` property can not not be set.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public ApplicationState()
        {
        }
    }
}
