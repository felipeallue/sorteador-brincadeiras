import unittest
import json
from app import app, carregar_brincadeiras

class TestSorteadorApp(unittest.TestCase):
    
    def setUp(self):
        """Configurar o cliente de teste antes de cada teste"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_index_route(self):
        """Testar se a rota principal retorna status 200"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_sortear_route(self):
        """Testar se a rota /sortear retorna uma brincadeira válida"""
        response = self.app.get('/sortear')
        self.assertEqual(response.status_code, 200)
        
        # Verificar se o retorno é JSON
        self.assertEqual(response.content_type, 'application/json; charset=utf-8')
        
        # Verificar se o JSON contém os campos esperados
        data = json.loads(response.data.decode('utf-8'))
        self.assertIn('nome', data)
        self.assertIn('descricao', data)
        self.assertIn('imagem', data)
    
    def test_carregar_brincadeiras(self):
        """Testar se a função carregar_brincadeiras retorna uma lista válida"""
        brincadeiras = carregar_brincadeiras()
        
        # Verificar se retorna uma lista
        self.assertIsInstance(brincadeiras, list)
        
        # Verificar se a lista não está vazia
        self.assertGreater(len(brincadeiras), 0)
        
        # Verificar se cada brincadeira tem os campos necessários
        for brincadeira in brincadeiras:
            self.assertIn('nome', brincadeira)
            self.assertIn('descricao', brincadeira)
            self.assertIn('imagem', brincadeira)
    
    def test_sortear_returns_valid_brincadeira(self):
        """Testar se a brincadeira sorteada está na lista de brincadeiras"""
        brincadeiras = carregar_brincadeiras()
        nomes_brincadeiras = [b['nome'] for b in brincadeiras]
        
        response = self.app.get('/sortear')
        data = json.loads(response.data.decode('utf-8'))
        
        # Verificar se a brincadeira sorteada está na lista
        self.assertIn(data['nome'], nomes_brincadeiras)

if __name__ == '__main__':
    unittest.main()
