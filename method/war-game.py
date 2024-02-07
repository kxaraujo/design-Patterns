from abc import ABC, abstractmethod

# Definição da Classe Abstrata
class BattleTemplate(ABC):
    def executeBattle(self):
        # Método template que define o esqueleto do algoritmo de batalha
        self.prepare()        # Preparação para a batalha
        self.performAttack()  # Execução do ataque
        self.performDefense() # Execução da defesa
        self.conclude()       # Conclusão da batalha

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def performAttack(self):
        pass

    @abstractmethod
    def performDefense(self):
        pass

    @abstractmethod
    def conclude(self):
        pass

# Implementação das Subclasses Concretas
class AggressiveBattle(BattleTemplate):
    def prepare(self):
        print("Preparing for aggressive battle...")

    def performAttack(self):
        print("Executing aggressive attack...")

    def performDefense(self):
        print("Performing minimal defense...")

    def conclude(self):
        print("Concluding aggressive battle...")

class BalancedBattle(BattleTemplate):
    def prepare(self):
        print("Preparing for balanced battle...")

    def performAttack(self):
        print("Executing balanced attack...")

    def performDefense(self):
        print("Performing balanced defense...")

    def conclude(self):
        print("Concluding balanced battle...")

# Chamada do Template Method
def startBattle(battle):
    print("Starting battle...")
    battle.executeBattle()

# Exemplo de Uso
aggressive_battle = AggressiveBattle()
balanced_battle = BalancedBattle()

startBattle(aggressive_battle)  # Inicia uma batalha agressiva
print("-" * 20)
startBattle(balanced_battle)   # Inicia uma batalha balanceada
