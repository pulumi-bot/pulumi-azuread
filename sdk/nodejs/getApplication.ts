// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Use this data source to access information about an existing Application within Azure Active Directory.
 *
 * > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all (or owned by) applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuread from "@pulumi/azuread";
 *
 * const example = pulumi.output(azuread.getApplication({
 *     name: "My First AzureAD Application",
 * }, { async: true }));
 *
 * export const azureAdObjectId = example.id;
 * ```
 */
export function getApplication(args?: GetApplicationArgs, opts?: pulumi.InvokeOptions): Promise<GetApplicationResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("azuread:index/getApplication:getApplication", {
        "name": args.name,
        "oauth2Permissions": args.oauth2Permissions,
        "objectId": args.objectId,
        "optionalClaims": args.optionalClaims,
    }, opts);
}

/**
 * A collection of arguments for invoking getApplication.
 */
export interface GetApplicationArgs {
    /**
     * Specifies the name of the Application within Azure Active Directory.
     */
    readonly name?: string;
    /**
     * A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a `oauth2Permission` block as documented below.
     */
    readonly oauth2Permissions?: inputs.GetApplicationOauth2Permission[];
    /**
     * Specifies the Object ID of the Application within Azure Active Directory.
     */
    readonly objectId?: string;
    /**
     * A collection of `accessToken` or `idToken` blocks as documented below which list the optional claims configured for each token type. For more information see https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims
     */
    readonly optionalClaims?: inputs.GetApplicationOptionalClaims;
}

/**
 * A collection of values returned by getApplication.
 */
export interface GetApplicationResult {
    /**
     * A collection of `appRole` blocks as documented below. For more information https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles
     */
    readonly appRoles: outputs.GetApplicationAppRole[];
    /**
     * the Application ID of the Azure Active Directory Application.
     */
    readonly applicationId: string;
    /**
     * Is this Azure AD Application available to other tenants?
     */
    readonly availableToOtherTenants: boolean;
    /**
     * The `groups` claim issued in a user or OAuth 2.0 access token that the app expects.
     */
    readonly groupMembershipClaims: string;
    readonly homepage: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
     */
    readonly identifierUris: string[];
    /**
     * The URL of the logout page.
     */
    readonly logoutUrl: string;
    /**
     * The name of the optional claim.
     */
    readonly name: string;
    /**
     * Does this Azure AD Application allow OAuth2.0 implicit flow tokens?
     */
    readonly oauth2AllowImplicitFlow: boolean;
    /**
     * A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by a `oauth2Permission` block as documented below.
     */
    readonly oauth2Permissions: outputs.GetApplicationOauth2Permission[];
    /**
     * the Object ID of the Azure Active Directory Application.
     */
    readonly objectId: string;
    /**
     * A collection of `accessToken` or `idToken` blocks as documented below which list the optional claims configured for each token type. For more information see https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims
     */
    readonly optionalClaims?: outputs.GetApplicationOptionalClaims;
    /**
     * A list of User Object IDs that are assigned ownership of the application registration.
     */
    readonly owners: string[];
    /**
     * A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.
     */
    readonly replyUrls: string[];
    /**
     * A collection of `requiredResourceAccess` blocks as documented below.
     */
    readonly requiredResourceAccesses: outputs.GetApplicationRequiredResourceAccess[];
    /**
     * The type of the permission
     */
    readonly type: string;
}
