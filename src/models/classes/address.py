class Address:
    #Classe que representa um endereço, com as características de logradouro, bairro e cidade/estado.
    def __init__(self, public_place, neighborhood, city_state) -> None:
        self.public_place = public_place
        self.neighborhood = neighborhood
        self.city_state = city_state