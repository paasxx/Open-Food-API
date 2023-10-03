from django.test import SimpleTestCase
from django.urls import reverse,resolve
from djangoapp.views import getFoods
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User


class ApiUrlsTests(SimpleTestCase):

    def test_get_foods_is_resolved(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, getFoods)


class FoodAPITests(APITestCase):

    foods_url = reverse('products')

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='some-strong-password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token.key)

    def tearDown(self):
        # Do not need to be defined because django by default deletes datatabase data for the test.
        pass

    def test_get_foods_authenticated(self):
        response = self.client.get(self.foods_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_foods_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.foods_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class FoodAPIDetailTests(APITestCase):

    foods_url = reverse('products')
    food_url = reverse('product_id', args=[1])
    food_delete_url = reverse('delete', args=[1])
    food_create_url = reverse('create')
    

   

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='some-strong-password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token.key)

        self.data={
                "code": "7898253589433",
                "status": "tested",
                "imported_t": None,
                "url": None,
                "creator": "GeoByte-Pedro",
                "created_t": None,
                "last_modified_t": None,
                "product_name": "Pão para hamburger tradicional",
                "quantity": "200 g",
                "brands": "Limiar",
                "categories": "Pães para hamburgers",
                "labels": "100% brasileira, Fermentação natural, Zero gorduras trans",
                "cities": None,
                "purchase_places": None,
                "stores": None,
                "ingredients_text": "Farinha de trigo enriquecida com ferro e ácido fólico, água, açúcar, fermento fresco, gordura vegetal, glúten de trigo, farinha de centeio e sal refinado. Conservante: propionato de cálcio; oxidantes: ácido ascórbico e azodicarbonamida, espessante: carboximetilcelulose sódica; emulsificantes: ésteres de mono e diglicerideos de ácidos graxos com ácido diacetil tartárico e estearoil-2-lactil-lactato de sódio.",
                "traces": "Ovos, Glúten, Leite, Soja, Soro de leite",
                "serving_size": None,
                "serving_quantity": None,
                "nutriscore_score": None,
                "nutriscore_grade": None,
                "main_category": None,
                "image_url": None }
        
        # Creating the object in database to test update bellow.
        response = self.client.post(self.food_create_url, self.data, format='json')
        self.id_created = response.data['id']

    def test_update_food_authenticated(self):
        food_update_url = reverse('update', args=[self.id_created])
        response = self.client.put(food_update_url,self.data, format='json')
        self.assertEqual(response.status_code, 200)
        

    def test_update_food_un_authenticated(self):
        food_update_url = reverse('update', args=[self.id_created])
        self.client.force_authenticate(user=None, token=None)
        response = self.client.put(food_update_url,self.data, format='json')
        self.assertEqual(response.status_code, 401)
    
    
    def test_get_food_authenticated(self):
        response = self.client.get(self.food_url)
        self.assertEqual(response.status_code, 200)
        

    def test_get_food_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.food_url)
        self.assertEqual(response.status_code, 401)

    def test_delete_food_authenticated(self):
        response = self.client.delete(self.food_delete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_food_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.delete(self.food_delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)