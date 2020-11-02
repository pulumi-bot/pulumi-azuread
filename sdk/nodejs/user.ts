// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages a User within Azure Active Directory.
 *
 * > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Directory.ReadWrite.All` within the `Windows Azure Active Directory` API.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuread from "@pulumi/azuread";
 *
 * const example = new azuread.User("example", {
 *     displayName: "J. Doe",
 *     mailNickname: "jdoe",
 *     password: "SecretP@sswd99!",
 *     userPrincipalName: "jdoe@hashicorp.com",
 * });
 * ```
 *
 * ## Import
 *
 * Azure Active Directory Users can be imported using the `object id`, e.g.
 */
export class User extends pulumi.CustomResource {
    /**
     * Get an existing User resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserState, opts?: pulumi.CustomResourceOptions): User {
        return new User(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azuread:index/user:User';

    /**
     * Returns true if the given object is an instance of User.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is User {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === User.__pulumiType;
    }

    /**
     * `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
     */
    public readonly accountEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The name to display in the address book for the user.
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
     */
    public readonly forcePasswordChange!: pulumi.Output<boolean | undefined>;
    /**
     * The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
     */
    public readonly immutableId!: pulumi.Output<string>;
    /**
     * The primary email address of the Azure AD User.
     */
    public /*out*/ readonly mail!: pulumi.Output<string>;
    /**
     * The mail alias for the user. Defaults to the user name part of the User Principal Name.
     */
    public readonly mailNickname!: pulumi.Output<string>;
    /**
     * The Object ID of the Azure AD User.
     */
    public /*out*/ readonly objectId!: pulumi.Output<string>;
    /**
     * The on premise sam account name of the Azure AD User.
     */
    public /*out*/ readonly onpremisesSamAccountName!: pulumi.Output<string>;
    /**
     * The on premise user principal name of the Azure AD User.
     */
    public /*out*/ readonly onpremisesUserPrincipalName!: pulumi.Output<string>;
    /**
     * The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
     */
    public readonly password!: pulumi.Output<string>;
    /**
     * The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set.
     */
    public readonly usageLocation!: pulumi.Output<string>;
    /**
     * The User Principal Name of the Azure AD User.
     */
    public readonly userPrincipalName!: pulumi.Output<string>;

    /**
     * Create a User resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: UserArgs | UserState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as UserState | undefined;
            inputs["accountEnabled"] = state ? state.accountEnabled : undefined;
            inputs["displayName"] = state ? state.displayName : undefined;
            inputs["forcePasswordChange"] = state ? state.forcePasswordChange : undefined;
            inputs["immutableId"] = state ? state.immutableId : undefined;
            inputs["mail"] = state ? state.mail : undefined;
            inputs["mailNickname"] = state ? state.mailNickname : undefined;
            inputs["objectId"] = state ? state.objectId : undefined;
            inputs["onpremisesSamAccountName"] = state ? state.onpremisesSamAccountName : undefined;
            inputs["onpremisesUserPrincipalName"] = state ? state.onpremisesUserPrincipalName : undefined;
            inputs["password"] = state ? state.password : undefined;
            inputs["usageLocation"] = state ? state.usageLocation : undefined;
            inputs["userPrincipalName"] = state ? state.userPrincipalName : undefined;
        } else {
            const args = argsOrState as UserArgs | undefined;
            if (!args || args.displayName === undefined) {
                throw new Error("Missing required property 'displayName'");
            }
            if (!args || args.password === undefined) {
                throw new Error("Missing required property 'password'");
            }
            if (!args || args.userPrincipalName === undefined) {
                throw new Error("Missing required property 'userPrincipalName'");
            }
            inputs["accountEnabled"] = args ? args.accountEnabled : undefined;
            inputs["displayName"] = args ? args.displayName : undefined;
            inputs["forcePasswordChange"] = args ? args.forcePasswordChange : undefined;
            inputs["immutableId"] = args ? args.immutableId : undefined;
            inputs["mailNickname"] = args ? args.mailNickname : undefined;
            inputs["password"] = args ? args.password : undefined;
            inputs["usageLocation"] = args ? args.usageLocation : undefined;
            inputs["userPrincipalName"] = args ? args.userPrincipalName : undefined;
            inputs["mail"] = undefined /*out*/;
            inputs["objectId"] = undefined /*out*/;
            inputs["onpremisesSamAccountName"] = undefined /*out*/;
            inputs["onpremisesUserPrincipalName"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(User.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering User resources.
 */
export interface UserState {
    /**
     * `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
     */
    readonly accountEnabled?: pulumi.Input<boolean>;
    /**
     * The name to display in the address book for the user.
     */
    readonly displayName?: pulumi.Input<string>;
    /**
     * `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
     */
    readonly forcePasswordChange?: pulumi.Input<boolean>;
    /**
     * The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
     */
    readonly immutableId?: pulumi.Input<string>;
    /**
     * The primary email address of the Azure AD User.
     */
    readonly mail?: pulumi.Input<string>;
    /**
     * The mail alias for the user. Defaults to the user name part of the User Principal Name.
     */
    readonly mailNickname?: pulumi.Input<string>;
    /**
     * The Object ID of the Azure AD User.
     */
    readonly objectId?: pulumi.Input<string>;
    /**
     * The on premise sam account name of the Azure AD User.
     */
    readonly onpremisesSamAccountName?: pulumi.Input<string>;
    /**
     * The on premise user principal name of the Azure AD User.
     */
    readonly onpremisesUserPrincipalName?: pulumi.Input<string>;
    /**
     * The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
     */
    readonly password?: pulumi.Input<string>;
    /**
     * The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set.
     */
    readonly usageLocation?: pulumi.Input<string>;
    /**
     * The User Principal Name of the Azure AD User.
     */
    readonly userPrincipalName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a User resource.
 */
export interface UserArgs {
    /**
     * `true` if the account should be enabled, otherwise `false`. Defaults to `true`.
     */
    readonly accountEnabled?: pulumi.Input<boolean>;
    /**
     * The name to display in the address book for the user.
     */
    readonly displayName: pulumi.Input<string>;
    /**
     * `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.
     */
    readonly forcePasswordChange?: pulumi.Input<boolean>;
    /**
     * The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.
     */
    readonly immutableId?: pulumi.Input<string>;
    /**
     * The mail alias for the user. Defaults to the user name part of the User Principal Name.
     */
    readonly mailNickname?: pulumi.Input<string>;
    /**
     * The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.
     */
    readonly password: pulumi.Input<string>;
    /**
     * The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set.
     */
    readonly usageLocation?: pulumi.Input<string>;
    /**
     * The User Principal Name of the Azure AD User.
     */
    readonly userPrincipalName: pulumi.Input<string>;
}
