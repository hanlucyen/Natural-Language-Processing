Python 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:17:27) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import nltk
from nltk.book import *
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
text1
<Text: Moby Dick by Herman Melville 1851>
text2
<Text: Sense and Sensibility by Jane Austen 1811>
>>> text3
<Text: The Book of Genesis>
>>> text1.concordane("montrous")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    text1.concordane("montrous")
AttributeError: 'Text' object has no attribute 'concordane'. Did you mean: 'concordance'?
>>> text1.concordance("montrous")
no matches
>>> text1.concordance("monstrous")
Displaying 11 of 11 matches:
ong the former , one was of a most monstrous size . ... This came towards us , 
ON OF THE PSALMS . " Touching that monstrous bulk of the whale or ork we have r
ll over with a heathenish array of monstrous clubs and spears . Some were thick
d as you gazed , and wondered what monstrous cannibal and savage could ever hav
that has survived the flood ; most monstrous and most mountainous ! That Himmal
they might scout at Moby Dick as a monstrous fable , or still worse and more de
th of Radney .'" CHAPTER 55 Of the Monstrous Pictures of Whales . I shall ere l
ing Scenes . In connexion with the monstrous pictures of whales , I am strongly
ere to enter upon those still more monstrous stories of them which are to be fo
ght have been rummaged out of this monstrous cabinet there is no telling . But 
of Whale - Bones ; for Whales of a monstrous size are oftentimes cast up dead u
>>> text1.similar("monstrous")
true contemptible christian abundant few part mean careful puzzled
mystifying passing curious loving wise doleful gamesome singular
delightfully perilous fearless
>>> text2.similar("monstrous")
very so exceedingly heartily a as good great extremely remarkably
sweet vast amazingly
>>> text2.common_contexts(["monstrous","very"])
am_glad a_pretty a_lucky is_pretty be_glad
>>> text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
>>> a=text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
>>> a
>>> text3.generate()
Building ngram index...
laid by her , and said unto Cain , Where art thou , and said , Go to ,
I will not do it for ten ' s sons ; we dreamed each man according to
their generatio the firstborn said unto Laban , Because I said , Nay ,
but Sarah shall her name be . , duke Elah , duke Shobal , and Akan .
and looked upon my affliction . Bashemath Ishmael ' s blood , but Isra
for as a prince hast thou found of all the cattle in the valley , and
the wo The
"laid by her , and said unto Cain , Where art thou , and said , Go to ,\nI will not do it for ten ' s sons ; we dreamed each man according to\ntheir generatio the firstborn said unto Laban , Because I said , Nay ,\nbut Sarah shall her name be . , duke Elah , duke Shobal , and Akan .\nand looked upon my affliction . Bashemath Ishmael ' s blood , but Isra\nfor as a prince hast thou found of all the cattle in the valley , and\nthe wo The"
>>> len(text3)
44764
>>> sorted(set(text3))

>>> len(set(text3))
2789
>>> from __future__ import division
>>> len(text3)/len(set(text3))
16.050197203298673
>>> text3.count("smote")
5
>>> 100*text4.count('a')/len(text4)
1.4569256756756757
