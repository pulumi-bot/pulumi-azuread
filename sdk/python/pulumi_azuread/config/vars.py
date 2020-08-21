# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'client_certificate_password',
    'client_certificate_path',
    'client_id',
    'client_secret',
    'environment',
    'msi_endpoint',
    'subscription_id',
    'tenant_id',
    'use_msi',
]

__config__ = pulumi.Config('azuread')

client_certificate_password = __config__.get('clientCertificatePassword') or (_utilities.get_env('ARM_CLIENT_CERTIFICATE_PASSWORD') or '')

client_certificate_path = __config__.get('clientCertificatePath') or (_utilities.get_env('ARM_CLIENT_CERTIFICATE_PATH') or '')

client_id = __config__.get('clientId') or (_utilities.get_env('ARM_CLIENT_ID') or '')

client_secret = __config__.get('clientSecret') or (_utilities.get_env('ARM_CLIENT_SECRET') or '')

environment = __config__.get('environment') or (_utilities.get_env('ARM_ENVIRONMENT') or 'public')

msi_endpoint = __config__.get('msiEndpoint') or (_utilities.get_env('ARM_MSI_ENDPOINT') or '')

subscription_id = __config__.get('subscriptionId') or (_utilities.get_env('ARM_SUBSCRIPTION_ID') or '')

tenant_id = __config__.get('tenantId') or (_utilities.get_env('ARM_TENANT_ID') or '')

use_msi = __config__.get('useMsi') or (_utilities.get_env_bool('ARM_USE_MSI') or False)

