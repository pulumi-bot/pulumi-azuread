// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages a Group within Azure Active Directory.
 *
 * > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read and write all groups` within the `Windows Azure Active Directory` API. In addition it must also have either the `Company Administrator` or `User Account Administrator` Azure Active Directory roles assigned in order to be able to delete groups. You can assign one of the required Azure Active Directory Roles with the **AzureAD PowerShell Module**, which is available for Windows PowerShell or in the Azure Cloud Shell. Please refer to [this documentation](https://docs.microsoft.com/en-us/powershell/module/azuread/add-azureaddirectoryrolemember) for more details.
 *
 * ## Example Usage
 *
 * *Basic example*
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuread from "@pulumi/azuread";
 *
 * const example = new azuread.Group("example", {
 *     displayName: "A-AD-Group",
 * });
 * ```
 *
 * *A group with members*
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuread from "@pulumi/azuread";
 *
 * const exampleUser = new azuread.User("exampleUser", {
 *     displayName: "J Doe",
 *     password: "notSecure123",
 *     userPrincipalName: "jdoe@hashicorp.com",
 * });
 * const exampleGroup = new azuread.Group("exampleGroup", {
 *     displayName: "MyGroup",
 *     members: [exampleUser.objectId],
 * });
 * ```
 *
 * ## Import
 *
 * Azure Active Directory Groups can be imported using the `object id`, e.g.
 *
 * ```sh
 *  $ pulumi import azuread:index/group:Group my_group 00000000-0000-0000-0000-000000000000
 * ```
 */
export class Group extends pulumi.CustomResource {
    /**
     * Get an existing Group resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupState, opts?: pulumi.CustomResourceOptions): Group {
        return new Group(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azuread:index/group:Group';

    /**
     * Returns true if the given object is an instance of Group.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Group {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Group.__pulumiType;
    }

    /**
     * The description for the Group.  Changing this forces a new resource to be created.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The display name for the Group. Changing this forces a new resource to be created.
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.
     */
    public readonly members!: pulumi.Output<string[]>;
    /**
     * @deprecated This property has been renamed to `display_name` and will be removed in v2.0 of this provider.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The Object ID of the Group.
     */
    public /*out*/ readonly objectId!: pulumi.Output<string>;
    /**
     * A set of owners who own this Group. Supported Object types are Users or Service Principals.
     */
    public readonly owners!: pulumi.Output<string[]>;
    /**
     * If `true`, will return an error when an existing Group is found with the same name. Defaults to `false`.
     */
    public readonly preventDuplicateNames!: pulumi.Output<boolean | undefined>;

    /**
     * Create a Group resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: GroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GroupArgs | GroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as GroupState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["displayName"] = state ? state.displayName : undefined;
            inputs["members"] = state ? state.members : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["objectId"] = state ? state.objectId : undefined;
            inputs["owners"] = state ? state.owners : undefined;
            inputs["preventDuplicateNames"] = state ? state.preventDuplicateNames : undefined;
        } else {
            const args = argsOrState as GroupArgs | undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["displayName"] = args ? args.displayName : undefined;
            inputs["members"] = args ? args.members : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["owners"] = args ? args.owners : undefined;
            inputs["preventDuplicateNames"] = args ? args.preventDuplicateNames : undefined;
            inputs["objectId"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Group.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Group resources.
 */
export interface GroupState {
    /**
     * The description for the Group.  Changing this forces a new resource to be created.
     */
    readonly description?: pulumi.Input<string | undefined>;
    /**
     * The display name for the Group. Changing this forces a new resource to be created.
     */
    readonly displayName?: pulumi.Input<string | undefined>;
    /**
     * A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.
     */
    readonly members?: pulumi.Input<pulumi.Input<string>[] | undefined>;
    /**
     * @deprecated This property has been renamed to `display_name` and will be removed in v2.0 of this provider.
     */
    readonly name?: pulumi.Input<string | undefined>;
    /**
     * The Object ID of the Group.
     */
    readonly objectId?: pulumi.Input<string | undefined>;
    /**
     * A set of owners who own this Group. Supported Object types are Users or Service Principals.
     */
    readonly owners?: pulumi.Input<pulumi.Input<string>[] | undefined>;
    /**
     * If `true`, will return an error when an existing Group is found with the same name. Defaults to `false`.
     */
    readonly preventDuplicateNames?: pulumi.Input<boolean | undefined>;
}

/**
 * The set of arguments for constructing a Group resource.
 */
export interface GroupArgs {
    /**
     * The description for the Group.  Changing this forces a new resource to be created.
     */
    readonly description?: pulumi.Input<string | undefined>;
    /**
     * The display name for the Group. Changing this forces a new resource to be created.
     */
    readonly displayName?: pulumi.Input<string | undefined>;
    /**
     * A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.
     */
    readonly members?: pulumi.Input<pulumi.Input<string>[] | undefined>;
    /**
     * @deprecated This property has been renamed to `display_name` and will be removed in v2.0 of this provider.
     */
    readonly name?: pulumi.Input<string | undefined>;
    /**
     * A set of owners who own this Group. Supported Object types are Users or Service Principals.
     */
    readonly owners?: pulumi.Input<pulumi.Input<string>[] | undefined>;
    /**
     * If `true`, will return an error when an existing Group is found with the same name. Defaults to `false`.
     */
    readonly preventDuplicateNames?: pulumi.Input<boolean | undefined>;
}
