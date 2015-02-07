__author__ = 'Josh!'
import wave


def converter(string):
    """This just converts the letters in a string to their morse code counterpart. This doesn't include any punctuation or numbers as of yet."""
    string = string.upper()
    morseString = ''
    morseDict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                 'Q': '--.-', 'R': '-.-', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                 'Y': '-.--', 'Z': '--..'}
    for x in string:
        try:
            morseString += (morseDict[x] + ' ')
        except KeyError:
            pass
    return morseString


def soundImport(morseList):
    """Witchcraft found at: http://stackoverflow.com/questions/2890703/how-to-join-two-wav-file-using-python"""
    outfile = "morse.wav"
    data = []
    dataCounter = 0  # This just counts how many dots and dashes make up the entire string
    for x in morseList:
        for y in x:
            # It may seem inefficient to open/close the .wav files every time, but weirds things happen if the files aren't closed properly
            if y == '.':
                w = wave.open('dot.wav', 'rb')
                data.append([w.getparams(), w.readframes(w.getnframes())])
                w.close()
                dataCounter += 1
            elif y == '-':
                w = wave.open('dash.wav', 'rb')
                data.append([w.getparams(), w.readframes(w.getnframes())])
                w.close()
                dataCounter += 1
        # This is so that you can differentiate between letters or else it is indecipherable
        w = wave.open('blank.wav', 'rb')
        data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()
        dataCounter += 1

    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for x in range(dataCounter):
        output.writeframes(data[x][1])
    output.close()


def main():
    string = input("Please enter a string: ")
    morseString = converter(string)
    morseList = (list(morseString.split(' ')))
    print(morseList)
    soundImport(morseList)


main()