from cs50 import SQL
# any like db and sql specify from cs50 library

db = SQL("sqlite:///favorites.db") # opeining in python code

favorite = input("Favorite: ")

rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE language = ?", favorite)
# need to mention the value not then error ,count() and () no space COUNT(*)
           # a function or a method and to find how many people like ...
    # single is meant to be a placeholder for a value like the string ? without any quote  like % s in c

# if is a list of 0 or more rows.So if you match a row, you get back a list of one row.
#If you match two rows, you get back a Python list of two rows.
#If you match nothing, you get back a list with nothing in it, of length 0in that case.
row = rows[0] #Row equals rows bracket 0.So I'm just, for the sake of discussion now,assuming that I'm going to get back at least 1 and, frankly, just 1 row.
# as rows is a list and one row

#But row is now a single row.
#And, now, what this function db.execute does, per its own documentation,
#is it returns to you, yes, a list of rows.
#But, much like the DictReader in the context of CSV files,
#each of the elements in that list of rows is itself going to be a dictionary.
#And the keys for each of those dictionaries
#is going to be the name of the columns from the SQL table,
#just like the DictReader is grabbing the column names from the CSV itself.
print(row["n"]) # print row, quote, unquote, "n" because I want into index into that one dictionaryand get back the value of n, which, c be clear,was the alias that I gave to COUNT * just so I don't have to keep typingCOUNT *, COUNT *.

# as there is not same coloum or file as video so the file will not be found 
