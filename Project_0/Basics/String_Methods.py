# text = "hello world"
# print(text.capitalize())

# text = "pYtHoN pRoGRamMInG"
# print(text.capitalize())

# text = "HELLO WORLD"
# print(text.casefold())

# text = "Zafar Sir"
# print(f"'{text.center(50, '_')}'")

# text = "hello world"
# print(text.count('l', 2, 5))

# text = "cafē"
# print(text.encode(encoding='ascii', errors='ignore'))

# text = "python programming is fun"
# print(text.endswith('is fun'))
# print("Hello\tWorld abc".expandtabs(8))

# print("hello world".find('o', 3, 7))
# print("python programming".find('prog'))

# text = "Good {}!"
# print(text.format("Evening"))
# print("Addition of {} and {} is {}".format(5, 3, (5+3)))
# print("Addition of {0} and {2} is {1}".format(5, 5+3, 3))
# print(f"Addition of {5} and {3} is {5+3}")

# print("hello world".index('o'))
# print("HELLO124".isupper())
# print("hello124".islower())
# print("hello".isalpha())
# print("1he2llo12".isalnum())
# print("1he2llo12".isascii())
# print("9992399".isdigit())
# print("99923992".isdecimal())
# print("9992399".isnumeric())
# print("_1var".isidentifier())
# print("cafē\t".isprintable())
# print("  ".isspace())
# print(" Hello World".istitle())
# print("_".join("123"))
# print(" ".join(" Zafar Sir "))
# print("'", "hello".ljust(10, '-'), "'", sep="")
# print("-*-*-|*-*-*-*|-*-*-*-*|-*-*-hello".lstrip('|*-'))

# string = "royal technosoft pvt. ltd."
# table = str.maketrans("ot", "0😊")
# print(table)        # print the translation table
# print(string.translate(table)) # print the actual replaced string

# print("royal technosoft".partition("tech"))
# print("royal technosoft".partition(" "))
# print("royal technosoft".partition("o"))
# print("royal technosoft".partition(""))     #ValueError: empty separator
# print("royal technosoft".partition("@"))
# print("royal technosoft".partition("ft"))

# print("royal technosoft".replace("tech", "TECH"))
# print("royal technosoft".replace("tech", ""))

# print("'", "royal technosoft  m      ".rstrip(" "), "'", sep='')
# print("royal technosoft".removeprefix("Ro".casefold()))
# print("royal technosoft".removesuffix("nosoft"))
# print("royal technosoft".rfind("o"))
# print("royal technosoft".rindex("e"))
# print("'", "royal technosoft".rjust(50, '-'), "'", sep="")
# print("royal technosoft".rsplit("tech"))
# print("royal technosoft".rpartition("o"))

# print("royal technosoft".startswith("roy"))
# print("royal Technosoft".split("Tech"))
# print("Lorem ipsum \ndolor sit amet consectetur \n\nadipisicing elit. Error iusto, quam culpa odit non, quae, facilis perspiciatis praesentium optio possimus nisi totam? ".splitlines())
# print("^^^^^^^^^^^^^^-^^---$-----^^----^-0----&--------NAIMISHJI-^^---$-----^^----^-0----&--------^^^^^^^^^^^^".strip("-^$0&"))
# print("NaiMish JiIiIiIi".swapcase())

# print("nAIMiSHjI Maare gAnthiya khaVa Jau he".title())
# print("naimishJII".upper())
print("11001".zfill(8))