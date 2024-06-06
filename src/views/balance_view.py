class BalanceView:
    #Tela para exibir o saldo da conta corrente
    def display_balance(self, balance: float):
        print(f'\nSaldo R$ {balance:.2f}\n')

        command = input("Pressione enter para voltar ao menu!")