
ciphertext = """
lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt

wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd

"""
#print(ciphertext)
lettersalph = 'abcdefghijklmnopqrstuvwxyz'    #the 26 letters of the alphabet function

lettersloop = {letteralph: 0 for letteralph in lettersalph}   # loop that iterate the prev funct

#print(lettersloop)

#for loop to iterate the ciphertext and if state inside the loop
for char in ciphertext:
  if char in lettersalph:
    lettersloop[char] +=1

totalCount = sum(lettersloop.values())

sortingLetters= sorted([(value, key) for (key, value) in
                        lettersloop.items()], reverse= True)


# total count of the letters occuring in the loops and adding them, also sorting the list high to low


#print(lettersloop)
#print(sortingLetters)

for value, letter in sortingLetters:
  percentage = 100* value / totalCount
  print(f'{letter}: {value}\t({percentage:.4f}%)')


letterConv = {

  "r": "e",
  "b": "t",
  "m": "a",
  "k": "o",
  "j": "i",
  "w": "n",
  "i": "s",
  "p": "h",
  "u": "r",
  "h": "d",
  "d": "l",
  "v": "c",
  "x": "u",
  "y": "m",
  "s": "w",
  "n": "f",
  "t": "g",
  "l": "y",
  "q": "p",
  "o": "b",
  "e": "v",
  "c": "k",
  "a": "j",
  "g": "x",
  "f": "q",
  "z": "z",

}
# above here is the Dictionario replacion the most common words in the ciphertext by the one given in the project. also the percentage of the usage of the words
cipherT = """

lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt

wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb

"""
cipherList = []
for words in cipherT.strip():
  cipherList.append(letterConv.get(words, words))

re= " ".join(cipherList)

print("\n""Decryption is: " +"\n"+ str(re))

# the function cipherList that is append with the Dictionario and the for loop that iterate the ciphertext

decryption = """

y e c a f s e   t h e   w r a c t n c e   i u   t h e   y a s n c   m i v e m e o t s   i u  p a t a   n s 
 t h e   u i c f s   a o l   m a s t e r g   i u   s e d u   n s   t h e   e s s e o c e   i u 
 m a t s f y a g a s h n   r g f   p a r a t e   l i   n   s h a d d   t r g   t i   e d f c n l a t e   t h e 
 m i v e m e o t s   i u   t h e   p a t a   a c c i r l n o b   t i   m g   n o t e r w r e t a t n i o 
 y a s e l   i o   u i r t g   g e a r s   i u   s t f l g 

 n t   n s   o i t   a o   e a s g   t a s p   t i   e j w d a n o   e a c h   m i v e m e o t   a o l   n t s 
 s n b o n u n c a o c e   a o l   s i m e   m f s t   r e m a n o   f o e j w d a n o e l   t i   b n v e   a 
 c i m w d e t e   e j w d a o a t n i o   i o e   k i f d l   h a v e   t i   y e   q f a d n u n e l   a o l 
 n o s w n r e l   t i   s f c h   a o   e j t e o t   t h a t   h e   c i f d l   r e a c h   t h e   s t a t e 
 i u   e o d n b h t e o e l   m n o l   c a w a y d e   i u   r e c i b o n x n o b   s i f o l d e s s 
 s i f o l   a o l   s h a w e d e s s   s h a w e   n   l i   o i t   l e e m   m g s e d u   t h e   u n o a d 
 a f t h i r n t g   y f t   m g   e j w e r n e o c e   k n t h   p a t a   h a s   d e u t   o i   l i f y t 
 t h a t   t h e   u i d d i k n o b   n s   t h e   w r i w e r   a w w d n c a t n i o   a o l 
 n o t e r w r e t a t n i o   n   i u u e r   m g   t h e i r n e s   n o   t h e   h i w e   t h a t   t h e 
 e s s e o c e   i u   i p n o a k a o   p a r a t e   k n d d   r e m a n o   n o t a c t

"""
messageDecr = """
because the practice of the basic movements of kata is
the focus and mastery of self is the essence of matsubayashi ryu karate do i shall try to elucidate the
movements of the kata according to my interpretation
based on forty years of study

it is not an easy task to explain each movement and its 
significance and some must remain unexplained to give a 
complete explanation one would have to be qualified and
inspired to such an extent that he could reach the state
of enlightened mind capable of recognizing soundless
sound and shapeless shape i do not deem myself the final
authority but my experience with kata has left no doubt
that the following is the proper application and 
interpretation i offer my theories in the hope that the
essence of okinawan karate will remain intact 
"""




print("\nThe hidden message in the decryption is: " + messageDecr)

