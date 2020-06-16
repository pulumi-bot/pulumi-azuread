// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages a Certificate associated with an Application within Azure Active Directory.
 *
 * > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuread from "@pulumi/azuread";
 * import * as fs from "fs";
 *
 * const exampleApplication = new azuread.Application("example", {});
 * const exampleApplicationCertificate = new azuread.ApplicationCertificate("example", {
 *     applicationObjectId: exampleApplication.id,
 *     endDate: "2021-05-01T01:02:03Z",
 *     type: "AsymmetricX509Cert",
 *     value: fs.readFileSync("cert.pem", "utf-8"),
 * });
 * ```
 *
 * {{% examples %}}
 * {{% /examples %}}
 */
export class ApplicationCertificate extends pulumi.CustomResource {
    /**
     * Get an existing ApplicationCertificate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationCertificateState, opts?: pulumi.CustomResourceOptions): ApplicationCertificate {
        return new ApplicationCertificate(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azuread:index/applicationCertificate:ApplicationCertificate';

    /**
     * Returns true if the given object is an instance of ApplicationCertificate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApplicationCertificate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApplicationCertificate.__pulumiType;
    }

    /**
     * The Object ID of the Application for which this Certificate should be created. Changing this field forces a new resource to be created.
     */
    public readonly applicationObjectId!: pulumi.Output<string>;
    /**
     * The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
     */
    public readonly endDate!: pulumi.Output<string>;
    /**
     * A relative duration for which the Certificate is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
     */
    public readonly endDateRelative!: pulumi.Output<string | undefined>;
    /**
     * A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.
     */
    public readonly keyId!: pulumi.Output<string>;
    /**
     * The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
     */
    public readonly startDate!: pulumi.Output<string>;
    /**
     * The type of key/certificate. Must be one of `AsymmetricX509Cert` or `Symmetric`. Changing this fields forces a new resource to be created.
     */
    public readonly type!: pulumi.Output<string | undefined>;
    /**
     * The Certificate for this Service Principal.
     */
    public readonly value!: pulumi.Output<string>;

    /**
     * Create a ApplicationCertificate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ApplicationCertificateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApplicationCertificateArgs | ApplicationCertificateState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ApplicationCertificateState | undefined;
            inputs["applicationObjectId"] = state ? state.applicationObjectId : undefined;
            inputs["endDate"] = state ? state.endDate : undefined;
            inputs["endDateRelative"] = state ? state.endDateRelative : undefined;
            inputs["keyId"] = state ? state.keyId : undefined;
            inputs["startDate"] = state ? state.startDate : undefined;
            inputs["type"] = state ? state.type : undefined;
            inputs["value"] = state ? state.value : undefined;
        } else {
            const args = argsOrState as ApplicationCertificateArgs | undefined;
            if (!args || args.applicationObjectId === undefined) {
                throw new Error("Missing required property 'applicationObjectId'");
            }
            if (!args || args.value === undefined) {
                throw new Error("Missing required property 'value'");
            }
            inputs["applicationObjectId"] = args ? args.applicationObjectId : undefined;
            inputs["endDate"] = args ? args.endDate : undefined;
            inputs["endDateRelative"] = args ? args.endDateRelative : undefined;
            inputs["keyId"] = args ? args.keyId : undefined;
            inputs["startDate"] = args ? args.startDate : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["value"] = args ? args.value : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ApplicationCertificate.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ApplicationCertificate resources.
 */
export interface ApplicationCertificateState {
    /**
     * The Object ID of the Application for which this Certificate should be created. Changing this field forces a new resource to be created.
     */
    readonly applicationObjectId?: pulumi.Input<string>;
    /**
     * The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
     */
    readonly endDate?: pulumi.Input<string>;
    /**
     * A relative duration for which the Certificate is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
     */
    readonly endDateRelative?: pulumi.Input<string>;
    /**
     * A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.
     */
    readonly keyId?: pulumi.Input<string>;
    /**
     * The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
     */
    readonly startDate?: pulumi.Input<string>;
    /**
     * The type of key/certificate. Must be one of `AsymmetricX509Cert` or `Symmetric`. Changing this fields forces a new resource to be created.
     */
    readonly type?: pulumi.Input<string>;
    /**
     * The Certificate for this Service Principal.
     */
    readonly value?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ApplicationCertificate resource.
 */
export interface ApplicationCertificateArgs {
    /**
     * The Object ID of the Application for which this Certificate should be created. Changing this field forces a new resource to be created.
     */
    readonly applicationObjectId: pulumi.Input<string>;
    /**
     * The End Date which the Certificate is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
     */
    readonly endDate?: pulumi.Input<string>;
    /**
     * A relative duration for which the Certificate is valid until, for example `240h` (10 days) or `2400h30m`. Changing this field forces a new resource to be created.
     */
    readonly endDateRelative?: pulumi.Input<string>;
    /**
     * A GUID used to uniquely identify this Certificate. If not specified a GUID will be created. Changing this field forces a new resource to be created.
     */
    readonly keyId?: pulumi.Input<string>;
    /**
     * The Start Date which the Certificate is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
     */
    readonly startDate?: pulumi.Input<string>;
    /**
     * The type of key/certificate. Must be one of `AsymmetricX509Cert` or `Symmetric`. Changing this fields forces a new resource to be created.
     */
    readonly type?: pulumi.Input<string>;
    /**
     * The Certificate for this Service Principal.
     */
    readonly value: pulumi.Input<string>;
}
