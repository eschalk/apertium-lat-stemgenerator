import csv
import string

# Set up input and output variables for the script
dogbreedlist = open("export.tsv", "r")
csv.register_dialect('dogbreeds', delimiter='\t', quoting=csv.QUOTE_NONE)
# also works:
#csv.register_dialect('dogbreeds', delimiter='	', quoting=csv.QUOTE_NONE)

# Set up CSV reader and process the header
csvReader = csv.reader(dogbreedlist, dialect="dogbreeds")
header = csvReader.__next__()

# Make an empty list
lemmaList = []
count = 0

# Loop through the lines in the file and get each coordinate
for row in csvReader:
    row.append("placeholder")
    row.append("placeholder2")
    row.append("placeholder3")
    row.append("placeholder4")
    row.append("placeholder5")
    row.append("placeholder6")
    row.append("placeholder7")


    if row[6]=="\"Preposition\"":
        print("<e a=\"agfl-lat\" lm=",row[0],"><i>",row[0].replace('"', ''),"</i><par n=\"ab__pr\"/></e>","<!--",row[2],"-->",sep="")
    if row[6]=="\"Conjunction\"":
        print("<e a=\"agfl-lat\" lm=",row[0],"><i>",row[0].replace('"', ''),"</i><par n=\"et__cnjcoo\"/></e>","<!--",row[2],"-->",sep="")
    if row[6]=="\"Interjection\"":
        print("<e a=\"agfl-lat\" lm=",row[0],"><i>",row[0].replace('"', ''),"</i><par n=\"o__ij\"/></e>","<!--",row[2],"-->",sep="")
    if row[6]=="\"Adverb\"":
        print("<e a=\"agfl-lat\" lm=",row[0],"><i>",row[0].replace('"', ''),"</i><par n=\"quasi__adv\"/></e>","<!--",row[2],"-->",sep="")
    if row[6]=="\"Verb\"":
        consonants=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","u","v","w","x","y","z"]
        translator = str.maketrans('', '', string.punctuation+'–')
        pieces = row[0].translate(translator).split()
        pieces22 = row[0].split()
        pieces.append("placeholder")
        pieces.append("placeholder2")
        pieces.append("placeholder3")
        presentStem=("placeholder")
        perfectpsvStem=("placeholder")
        perfectStem=("placeholder")
        p1 = pieces[0]
        p2 = pieces[1]
        p3 = pieces[2]
        p4 = pieces[3]
        lemma = p1
        #perfectStem = p3[:-1]
        #perfectpsvStem = p4[:-2]
        paradigm = "paradigm"
        if p4=="sum":
            perfectpsvStem = p3[:-2]
            if p2.endswith("ari"):
                paradigm = "con/ari__vblex"
                presentStem = p2[:-3]
            else:
                paradigm = "loqu/i__vblex"
                presentStem = p2[:-1]
            if perfectpsvStem=="":
                perfectpsvStem="placeholder"
            if presentStem=="":
                presentStem="placeholder"
            print("<e a=\"agfl-lat\" lm= \"",lemma,"\" ><i>",presentStem.replace('"', ''),"</i><par n=\"",paradigm,"\"/></e>","<!--",row[2],"-->",sep="")
            print("<e a=\"agfl-lat\" lm= \"",lemma,"\" ><i>",perfectpsvStem.replace('"', ''),"</i><par n=\"amat/us__vblex\"/></e>","<!--",row[2],"-->",sep="")
        else:
            perfectpsvStem = p4[:-2]
            perfectStem = p3[:-1]
            if p2.endswith("are"):
                paradigm = "am/are__vblex"
                presentStem = p2[:-3]
            if p2.endswith("ire"):
                paradigm = "aud/ire__vblex"
                presentStem = p2[:-3]
            if p2.endswith("ere"):
                firstperson = p1[:-1]
                if firstperson.endswith("e"):
                    paradigm = "man/ere__vblex"
                    presentStem = p2[:-3]
                else:
                    paradigm = "teg/ere__vblex"
                    presentStem = p2[:-3]
            if perfectStem=="":
                perfectStem="placeholder"
            if perfectpsvStem=="":
                perfectpsvStem="placeholder"
            if presentStem=="":
                presentStem="placeholder"
            print("<e a=\"agfl-lat\" lm= \"",lemma,"\" ><i>",presentStem.replace('"', ''),"</i><par n=\"",paradigm,"\"/></e>","<!--",row[2],"-->",sep="")
            print("<e a=\"agfl-lat\" lm= \"",lemma,"\" ><i>",perfectStem.replace('"', ''),"</i><par n=\"amav/isse__vblex\"/></e>","<!--",row[2],"-->",sep="")
            print("<e a=\"agfl-lat\" lm= \"",lemma,"\" ><i>",perfectpsvStem.replace('"', ''),"</i><par n=\"amat/us__vblex\"/></e>","<!--",row[2],"-->",sep="")
        if paradigm=="paradigm":
            count=count+1
    if row[6]=="\"Noun\"":
        translator = str.maketrans('', '', string.punctuation+'–')
        pieces = row[0].translate(translator).split()
        pieces.append("placeholder")
        pieces.append("placeholder2")
        lemma = pieces[0]
        bit = pieces[1]
        gender = pieces[2]
        stem = "stem"
        paradigm = "paradigm"
        if lemma.endswith("us") and bit.endswith("i"):
            paradigm="mur/us__n"
            stem=lemma[:-2]
        if lemma.endswith("a") and bit.endswith("ae"):
            paradigm="aqu/a__n"
            stem=lemma[:-1]
        if lemma.endswith("um") and bit.endswith("i"):
            paradigm="bell/um__n"
            stem=lemma[:-2]
        if lemma.endswith("us") and bit.endswith("us"):
            paradigm="dom/us__n"
            stem=lemma[:-2]
        if bit.endswith("is"):
            if lemma.endswith("or") and gender=="f":
                paradigm="soror/__n"
                stem=bit[:-2]
            if lemma.endswith("x") and gender=="f":
                paradigm="ar/x__n"
                stem=bit[:-3]
            if lemma.endswith("s") and bit.endswith("atis") and gender=="f":
                paradigm="tempesta/s__n"
                stem=bit[:-3]
            if lemma.endswith("a") and bit.endswith("tis") and gender=="n":
                paradigm="systema/__n"
                stem=bit[:-3]
            if lemma.endswith("o") and bit.endswith("nis") and gender=="m":
                paradigm="hom/o__n"
                stem=bit[:-4]
            if lemma.endswith("is") and gender=="m":
                paradigm="can/is__n"
                stem=bit[:-2]
            if lemma.endswith("is") and gender=="f":
                paradigm="av/is__n"
                stem=bit[:-2]
            if lemma.endswith("al") and gender=="n":
                paradigm="animal/__n"
                stem=bit[:-2]
            if lemma.endswith("ol") and bit.endswith("olis") and gender=="m":
                paradigm="sol/__n"
                stem=bit[:-2]
            if lemma.endswith("us") and gender=="n":
                paradigm="temp/us__n"
                stem=bit[:-4]
            if lemma.endswith("ut") and bit.endswith("itis") and gender=="n":
                paradigm="cap/ut__n"
                stem=bit[:-4]
            if lemma.endswith("io") and gender=="f":
                paradigm="regio/__n"
                stem=bit[:-3]
            if lemma.endswith("itudo") and bit.endswith("itudinis") and gender=="f":
                paradigm="magnitud/o__n"
                stem=bit[:-4]
            if lemma.endswith("ger") and bit.endswith("gris") and gender=="m":
                paradigm="ag/er__n"
                stem=bit[:-2]
            if lemma.endswith("ter") and bit.endswith("tris") and gender=="f":
                paradigm="mat/er__n"
                stem=bit[:-2]
            elif gender=="f":
                paradigm="av/is__n"
                stem=bit[:-2]
            if gender=="m":
                paradigm="can/is__n"
                stem=bit[:-2]
        if stem=="":
            stem="placeholder"
        print("<e a=\"agfl-lat\" lm= \"",lemma,"\" ><i>",stem.replace('"', ''),"</i><par n=\"",paradigm,"\"/></e>","<!--",row[2],"-->",sep="")
    if row[6]=="\"Adjective\"":
        translator = str.maketrans('', '', string.punctuation+'–')
        pieces = row[0].translate(translator).split()
        pieces.append("placeholder")
        lemma = pieces[0]
        stem = "stem"
        paradigm = "paradigm"
        if lemma.endswith("us"):
            stem = lemma[:-2]
            paradigm = "alt/us__adj"
        if lemma.endswith("er") and pieces[1].endswith("a"):
            stem = lemma[:-2]
            paradigm = "pulch/er__adj"
        if lemma.endswith("ns") and pieces[1].endswith("ntis"):
            stem = lemma[:-1]
            paradigm = "distan/s__adj"
        if lemma.endswith("er") and pieces[1].endswith("e"):
            stem = lemma[:-2]
            paradigm = "terrest/er__adj"
        if lemma.endswith("is") and pieces[1].endswith("e"):
            stem = lemma[:-2]
            paradigm = "commun/is__adj"
        if lemma.endswith("is") and pieces[1].endswith("is"):
            stem = lemma[:-2]
            paradigm = "commun/is__adj"
        print("<e a=\"agfl-lat\" lm= \"",lemma,"\" ><i>",stem.replace('"', ''),"</i><par n=\"",paradigm,"\"/></e>","<!--",row[2],"-->",sep="")
    #if paradigm == "paradigm":
    #    count = count+1

# Print the coordinate list
print(count)
