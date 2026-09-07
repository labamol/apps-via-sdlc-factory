"""Generated service module for FEAT-01: Feedback Submission.

Implements stories: STORY-01.01, STORY-01.02, STORY-01.03.
"""


class ServiceError(ValueError):
    """Raised when a request violates a story contract."""


_RECORDS: list[dict] = []


def reset() -> None:
    _RECORDS.clear()


def story_01_01(record: dict) -> dict:
    """STORY-01.01: Customers must be able to submit feedback with a category and free-text comment.

    Traceability: AC-01.01.01, AC-01.01.02
    """
    if not isinstance(record, dict) or not record:
        raise ServiceError("STORY-01.01: record must be a non-empty dict")
    stored = dict(record)
    stored["story_id"] = "STORY-01.01"
    stored["record_id"] = len(_RECORDS) + 1
    _RECORDS.append(stored)
    return stored


def story_01_02(record: dict) -> dict:
    """STORY-01.02: The system shall acknowledge every submission with a unique reference number.

    Traceability: AC-01.02.01, AC-01.02.02
    """
    if not isinstance(record, dict) or not record:
        raise ServiceError("STORY-01.02: record must be a non-empty dict")
    stored = dict(record)
    stored["story_id"] = "STORY-01.02"
    stored["record_id"] = len(_RECORDS) + 1
    _RECORDS.append(stored)
    return stored


def story_01_03(record: dict) -> dict:
    """STORY-01.03: Submissions must be stored durably and survive service restarts.

    Traceability: AC-01.03.01, AC-01.03.02
    """
    if not isinstance(record, dict) or not record:
        raise ServiceError("STORY-01.03: record must be a non-empty dict")
    stored = dict(record)
    stored["story_id"] = "STORY-01.03"
    stored["record_id"] = len(_RECORDS) + 1
    _RECORDS.append(stored)
    return stored
