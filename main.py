def get_book_text(path):
	try:
		print("Opening file")
		with open(path) as f:
			print("Reading file")
			file_contents = f.read()
		return file_contents
	except FileNotFoundError:
		print("File not found")
		return None
	finally:
		print("Closing file")
		f.close()

def get_num_words(file_content):
	words = file_content.split()
	return len(words)

def get_chars_dict(file_content):
	char_dict = {}
	for char in file_content:
		lowered = char.lower()
		if lowered in char_dict:
			char_dict[lowered] += 1
		else:
			char_dict[lowered] = 1
	return char_dict

def generate_report(num_words, char_list):
	print(f"--- Begin of report of {path_to_file} ---")
	print(f"{num_words} words found in the book")
	print(f"")

	for char in char_list:
		print(f"The {char['char']} character was found {char['count']} times")
	
	print(f"--- End report ---")

def get_sorted_char_list(char_dict):

	def sort_on(dict):
		return dict["count"]

	char_list = []
	for char in char_dict:
		if char.isalpha():
			char_list.append({"char": char, "count": char_dict[char]})

	char_list.sort(key=sort_on, reverse=True)
	return char_list


def main():
	path_to_file = "books/frankenstein.txt"
	book = get_book_text(path_to_file)

	if book:
		num_words = get_num_words(book)
		chars_dict = get_chars_dict(book)
		char_list = get_sorted_char_list(chars_dict)
		generate_report(num_words, char_list)


main()
