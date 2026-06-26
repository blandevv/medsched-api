from enum import StrEnum


class PermissionResource(StrEnum):
    USERS = "users"
    ROLES = "roles"
    PERMISSIONS = "permissions"
    DOCUMENT_TYPES = "document_types"

    PATIENTS = "patients"
    NURSES = "nurses"
    DOCTORS = "doctors"
    SPECIALTIES = "specialties"

    APPOINTMENTS = "appointments"

    SURGERIES = "surgeries"
    OPERATING_ROOMS = "operating_rooms"

    RESOURCES = "resources"

    REPORTS = "reports"
