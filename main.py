#DROP NOTE outils de prise de note

#Variable général utile
number_of_note = 0
tableau_book_note = []

#Fonction message d'acceuil 
def welcome_message():
	print("=== DROP NOT ===")

#Fonction affichage menu + choix user
def print_menu_and_choice():
	print(" 1. (+) Note")
	print(" 2. Mes notes")
	print(" 3. Quitter")
	print("================")

	user_choice = (input("Choix (1-3): "))

	while user_choice not in ["1", "2", "3"]:
		user_choice = (input("Chox invalide. Entrez votre choix en fonction des valeurs proposées (1-3): "))

	return user_choice

#Fonction add note
def add_and_name_note(tableau_book_note,number_of_note):

	# Incrémenter le compteur de note
	note_id_and_number_of_note

	#Création de la note par le user (content,title,user)
	content_note = input("Entrez votre texte: ")
	title_note = input("Nommez votre note: ")
	id_note = title_note

	#
	tableau_book_note = [
	{
	"id": id_note,
	"title": title_note,
	"content": content_note
	}
]

	#Proposer au user d'afficher l'aperçu de la note 
	ask_preview_note = input("Voir l'aperçu Y/N ?: ")
	ask_preview_note = minuscule_ask_preview.lower
	y = True
	n = False
	if ask_preview.lower == True:
		print(title_note, content_note)


	return number_of_note

#Fonction calcule id note et nombe de note
def note_id_and_number_of_note(user_choice,number_of_note):
	if user_choice == 1:
		number_of_note = number_of_note + 1
		id_note = number_of_note

	return(number_of_note, id_note)

#Fonction affichage carnet
def book_notes():
	print("Fonctionnalité non disponible")

#Fonction suppression de note
def delete_note():
	print("Fonctionnalité non disponible")

#Fonction modification texte d'une note
def modify_text_note():
	print("Fonctionnalité non disponible")

#Fonction modification titre d'une note
def modify_title_note():
	print("Fonctionnalité non disponible")

#Fonction quitter drop note
def quit_drop_note():
	print("Fonctionnalité non disponible")

#Fonction notebook en marche
def run_drop_note(user_choice):
	match user_choice:
		case '1':
			choice = add_and_name_note(tableau_book_note,number_of_note)
		case '2':
			choice = book_notes()
		case '3':
			choice = quit_drop_note()
		case _:
			print("Choix invalide")

#Obligatoire pour lancer un programme avec fonction mais pourquoi
if __name__ == '__main__':
	welcome_message()
	user_choice = print_menu_and_choice()
	choice = run_drop_note(user_choice)
