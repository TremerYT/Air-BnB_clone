#!/usr/bin/python3
import datetime
import uuid

from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BaseModel:
	id = Column(String(60), unique=True, nullable=False, primary_key=True)
	created_at = Column(DateTime, nullable=False, default=datetime.datetime.now(datetime.timezone.utc))
	updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now(datetime.timezone.utc))

	def __init__(self, **kwargs):
		if kwargs:
			for key, value in kwargs.items():
				if key == "__class__":
					continue
				if key in ("created_at", "updated_at") and isinstance(value, str):
					value = datetime.datetime.fromisoformat(value)
				setattr(self, key, value)
			if "id" not in kwargs:
				self.id = str(uuid.uuid4())
			if "created_at" not in kwargs:
				self.created_at = datetime.datetime.now(datetime.timezone.utc)
			if "updated_at" not in kwargs:
				self.updated_at = datetime.datetime.now(datetime.timezone.utc)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.datetime.now(datetime.timezone.utc)
			self.updated_at = datetime.datetime.now(datetime.timezone.utc)

	def save(self):
		self.updated_at = datetime.datetime.now()
		from models import storage
		storage.new(self)
		storage.save()

	def to_dict(self):
		key = "_sa_instance_state"
		dictionary = self.__dict__.copy()
		if key in dictionary:
			del dictionary[key]
		dictionary["__class__"] = self.__class__.__name__
		if isinstance(self.created_at, datetime.datetime):
			dictionary["created_at"] = self.created_at.isoformat()
		if isinstance(self.updated_at, datetime.datetime):
			dictionary["updated_at"] = self.updated_at.isoformat()
		return dictionary

	def delete(self):
		from models import storage
		storage.delete(self)

	def __str__(self):
		return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__ )
