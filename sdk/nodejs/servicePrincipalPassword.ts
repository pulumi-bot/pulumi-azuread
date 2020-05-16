// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Manages a Password associated with a Service Principal within Azure Active Directory.
 *
 * > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuread from "@pulumi/azuread";
 *
 * const exampleApplication = new azuread.Application("example", {
 *     availableToOtherTenants: false,
 *     homepage: "http://homepage",
 *     identifierUris: ["http://uri"],
 *     oauth2AllowImplicitFlow: true,
 *     replyUrls: ["http://replyurl"],
 * });
 * const exampleServicePrincipal = new azuread.ServicePrincipal("example", {
 *     applicationId: exampleApplication.applicationId,
 * });
 * const exampleServicePrincipalPassword = new azuread.ServicePrincipalPassword("example", {
 *     endDate: "2099-01-01T01:02:03Z",
 *     servicePrincipalId: exampleServicePrincipal.id,
 *     value: "VT=uSgbTanZhyz@%nL9Hpd+Tfay_MRV#",
 * });
 * ```
 */
export class ServicePrincipalPassword extends pulumi.CustomResource {
    /**
     * Get an existing ServicePrincipalPassword resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServicePrincipalPasswordState, opts?: pulumi.CustomResourceOptions): ServicePrincipalPassword {
        return new ServicePrincipalPassword(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azuread:index/servicePrincipalPassword:ServicePrincipalPassword';

    /**
     * Returns true if the given object is an instance of ServicePrincipalPassword.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ServicePrincipalPassword {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ServicePrincipalPassword.__pulumiType;
    }

    /**
     * The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
     */
    public readonly endDate!: pulumi.Output<string>;
    /**
     * A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". Changing this field forces a new resource to be created.
     */
    public readonly endDateRelative!: pulumi.Output<string | undefined>;
    /**
     * A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.
     */
    public readonly keyId!: pulumi.Output<string>;
    /**
     * The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.
     */
    public readonly servicePrincipalId!: pulumi.Output<string>;
    /**
     * The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
     */
    public readonly startDate!: pulumi.Output<string>;
    /**
     * The Password for this Service Principal.
     */
    public readonly value!: pulumi.Output<string>;

    /**
     * Create a ServicePrincipalPassword resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ServicePrincipalPasswordArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ServicePrincipalPasswordArgs | ServicePrincipalPasswordState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ServicePrincipalPasswordState | undefined;
            inputs["endDate"] = state ? state.endDate : undefined;
            inputs["endDateRelative"] = state ? state.endDateRelative : undefined;
            inputs["keyId"] = state ? state.keyId : undefined;
            inputs["servicePrincipalId"] = state ? state.servicePrincipalId : undefined;
            inputs["startDate"] = state ? state.startDate : undefined;
            inputs["value"] = state ? state.value : undefined;
        } else {
            const args = argsOrState as ServicePrincipalPasswordArgs | undefined;
            if (!args || args.servicePrincipalId === undefined) {
                throw new Error("Missing required property 'servicePrincipalId'");
            }
            if (!args || args.value === undefined) {
                throw new Error("Missing required property 'value'");
            }
            inputs["endDate"] = args ? args.endDate : undefined;
            inputs["endDateRelative"] = args ? args.endDateRelative : undefined;
            inputs["keyId"] = args ? args.keyId : undefined;
            inputs["servicePrincipalId"] = args ? args.servicePrincipalId : undefined;
            inputs["startDate"] = args ? args.startDate : undefined;
            inputs["value"] = args ? args.value : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ServicePrincipalPassword.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ServicePrincipalPassword resources.
 */
export interface ServicePrincipalPasswordState {
    /**
     * The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
     */
    readonly endDate?: pulumi.Input<string>;
    /**
     * A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". Changing this field forces a new resource to be created.
     */
    readonly endDateRelative?: pulumi.Input<string>;
    /**
     * A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.
     */
    readonly keyId?: pulumi.Input<string>;
    /**
     * The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.
     */
    readonly servicePrincipalId?: pulumi.Input<string>;
    /**
     * The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
     */
    readonly startDate?: pulumi.Input<string>;
    /**
     * The Password for this Service Principal.
     */
    readonly value?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ServicePrincipalPassword resource.
 */
export interface ServicePrincipalPasswordArgs {
    /**
     * The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
     */
    readonly endDate?: pulumi.Input<string>;
    /**
     * A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". Changing this field forces a new resource to be created.
     */
    readonly endDateRelative?: pulumi.Input<string>;
    /**
     * A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.
     */
    readonly keyId?: pulumi.Input<string>;
    /**
     * The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.
     */
    readonly servicePrincipalId: pulumi.Input<string>;
    /**
     * The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
     */
    readonly startDate?: pulumi.Input<string>;
    /**
     * The Password for this Service Principal.
     */
    readonly value: pulumi.Input<string>;
}
