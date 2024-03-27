#Palindrome Keimeler

kelime=input("Bir kelime giriniz:")
ters=kelime[::-1]

if(kelime==ters):
    print(kelime,"palindrome kelimedir.")
else:
    print(kelime, "palindrome kelime değildir.")


