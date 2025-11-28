from django.test import TestCase
from unittest.mock import Mock, patch
from rest_framework import status
from activities.views import DailyActivityDetailView
from activities.serializers import DailyActivitySerializer

class DailyActivityViewTests(TestCase):

    def setUp(self):
        self.mock_request = Mock()
        self.mock_request.user = Mock()
        self.mock_request.data = {}

        self.mock_instance = Mock()
        self.mock_instance.status = "planned"
        self.mock_instance.save = Mock()

        self.view = DailyActivityDetailView()

    def test_patch_invalid_status(self):
        self.mock_request.data = {"status": "invalid_status"}

        with patch.object(self.view, "get_object", return_value=self.mock_instance):
            response = self.view.patch(self.mock_request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data["error"],
            "Invalid status value. Must be 'planned', 'in progress', or 'completed'."
        )
