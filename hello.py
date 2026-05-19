import sys 
print("=" * 40)
print("bienvenue dans mon premier job jenkins")
if len(sys.argv) > 1:
  nom = sys.arg[1]
else:
  nom = "Etudiant jenkins
print(f"Bonjour{nom}, ton job jenkins a réussi")

a=10
b=5
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")

assert a+b == 15,"le test a échoué"
print("tous les tests passent avec succès")
