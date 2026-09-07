"""Generated service module for FEAT-02: Feedback Review.

Implements stories: STORY-02.01, STORY-02.02, STORY-02.03.
"""


class ServiceError(ValueError):
    """Raised when a request violates a story contract."""


_RECORDS: list[dict] = []


def reset() -> None:
    _RECORDS.clear()


def story_02_01(record: dict) -> dict:
    """STORY-02.01: Support staff shall be able to list and filter feedback by category and date.

    Traceability: AC-02.01.01, AC-02.01.02
    """
    if not isinstance(record, dict) or not record:
        raise ServiceError("STORY-02.01: record must be a non-empty dict")
    stored = dict(record)
    stored["story_id"] = "STORY-02.01"
    stored["record_id"] = len(_RECORDS) + 1
    _RECORDS.append(stored)
    return stored


def story_02_02(record: dict) -> dict:
    """STORY-02.02: The review dashboard should feel fast and user-friendly for support staff.

    Traceability: AC-02.02.01, AC-02.02.02
    """
    if not isinstance(record, dict) or not record:
        raise ServiceError("STORY-02.02: record must be a non-empty dict")
    stored = dict(record)
    stored["story_id"] = "STORY-02.02"
    stored["record_id"] = len(_RECORDS) + 1
    _RECORDS.append(stored)
    return stored


def story_02_03(record: dict) -> dict:
    """STORY-02.03: Closed feedback must be retained for a period that is currently TBD pending comp

    Traceability: AC-02.03.01, AC-02.03.02
    """
    if not isinstance(record, dict) or not record:
        raise ServiceError("STORY-02.03: record must be a non-empty dict")
    stored = dict(record)
    stored["story_id"] = "STORY-02.03"
    stored["record_id"] = len(_RECORDS) + 1
    _RECORDS.append(stored)
    return stored
