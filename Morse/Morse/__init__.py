
import string, winsound, time

morse_map = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.',
             'h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.',
             'o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-',
             'v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','0':'-----','1':'.----',
             '2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...',
             '8':'---..','9':'----.',' ':'/'}


input_string = input("Enter English Text ").lower()
morse_string = ' '.join(morse_map[x] for x in input_string)
#for ch in input_string:
#    morse_char = morse_map[ch]
#    morse_string += morse_char
#    morse_string += ' '
    
print(morse_string)

for ch in morse_string:
    if ch is '.': winsound.Beep(900,150)
    elif ch is '-': winsound.Beep(900,300)
    elif ch is '/': time.sleep(.2)
    else: time.sleep(.2)