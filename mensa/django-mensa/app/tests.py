from django.test import TestCase
from app.models import Plates, Day,WeekDay, Service
from decimal import Decimal
from django.urls import reverse


class PlatesTestCase(TestCase):
    # Test sugli input del modello Plates

    # Test sul prezzo del piatto
    def test_price_negative(self):
        plate = Plates(50,"piatto_fake",4.20,False,0)
        self.assertGreaterEqual(plate.price, 0,"Il prezzo non puo' essere negativo")

    def test_format_price(self):
        plate = Plates(50,"piatto_fake",443.25,False,0)
        self.assertAlmostEqual(plate.price,round(plate.price,2))
        self.assertLessEqual(plate.price,999999.99,"Prezzo troppo grande")

    # Test sul nome del piatto
    def test_len_max_name(self):
        plate = Plates(50,"piatto_fake",4.20,False,0)
        self.assertLessEqual(len(plate.name), 30,"Il nome del piatto non puo' superare la lunghezza 30")

    def test_len_min_name(self):
        plate = Plates(50,"piatto_fake",4.20,False,0)
        self.assertGreater(len(plate.name), 0,"Il nome del piatto non puo' essere vuoto")


    # Test sulla portata come indice deve avere questo range 0 <= x <= 3
    def test_service(self):
        plate = Plates(50,"piatto_fake",4.20,False,2)
        self.assertGreaterEqual(plate.menu_name_id, 0,"Errore: Portata non trovata")
        self.assertLessEqual(plate.menu_name_id, 3,"Errore: Portata non trovata")
        self.assertEqual(plate.menu_name_id-int(plate.menu_name_id), 0,"Valore non puo' essere float")


## Test sulle Views

class ListPlatesViewTests(TestCase):
    def test_view_with_no_plates(self):
        """
        Se nessun piatto e' presente stampa un messaggio appropriato
        """
        response = self.client.get(reverse('app:listplate'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['list_plates'], [])

class OrdineViewTests(TestCase):
    def test_view_ordine(self):
        """
        Test sulla view ordine
        """
        response = self.client.get(reverse('app:ordine'))
        self.assertEqual(response.status_code, 200)


class ListOrdiniViewTests(TestCase):
        def test_view_with_no_ordini(self):
            """
            Se nessun ordine e' presente stampa un messaggio appropriato
            """
            response = self.client.get(reverse('app:listordini'))
            self.assertEqual(response.status_code, 200)
            self.assertQuerysetEqual(response.context['list_ordini'], { "'Monday'":[],"'Tuesday'":[],"'Wednesday'":[],"'Thursday'":[],
                                      "'Friday'":[],"'Saturday'":[],"'Sunday'":[] })
class StatisticheViewTests(TestCase):
    def test_view_statistics(self):
        """
        Test sulla view app:statistics
        """
        response = self.client.get(reverse('app:statistics'))
        self.assertEqual(response.status_code, 200)

class MenuTestView(TestCase):
    def test_view_menu(self):
        """
        Test sulla view app:menu
        """
        response = self.client.get(reverse('app:menu'))
        self.assertEqual(response.status_code, 200)
