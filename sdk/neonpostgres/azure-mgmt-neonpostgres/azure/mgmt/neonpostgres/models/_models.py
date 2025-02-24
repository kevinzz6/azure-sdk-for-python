# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=useless-super-delegation

import datetime
from typing import Any, Dict, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class CompanyDetails(_model_base.Model):
    """Company details for an organization.

    :ivar company_name: Company name.
    :vartype company_name: str
    :ivar country: Country name of the company.
    :vartype country: str
    :ivar office_address: Office address of the company.
    :vartype office_address: str
    :ivar business_phone: Business phone number of the company.
    :vartype business_phone: str
    :ivar domain: Domain of the user.
    :vartype domain: str
    :ivar number_of_employees: Number of employees in the company.
    :vartype number_of_employees: int
    """

    company_name: Optional[str] = rest_field(name="companyName")
    """Company name."""
    country: Optional[str] = rest_field()
    """Country name of the company."""
    office_address: Optional[str] = rest_field(name="officeAddress")
    """Office address of the company."""
    business_phone: Optional[str] = rest_field(name="businessPhone")
    """Business phone number of the company."""
    domain: Optional[str] = rest_field()
    """Domain of the user."""
    number_of_employees: Optional[int] = rest_field(name="numberOfEmployees")
    """Number of employees in the company."""

    @overload
    def __init__(
        self,
        *,
        company_name: Optional[str] = None,
        country: Optional[str] = None,
        office_address: Optional[str] = None,
        business_phone: Optional[str] = None,
        domain: Optional[str] = None,
        number_of_employees: Optional[int] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ErrorAdditionalInfo(_model_base.Model):
    """The resource management error additional info.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: any
    """

    type: Optional[str] = rest_field(visibility=["read"])
    """The additional info type."""
    info: Optional[Any] = rest_field(visibility=["read"])
    """The additional info."""


class ErrorDetail(_model_base.Model):
    """The error detail.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.neonpostgres.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure.mgmt.neonpostgres.models.ErrorAdditionalInfo]
    """

    code: Optional[str] = rest_field(visibility=["read"])
    """The error code."""
    message: Optional[str] = rest_field(visibility=["read"])
    """The error message."""
    target: Optional[str] = rest_field(visibility=["read"])
    """The error target."""
    details: Optional[List["_models.ErrorDetail"]] = rest_field(visibility=["read"])
    """The error details."""
    additional_info: Optional[List["_models.ErrorAdditionalInfo"]] = rest_field(
        name="additionalInfo", visibility=["read"]
    )
    """The error additional info."""


class ErrorResponse(_model_base.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed
    operations.

    :ivar error: The error object.
    :vartype error: ~azure.mgmt.neonpostgres.models.ErrorDetail
    """

    error: Optional["_models.ErrorDetail"] = rest_field()
    """The error object."""

    @overload
    def __init__(
        self,
        *,
        error: Optional["_models.ErrorDetail"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class MarketplaceDetails(_model_base.Model):
    """Marketplace details for an organization.


    :ivar subscription_id: SaaS subscription id for the the marketplace offer.
    :vartype subscription_id: str
    :ivar subscription_status: Marketplace subscription status. Known values are:
     "PendingFulfillmentStart", "Subscribed", "Suspended", and "Unsubscribed".
    :vartype subscription_status: str or
     ~azure.mgmt.neonpostgres.models.MarketplaceSubscriptionStatus
    :ivar offer_details: Offer details for the marketplace that is selected by the user. Required.
    :vartype offer_details: ~azure.mgmt.neonpostgres.models.OfferDetails
    """

    subscription_id: Optional[str] = rest_field(name="subscriptionId")
    """SaaS subscription id for the the marketplace offer."""
    subscription_status: Optional[Union[str, "_models.MarketplaceSubscriptionStatus"]] = rest_field(
        name="subscriptionStatus"
    )
    """Marketplace subscription status. Known values are: \"PendingFulfillmentStart\", \"Subscribed\",
     \"Suspended\", and \"Unsubscribed\"."""
    offer_details: "_models.OfferDetails" = rest_field(name="offerDetails")
    """Offer details for the marketplace that is selected by the user. Required."""

    @overload
    def __init__(
        self,
        *,
        offer_details: "_models.OfferDetails",
        subscription_id: Optional[str] = None,
        subscription_status: Optional[Union[str, "_models.MarketplaceSubscriptionStatus"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class OfferDetails(_model_base.Model):
    """Offer details for the marketplace that is selected by the user.


    :ivar publisher_id: Publisher Id for the marketplace offer. Required.
    :vartype publisher_id: str
    :ivar offer_id: Offer Id for the marketplace offer. Required.
    :vartype offer_id: str
    :ivar plan_id: Plan Id for the marketplace offer. Required.
    :vartype plan_id: str
    :ivar plan_name: Plan Name for the marketplace offer.
    :vartype plan_name: str
    :ivar term_unit: Term Name for the marketplace offer.
    :vartype term_unit: str
    :ivar term_id: Term Id for the marketplace offer.
    :vartype term_id: str
    """

    publisher_id: str = rest_field(name="publisherId")
    """Publisher Id for the marketplace offer. Required."""
    offer_id: str = rest_field(name="offerId")
    """Offer Id for the marketplace offer. Required."""
    plan_id: str = rest_field(name="planId")
    """Plan Id for the marketplace offer. Required."""
    plan_name: Optional[str] = rest_field(name="planName")
    """Plan Name for the marketplace offer."""
    term_unit: Optional[str] = rest_field(name="termUnit")
    """Term Name for the marketplace offer."""
    term_id: Optional[str] = rest_field(name="termId")
    """Term Id for the marketplace offer."""

    @overload
    def __init__(
        self,
        *,
        publisher_id: str,
        offer_id: str,
        plan_id: str,
        plan_name: Optional[str] = None,
        term_unit: Optional[str] = None,
        term_id: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Operation(_model_base.Model):
    """Details of a REST API operation, returned from the Resource Provider Operations API.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: The name of the operation, as per Resource-Based Access Control (RBAC). Examples:
     "Microsoft.Compute/virtualMachines/write", "Microsoft.Compute/virtualMachines/capture/action".
    :vartype name: str
    :ivar is_data_action: Whether the operation applies to data-plane. This is "true" for
     data-plane operations and "false" for Azure Resource Manager/control-plane operations.
    :vartype is_data_action: bool
    :ivar display: Localized display information for this particular operation.
    :vartype display: ~azure.mgmt.neonpostgres.models.OperationDisplay
    :ivar origin: The intended executor of the operation; as in Resource Based Access Control
     (RBAC) and audit logs UX. Default value is "user,system". Known values are: "user", "system",
     and "user,system".
    :vartype origin: str or ~azure.mgmt.neonpostgres.models.Origin
    :ivar action_type: Extensible enum. Indicates the action type. "Internal" refers to actions
     that are for internal only APIs. "Internal"
    :vartype action_type: str or ~azure.mgmt.neonpostgres.models.ActionType
    """

    name: Optional[str] = rest_field(visibility=["read"])
    """The name of the operation, as per Resource-Based Access Control (RBAC). Examples:
     \"Microsoft.Compute/virtualMachines/write\",
     \"Microsoft.Compute/virtualMachines/capture/action\"."""
    is_data_action: Optional[bool] = rest_field(name="isDataAction", visibility=["read"])
    """Whether the operation applies to data-plane. This is \"true\" for data-plane operations and
     \"false\" for Azure Resource Manager/control-plane operations."""
    display: Optional["_models.OperationDisplay"] = rest_field(visibility=["read"])
    """Localized display information for this particular operation."""
    origin: Optional[Union[str, "_models.Origin"]] = rest_field(visibility=["read"])
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
     logs UX. Default value is \"user,system\". Known values are: \"user\", \"system\", and
     \"user,system\"."""
    action_type: Optional[Union[str, "_models.ActionType"]] = rest_field(name="actionType")
    """Extensible enum. Indicates the action type. \"Internal\" refers to actions that are for
     internal only APIs. \"Internal\""""

    @overload
    def __init__(
        self,
        *,
        action_type: Optional[Union[str, "_models.ActionType"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class OperationDisplay(_model_base.Model):
    """Localized display information for and operation.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar provider: The localized friendly form of the resource provider name, e.g. "Microsoft
     Monitoring Insights" or "Microsoft Compute".
    :vartype provider: str
    :ivar resource: The localized friendly name of the resource type related to this operation.
     E.g. "Virtual Machines" or "Job Schedule Collections".
    :vartype resource: str
    :ivar operation: The concise, localized friendly name for the operation; suitable for
     dropdowns. E.g. "Create or Update Virtual Machine", "Restart Virtual Machine".
    :vartype operation: str
    :ivar description: The short, localized friendly description of the operation; suitable for
     tool tips and detailed views.
    :vartype description: str
    """

    provider: Optional[str] = rest_field(visibility=["read"])
    """The localized friendly form of the resource provider name, e.g. \"Microsoft Monitoring
     Insights\" or \"Microsoft Compute\"."""
    resource: Optional[str] = rest_field(visibility=["read"])
    """The localized friendly name of the resource type related to this operation. E.g. \"Virtual
     Machines\" or \"Job Schedule Collections\"."""
    operation: Optional[str] = rest_field(visibility=["read"])
    """The concise, localized friendly name for the operation; suitable for dropdowns. E.g. \"Create
     or Update Virtual Machine\", \"Restart Virtual Machine\"."""
    description: Optional[str] = rest_field(visibility=["read"])
    """The short, localized friendly description of the operation; suitable for tool tips and detailed
     views."""


class OrganizationProperties(_model_base.Model):
    """Properties specific to Data Organization resource.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar marketplace_details: Marketplace details of the resource. Required.
    :vartype marketplace_details: ~azure.mgmt.neonpostgres.models.MarketplaceDetails
    :ivar user_details: Details of the user. Required.
    :vartype user_details: ~azure.mgmt.neonpostgres.models.UserDetails
    :ivar company_details: Details of the company. Required.
    :vartype company_details: ~azure.mgmt.neonpostgres.models.CompanyDetails
    :ivar provisioning_state: Provisioning state of the resource. Known values are: "Succeeded",
     "Failed", and "Canceled".
    :vartype provisioning_state: str or ~azure.mgmt.neonpostgres.models.ResourceProvisioningState
    :ivar partner_organization_properties: Organization properties.
    :vartype partner_organization_properties:
     ~azure.mgmt.neonpostgres.models.PartnerOrganizationProperties
    """

    marketplace_details: "_models.MarketplaceDetails" = rest_field(
        name="marketplaceDetails", visibility=["read", "create"]
    )
    """Marketplace details of the resource. Required."""
    user_details: "_models.UserDetails" = rest_field(name="userDetails")
    """Details of the user. Required."""
    company_details: "_models.CompanyDetails" = rest_field(name="companyDetails")
    """Details of the company. Required."""
    provisioning_state: Optional[Union[str, "_models.ResourceProvisioningState"]] = rest_field(
        name="provisioningState", visibility=["read"]
    )
    """Provisioning state of the resource. Known values are: \"Succeeded\", \"Failed\", and
     \"Canceled\"."""
    partner_organization_properties: Optional["_models.PartnerOrganizationProperties"] = rest_field(
        name="partnerOrganizationProperties"
    )
    """Organization properties."""

    @overload
    def __init__(
        self,
        *,
        marketplace_details: "_models.MarketplaceDetails",
        user_details: "_models.UserDetails",
        company_details: "_models.CompanyDetails",
        partner_organization_properties: Optional["_models.PartnerOrganizationProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Resource(_model_base.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.neonpostgres.models.SystemData
    """

    id: Optional[str] = rest_field(visibility=["read"])
    """Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long"""
    name: Optional[str] = rest_field(visibility=["read"])
    """The name of the resource."""
    type: Optional[str] = rest_field(visibility=["read"])
    """The type of the resource. E.g. \"Microsoft.Compute/virtualMachines\" or
     \"Microsoft.Storage/storageAccounts\"."""
    system_data: Optional["_models.SystemData"] = rest_field(name="systemData", visibility=["read"])
    """Azure Resource Manager metadata containing createdBy and modifiedBy information."""


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which
    has 'tags' and a 'location'.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.neonpostgres.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    """

    tags: Optional[Dict[str, str]] = rest_field()
    """Resource tags."""
    location: str = rest_field(visibility=["read", "create"])
    """The geo-location where the resource lives. Required."""

    @overload
    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class OrganizationResource(TrackedResource):
    """Organization Resource by Neon.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.neonpostgres.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar properties: The resource-specific properties for this resource.
    :vartype properties: ~azure.mgmt.neonpostgres.models.OrganizationProperties
    """

    properties: Optional["_models.OrganizationProperties"] = rest_field()
    """The resource-specific properties for this resource."""

    @overload
    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        properties: Optional["_models.OrganizationProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class PartnerOrganizationProperties(_model_base.Model):
    """Properties specific to Partner's organization.


    :ivar organization_id: Organization Id in partner's system.
    :vartype organization_id: str
    :ivar organization_name: Organization name in partner's system. Required.
    :vartype organization_name: str
    :ivar single_sign_on_properties: Single Sign On properties for the organization.
    :vartype single_sign_on_properties: ~azure.mgmt.neonpostgres.models.SingleSignOnProperties
    """

    organization_id: Optional[str] = rest_field(name="organizationId")
    """Organization Id in partner's system."""
    organization_name: str = rest_field(name="organizationName")
    """Organization name in partner's system. Required."""
    single_sign_on_properties: Optional["_models.SingleSignOnProperties"] = rest_field(name="singleSignOnProperties")
    """Single Sign On properties for the organization."""

    @overload
    def __init__(
        self,
        *,
        organization_name: str,
        organization_id: Optional[str] = None,
        single_sign_on_properties: Optional["_models.SingleSignOnProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SingleSignOnProperties(_model_base.Model):
    """Properties specific to Single Sign On Resource.

    :ivar single_sign_on_state: State of the Single Sign On for the organization. Known values are:
     "Initial", "Enable", and "Disable".
    :vartype single_sign_on_state: str or ~azure.mgmt.neonpostgres.models.SingleSignOnStates
    :ivar enterprise_app_id: AAD enterprise application Id used to setup SSO.
    :vartype enterprise_app_id: str
    :ivar single_sign_on_url: URL for SSO to be used by the partner to redirect the user to their
     system.
    :vartype single_sign_on_url: str
    :ivar aad_domains: List of AAD domains fetched from Microsoft Graph for user.
    :vartype aad_domains: list[str]
    """

    single_sign_on_state: Optional[Union[str, "_models.SingleSignOnStates"]] = rest_field(name="singleSignOnState")
    """State of the Single Sign On for the organization. Known values are: \"Initial\", \"Enable\",
     and \"Disable\"."""
    enterprise_app_id: Optional[str] = rest_field(name="enterpriseAppId")
    """AAD enterprise application Id used to setup SSO."""
    single_sign_on_url: Optional[str] = rest_field(name="singleSignOnUrl")
    """URL for SSO to be used by the partner to redirect the user to their system."""
    aad_domains: Optional[List[str]] = rest_field(name="aadDomains")
    """List of AAD domains fetched from Microsoft Graph for user."""

    @overload
    def __init__(
        self,
        *,
        single_sign_on_state: Optional[Union[str, "_models.SingleSignOnStates"]] = None,
        enterprise_app_id: Optional[str] = None,
        single_sign_on_url: Optional[str] = None,
        aad_domains: Optional[List[str]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SystemData(_model_base.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or ~azure.mgmt.neonpostgres.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or ~azure.mgmt.neonpostgres.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    created_by: Optional[str] = rest_field(name="createdBy")
    """The identity that created the resource."""
    created_by_type: Optional[Union[str, "_models.CreatedByType"]] = rest_field(name="createdByType")
    """The type of identity that created the resource. Known values are: \"User\", \"Application\",
     \"ManagedIdentity\", and \"Key\"."""
    created_at: Optional[datetime.datetime] = rest_field(name="createdAt", format="rfc3339")
    """The timestamp of resource creation (UTC)."""
    last_modified_by: Optional[str] = rest_field(name="lastModifiedBy")
    """The identity that last modified the resource."""
    last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = rest_field(name="lastModifiedByType")
    """The type of identity that last modified the resource. Known values are: \"User\",
     \"Application\", \"ManagedIdentity\", and \"Key\"."""
    last_modified_at: Optional[datetime.datetime] = rest_field(name="lastModifiedAt", format="rfc3339")
    """The timestamp of resource last modification (UTC)."""

    @overload
    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UserDetails(_model_base.Model):
    """User details for an organization.

    :ivar first_name: First name of the user.
    :vartype first_name: str
    :ivar last_name: Last name of the user.
    :vartype last_name: str
    :ivar email_address: Email address of the user.
    :vartype email_address: str
    :ivar upn: User's principal name.
    :vartype upn: str
    :ivar phone_number: User's phone number.
    :vartype phone_number: str
    """

    first_name: Optional[str] = rest_field(name="firstName")
    """First name of the user."""
    last_name: Optional[str] = rest_field(name="lastName")
    """Last name of the user."""
    email_address: Optional[str] = rest_field(name="emailAddress")
    """Email address of the user."""
    upn: Optional[str] = rest_field()
    """User's principal name."""
    phone_number: Optional[str] = rest_field(name="phoneNumber")
    """User's phone number."""

    @overload
    def __init__(
        self,
        *,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email_address: Optional[str] = None,
        upn: Optional[str] = None,
        phone_number: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
