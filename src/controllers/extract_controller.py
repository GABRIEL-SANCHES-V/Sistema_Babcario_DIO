from src import models

class ExtractController:
    def extract(self, account: models.classes.Account):
        try:      
            account_extract = self.__extract(account)
            response = self.__format_response(account_extract)
            return {'Success': True, 'message': response}

        except Exception as error:
            return {'Success': False, 'error': str(error)}
        
    def __extract(self, account_infortmation: models.classes.Account):
        password = account_infortmation.password
        account_number = int(account_infortmation.number_account)

        account = models.data.account_data.find_account_by_account_number(password, account_number)

        if account.extract == []:
            raise Exception('Conta não possui transações finaceiras!')
        
        return account
        
    def __format_extract(self, extract):
        response = ''

        for transaction in extract:
            if transaction['type'] == 'Depósito':
                response += f"Depósito de R$ {transaction['value']}\n"
            elif transaction['type'] == 'Saque':
                response += f"Saque de R$ {transaction['value']}\n"

        return response
            
    def __format_response(self, account: models.classes.Account):
        response = {
            'extract': self.__format_extract(account.extract),
            'balance': account.balance
        }
        return response

