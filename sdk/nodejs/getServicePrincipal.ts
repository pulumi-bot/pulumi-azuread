// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Gets information about an existing Service Principal associated with an Application within Azure Active Directory.
 *
 * > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
 *
 * ## Example Usage
 * ### By Application Display Name)
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuread from "@pulumi/azuread";
 *
 * const example = pulumi.output(azuread.getServicePrincipal({
 *     displayName: "my-awesome-application",
 * }, { async: true }));
 * ```
 * ### By Application ID)
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuread from "@pulumi/azuread";
 *
 * const example = pulumi.output(azuread.getServicePrincipal({
 *     applicationId: "00000000-0000-0000-0000-000000000000",
 * }, { async: true }));
 * ```
 * ### By Object ID)
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuread from "@pulumi/azuread";
 *
 * const example = pulumi.output(azuread.getServicePrincipal({
 *     objectId: "00000000-0000-0000-0000-000000000000",
 * }, { async: true }));
 * ```
 */
export function getServicePrincipal(args?: GetServicePrincipalArgs, opts?: pulumi.InvokeOptions): Promise<GetServicePrincipalResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("azuread:index/getServicePrincipal:getServicePrincipal", {
        "applicationId": args.applicationId,
        "displayName": args.displayName,
        "oauth2Permissions": args.oauth2Permissions,
        "objectId": args.objectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getServicePrincipal.
 */
export interface GetServicePrincipalArgs {
    /**
     * The ID of the Azure AD Application.
     */
    readonly applicationId?: string;
    /**
     * The Display Name of the Azure AD Application associated with this Service Principal.
     */
    readonly displayName?: string;
    /**
     * A collection of OAuth 2.0 permissions exposed by the associated application. Each permission is covered by a `oauth2Permission` block as documented below.
     */
    readonly oauth2Permissions?: inputs.GetServicePrincipalOauth2Permission[];
    /**
     * The ID of the Azure AD Service Principal.
     */
    readonly objectId?: string;
}

/**
 * A collection of values returned by getServicePrincipal.
 */
export interface GetServicePrincipalResult {
    readonly appRoles: outputs.GetServicePrincipalAppRole[];
    readonly applicationId: string;
    /**
     * Display name for the permission that appears in the admin consent and app assignment experiences.
     */
    readonly displayName: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly oauth2Permissions: outputs.GetServicePrincipalOauth2Permission[];
    readonly objectId: string;
}
