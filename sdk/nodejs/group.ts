// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Group extends pulumi.CustomResource {
    /**
     * Get an existing Group resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
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
     * A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.
     */
    public readonly members!: pulumi.Output<string[]>;
    /**
     * The display name for the Group. Changing this forces a new resource to be created.
     */
    public readonly name!: pulumi.Output<string>;
    public /*out*/ readonly objectId!: pulumi.Output<string>;
    /**
     * A set of owners who own this Group. Supported Object types are Users or Service Principals.
     */
    public readonly owners!: pulumi.Output<string[]>;

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
            inputs["members"] = state ? state.members : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["objectId"] = state ? state.objectId : undefined;
            inputs["owners"] = state ? state.owners : undefined;
        } else {
            const args = argsOrState as GroupArgs | undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["members"] = args ? args.members : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["owners"] = args ? args.owners : undefined;
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
    readonly description?: pulumi.Input<string>;
    /**
     * A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.
     */
    readonly members?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The display name for the Group. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    readonly objectId?: pulumi.Input<string>;
    /**
     * A set of owners who own this Group. Supported Object types are Users or Service Principals.
     */
    readonly owners?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a Group resource.
 */
export interface GroupArgs {
    /**
     * The description for the Group.  Changing this forces a new resource to be created.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A set of members who should be present in this Group. Supported Object types are Users, Groups or Service Principals.
     */
    readonly members?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The display name for the Group. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A set of owners who own this Group. Supported Object types are Users or Service Principals.
     */
    readonly owners?: pulumi.Input<pulumi.Input<string>[]>;
}
