from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    country: str = "USA"
    zipcode: str


class Person:
    first_name: str
    last_name: Optional[str]
    address: Optional[Address]
    favorite_numbers: List[int]


class A:
    def __init__(self) -> None:
        super().__init__()
     