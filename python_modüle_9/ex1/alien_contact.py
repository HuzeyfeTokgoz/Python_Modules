from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
import random, csv, json

class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"

class AlienContact(BaseModel):
    contact_id: str = Field(min_length= 5, max_length= 15)
    timestamp: datetime
    location: str = Field(min_length= 3, max_length= 100)
    contact_type: ContactType
    signal_strength: float = Field(ge= 0.0, le= 10.0)
    duration_minutes: int = Field(ge= 1, le= 1440)
    witness_count: int = Field(ge= 1, le= 100)
    message_received: str | None = Field(default= None, max_length= 500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_contact(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type is ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type is ContactType.telepathic and not self.witness_count >= 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include received messages")

        return self

    def __str__(self):
        return "\n".join([
                f"ID: {self.contact_id}",
                f"Type: {self.contact_type.value}",
                f"Location: {self.location}",
                f"Signal: {self.signal_strength}/10",
                f"Duration: {self.duration_minutes} minutes",
                f"Witnesses: {self.witness_count}",
                f"Message: '{self.message_received}'",
        ])

def csv_plugin():
    try:
        with open("../generated_data/alien_contacts.csv") as dosya:
            reader = csv.DictReader(dosya)
            data = random.choices(list(reader), k=3)
    except FileNotFoundError as e:
        print(e)
    else:
        return data

def json_plugin():
    try:
        with open("../generated_data/alien_contacts.json") as dosya:
            reader = json.load(dosya)
            data = random.choices(reader, k=3)
    except FileNotFoundError as e:
        print(e)
    else:
        return data



if __name__ == "__main__":
    data = csv_plugin() or json_plugin()

    print("Alien Contact Log Validation\n")
    print("======================================")
    for i in range(len(data)):
        if not data:
            break
        try:
            print("Valid contact report:")
            print(AlienContact(
                contact_id = data[i]["contact_id"],
                timestamp = data[i]["timestamp"],
                contact_type = data[i]["contact_type"],
                location = data[i]["location"],
                signal_strength = data[i]["signal_strength"],
                duration_minutes = data[i]["duration_minutes"],
                witness_count = data[i]["witness_count"],
                message_received = data[i]["message_received"]
            ))
        except ValidationError as e:
            error = e.errors()
            print("Expected validation error:\n", error[0]['msg'])
        print("======================================\n")
