#DROP NOTE outils de prise de note

#Variable général utile
number_of_note = 0
tableau_book_note = []

'''
------------------------------------------------------------------
LES MENUS
------------------------------------------------------------------
'''
#Fonction message d'acceuil 
def welcome_message():
	print("=== DROP NOT ===")

#Fonction affichage menu + choix user
def print_menu_and_choice():
	print(" 1. (+) Note")
	print(" 2. Mes notes")
	print(" 3. Quitter")
	print("================")

	user_choice_menu = (input("Choix (1-3): "))

	while user_choice_menu not in ["1", "2", "3"]:
		user_choice_menu = (input("Chox invalide. Entrez votre choix en fonction des valeurs proposées (1-3): "))

	return user_choice_menu


#Fonction under menu add note + choix user
def print_under_menu_add_note():
	print(" 1. Aperçu")
	print(" 2. Sauvegarder")
	print(" 3. Modifier")
	print(" 4. Supprimer")

	user_choice_add_note = (input("Choix (1-4): "))

	while user_choice_add_note not in ["1", "2", "3", "4"]:
		user_choice_add_note = (input("Chox invalide. Entrez votre choix en fonction des valeurs proposées (1-4): "))

	return user_choice_add_note

#Fonction print biblio_note
def biblio_note():
	print("Fonctionnalité non disponible")

'''
------------------------------------------------------------------
MECANIQUES GESTION DES NOTES
------------------------------------------------------------------
'''

#Fonction calcul id note et nombe de note
def note_id_and_number_of_note(user_choice_menu,number_of_note):
	if user_choice_menu == "1":
		number_of_note = number_of_note + 1
		id_note = number_of_note

	return(number_of_note, id_note)


'''
------------------------------------------------------------------
OUTILS GESTION DE NOTE
------------------------------------------------------------------
'''
#Fonction add note
def add_and_name_note(user_choice_menu, tableau_book_note,number_of_note):

	# Incrémenter le compteur de note
	note_id_and_number_of_note(user_choice_menu,number_of_note)

	#Création de la note par le user (content,title,user)
	content_note = input("Entrez votre texte: ")
	title_note = input("Nommez votre note: ")

	#Tableau association avec variable
	tableau_book_note = [
		{
		"id": id_note,
		"title": title_note,
		"content": content_note
		}
	]

	return(title_note, content_note)


#Fonction affichage carnet
def book_notes():
	print("Fonctionnalité non disponible")

#Fonction preview note
def preview_note():
	print("Fonctionnalité non disponible")

#Fonction save note
def save_note():
	print("Fonctionnalité non disponible")

#Fonction modification texte d'une note
def edit_text_note():
	print("Fonctionnalité non disponible")

#Fonction modification titre d'une note
def edit_title_note():
	print("Fonctionnalité non disponible")

#Fonction suppression de note
def delete_note():
	print("Fonctionnalité non disponible")

#Fonction quitter drop note
def quit_drop_note():
	print("Fonctionnalité non disponible")


'''
------------------------------------------------------------------
MECANIQUE DU DROP NOTE
------------------------------------------------------------------
'''

#Fonction notebook en marche
def run_drop_note(user_choice_menu):
	match user_choice_menu:
		case '1':
			choice_menu = add_and_name_note(user_choice_menu, tableau_book_note,number_of_note)
		case '2':
			choice_menu = book_notes()
		case '3':
			choice_menu = quit_drop_note()
		case _:
			print("Choix invalide")

#Fonction gestion add note en marche
def run_gestion_add_note(user_choice_add_note):
	match user_choice_add_note:
		case '1':
			choice_under_menu = preview_note()
		case '2':
			choice_under_menu = save_note()
		case '3':
			choice_under_menu = edit_text_note()
		case '4':
			choice_under_menu = delete_note()
		case _:
			print("Choix invalide")


	return number_of_note

#Obligatoire pour lancer un programme avec fonction mais pourquoi
if __name__ == '__main__':
	welcome_message()
	user_choice_menu = print_menu_and_choice()
	choice_menu = run_drop_note(user_choice_menu)
	user_choice_add_note = print_under_menu_add_note()
	choice_under_menu = run_gestion_add_note(user_choice_add_note)

