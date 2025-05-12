import os.path
import unittest

from sqlalchemy.event import remove

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
	def setUp(self):
		self.storage = FileStorage()
		self.storage._FileStorage__objects = {}
		self.storage._FileStorage__file_path = "test_file.json"
		self.storage.reload = lambda: None


	def tearDown(self):
		self.storage._FileStorage__objects = {}
		try:
			import os
			os.remove("test_file.json")
		except FileNotFoundError:
			pass

	def test_all_empty(self):
		self.assertEqual(self.storage.all(), {})

	def test_new(self):
		objects = BaseModel()
		objects.id = "12345"
		self.storage.new(objects)
		self.assertIn("BaseModel.12345", self.storage.all())
		self.assertEqual(self.storage.all()["BaseModel.12345"], objects)

