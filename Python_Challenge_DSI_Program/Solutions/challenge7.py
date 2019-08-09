"""author = Rockefeller""""

#the word is  "congratulations"


#Here is the code:

from string import ascii_lowercase

def ceasar_cipher(size_of_alphabet , correct_shift):
    
    encrypted_word= 'htslwfyzqfyntsx'
    James_BagOfWords = []
    
    for shift in range(size_of_alphabet+1):
        
        counter = 0
        word_sample = ''
        
        for i in encrypted_word:
            
            counter = (ascii_lowercase.find(i) + shift)%26
            word_sample+= ascii_lowercase[counter]
        James_BagOfWords.append(word_sample)
        
    return James_BagOfWords[correct_shift]

ceasar_cipher(26,21)
