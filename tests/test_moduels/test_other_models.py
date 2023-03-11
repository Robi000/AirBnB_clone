#!/usr/bin/python3
"""
This module unit tests the module models/state
"""
import unittest
from time import sleep
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity


class TestOtherModels(unittest.TestCase):
    """
    Tests all methods of User
    """

    def test_UserClass(self):
        """Tests if instances of User have none-empty attributes"""
        u = User()
        u.email = "alanwalker@ubi.com"
        u.password = "as34b2"
        u.first_name = "Alan"
        u.last_name = "Walker"
        self.assertIsNotNone(u)
        self.assertIsNotNone(u.id)
        self.assertIsNotNone(u.created_at)
        self.assertIsNotNone(u.updated_at)
        u.save()
        self.assertNotEqual(u.created_at, u.updated_at)

    def test_StateClass(self):
        """Tests if instances of State have none-empty attributes"""
        s = State()
        s.name = "New Hampshire"
        self.assertIsNotNone(s)
        self.assertIsNotNone(s.id)
        self.assertIsNotNone(s.created_at)
        self.assertIsNotNone(s.updated_at)
        self.assertIsNotNone(s.name)
        s.save()
        self.assertNotEqual(s.created_at, s.updated_at)

    def test_ReviewClass(self):
        """Tests if instances of Review have none-empty attributes"""
        r = Review()
        r.text = "This place was wonderful!"
        self.assertIsNotNone(r)
        self.assertIsNotNone(r.id)
        self.assertIsNotNone(r.created_at)
        self.assertIsNotNone(r.updated_at)
        self.assertIsNotNone(r.text)
        r.save()
        self.assertNotEqual(r.created_at, r.updated_at)

    def test_PlaceClass(self):
        """Tests if instances of Place have none-empty attributes"""
        p = Place()
        p.name = "1743 Berry St"
        p.description = "A lovely appartment for two"
        p.number_rooms = 2
        p.number_bathrooms = 1
        p.max_guest = 3
        p.price_by_night = 125
        p.latitude = 74.5082
        p.longitude = 12.3484
        self.assertIsNotNone(p)
        self.assertIsNotNone(p.id)
        self.assertIsNotNone(p.created_at)
        self.assertIsNotNone(p.updated_at)
        self.assertIsNotNone(p.name)
        self.assertIsNotNone(p.description)
        self.assertIsNotNone(p.number_rooms)
        self.assertIsNotNone(p.number_bathrooms)
        self.assertIsNotNone(p.max_guest)
        self.assertIsNotNone(p.price_by_night)
        self.assertIsNotNone(p.latitude)
        self.assertIsNotNone(p.longitude)

        p.save()
        self.assertNotEqual(p.created_at, p.updated_at)

    def test_CityClass(self):
        """Tests if instances of City have none-empty attributes"""
        c = City()
        c.name = "New England"
        self.assertIsNotNone(c)
        self.assertIsNotNone(c.id)
        self.assertIsNotNone(c.created_at)
        self.assertIsNotNone(c.updated_at)
        self.assertIsNotNone(c.name)
        c.save()
        self.assertNotEqual(c.created_at, c.updated_at)

    def test_AmenityClass(self):
        """Tests if instances of Amenity have none-empty attributes"""
        a = Amenity()
        a.name = "Splendid"
        self.assertIsNotNone(a)
        self.assertIsNotNone(a.id)
        self.assertIsNotNone(a.created_at)
        self.assertIsNotNone(a.updated_at)
        self.assertIsNotNone(a.name)
        a.save()
        self.assertNotEqual(a.created_at, a.updated_at)

    def test_string_representation(self):
        """Tests the output of __str__ method of User"""
        u = User()
        u.email = "alanwalker@ubi.com"
        u.password = "as34b2"
        u.first_name = "Alan"
        u.last_name = "Walker"
        self.assertEqual(u.__str__(), "[{}] ({}) {}".format(
            u.__class__.__name__, u.id, u.__dict__))

    def test_save(self):
        """Tests if update_time is updated correctly when User's save() is
        called"""
        u = User()
        u.email = "alanwalker@ubi.com"
        u.password = "as34b2"
        u.first_name = "Alan"
        u.last_name = "Walker"
        update_time = u.updated_at
        sleep(0.0001)
        u.save()
        self.assertNotEqual(update_time, u.updated_at)

    def test_to_dict(self):
        """Tests the to_dict() method of User and makes
        sure it returns the correct dictionary"""
        u = User()
        u.email = "alanwalker@ubi.com"
        u.password = "as34b2"
        u.first_name = "Alan"
        u.last_name = "Walker"
        created_at = u.created_at.isoformat()
        self.assertEqual(u.to_dict().get("__class__"), "User")
        self.assertEqual(u.to_dict().get("created_at"), created_at)
        self.assertEqual(u.to_dict().get("updated_at"),
                         u.updated_at.isoformat())
        self.assertEqual(u.to_dict().get("email"), "alanwalker@ubi.com")
        self.assertEqual(u.to_dict().get("password"), "as34b2")
        self.assertEqual(u.to_dict().get("first_name"), "Alan")
        self.assertEqual(u.to_dict().get("last_name"), "Walker")

    def test_kwargs(self):
        """Tests the handling of **kwargs (dictionary)
        instantiation of User"""
        u1 = User()
        u1.email = "alanwalker@ubi.com"
        u1.password = "as34b2"
        u1.first_name = "Alan"
        u1.last_name = "Walker"
        u2 = User(**u1.to_dict())
        self.assertEqual(u1.to_dict(), u2.to_dict())
        self.assertFalse(u1 is u2)

        u1 = User()
        sleep(0.003)
        u1.save()
        self.assertFalse(u1 is u2)
        u2 = User(**u1.to_dict())
        self.assertEqual(u1.to_dict(), u2.to_dict())


if __name__ == '__main__':
    unittest.main()
