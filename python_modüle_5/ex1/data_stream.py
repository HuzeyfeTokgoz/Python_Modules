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


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            flg = False
            for proc in self.processors:
                if proc.validate(element):
                    flg = True
                    proc.ingest(element)
                    break

            if not flg:
                print("DataStream error - "
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(f"{name}: total {proc.number} items processed, "
                  f"remaining {len(proc.storage)} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    data_stream = DataStream()

    print("\n== DataStream statistics ==")
    data_stream.print_processors_stats()
    test_data = [
                'Hello world',
                [3.14, -1, 2.71],
                [
                    {'log_level': 'WARNING', 'log_message':
                     'Telnet access! Use ssh instead'},
                    {'log_level': 'INFO', 'log_message':
                     'User wil is connected'}
                ],
                42,
                ['Hi', 'five']
        ]

    print("\nRegistering Numeric Processor")
    numeric = NumericProcessor()
    data_stream.register_processor(numeric)

    print(f"\nSend first batch of data on stream: {test_data}")
    data_stream.process_stream(test_data)

    print("== DataStream statistics ==")
    data_stream.print_processors_stats()

    print("\nRegistering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    data_stream.register_processor(text)
    data_stream.register_processor(log)

    print("Send the same batch again")
    data_stream.process_stream(test_data)

    print("== DataStream statistics ==")
    data_stream.print_processors_stats()

    print("\nConsume some elements from the data "
          "processors: Numeric 3, Text 2, Log 1")

    for _ in 0, 1, 2:
        numeric.output()
    for _ in 0, 1:
        text.output()
    log.output()

    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
