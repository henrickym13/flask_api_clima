from geopy.geocoders import Nominatim
import requests
import urllib.request


class Tempo:
    """Classe principal"""

    def __init__(self, nome):
        """Método construtor da classe"""
        self.nome = nome
    

    def obter_lat_lon(self):
        """Método para obter latitude e longitude do
        Estado informado pelo usuario"""

        # fazendo chamada do método do pacote geopy
        # e pegando as informações necessarias
        loc = Nominatim(user_agent="GetLoc") 
        getLoc = loc.geocode(self.nome)
        
        # retornando uma lista com as informações 
        return [getLoc.latitude, getLoc.longitude]
    

    def consultar_clima(self):
        """Método para realizar a consulta do climea"""

        # chave da api gerada pelo site openweathermap.org
        chave_api = 'sua chave aqui!!!'

        # chamar método obter_lat_log e pegar latitude e longitude
        coordenadas = self.obter_lat_lon()
        lat = coordenadas[0]
        lon = coordenadas[1]

        # fazer a requisição da api e obter os dados e converter em
        # um arquivo json
        url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric"\
         % (lat, lon, chave_api)
        response = requests.get(url)
        data = response.json()

        return data
    

    def obter_icone_tempo(self, data):
        """Método para obter a string do icone do clima"""

        for chave in data['current']['weather']:
            pass
        return chave['icon']
    

    def obter_url_icone_tempo(self, icone):
        """Método para exibir a imagem do icone na pagina"""

        # fazendo a requisção na api do icone
        url = f"http://openweathermap.org/img/wn/{icone}@2x.png"

        return url
    

    def converter_mh_kmh(self, milhas):
        """Converter a velocidade do vento de milhas para km"""

        return int(milhas * 3.6)
    

    def exibir_informacoes_tempo(self):
        """Método para exibir as informações do clima do Estado
        selecionado"""

        # chamada do método para obter as informações
        informacao_tempo = self.consultar_clima()

        #passar informações para os respectivos campos
        temperatura = int(informacao_tempo["current"]["temp"])
        velocidade_vento = self.converter_mh_kmh(
            informacao_tempo['current']['wind_speed'])
        umidade = informacao_tempo['current']['humidity']
        url_icone = self.obter_icone_tempo(informacao_tempo)
        icone = self.obter_url_icone_tempo(url_icone)

        return[temperatura, velocidade_vento, umidade, icone]