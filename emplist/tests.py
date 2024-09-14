from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Emp

class EmpModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.emp = Emp.objects.create(
            code = "0001",
            name = "This is name"
        )


    def test_code_content(self):
        emp = Emp.objects.get(id=1)
        excepted_code = f"{emp.code}"
        self.assertEqual(excepted_code,"0001")

    def test_name_content(self):
        emp = Emp.objects.get(id=1)
        excepted_name = f"{emp.name}"
        self.assertEqual(excepted_name,"This is name")

    def test_api_listview(self):
        response = self.client.get(reverse("emp_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Emp.objects.count(),1)
        self.assertContains(response, self.emp)

    def test_api_detailview(self):
        response = self.client.get(
            reverse("emp_detail", kwargs={"pk": self.emp.id}),
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Emp.objects.count(),1)
        self.assertContains(response, "0001")