from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class ApiTest(APITestCase):
    def test_list_processors(self):
        request = self.client.get("/processors/")

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(request.data), 4)

    def test_list_memories(self):
        request = self.client.get("/rammemorys/")

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(request.data), 5)

    def test_list_mother_board(self):
        request = self.client.get("/motherboards/")

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(request.data), 3)

    def test_list_video_board(self):
        request = self.client.get("/videocards/")

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(request.data), 3)

