import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
	def __init__(self) -> None:
		self.storage: list[tuple[int, str]] = []
		self.number: int = 0

	@abstractmethod
	def validate(self, data: typing.Any) -> bool:
		pass

	@abstractmethod
	def ingest(self, data: typing.Any) -> None:
		pass

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

	def ingest(self, data: dict[str, str] | list[dict[str, str]]):
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


class ExportPlugin(typing.Protocol):
	def process_output(self, data: list[tuple[int, str]]) -> None:
		pass


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
				print(f"DataStream error - Can't process element in stream: {element}")

	def print_processors_stats(self) -> None:
		print("\n== DataStream statistics ==")
		if not self.processors:
			print("No processor found, no data")
			return
		for proc in self.processors:
			name = proc.__class__.__name__.replace("Processor", " Processor")
			print(f"{name}: total {proc.number} items processed, remaining {len(proc.storage)} on processor")


	def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
		for proc in self.processors:
			count: int = 0
			data: list[tuple[int, str]] = []
			
			while len(proc.storage) > 0 and count < nb:
				item = proc.output()
				data.append(item)
				count += 1

			if data:
				plugin.process_output(data)


class CSVPlugin(ExportPlugin):
	def process_output(self, data: list[tuple[int, str]]) -> None:
		if not data:
			return

		csv_line: list[str] = []
		for _ , value in data:
			csv_line.append(value)
		
		print("CSV Output:")
		print(",".join(csv_line))


class JSONPlugin(ExportPlugin):
	def process_output(self, data: list[tuple[int, str]]) -> None:
		if not data:
			return

		json_line: list[str] = []
		for i, value in data:
			json_line.append(f'"item_{i}": "{value}"')

		print("JSON Output:")
		print("{" + ", ".join(json_line) + "}")


if __name__ == "__main__":
	print("=== Code Nexus - Data Pipeline ===")
	print("\nInitialize Data Stream...")
	
	data_stream = DataStream()
	data_stream.print_processors_stats()
	
	print("\nRegistering Processors")
	numeric = NumericProcessor()
	text = TextProcessor()
	log = LogProcessor()

	data_stream.register_processor(numeric)
	data_stream.register_processor(text)
	data_stream.register_processor(log)
	
	test_data = [
        'Hello world', 
        [3.14, -1, 2.71], 
        [
            {'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
            {'log_level': 'INFO', 'log_message': 'User Wil is connected'}
        ], 
        42, 
        ['Hi', 'five']
    ]

	print(f"\nSend first batch of data on stream: {test_data}")
	data_stream.process_stream(test_data)
	data_stream.print_processors_stats()

	print("\nSend 3 processed data from each processor to a CSV plugin:")
	csv_plugin = CSVPlugin()
	data_stream.output_pipeline(3, csv_plugin)
	data_stream.print_processors_stats()	

	test_2 = [
		21, 
		['I love AI', 'LLMs are wonderful', 'Stay healthy'], 
		[
			{'log_level': 'ERROR', 'log_message': '500 server crash'}, 
			{'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}
		], 
		[32, 42, 64, 84, 128, 168], 
		'World hello'
	]

	print(f"\nSend another batch of data: {test_2}")
	data_stream.process_stream(test_2)
	data_stream.print_processors_stats()
	
	print("\nSend 5 processed data from each processor to a JSON plugin:")
	json_plugin = JSONPlugin()
	data_stream.output_pipeline(5, json_plugin)
	data_stream.print_processors_stats()
