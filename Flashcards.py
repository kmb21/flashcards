"""
This is a program which allows people studying a language to review words learned each day
WOrds are stored in a file
"""

from random import shuffle


def read_flashcard_data(filename):
    """
    Open and read the flashcard data file, storing the data as 
    a list of lists.
    Parameter:
      name_of_file: a str storing the name of the file
    Return:
      list of lists of the form [ [question1, answer1], [q2,a2], ... ]
    Side effects:
      none
    """
    input_file = open("%s.csv"%filename, 'r')
    data = []
    for line in input_file:
        line = line.rstrip()  # removes the \n from the end of line
        word_translation = line.split(',')
        data.append(word_translation)
    print(data)
    return data


def test_user(flashcards):
    """
    Test the user on each flashcard, accumulating the number
    of correct answers.
    Parameter:
      flashcards: a list of lists with questions and answers
    Return:
      int representing the # of correct answers
    Side effects:
      prints questions to the screen and asks for user input
    """
    correct = 0
    print("You got this. Let's GO!!")
    for line in flashcards:
      word = line[0]
      meaning = input("Word: %s  meaning: "%(word))
      if meaning == line[1]:
        correct += 1
        print("Correct. Let's go!!")
      else: 
        print("Incorrect...")
    return correct

def report_results(num_correct, num_flashcards):
    """
    Report on how well they did
    Parameters:
        num_correct (int): number of correct responses
        num_flashcards (int): number of total flashcards
    Return: 
        None
    Side effects:
      Printing the results to the screen
    """
    print("Results: ")
    correct_rate = (num_correct/num_flashcards)*100
    print("You got %.1f correct"%correct_rate)
    if correct_rate > 80:
      print("You got a hold of this. Almost there. Keep up!")
    elif correct_rate < 50:
      print("You need to study harder. You got this!!")
      
    else:
      print("Nice try. Keep up!")
      
  


def go_again():
    """
    See if they want to try again by asking the user to
    type 'y' or 'n'. Repeatedly ask until they type a valid
    response.
    Parameters:
       None
    Return:
       a str either 'y' or 'n'

    Side effects:
       Ask the user for a 'y' or 'n' response
    """
    valid = False
    while not valid:
        print("Enter y or n")
        answer = input('Do you want to study again? ')
        if answer == 'y' or answer == 'n':
            valid = True
        else:
            print("Try again.")
    return answer

def main():
  filename = input('Enter filename: ')
  while filename not in ['Words', 'German']:
    print("Available files: [Words, German]")
    filename = input('Enter filename: ')
    # Open and read the flashcard data file, storing the data as 
    # a list of lists.
    data = read_flashcard_data(filename)

    done = False
    while not done:
        # Shuffle the order of the flashcards so they're in a random order.
        shuffle(data)    
        # Test the user on each flashcard, accumulating the number
        # of correct answers.
        num_correct = test_user(data)
        # Report on how well they did
        report_results(num_correct, len(data))
        # See if they want to try again
        answer = go_again()
        if answer == 'n':
            done = True
            print("Sad to see you go!")


main()