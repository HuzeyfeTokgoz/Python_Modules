import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[tuple[int, str]] = []
        self.number: int = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise IndexError("Processor storage is empty.")

        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if type(data) in (float, int):
            return True

        elif type(data) is list and len(data) > 0:
            for x in data:
                if not type(x) in (int, float):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if type(data) is list:
            for x in data:
                self.storage.append((self.number, str(x)))
                self.number += 1

        elif type(data) in (int, float):
            self.storage.append((self.number, str(data)))
            self.number += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if type(data) is str:
            return True

        if type(data) is list and len(data) > 0:
            for x in data:
                if not type(x) is str:
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if type(data) is list:
            for x in data:
                self.storage.append((self.number, x))
                self.number += 1

        elif type(data) is str:
            self.storage.append((self.number, data))
            self.number += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if type(data) is dict:
            if (
                "log_level" in data and
                type(data["log_level"]) is str and
                "log_message" in data and
                type(data["log_message"]) is str
            ):
                return True

        elif type(data) is list and len(data) > 0:
            for x in data:
                if not (
                    type(x) is dict and
                    "log_level" in x and
                    "log_message" in x and
                    type(x["log_level"]) is str and
                    type(x["log_message"]) is str
                ):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if type(data) is list:
            for x in data:
                key = x['log_level']
                value = x['log_message']
                formatted_log = f"{key}: {value}"
                self.storage.append((self.number, formatted_log))
                self.number += 1

        elif type(data) is dict:
            key = data['log_level']
            value = data['log_message']
            formatted_log = f"{key}: {value}"
            self.storage.append((self.number, formatted_log))
            self.number += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    numeric = NumericProcessor()

    test: typing.Any = 42
    print(f"Trying to validate input '{test}': {numeric.validate(test)}")

    test = "Hello"
    print(f"Trying to validate input '{test}': {numeric.validate(test)}")

    test = "foo"
    print(f"Test invalid ingestion of string '{test}' "
          "without prior validation:")
    try:
        numeric.ingest(test)
    except Exception as e:
        print(f"Got exception: {e}")

    test_int_list: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {test_int_list}")

    print("Extracting 3 values...")
    numeric.ingest(test_int_list)
    for _ in 0, 1, 2:
        value, data = numeric.output()
        print(f"Numeric value {value}: {data}")

    print("\nTesting Text Processor...")
    text = TextProcessor()
    test = 42
    print(f"Trying to validate input '{test}': {text.validate(test)}")
    test_str_list: list[str] = ["Hello", "Nexus", "World"]
    print(f"Processing data: {test_str_list}")

    print("Extracting 1 value...")
    text.ingest(test_str_list)
    value, data = text.output()
    print(f"Text value {value}: {data}")

    print("\nTesting Log Processor...")
    log = LogProcessor()

    test = "Hello"
    print(f"Trying to validate input '{test}': {log.validate(test)}")

    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {log_data}")

    print("Extracting 2 values...")
    log.ingest(log_data)

    for _ in 0, 1:
        log_key, log_value = log.output()
        print(f"Log entry {log_key}: {log_value}")
