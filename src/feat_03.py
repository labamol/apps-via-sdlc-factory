"""Generated service module for FEAT-03: Reporting.

Implements stories: STORY-03.01, STORY-03.02.
"""


class ServiceError(ValueError):
    """Raised when a request violates a story contract."""


_RECORDS: list[dict] = []


def reset() -> None:
    _RECORDS.clear()


def story_03_01(record: dict) -> dict:
    """STORY-03.01: Managers must receive a weekly summary report of feedback volume by category.

    Traceability: AC-03.01.01, AC-03.01.02
    """
    if not isinstance(record, dict) or not record:
        raise ServiceError("STORY-03.01: record must be a non-empty dict")
    stored = dict(record)
    stored["story_id"] = "STORY-03.01"
    stored["record_id"] = len(_RECORDS) + 1
    _RECORDS.append(stored)
    return stored


def story_03_02(record: dict) -> dict:
    """STORY-03.02: The report delivery channel must be chosen; email vs. dashboard is a pending dec

    Traceability: AC-03.02.01, AC-03.02.02
    """
    if not isinstance(record, dict) or not record:
        raise ServiceError("STORY-03.02: record must be a non-empty dict")
    stored = dict(record)
    stored["story_id"] = "STORY-03.02"
    stored["record_id"] = len(_RECORDS) + 1
    _RECORDS.append(stored)
    return stored
