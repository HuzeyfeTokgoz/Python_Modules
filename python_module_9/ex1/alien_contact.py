from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
import random
import csv
import json
from typing import Any


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_contact(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if (self.contact_type is ContactType.physical and
                not self.is_verified):
            raise ValueError("Physical contact reports must be verified")

        if (self.contact_type is ContactType.telepathic and
                self.witness_count < 3):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) "
                             "should include received messages")

        return self

    def __str__(self) -> str:
        return "\n".join([
                f"ID: {self.contact_id}",
                f"Type: {self.contact_type.value}",
                f"Location: {self.location}",
                f"Signal: {self.signal_strength}/10",
                f"Duration: {self.duration_minutes} minutes",
                f"Witnesses: {self.witness_count}",
                f"Message: '{self.message_received}'",
        ])


def csv_plugin() -> list[dict[str, Any]]:
    try:
        with open("generated_data/alien_contacts.csv") as dosya:
            reader = csv.DictReader(dosya)
            data = random.choices(list(reader), k=3)
    except FileNotFoundError as e:
        print(e)
        return []
    else:
        return data


def json_plugin() -> list[dict[str, Any]]:
    try:
        with open("generated_data/alien_contacts.json") as dosya:
            reader = json.load(dosya)
            data = random.choices(reader, k=3)
    except FileNotFoundError as e:
        print(e)
        return []
    else:
        return data


def invalid_plugin() -> list[dict[str, Any]]:
    try:
        with open("generated_data/invalid_contacts.json") as dosya:
            reader = json.load(dosya)
            data = random.choices(reader, k=3)
    except FileNotFoundError as e:
        print(e)
        return []
    else:
        return data


def main() -> None:
    plugin = json_plugin() + csv_plugin() + invalid_plugin()
    data = random.choices(plugin, k=3)
    if not data:
        print("Data not found")

    print("Alien Contact Log Validation")
    print("======================================")
    for i in data:
        try:
            print("Valid contact report:")
            print(AlienContact(
                contact_id=i["contact_id"],
                timestamp=i["timestamp"],
                contact_type=i["contact_type"],
                location=i["location"],
                signal_strength=i["signal_strength"],
                duration_minutes=i["duration_minutes"],
                witness_count=i["witness_count"],
                message_received=i["message_received"]
            ))
        except ValidationError as e:
            error = e.errors()
            print("Expected validation error:\n", error[0]['msg'])
        print("\n======================================")


if __name__ == "__main__":
    main()
