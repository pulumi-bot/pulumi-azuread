// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages a single Group Membership within Azure Active Directory.
 *
 * > **NOTE:** Do not use this resource at the same time as `azuread_group.members`.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuread from "@pulumi/azuread";
 *
 * const exampleUser = azuread.getUser({
 *     userPrincipalName: "jdoe@hashicorp.com",
 * });
 * const exampleGroup = new azuread.Group("exampleGroup", {});
 * const exampleGroupMember = new azuread.GroupMember("exampleGroupMember", {
 *     groupObjectId: exampleGroup.id,
 *     memberObjectId: exampleUser.then(exampleUser => exampleUser.id),
 * });
 * ```
 *
 * ## Import
 *
 * Azure Active Directory Group Members can be imported using the `object id`, e.g.
 *
 * ```sh
 *  $ pulumi import azuread:index/groupMember:GroupMember test 00000000-0000-0000-0000-000000000000/member/11111111-1111-1111-1111-111111111111
 * ```
 */
export class GroupMember extends pulumi.CustomResource {
    /**
     * Get an existing GroupMember resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupMemberState, opts?: pulumi.CustomResourceOptions): GroupMember {
        return new GroupMember(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azuread:index/groupMember:GroupMember';

    /**
     * Returns true if the given object is an instance of GroupMember.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GroupMember {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GroupMember.__pulumiType;
    }

    /**
     * The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
     */
    public readonly groupObjectId!: pulumi.Output<string>;
    /**
     * The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.
     */
    public readonly memberObjectId!: pulumi.Output<string>;

    /**
     * Create a GroupMember resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GroupMemberArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GroupMemberArgs | GroupMemberState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as GroupMemberState | undefined;
            inputs["groupObjectId"] = state ? state.groupObjectId : undefined;
            inputs["memberObjectId"] = state ? state.memberObjectId : undefined;
        } else {
            const args = argsOrState as GroupMemberArgs | undefined;
            if (!args || args.groupObjectId === undefined) {
                throw new Error("Missing required property 'groupObjectId'");
            }
            if (!args || args.memberObjectId === undefined) {
                throw new Error("Missing required property 'memberObjectId'");
            }
            inputs["groupObjectId"] = args ? args.groupObjectId : undefined;
            inputs["memberObjectId"] = args ? args.memberObjectId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(GroupMember.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GroupMember resources.
 */
export interface GroupMemberState {
    /**
     * The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
     */
    readonly groupObjectId?: pulumi.Input<string>;
    /**
     * The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.
     */
    readonly memberObjectId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a GroupMember resource.
 */
export interface GroupMemberArgs {
    /**
     * The Object ID of the Azure AD Group you want to add the Member to.  Changing this forces a new resource to be created.
     */
    readonly groupObjectId: pulumi.Input<string>;
    /**
     * The Object ID of the Azure AD Object you want to add as a Member to the Group. Supported Object types are Users, Groups or Service Principals. Changing this forces a new resource to be created.
     */
    readonly memberObjectId: pulumi.Input<string>;
}
