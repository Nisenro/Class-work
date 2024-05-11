english_to_german = {
		"good day": "Guten Tag!",
		"good morning": "Guten Morgen!",
		"goodbye": "Auf Wiedersehen!",
		"how are you": "Wie geht's?",
		"my name is python": "Mein Name ist Python!",
		"do you speak english": "Sprechen sie Englisch?",
		"where is the bathroom": "Wo ist die Toilette?",
		"thank you": "Danke!",
		"i am sorry": "Es tut mir leid!",
		"a large beer please": "Ein grosses Bier, bitte!"
}

inputted_word = input("English sentence to translate: ")

inputted_word = ''.join(char for char in inputted_word if char.isalpha() or char.isspace()).lower()

translated_words = english_to_german.get(inputted)