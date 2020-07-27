# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from . import _utilities, _tables

__all__ = ['Provider']


class Provider(pulumi.ProviderResource):
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, client_certificate_password: Optional[pulumi.Input[str]] = None, client_certificate_path: Optional[pulumi.Input[str]] = None, client_id: Optional[pulumi.Input[str]] = None, client_secret: Optional[pulumi.Input[str]] = None, environment: Optional[pulumi.Input[str]] = None, msi_endpoint: Optional[pulumi.Input[str]] = None, subscription_id: Optional[pulumi.Input[str]] = None, tenant_id: Optional[pulumi.Input[str]] = None, use_msi: Optional[pulumi.Input[bool]] = None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        The provider type for the azuread package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if client_certificate_password is None:
                client_certificate_password = (_utilities.get_env('ARM_CLIENT_CERTIFICATE_PASSWORD') or '')
            __props__['client_certificate_password'] = client_certificate_password
            if client_certificate_path is None:
                client_certificate_path = (_utilities.get_env('ARM_CLIENT_CERTIFICATE_PATH') or '')
            __props__['client_certificate_path'] = client_certificate_path
            if client_id is None:
                client_id = (_utilities.get_env('ARM_CLIENT_ID') or '')
            __props__['client_id'] = client_id
            if client_secret is None:
                client_secret = (_utilities.get_env('ARM_CLIENT_SECRET') or '')
            __props__['client_secret'] = client_secret
            if environment is None:
                environment = (_utilities.get_env('ARM_ENVIRONMENT') or 'public')
            __props__['environment'] = environment
            if msi_endpoint is None:
                msi_endpoint = (_utilities.get_env('ARM_MSI_ENDPOINT') or '')
            __props__['msi_endpoint'] = msi_endpoint
            if subscription_id is None:
                subscription_id = (_utilities.get_env('ARM_SUBSCRIPTION_ID') or '')
            __props__['subscription_id'] = subscription_id
            if tenant_id is None:
                tenant_id = (_utilities.get_env('ARM_TENANT_ID') or '')
            __props__['tenant_id'] = tenant_id
            if use_msi is None:
                use_msi = (_utilities.get_env_bool('ARM_USE_MSI') or False)
            __props__['use_msi'] = pulumi.Output.from_input(use_msi).apply(json.dumps) if use_msi is not None else None
        super(Provider, __self__).__init__(
            'azuread',
            resource_name,
            __props__,
            opts)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

