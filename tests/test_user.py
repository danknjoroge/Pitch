import unittest
from app.models import User, Comments, Pitches
from app import db

class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User(password = "octopizzo")

    def test_password_setter(self):
        
        self.assertTrue(self.new_user.password_hash is not None)
    
    def test_no_access_password(self):
       
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
       
        self.assertTrue(self.new_user.verify_password('octopizzo'))



class TestComments(unittest.TestCase):
    def setUp(self):
        self.comments = Comments(comment='We are safe')
    
    def tearDown(self):
        Comments.query.delete()

    def test_save_comment(self):
        self.new_comment.save_comments()
        self.assertTrue(len(Comments.query.all())>0)



class TestPitches(unittest.TestCase):
    def setUp(self):
        self.pitches = Pitches(comment='We are safe')
    
    def tearDown(self):
        Pitches.query.delete()

    def test_save_comment(self):
        self.new_pitch.save_pitches()
        self.assertTrue(len(Pitches.query.all())>0)

