from contextlib import ExitStack as does_not_raise
from typing import Dict, List, Optional

import pytest
from specklepy.api import operations
from specklepy.logging.exceptions import SpeckleException
from specklepy.objects.base import Base, DataChunk


@pytest.mark.parametrize(
    "invalid_prop_name",
    [
        (""),
        ("@"),
        ("@@wow"),
        ("this.is.bad"),
        ("super/bad"),
    ],
)
def test_empty_prop_names(invalid_prop_name: str) -> None:
    base = Base()
    with pytest.raises(ValueError):
        base[invalid_prop_name] = "🐛️"


class FakeModel(Base):
    """Just a test class type."""

    foo: str = ""


def test_new_type_registration() -> None:
    """Test if a new subclass is registered into the type register."""
    assert Base.get_registered_type("FakeModel") == FakeModel
    assert Base.get_registered_type("🐺️") is None


def test_fake_base_serialization() -> None:
    fake_model = FakeModel(foo="bar")

    serialized = operations.serialize(fake_model)
    deserialized = operations.deserialize(serialized)

    assert fake_model.get_id() == deserialized.get_id()


def test_duplicate_speckle_type_raises_error():
    with pytest.raises(ValueError):

        class NaughtyClass(Base, speckle_type="Base"):
            """This class has a speckle_type that is already taken."""


@pytest.mark.parametrize(
    "forbidden_attribute_name, expectation",
    [
        ("", pytest.raises(ValueError)),
        ("@", pytest.raises(ValueError)),
        ("@@", pytest.raises(ValueError)),
        ("im.cheeky", pytest.raises(ValueError)),
        ("im.cheeky", pytest.raises(ValueError)),
        ("imgood", does_not_raise()),
    ],
)
def test_attribute_name_validation(
    forbidden_attribute_name: str,
    expectation,
    base: Base,
):
    with expectation:
        base[forbidden_attribute_name] = None


def test_speckle_type_cannot_be_set(base: Base) -> None:
    assert base.speckle_type == "Base"
    base.speckle_type = "unset"
    assert base.speckle_type == "Base"


def test_base_of_custom_speckle_type() -> None:
    b1 = Base.of_type("BirdHouse", name="Tweety's Crib")
    assert b1.speckle_type == "BirdHouse"
    assert b1.name == "Tweety's Crib"


class FrozenYoghurt(Base):
    """Testing type checking"""

    servings: int
    flavours: List[str]  # list item types won't be checked
    customer: str
    add_ons: Optional[Dict[str, float]]  # dict item types won't be checked
    price: float = 0.0


def test_type_checking() -> None:
    order = FrozenYoghurt()

    order.servings = 2
    order.price = "7"  # will get converted
    order.customer = "izzy"

    with pytest.raises(SpeckleException):
        order.flavours = "not a list"
    with pytest.raises(SpeckleException):
        order.servings = "five"
    with pytest.raises(SpeckleException):
        order.add_ons = ["sprinkles"]

    order.add_ons = {"sprinkles": 0.2, "chocolate": 1.0}
    order.flavours = ["strawberry", "lychee", "peach", "pineapple"]

    assert order.price == 7.0
