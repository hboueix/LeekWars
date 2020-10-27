import os
import sys

class Menu:
	def __init__(self, client) -> None:
		self.client = client
		self.choices = dict()

	def intro(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		self.choices = {
			'1': self.leek_choice,
			'0': self.exit
		}
		print("=====================================================================")
		print("                             CONNEXION                               ")
		print("=====================================================================")
		# print("1. Utiliser un compte sauvegardé")
		# print("2. Se connecter via Invite de commande")
		# print("3. Ajouter un compte")
		print(f"\nNom d'utilisateur : {self.client.user}")#    Habs actuels :  {}\n\n{} Victoires         {} Nuls         {} Défaites \nRatio : {} ".format(login, money, victories, draws, defeats, ratio))
		print("Veuillez choisir le menu que vous souhaitez utiliser :")
		print ("\n1. Combats Solo")
		# print ("2. Combats d'Eleveurs")
		# print ("3. Combats d'Equipe")
		# print ("4. Inscription tournois")
		# print("\n9. Retour")
		print("\n 0. Quitter")
		choice = input(" >>  ")
		if choice in self.choices:
			self.choices[choice]()
		else:
			self.intro()

	def leek_choice(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		self.choices = {'0': self.exit}
		leeks = self.client.farmer.get_leek_names()
		for idx, value in enumerate(leeks):
			self.choices[str(idx+1)] = self.how_many_fights
		print("=====================================================================")
		print("                          CHOIX DU POIREAU                           ")
		print("=====================================================================")
		print(f"\nNom d'utilisateur : {self.client.user}")#    Habs actuels :  {}\n\n{} Victoires         {} Nuls         {} Défaites \nRatio : {} ".format(login, money, victories, draws, defeats, ratio))
		print("=====================================================================")
		print("                           COMBATS SOLO                              ")
		print("=====================================================================\n")
		print("Veuillez choisir le poireau que vous souhaitez utiliser :\n")
		print("\n".join([f"{idx+1}. {leek}" for idx, leek in enumerate(leeks)]))
		print("\n0. Quitter")
		choice = input(" >>  ")
		if choice in self.choices:
			if choice == '0':
				self.choices[choice]()
			else:
				leek_choice = leeks[int(choice)-1]
				self.choices[choice](leek_choice)
		else:
			self.leek_choice()

	def how_many_fights(self, leek_choice):
		os.system('cls' if os.name == 'nt' else 'clear')
		farmer = self.client.farmer
		leek_id = farmer.get_leek_id(leek_choice)
		leek = farmer.leeks[leek_id]
		print("=====================================================================")
		print("                          NOMBRE DE COMBAT                           ")
		print("=====================================================================")
		print(f"\nNom d'utilisateur : {self.client.user}")#    Habs actuels :  {}\n\n{} Victoires         {} Nuls         {} Défaites \nRatio : {} ".format(login, money, victories, draws, defeats, ratio))
		print(f"Poireau sélectionné : {leek['name']}")
		print("=====================================================================")
		print("                           COMBATS SOLO                              ")
		print("=====================================================================\n")
		print(f"Nombre de combats restants : {farmer.fights}")
		print("Veuillez choisir le nombre de combats à lancer :\n")
		choice = input(" >>  ")
		if choice == '0':
			self.exit()
		elif int(choice) <= farmer.fights:
			farmer.solo_fight(leek_id, int(choice))
		print(choice)

	def exit(self):
		sys.exit()