# generated by datamodel-codegen:
#   filename:  DirectShape.json
#   timestamp: 2020-11-24T16:33:06+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class Category(Enum):
    integer_0 = 0
    integer_1 = 1
    integer_2 = 2
    integer_3 = 3
    integer_4 = 4
    integer_5 = 5
    integer_6 = 6
    integer_7 = 7
    integer_8 = 8
    integer_9 = 9
    integer_10 = 10
    integer_11 = 11
    integer_12 = 12
    integer_13 = 13
    integer_14 = 14
    integer_15 = 15
    integer_16 = 16
    integer_17 = 17
    integer_18 = 18
    integer_19 = 19
    integer_20 = 20
    integer_21 = 21
    integer_22 = 22
    integer_23 = 23
    integer_24 = 24
    integer_25 = 25
    integer_26 = 26
    integer_27 = 27
    integer_28 = 28
    integer_29 = 29
    integer_30 = 30
    integer_31 = 31
    integer_32 = 32
    integer_33 = 33
    integer_34 = 34
    integer_35 = 35
    integer_36 = 36


class IGeometry(BaseModel):
    __root__: Optional[Dict[str, Any]]


class Mesh(BaseModel):
    vertices: Optional[List[float]] = None
    faces: Optional[List[int]] = None
    colors: Optional[List[int]] = None
    textureCoordinates: Optional[List[float]] = None
    id: Optional[Optional[str]] = None
    totalChildrenCount: Optional[int] = None
    applicationId: Optional[Optional[str]] = None
    speckle_type: Optional[Optional[str]] = None


class Level(BaseModel):
    name: Optional[Optional[str]] = None
    elevation: Optional[float] = None
    baseGeometry: Optional[IGeometry] = None
    displayMesh: Optional[Mesh] = None
    type: Optional[Optional[str]] = None
    level: Optional[Level] = None
    id: Optional[Optional[str]] = None
    totalChildrenCount: Optional[int] = None
    applicationId: Optional[Optional[str]] = None
    speckle_type: Optional[Optional[str]] = None


class DirectShape(BaseModel):
    category: Optional[Category] = None
    parameters: Optional[Optional[Dict[str, Any]]] = None
    baseGeometry: Optional[IGeometry] = None
    displayMesh: Optional[Mesh] = None
    type: Optional[Optional[str]] = None
    level: Optional[Level] = None
    id: Optional[Optional[str]] = None
    totalChildrenCount: Optional[int] = None
    applicationId: Optional[Optional[str]] = None
    speckle_type: Optional[Optional[str]] = None


Level.update_forward_refs()