import datetime
import time
import unittest

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
	def test_initialization(self):
		model = BaseModel()
		self.assertIsInstance(model.id, str)
		self.assertIsInstance(model.created_at, datetime.date)
		self.assertIsInstance(model.updated_at, datetime.datetime)
		self.assertEqual(model.created_at, model.updated_at)
		
	def test_initialization_kwargs(self):
		data = {
			"name" : "My_first_model",
			"id": "12345"
		}
		model = BaseModel(**data)
		self.assertEqual(model.id, "12345")

	def test_save(self):
		model = BaseModel()
		old_updated_at = model.updated_at
		time.sleep(0.001)
		model.save()
		self.assertNotEqual(old_updated_at, model.updated_at)
		self.assertGreater(model.updated_at, old_updated_at)

	def test_dict(self):
		model = BaseModel()
		model_dictionary = model.to_dict()
		self.assertIn("__class__", model_dictionary)
		self.assertIn("id", model_dictionary)
		self.assertIn("created_at", model_dictionary)
		self.assertIn("updated_at", model_dictionary)

		self.assertIsInstance(model_dictionary["__class__"], str)
		self.assertIsInstance(model_dictionary["id"], str)
		self.assertIsInstance(model_dictionary["created_at"], str)
		self.assertIsInstance(model_dictionary["updated_at"], str)


		self.assertEqual(model_dictionary["__class__"], "BaseModel")

	def test_str(self):
		model = BaseModel()
		expected_string = "[BaseModel] ({}) {}".format(model.id, model.__dict__ )
		self.assertEqual(model.__str__(), expected_string)