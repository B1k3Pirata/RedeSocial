from django.test import TestCase

class TestePagina(TestCase):
    def testa(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, 'basePG/base.html')
        self.assertContains(response, 'cadastro')
