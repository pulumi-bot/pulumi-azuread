// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Manages a Password associated with an Application within Azure Active Directory.
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
 * const exampleApplicationPassword = new azuread.ApplicationPassword("example", {
 *     applicationId: exampleApplication.id,
 *     endDate: "2099-01-01T01:02:03Z",
 *     value: "VT=uSgbTanZhyz@%nL9Hpd+Tfay_MRV#",
 * });
 * ```
 */
export class ApplicationPassword extends pulumi.CustomResource {
    /**
     * Get an existing ApplicationPassword resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationPasswordState, opts?: pulumi.CustomResourceOptions): ApplicationPassword {
        return new ApplicationPassword(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azuread:index/applicationPassword:ApplicationPassword';

    /**
     * Returns true if the given object is an instance of ApplicationPassword.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApplicationPassword {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApplicationPassword.__pulumiType;
    }

    public readonly applicationId!: pulumi.Output<string>;
    /**
     * The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
     */
    public readonly applicationObjectId!: pulumi.Output<string>;
    /**
     * The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
     */
    public readonly endDate!: pulumi.Output<string>;
    /**
     * A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
     */
    public readonly endDateRelative!: pulumi.Output<string | undefined>;
    /**
     * A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
     */
    public readonly keyId!: pulumi.Output<string>;
    /**
     * The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
     */
    public readonly startDate!: pulumi.Output<string>;
    /**
     * The Password for this Application .
     */
    public readonly value!: pulumi.Output<string>;

    /**
     * Create a ApplicationPassword resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ApplicationPasswordArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApplicationPasswordArgs | ApplicationPasswordState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ApplicationPasswordState | undefined;
            inputs["applicationId"] = state ? state.applicationId : undefined;
            inputs["applicationObjectId"] = state ? state.applicationObjectId : undefined;
            inputs["endDate"] = state ? state.endDate : undefined;
            inputs["endDateRelative"] = state ? state.endDateRelative : undefined;
            inputs["keyId"] = state ? state.keyId : undefined;
            inputs["startDate"] = state ? state.startDate : undefined;
            inputs["value"] = state ? state.value : undefined;
        } else {
            const args = argsOrState as ApplicationPasswordArgs | undefined;
            if (!args || args.value === undefined) {
                throw new Error("Missing required property 'value'");
            }
            inputs["applicationId"] = args ? args.applicationId : undefined;
            inputs["applicationObjectId"] = args ? args.applicationObjectId : undefined;
            inputs["endDate"] = args ? args.endDate : undefined;
            inputs["endDateRelative"] = args ? args.endDateRelative : undefined;
            inputs["keyId"] = args ? args.keyId : undefined;
            inputs["startDate"] = args ? args.startDate : undefined;
            inputs["value"] = args ? args.value : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ApplicationPassword.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ApplicationPassword resources.
 */
export interface ApplicationPasswordState {
    readonly applicationId?: pulumi.Input<string>;
    /**
     * The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
     */
    readonly applicationObjectId?: pulumi.Input<string>;
    /**
     * The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
     */
    readonly endDate?: pulumi.Input<string>;
    /**
     * A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
     */
    readonly endDateRelative?: pulumi.Input<string>;
    /**
     * A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
     */
    readonly keyId?: pulumi.Input<string>;
    /**
     * The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
     */
    readonly startDate?: pulumi.Input<string>;
    /**
     * The Password for this Application .
     */
    readonly value?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ApplicationPassword resource.
 */
export interface ApplicationPasswordArgs {
    readonly applicationId?: pulumi.Input<string>;
    /**
     * The Object ID of the Application for which this password should be created. Changing this field forces a new resource to be created.
     */
    readonly applicationObjectId?: pulumi.Input<string>;
    /**
     * The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
     */
    readonly endDate?: pulumi.Input<string>;
    /**
     * A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
     */
    readonly endDateRelative?: pulumi.Input<string>;
    /**
     * A GUID used to uniquely identify this Password. If not specified a GUID will be created. Changing this field forces a new resource to be created.
     */
    readonly keyId?: pulumi.Input<string>;
    /**
     * The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
     */
    readonly startDate?: pulumi.Input<string>;
    /**
     * The Password for this Application .
     */
    readonly value: pulumi.Input<string>;
}
