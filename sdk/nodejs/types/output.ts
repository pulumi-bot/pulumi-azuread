// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";

export interface ApplicationAppRole {
    /**
     * Specifies whether this app role definition can be assigned to users and groups by setting to `User`, or to other applications (that are accessing this application in daemon service scenarios) by setting to `Application`, or to both.
     */
    allowedMemberTypes: string[];
    /**
     * Permission help text that appears in the admin app assignment and consent experiences.
     */
    description: string;
    /**
     * Display name for the permission that appears in the admin consent and app assignment experiences.
     */
    displayName: string;
    /**
     * The unique identifier of the `appRole`.
     */
    id: string;
    /**
     * Determines if the permission is enabled: defaults to `true`.
     */
    isEnabled?: boolean;
    /**
     * The value of the scope claim that the resource application should expect in the OAuth 2.0 access token.
     */
    value?: string;
}

export interface ApplicationOauth2Permission {
    /**
     * Permission help text that appears in the admin consent and app assignment experiences.
     */
    adminConsentDescription: string;
    /**
     * Display name for the permission that appears in the admin consent and app assignment experiences.
     */
    adminConsentDisplayName: string;
    /**
     * The unique identifier for one of the `OAuth2Permission` or `AppRole` instances that the resource application exposes.
     */
    id: string;
    /**
     * Determines if the app role is enabled: Defaults to `true`.
     */
    isEnabled: boolean;
    /**
     * Type of an application: `webapp/api` or `native`. Defaults to `webapp/api`. For `native` apps type `identifierUris` property can not not be set.
     */
    type: string;
    /**
     * Permission help text that appears in the end user consent experience.
     */
    userConsentDescription: string;
    /**
     * Display name for the permission that appears in the end user consent experience.
     */
    userConsentDisplayName: string;
    /**
     * Specifies the value of the roles claim that the application should expect in the authentication and access tokens.
     */
    value: string;
}

export interface ApplicationOptionalClaims {
    accessTokens?: outputs.ApplicationOptionalClaimsAccessToken[];
    idTokens?: outputs.ApplicationOptionalClaimsIdToken[];
}

export interface ApplicationOptionalClaimsAccessToken {
    /**
     * List of Additional Properties of the claim. If a property exists in this list, it modifies the behaviour of the optional claim.
     */
    additionalProperties?: string[];
    /**
     * Whether the claim specified by the client is necessary to ensure a smooth authorization experience.
     */
    essential?: boolean;
    /**
     * The name of the optional claim.
     */
    name: string;
    /**
     * The source of the claim. If `source` is absent, the claim is a predefined optional claim. If `source` is `user`, the value of `name` is the extension property from the user object.
     */
    source?: string;
}

export interface ApplicationOptionalClaimsIdToken {
    /**
     * List of Additional Properties of the claim. If a property exists in this list, it modifies the behaviour of the optional claim.
     */
    additionalProperties?: string[];
    /**
     * Whether the claim specified by the client is necessary to ensure a smooth authorization experience.
     */
    essential?: boolean;
    /**
     * The display name for the application.
     */
    name: string;
    /**
     * The source of the claim. If `source` is absent, the claim is a predefined optional claim. If `source` is `user`, the value of `name` is the extension property from the user object.
     */
    source?: string;
}

export interface ApplicationRequiredResourceAccess {
    /**
     * A collection of `resourceAccess` blocks as documented below.
     */
    resourceAccesses: outputs.ApplicationRequiredResourceAccessResourceAccess[];
    /**
     * The unique identifier for the resource that the application requires access to. This should be equal to the appId declared on the target resource application.
     */
    resourceAppId: string;
}

export interface ApplicationRequiredResourceAccessResourceAccess {
    /**
     * The unique identifier for one of the `OAuth2Permission` or `AppRole` instances that the resource application exposes.
     */
    id: string;
    /**
     * Specifies whether the id property references an `OAuth2Permission` or an `AppRole`. Possible values are `Scope` or `Role`.
     */
    type: string;
}

export interface GetApplicationAppRole {
    /**
     * Specifies whether this app role definition can be assigned to users and groups, or to other applications (that are accessing this application in daemon service scenarios). Possible values are: `User` and `Application`, or both.
     */
    allowedMemberTypes: string[];
    /**
     * Permission help text that appears in the admin app assignment and consent experiences.
     */
    description: string;
    /**
     * Display name for the permission that appears in the admin consent and app assignment experiences.
     */
    displayName: string;
    /**
     * The unique identifier of the `appRole`.
     */
    id: string;
    /**
     * Determines if the app role is enabled.
     */
    isEnabled: boolean;
    /**
     * Specifies the value of the roles claim that the application should expect in the authentication and access tokens.
     */
    value: string;
}

export interface GetApplicationOauth2Permission {
    /**
     * The description of the admin consent
     */
    adminConsentDescription: string;
    /**
     * The display name of the admin consent
     */
    adminConsentDisplayName: string;
    /**
     * The unique identifier of the `appRole`.
     */
    id: string;
    /**
     * Determines if the app role is enabled.
     */
    isEnabled: boolean;
    /**
     * The type of the permission
     */
    type: string;
    /**
     * The description of the user consent
     */
    userConsentDescription: string;
    /**
     * The display name of the user consent
     */
    userConsentDisplayName: string;
    /**
     * Specifies the value of the roles claim that the application should expect in the authentication and access tokens.
     */
    value: string;
}

export interface GetApplicationOptionalClaims {
    accessTokens?: outputs.GetApplicationOptionalClaimsAccessToken[];
    idTokens?: outputs.GetApplicationOptionalClaimsIdToken[];
}

export interface GetApplicationOptionalClaimsAccessToken {
    /**
     * List of Additional Properties of the claim. If a property exists in this list, it modifies the behaviour of the optional claim.
     */
    additionalProperties?: string[];
    /**
     * Whether the claim specified by the client is necessary to ensure a smooth authorization experience.
     */
    essential?: boolean;
    /**
     * Specifies the name of the Application within Azure Active Directory.
     */
    name: string;
    /**
     * The source of the claim. If `source` is absent, the claim is a predefined optional claim. If `source` is `user`, the value of `name` is the extension property from the user object.
     */
    source?: string;
}

export interface GetApplicationOptionalClaimsIdToken {
    /**
     * List of Additional Properties of the claim. If a property exists in this list, it modifies the behaviour of the optional claim.
     */
    additionalProperties?: string[];
    /**
     * Whether the claim specified by the client is necessary to ensure a smooth authorization experience.
     */
    essential?: boolean;
    /**
     * Specifies the name of the Application within Azure Active Directory.
     */
    name: string;
    /**
     * The source of the claim. If `source` is absent, the claim is a predefined optional claim. If `source` is `user`, the value of `name` is the extension property from the user object.
     */
    source?: string;
}

export interface GetApplicationRequiredResourceAccess {
    /**
     * A collection of `resourceAccess` blocks as documented below
     */
    resourceAccesses: outputs.GetApplicationRequiredResourceAccessResourceAccess[];
    /**
     * The unique identifier for the resource that the application requires access to.
     */
    resourceAppId: string;
}

export interface GetApplicationRequiredResourceAccessResourceAccess {
    /**
     * The unique identifier of the `appRole`.
     */
    id: string;
    /**
     * The type of the permission
     */
    type: string;
}

export interface GetDomainsDomain {
    /**
     * The authentication type of the domain (Managed or Federated).
     */
    authenticationType: string;
    /**
     * The name of the domain.
     */
    domainName: string;
    /**
     * `True` if this is the default domain that is used for user creation.
     */
    isDefault: boolean;
    /**
     * `True` if this is the initial domain created by Azure Activie Directory.
     */
    isInitial: boolean;
    /**
     * `True` if the domain has completed domain ownership verification.
     */
    isVerified: boolean;
}

export interface GetServicePrincipalAppRole {
    /**
     * Specifies whether this app role definition can be assigned to users and groups, or to other applications (that are accessing this application in daemon service scenarios). Possible values are: `User` and `Application`, or both.
     */
    allowedMemberTypes: string[];
    /**
     * Permission help text that appears in the admin app assignment and consent experiences.
     */
    description: string;
    /**
     * The Display Name of the Azure AD Application associated with this Service Principal.
     */
    displayName: string;
    /**
     * The unique identifier of the `appRole`.
     */
    id: string;
    /**
     * Determines if the app role is enabled.
     */
    isEnabled: boolean;
    /**
     * Specifies the value of the roles claim that the application should expect in the authentication and access tokens.
     */
    value: string;
}

export interface GetServicePrincipalOauth2Permission {
    /**
     * The description of the admin consent
     */
    adminConsentDescription: string;
    /**
     * The display name of the admin consent
     */
    adminConsentDisplayName: string;
    /**
     * The unique identifier of the `appRole`.
     */
    id: string;
    /**
     * Determines if the app role is enabled.
     */
    isEnabled: boolean;
    /**
     * The type of the permission
     */
    type: string;
    /**
     * The description of the user consent
     */
    userConsentDescription: string;
    /**
     * The display name of the user consent
     */
    userConsentDisplayName: string;
    /**
     * Specifies the value of the roles claim that the application should expect in the authentication and access tokens.
     */
    value: string;
}

export interface GetUsersUser {
    /**
     * `True` if the account is enabled; otherwise `False`.
     */
    accountEnabled: boolean;
    /**
     * The Display Name of the Azure AD User.
     */
    displayName: string;
    /**
     * The value used to associate an on-premises Active Directory user account with their Azure AD user object.
     */
    immutableId: string;
    /**
     * The primary email address of the Azure AD User.
     */
    mail: string;
    /**
     * The email alias of the Azure AD User.
     */
    mailNickname: string;
    objectId: string;
    /**
     * The on premise sam account name of the Azure AD User.
     */
    onpremisesSamAccountName: string;
    /**
     * The on premise user principal name of the Azure AD User.
     */
    onpremisesUserPrincipalName: string;
    /**
     * The usage location of the Azure AD User.
     */
    usageLocation: string;
    /**
     * The User Principal Name of the Azure AD User.
     */
    userPrincipalName: string;
}

export interface ServicePrincipalOauth2Permission {
    /**
     * The description of the admin consent.
     */
    adminConsentDescription: string;
    /**
     * The display name of the admin consent.
     */
    adminConsentDisplayName: string;
    /**
     * The unique identifier for one of the `OAuth2Permission`.
     */
    id: string;
    /**
     * Is this permission enabled?
     */
    isEnabled: boolean;
    /**
     * The type of the permission.
     */
    type: string;
    /**
     * The description of the user consent.
     */
    userConsentDescription: string;
    /**
     * The display name of the user consent.
     */
    userConsentDisplayName: string;
    /**
     * The name of this permission.
     */
    value: string;
}
