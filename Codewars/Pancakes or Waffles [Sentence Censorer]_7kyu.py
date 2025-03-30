"""
Nombre: Patricia Pérez Cruz
Descripción:
Task 7 kyu
The owner of a certain chatbox app has came under fire recently for a drama regarding the age old debate
of pancakes or waffles. Because of this, he came to you in order to hide any words regarding pancakes.

The following words are the words that he is looking to censor by replacing it with an equal amount of astricks (*):
pancakes, flapjacks, slapjacks, hotcakes

In conjunction to that, the following words shall be highlighted with a double astricks (**):
waffles, crepes, blintzes
Finally, as long as there is no mention of a waffle relating word in the sentence, also censor the
following word unless, there is a waffle relating word then highlight it:

syrup, honey, jam, butter, chocolate, margarine

Examples
like waffles with chocolate")) --> "I like **waffles** with **chocolate**"

print(censor("I like pancakes with syrup" --> "I like ******* with *****"

print(censor("The debate between pancakes and waffles is as sweet as honey"
--> "The debate between ******** and **waffles** is as sweet as **honey**"
"""


def censor(text):
    #Creé mis listas para cada situación que se me planteó
    palabras_censura = ["pancakes", "flapjacks", "slapjacks", "hotcakes"]
    palabras_resaltar = ["waffles", "crepes", "blintzes"]
    palabras_extra = ["syrup", "honey", "jam", "butter", "chocolate", "margarine"]
    palabra_actual = ""
    contiene_resaltado = False
    resultado = ""

    #En la primera pasada revisé si el texto contiene alguna palabra a resaltar
    texto_lower = text.lower()
    for palabra in palabras_resaltar:
        if palabra in texto_lower:
            contiene_resaltado = True
            break

    #En la segunda pasada se podría decir que procesé el texto
    for i in range(len(text) + 1):
        if i < len(text) and text[i].isalpha():
            palabra_actual += text[i]
        else:
            if palabra_actual:
                palabra_lower = palabra_actual.lower()
                if palabra_lower in palabras_resaltar:
                    resultado += "**" + palabra_actual + "**"
                elif palabra_lower in palabras_censura:
                    resultado += "*" * len(palabra_actual)
                elif palabra_lower in palabras_extra:
                    if contiene_resaltado:
                        resultado += "**" + palabra_actual + "**"
                    else:
                        resultado += "*" * len(palabra_actual)
                else:
                    resultado += palabra_actual
                palabra_actual = ""
            if i < len(text):
                resultado += text[i]

    return resultado #Y ya por último devolví el resultado