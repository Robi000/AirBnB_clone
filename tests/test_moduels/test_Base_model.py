#!/usr/bin/python3
"""
This module unit tests the module models/base_model
"""
import unittest
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests all methods of BaseModel
    """

    def test_instantiation(self):
        """Tests if instances of BaseModel have none-empty attributes"""
        Base1 = BaseModel()
        self.assertIsNotNone(Base1)
        self.assertIsNotNone(Base1.id)
        self.assertIsNotNone(Base1.created_at)
        self.assertIsNotNone(Base1.updated_at)
        Base1.save()
        self.assertNotEqual(Base1.created_at, Base1.updated_at)

    def test_string_representation(self):
        """Tests the output of __str__ method of BaseModel"""
        Base1 = BaseModel()
        self.assertEqual(Base1.__str__(), "[{}] ({}) {}".format(
            Base1.__class__.__name__, Base1.id, Base1.__dict__))

    def test_save(self):
        """Tests if update_time is updated correctly when
        BaseModel's save() is called"""
        Base1 = BaseModel()
        update_time = Base1.updated_at
        sleep(0.0001)
        Base1.save()
        self.assertNotEqual(update_time, Base1.updated_at)

    def test_to_dict(self):
        """Tests the to_dict() method of BaseModel and makes
        sure it returns the correct dictionary"""
        Base1 = BaseModel()
        created_at = Base1.created_at.isoformat()
        self.assertEqual(Base1.to_dict().get("__class__"), "BaseModel")
        self.assertEqual(Base1.to_dict().get("created_at"), created_at)
        self.assertEqual(Base1.to_dict().get("updated_at"),
                         Base1.updated_at.isoformat())

    def test_kwargs(self):
        """Tests the handling of **kwargs (dictionary)
        instantiation of BaseModel"""
        Base1 = BaseModel()
        Base2 = BaseModel(**Base1.to_dict())
        self.assertEqual(Base1.to_dict(), Base2.to_dict())
        self.assertFalse(Base1 is Base2)

        Base1 = BaseModel()
        sleep(0.003)
        Base1.save()
        self.assertFalse(Base1 is Base2)
        Base2 = BaseModel(**Base1.to_dict())
        self.assertEqual(Base1.to_dict(), Base2.to_dict())


if __name__ == '__main__':
    unittest.main()
