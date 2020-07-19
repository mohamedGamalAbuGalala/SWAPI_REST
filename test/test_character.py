from src import app
import unittest
import json


class CharacterTestCases(unittest.TestCase):
    def test_characters_fails_for_not_providing_name(self):
        tester = app.test_client(self)
        response = tester.get('/api/characters/')

        json_response = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json_response['msg'], 'You must pass a name')

    def test_characters_fails_for_providing_empty_name(self):
        tester = app.test_client(self)
        response = tester.get('/api/characters/?name=')

        json_response = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json_response['msg'], 'You must pass a name')

    def test_characters_success_with_all_matching_list_for_a_search(self):
        tester = app.test_client(self)
        response = tester.get('/api/characters/?name=L')

        json_response = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(json_response) > 1)

    def test_characters_success_with_one_matching_list_for_a_specific_search(self):
        tester = app.test_client(self)
        response = tester.get('/api/characters/?name=Luke Skywalker')

        json_response = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(json_response) == 1)

    def test_characters_success_the_desired_schema(self):
        tester = app.test_client(self)
        response = tester.get('/api/characters/?name=R2-D2')

        json_response = json.loads(response.data)
        json_expected = json.loads(
            '[{"fullName": "R2-D2","gender": "n/a","homePlanet": "Naboo","movies": ["A New Hope", "The Empire Strikes Back", "Return of the Jedi", "The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],"species":[{"averageLifespan": "indefinite", "name": "Droid"}]}]')

        response_item = json_response[0]
        expected_item = json_expected[0]

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(json_response) == 1)

        self.assertEqual(response_item['fullName'], expected_item['fullName'])
        self.assertEqual(response_item['gender'], expected_item['gender'])

        self.assertEqual(len(response_item['movies']), len(
            expected_item['movies']))
        self.assertEqual(response_item['movies'], expected_item['movies'])

        self.assertEqual(len(response_item['species']), len(
            expected_item['species']))

        self.assertEqual(response_item['species'][0]['averageLifespan'],
                         expected_item['species'][0]['averageLifespan'])
        self.assertEqual(
            response_item['species'][0]['name'], expected_item['species'][0]['name'])

        self.assertEqual(response_item['species'], expected_item['species'])

        self.assertEqual(json_response, json_expected)


if __name__ == '__main__':
    unittest.main()
