// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Gets information about an Azure Active Directory group.
 * 
 * > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read directory data` within the `Windows Azure Active Directory` API.
 * 
 * ## Example Usage (by Group Display Name)
 * 
 * {{ % example typescript % }}
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuread from "@pulumi/azuread";
 * 
 * const example = pulumi.output(azuread.getGroup({
 *     name: "A-AD-Group",
 * }, { async: true }));
 * ```
 * {{ % /example % }}
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-azuread/blob/master/website/docs/d/group.html.markdown.
 */
export function getGroup(args?: GetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetGroupResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("azuread:index/getGroup:getGroup", {
        "name": args.name,
        "objectId": args.objectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getGroup.
 */
export interface GetGroupArgs {
    /**
     * The Name of the AD Group we want to lookup.
     */
    readonly name?: string;
    /**
     * Specifies the Object ID of the AD Group within Azure Active Directory.
     */
    readonly objectId?: string;
}

/**
 * A collection of values returned by getGroup.
 */
export interface GetGroupResult {
    /**
     * The description of the AD Group.
     */
    readonly description: string;
    /**
     * The Object IDs of the Azure AD Group members.
     */
    readonly members: string[];
    /**
     * The name of the Azure AD Group.
     */
    readonly name: string;
    readonly objectId: string;
    /**
     * The Object IDs of the Azure AD Group owners.
     */
    readonly owners: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
