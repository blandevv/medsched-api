from enum import StrEnum


class PermissionAction(StrEnum):
    CREATE = "create"
    READ = "read"
    UPDATE = "update"

    ACTIVATE = "activate"
    DEACTIVATE = "deactivate"

    ASSIGN = "assign"
    UNASSIGN = "unassign"

    CANCEL = "cancel"
    RESCHEDULE = "reschedule"

    CONFIRM = "confirm"
