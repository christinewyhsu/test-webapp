"""Testsq for Balloonicorn's Flask app."""
# Unit tests to test backend


import unittest
import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn(b"having a party", result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        # FIXME: Add a test to show we haven't RSVP'd yet
        # test that you see the RSVP form
        # test that you don't see the party details if you haven't RSVP
        result = self.client.get("/")
        self.assertIn(b"RSVP", result.data)

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""
        # Fake Form Data
        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        self.assertNotIn(b"ellHo World", result.data)
        self.assertIn(b"Yay", result.data)
        self.assertIn(b"Party Details", result.data)


    def test_rsvp_mel(self):
        """Can we keep Mel out?"""
        # Fake Form Data
        rsvp_info = {'name': "Mel", 'email': "mel@ubermelon.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)
       
        self.assertNotIn(b"Party Details", result.data)
        self.assertNotIn(b"Yay", result.data)

if __name__ == "__main__":
    unittest.main()
