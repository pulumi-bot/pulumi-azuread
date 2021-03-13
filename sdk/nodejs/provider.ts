// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The provider type for the azuread package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
 */
export class Provider extends pulumi.ProviderResource {
    /** @internal */
    public static readonly __pulumiType = 'azuread';

    /**
     * Returns true if the given object is an instance of Provider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Provider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Provider.__pulumiType;
    }


    /**
     * Create a Provider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProviderArgs, opts?: pulumi.ResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        {
            if ((!args || args.metadataHost === undefined) && !opts.urn) {
                throw new Error("Missing required property 'metadataHost'");
            }
            inputs["clientCertificatePassword"] = args ? args.clientCertificatePassword : undefined;
            inputs["clientCertificatePath"] = args ? args.clientCertificatePath : undefined;
            inputs["clientId"] = args ? args.clientId : undefined;
            inputs["clientSecret"] = args ? args.clientSecret : undefined;
            inputs["disableTerraformPartnerId"] = pulumi.output(args ? args.disableTerraformPartnerId : undefined).apply(JSON.stringify);
            inputs["environment"] = (args ? args.environment : undefined) ?? (utilities.getEnv("ARM_ENVIRONMENT") || "public");
            inputs["metadataHost"] = args ? args.metadataHost : undefined;
            inputs["msiEndpoint"] = (args ? args.msiEndpoint : undefined) ?? (utilities.getEnv("ARM_MSI_ENDPOINT") || "");
            inputs["partnerId"] = args ? args.partnerId : undefined;
            inputs["tenantId"] = args ? args.tenantId : undefined;
            inputs["useMsi"] = pulumi.output((args ? args.useMsi : undefined) ?? (<any>utilities.getEnvBoolean("ARM_USE_MSI") || false)).apply(JSON.stringify);
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Provider.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Provider resource.
 */
export interface ProviderArgs {
    readonly clientCertificatePassword?: pulumi.Input<string>;
    /**
     * The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service
     * Principal using a Client Certificate.
     */
    readonly clientCertificatePath?: pulumi.Input<string>;
    /**
     * The Client ID which should be used for service principal authentication.
     */
    readonly clientId?: pulumi.Input<string>;
    /**
     * The password to decrypt the Client Certificate. For use when authenticating as a Service Principal using a Client
     * Certificate
     */
    readonly clientSecret?: pulumi.Input<string>;
    /**
     * Disable the Terraform Partner ID which is used if a custom `partner_id` isn't specified.
     */
    readonly disableTerraformPartnerId?: pulumi.Input<boolean>;
    /**
     * The Cloud Environment which should be used. Possible values are `public`, `usgovernment`, `german`, and `china`.
     * Defaults to `public`.
     */
    readonly environment?: pulumi.Input<string>;
    /**
     * The Hostname which should be used for the Azure Metadata Service.
     */
    readonly metadataHost: pulumi.Input<string>;
    /**
     * The path to a custom endpoint for Managed Service Identity - in most circumstances this should be detected
     * automatically.
     */
    readonly msiEndpoint?: pulumi.Input<string>;
    /**
     * A GUID/UUID that is registered with Microsoft to facilitate partner resource usage attribution.
     */
    readonly partnerId?: pulumi.Input<string>;
    /**
     * The Tenant ID which should be used. Works with all authentication methods except MSI.
     */
    readonly tenantId?: pulumi.Input<string>;
    /**
     * Allow Managed Service Identity to be used for Authentication.
     */
    readonly useMsi?: pulumi.Input<boolean>;
}
