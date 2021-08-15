########################################################################################################################
# Author: Andrew Jacobson
# Date: July 2021
# Purpose: To take a specified keywords file and output a file with passwords based on the keywords (e.g. keywords like
# 'coffee' become 'Coffee123', 'coff33!', etc.
########################################################################################################################

# Function name: valid_keyword
# Parameters: Takes a string argument that is a single word/keyword
# Returns: boolean True/False
# Purpose: To run checks on the keywords that the user passes in to make sure they're valid
def valid_keyword(keyword):

    is_valid_keyword = True

    # Verify that keyword only contains alpha characters
    if not keyword.isalpha():

        is_valid_keyword = False

    return is_valid_keyword


# Function name: created_substituted_list
# Parameters: Takes a string argument that is a single word/keyword
# Returns: A list object
# Purpose: To create a list of potential words with common letters substituted for symbols/characters
def create_substituted_list(keyword):

    # Define the list object to be returned
    keyword_substitutions_list = []

    # Define dictionary of common substitutions - the key is the letter to be subbed and its value is a list of values
    # to substitute
    letter_substitutions = {'a': ['@'],
                            'e': ['3'],
                            'o': ['0'],
                            'i': ['1', '!'],
                            's': ['$', '5']}

    # Parse the word/keyword parameter into a list object (e.g. 'coffee' becomes ['c', 'o', 'f', 'f', 'e']
    # This is done so we can iterate through the word, character by character.
    keyword_list = list(keyword)

    # Iterate through the keyword list - enumerate it so that we can use the index to sub character by character
    for index, character in enumerate(keyword_list):

        # Create a copy of the keyword so that we can modify that and not the original passed keyword
        working_keyword = keyword_list.copy()

        # Check if the character is in the list of letter substitutions, if it's not then skip
        if character in letter_substitutions:

            # Get the list object of that character from the letter substitutions dict (e.g. 'e' has a value of ['3'])
            substitutions = letter_substitutions[character]

            # For each substitution in that letters list
            for value in substitutions:

                ####################################################################################################
                # Character by character substitution logic
                ####################################################################################################

                # Assign the substitution to the letter in the "working"/copy keyword
                # (e.g. 'coffee' becomes 'coff3e', 'coffe3', etc.)
                working_keyword[index] = value

                # Add the newly created value to the list of keywords to return
                keyword_substitutions_list.append(''.join(working_keyword))

                ####################################################################################################
                # Find/replace all characters substitution logic
                ####################################################################################################

                # Create a keyword that has all the letters substituted (e.g. 'coffee' becomes 'coff33')
                all_substituted_keyword = keyword.replace(character, value)

                # Add this new keyword to the list of keywords to return, if it's not already in the list
                if all_substituted_keyword not in keyword_substitutions_list:

                    keyword_substitutions_list.append(all_substituted_keyword)


    return keyword_substitutions_list


# Function name: create_appended_numbers_list
# Parameters: Takes a string argument that is a single word/keyword
# Returns: A list object
# Purpose: To create a list of potential passwords with number combinations appended to the front and end of the
# specified keyword.
def create_numbers_appended_list(keyword):

    # Define the list object to be returned
    numbers_appended_list = []

    # Define a list of common number combinations used in passwords
    number_combinations = ['123', '234', '345', '456', '567', '678', '789', '890',
                           '321', '432', '534', '654', '765', '876', '987', '098',
                           '1234', '2345', '3456', '4567', '5678', '6789', '7890',
                           '4321', '5432', '6543', '7654', '8765', '9876', '0987',
                           '12345', '54321', '123456', '654321',
                           '69', '420',
                           '00', '000', '11', '111', '22', '222']

    # Iterate through the number_combinations list and append the numbers to the keyword and add it to the list to
    # return
    for number in number_combinations:

        # Append numbers at the end
        numbers_appended_list.append(keyword + number)

        # Append numbers at the front
        numbers_appended_list.append(number + keyword)


    return numbers_appended_list


# Function name: create_capitalized_list
# Parameters: Takes a string argument that is a single word/keyword
# Returns: A list object
# Purpose: To create a list of potential passwords that have each letter capitalized (e.g. 'coffee' becomes 'Coffee',
# 'cOffee', 'coFFee', 'coffEE', etc.)
def create_capitalized_list(keyword):

    # Define the list object to be returned
    capitalized_list = []

    # For each character in the keyword
    for character in keyword:

        # Define a new character that is the uppercase version of the keyword's character
        new_character = character.upper()

        # Define a new keyword value that does a find/replace for the original character and capitalizes it
        new_keyword = keyword.replace(character, new_character)

        # If the keyword isn't in the list to return already, add it. Need this when there are multiple occurrences of a
        # letter in a word.
        if new_keyword not in capitalized_list:

            capitalized_list.append(new_keyword)

    # Finally, add a version of the keyword where the whole thing is capitalized
    capitalized_list.append(keyword.upper())

    return capitalized_list


# Function name: create_appended_numbers_list
# Parameters: Takes a string argument that is a single word/keyword
# Returns: A list object
# Purpose: To create a list of potential passwords with number combinations appended to the front and end of the
# specified keyword.
def create_symbols_appended_list(keyword):

    # Define the list object to be returned
    symbols_appended_list = []

    # Define a list of common symbol combinations used in passwords
    symbols_to_append = ['!', '!!', '!!!', '!@', '!@#']

    # For each symbol combination in the previously defined list
    for symbol in symbols_to_append:

        # Append the symbols to the end of the keyword
        new_keyword = keyword + symbol

        # Add the newly created password to the list to return
        symbols_appended_list.append(new_keyword)

    return symbols_appended_list

########################################################################################################################
########################################################################################################################
########################################################################################################################
# Main logic
########################################################################################################################
########################################################################################################################
########################################################################################################################

# Define the files used in the script - TODO: make these parameters you pass in upon script invocation
file_keywords = open("keywords.txt", "r")
file_passwords = open("passwords.txt", "w")

# Variables used to keep track of the keywords processed and passwords generated. Used for output at the end.
counter_keywords_processed = 0
counter_passwords_generated = 0

# Keywords from file list
users_keywords = []

# Keywords that are invalid
users_invalid_keywords = []

# Begin processing the keywords file
with file_keywords as reader:

    # For each word in the file
    for keyword in reader.readlines():

        # Strip off the newline character and make it lowercase (in case the user doesn't define the words correctly)
        keyword = keyword.replace("\n", "").lower()

        # Add the keyword to the list
        users_keywords.append(keyword)

# Close the keywords file
file_keywords.close()

# Validate users keywords - if they're good, continue. else, append them to a list of invalid keywords
for keyword in users_keywords:

    if valid_keyword(keyword):
        continue
    else:
        users_invalid_keywords.append(keyword)

# For each invalid keyword, remove it from the list we want to process
for keyword in users_invalid_keywords:

    users_keywords.remove(keyword)

# For each keyword the user provided, process it
for keyword in users_keywords:

    # Define the master keyword list - this gets reset for every keyword (don't want/need to hold EVERY keyword)
    master_keyword_list = []

    # Add the keyword to the master list
    master_keyword_list.append(keyword)

    ################################################################################################################
    # First pass - perform each keyword modifier function independently
    ################################################################################################################

    # Perform capitalization on the keyword
    capitalized = create_capitalized_list(keyword)
    master_keyword_list.extend(capitalized)

    ################################################################################################################

    # Perform substitutions on the keyword
    substitutions = create_substituted_list(keyword)
    master_keyword_list.extend(substitutions)

    ################################################################################################################

    # Append numbers to the keyword
    numbers_appended = create_numbers_appended_list(keyword)
    master_keyword_list.extend(numbers_appended)

    ################################################################################################################

    # Append symbols to the keyword
    symbols_appended = create_symbols_appended_list(keyword)
    master_keyword_list.extend(symbols_appended)

    ################################################################################################################
    # Second pass - perform keyword modifier functions on top of newly created keywords
    ################################################################################################################

    # Perform keyword modifiers on the capitalized keywords
    for capitalized_keyword in capitalized:

        # Append numbers
        capitalized_numbers = create_numbers_appended_list(capitalized_keyword)

        for new_keyword_1 in capitalized_numbers:

            if new_keyword_1 not in master_keyword_list:

                master_keyword_list.append(new_keyword_1)

            # Append symbols
            capitalized_numbers_symbols = create_symbols_appended_list(new_keyword_1)

            for new_keyword_2 in capitalized_numbers_symbols:

                if new_keyword_2 not in master_keyword_list:

                    master_keyword_list.append(new_keyword_2)

        # Append symbols
        capitalized_symbols = create_symbols_appended_list(capitalized_keyword)

        for new_keyword_1 in capitalized_symbols:

            if new_keyword_1 not in master_keyword_list:

                master_keyword_list.append(new_keyword_1)

            # Append numbers
            capitalized_symbols_numbers = create_numbers_appended_list(new_keyword_1)

            for new_keyword_2 in capitalized_symbols_numbers:

                if new_keyword_2 not in master_keyword_list:

                    master_keyword_list.append(new_keyword_2)

        # Perform substitutions
        capitalized_substitutions = create_substituted_list(capitalized_keyword)

        for new_keyword_1 in capitalized_substitutions:

            if new_keyword_1 not in master_keyword_list:

                master_keyword_list.append(new_keyword_1)

            # Append numbers
            capitalized_substitutions_numbers = create_numbers_appended_list(new_keyword_1)

            for new_keyword_2 in capitalized_symbols_numbers:

                if new_keyword_2 not in master_keyword_list:

                    master_keyword_list.append(new_keyword_2)

                # Append symbols
                capitalized_substitutions_numbers_symbols = create_symbols_appended_list(new_keyword_2)

                for new_keyword_3 in capitalized_substitutions_numbers_symbols:

                    if new_keyword_3 not in master_keyword_list:

                        master_keyword_list.append(new_keyword_3)

            # Append symbols
            capitalized_substitutions_symbols = create_symbols_appended_list(new_keyword_1)

            for new_keyword_2 in capitalized_substitutions_symbols:

                if new_keyword_2 not in master_keyword_list:

                    master_keyword_list.append(new_keyword_2)

                # Append numbers
                capitalized_substitutions_symbols_numbers = create_numbers_appended_list(new_keyword_2)

                for new_keyword_3 in capitalized_substitutions_symbols_numbers:

                    if new_keyword_3 not in master_keyword_list:

                        master_keyword_list.append(new_keyword_3)

    ################################################################################################################

    # Append numbers and symbols to the substitution keywords
    for substituted_keyword in substitutions:

        # Append numbers
        substituted_numbers = create_numbers_appended_list(substituted_keyword)

        for new_keyword_1 in substituted_numbers:

            if new_keyword_1 not in master_keyword_list:

                master_keyword_list.append(new_keyword_1)

            # Append symbols
            substituted_numbers_symbols = create_symbols_appended_list(new_keyword_1)

            for new_keyword_2 in substituted_numbers_symbols:

                if new_keyword_2 not in master_keyword_list:

                    master_keyword_list.append(new_keyword_2)

        # Append symbols
        substituted_symbols = create_symbols_appended_list(substituted_keyword)

        for new_keyword_1 in capitalized_symbols:

            if new_keyword_1 not in master_keyword_list:

                master_keyword_list.append(new_keyword_1)

            # Append numbers
            substituted_symbols_numbers = create_numbers_appended_list(new_keyword_1)

            for new_keyword_2 in substituted_symbols_numbers:

                if new_keyword_2 not in master_keyword_list:

                    master_keyword_list.append(new_keyword_2)

    ################################################################################################################

    # Append symbols to the number appended keywords
    for numbers_appended_keyword in numbers_appended:

        # Append symbols
        numbers_symbols = create_symbols_appended_list(numbers_appended_keyword)

        for new_keyword in capitalized_symbols:

            if new_keyword not in master_keyword_list:

                master_keyword_list.append(new_keyword)

    ################################################################################################################

    # Append numbers to the symbol appended keywords
    for symbols_appended_keyword in symbols_appended:

        # Append numbers
        symbols_numbers = create_numbers_appended_list(symbols_appended_keyword)

        for new_keyword in capitalized_symbols:

            if new_keyword not in master_keyword_list:

                master_keyword_list.append(new_keyword)

    ################################################################################################################

    # Increment the counter for keywords processed
    counter_keywords_processed += 1

# Now that all keywords have been created, write them to the passwords file
for keyword in master_keyword_list:

    keyword = keyword + "\n"
    file_passwords.write(keyword)

    counter_passwords_generated += 1

# Check if there were any keywords that weren't processed and display them
if users_invalid_keywords:

    print("Invalid keywords:", users_invalid_keywords)

# Print some output to the user
print("Keywords processed:", counter_keywords_processed)
print(" Passwords created:", counter_passwords_generated)

# Close the passwords file
file_passwords.close()
