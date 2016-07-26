def is_vowel(character):
	return character.lower() in 'aeiouy'

def position_of_first_vowel(word):
	for character in word:
		if is_vowel(character) and not (character.lower() == 'y' and word.index(character) == 0):
			return word.index(character)
	return -1

def pigify(word):
	if position_of_first_vowel(word) in [0,-1]:
		return word + "-way"
	elif word[:2].lower() == "qu":
		return word[2:] + "-quay"
	return word[position_of_first_vowel(word):] +'-'+ word[:position_of_first_vowel(word)] + 'ay'
