// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Gets Object IDs or Display Names for multiple Azure Active Directory groups.
 *
 * > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read directory data` within the `Windows Azure Active Directory` API.
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuread from "@pulumi/azuread";
 *
 * const groups = pulumi.output(azuread.getGroups({
 *     names: [
 *         "group-a",
 *         "group-b",
 *     ],
 * }, { async: true }));
 * ```
 */
export function getGroups(args?: GetGroupsArgs, opts?: pulumi.InvokeOptions): Promise<GetGroupsResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("azuread:index/getGroups:getGroups", {
        "names": args.names,
        "objectIds": args.objectIds,
    }, opts);
}

/**
 * A collection of arguments for invoking getGroups.
 */
export interface GetGroupsArgs {
    /**
     * The Display Names of the Azure AD Groups.
     */
    readonly names?: string[];
    /**
     * The Object IDs of the Azure AD Groups.
     */
    readonly objectIds?: string[];
}

/**
 * A collection of values returned by getGroups.
 */
export interface GetGroupsResult {
    /**
     * The Display Names of the Azure AD Groups.
     */
    readonly names: string[];
    /**
     * The Object IDs of the Azure AD Groups.
     */
    readonly objectIds: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
