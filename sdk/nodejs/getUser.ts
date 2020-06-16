// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Gets information about an Azure Active Directory user.
 *
 * > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read directory data` within the `Windows Azure Active Directory` API.
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuread from "@pulumi/azuread";
 *
 * const example = pulumi.output(azuread.getUser({
 *     userPrincipalName: "user@hashicorp.com",
 * }, { async: true }));
 * ```
 *
 * {{% examples %}}
 * {{% /examples %}}
 */
export function getUser(args?: GetUserArgs, opts?: pulumi.InvokeOptions): Promise<GetUserResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("azuread:index/getUser:getUser", {
        "mailNickname": args.mailNickname,
        "objectId": args.objectId,
        "userPrincipalName": args.userPrincipalName,
    }, opts);
}

/**
 * A collection of arguments for invoking getUser.
 */
export interface GetUserArgs {
    /**
     * The email alias of the Azure AD User.
     */
    readonly mailNickname?: string;
    /**
     * Specifies the Object ID of the Application within Azure Active Directory.
     */
    readonly objectId?: string;
    /**
     * The User Principal Name of the Azure AD User.
     */
    readonly userPrincipalName?: string;
}

/**
 * A collection of values returned by getUser.
 */
export interface GetUserResult {
    /**
     * `True` if the account is enabled; otherwise `False`.
     */
    readonly accountEnabled: boolean;
    /**
     * The Display Name of the Azure AD User.
     */
    readonly displayName: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The value used to associate an on-premises Active Directory user account with their Azure AD user object.
     */
    readonly immutableId: string;
    /**
     * The primary email address of the Azure AD User.
     */
    readonly mail: string;
    /**
     * The email alias of the Azure AD User.
     */
    readonly mailNickname: string;
    readonly objectId: string;
    /**
     * The on premise sam account name of the Azure AD User.
     */
    readonly onpremisesSamAccountName: string;
    /**
     * The on premise user principal name of the Azure AD User.
     */
    readonly onpremisesUserPrincipalName: string;
    /**
     * The usage location of the Azure AD User.
     */
    readonly usageLocation: string;
    /**
     * The User Principal Name of the Azure AD User.
     */
    readonly userPrincipalName: string;
}
