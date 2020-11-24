# generated by datamodel-codegen:
#   filename:  Vector.json
#   timestamp: 2020-11-24T16:33:36+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Vector(BaseModel):
    value: Optional[List[float]] = None
    id: Optional[Optional[str]] = None
    totalChildrenCount: Optional[int] = None
    applicationId: Optional[Optional[str]] = None
    speckle_type: Optional[Optional[str]] = None