import os
from typing import Dict

class ExtractView:
    def extract_success(self, extract: Dict):
        os.system('clear || cls')

        print('Extrato Bancário'.center(30,'-'))

        print(f'{extract["extract"]}')

        print(f'Saldo: R$ {extract["balance"]}')

    def extract_fail(self, error: str):
        os.system('clear || cls')

        fail_message = f'''Erro ao Puxar Extrato

        Erro: {error}'''

        print(fail_message)
    