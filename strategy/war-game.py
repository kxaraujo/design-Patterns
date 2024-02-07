# Definição das Interfaces

class AttackStrategy:
    def executeAttack(self):
        pass

class DefenseStrategy:
    def executeDefense(self):
        pass

# Implementação das Estratégias

class AggressiveAttack(AttackStrategy):
    def executeAttack(self):
        print("Executing aggressive attack...")

class BalancedAttack(AttackStrategy):
    def executeAttack(self):
        print("Executing balanced attack...")

class StrongDefense(DefenseStrategy):
    def executeDefense(self):
        print("Executing strong defense...")

# Integração no Player Module

class Player:
    def __init__(self, name):
        self.name = name
        self.attack_strategy = None
        self.defense_strategy = None

    def setAttackStrategy(self, attack_strategy):
        self.attack_strategy = attack_strategy

    def setDefenseStrategy(self, defense_strategy):
        self.defense_strategy = defense_strategy

    def attack(self):
        if self.attack_strategy:
            self.attack_strategy.executeAttack()  # Executa a estratégia de ataque atual
        else:
            print("No attack strategy set.")  # Mensagem caso não haja estratégia de ataque definida

    def defend(self):
        if self.defense_strategy:
            self.defense_strategy.executeDefense()  # Executa a estratégia de defesa atual
        else:
            print("No defense strategy set.")  # Mensagem caso não haja estratégia de defesa definida

# Exemplo de Uso

player1 = Player("Player 1")
player1.setAttackStrategy(AggressiveAttack())  # Define a estratégia de ataque como AggressiveAttack
player1.setDefenseStrategy(StrongDefense())   # Define a estratégia de defesa como StrongDefense

player1.attack()   # Executa a estratégia de ataque definida para o jogador
player1.defend()   # Executa a estratégia de defesa definida para o jogador

# Trocando dinamicamente as estratégias

player1.setAttackStrategy(BalancedAttack())  # Altera dinamicamente a estratégia de ataque para BalancedAttack
player1.attack()   # Executa a nova estratégia de ataque definida para o jogador
