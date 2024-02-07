import random

# Definição da Interface Observer
class BattleObserver:
    def notifyWinner(self, winner):
        pass

# Implementação do Subject
class BattleNotifier:
    def __init__(self):
        self.observers = []  # Lista para armazenar os observadores

    def addObserver(self, observer):
        self.observers.append(observer)  # Adiciona um observador à lista

    def removeObserver(self, observer):
        self.observers.remove(observer)  # Remove um observador da lista

    def notifyObservers(self, winner):
        for observer in self.observers:
            observer.notifyWinner(winner)  # Notifica todos os observadores sobre o vencedor

# Implementação dos Observadores
class Player(BattleObserver):
    def __init__(self, name, notifier):
        self.name = name
        self.notifier = notifier  # Referência ao BattleNotifier
        self.notifier.addObserver(self)  # Registra-se no BattleNotifier para receber notificações

    def notifyWinner(self, winner):
        if winner == self:
            print(f"{self.name} venceu a batalha!")  # Mensagem de vitória para o jogador

# Exemplo de Uso
battle_notifier = BattleNotifier()  # Cria uma instância de BattleNotifier

player1 = Player("Player 1", battle_notifier)  # Cria um jogador e o registra no BattleNotifier
player2 = Player("Player 2", battle_notifier)  # Cria outro jogador e o registra no BattleNotifier

# Simulação de uma batalha com resultado aleatório
winner = random.choice([player1, player2])  # Escolhe aleatoriamente um dos jogadores como vencedor
battle_notifier.notifyObservers(winner)  # Notifica os observadores sobre o vencedor
