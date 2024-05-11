import sqlite3
##Settings
#The location of your lbp.db database file. 
dblocation = """D:\DB.Browser.for.SQLite-3.12.2-win64\DB Browser for SQLite\lbp.db""" 
#The number of the game entry you want levels from. Self explanatory
GameNumber = 2 
#The SQL statement the script uses. Unless you know how SQL works i would advise not to change this
SQLStatement = """
SELECT name,description,npHandle,hex(rootLevel),game 
    from slot 
    WHERE heartCount > 30 AND game == ?-1 ORDER BY RANDOM()
                        """ 
WriteToFile = True #Makes the script write the level info to a file if it's set to true. Useful for programs like OBS to display the level info
#------------------
#print("Executing SQL Statement...")
con = sqlite3.connect(dblocation)
cursor = con.cursor()
result = cursor.execute(SQLStatement,[GameNumber])
#print("Done! ")
name,description,npHandle,rootLevel,game = result.fetchone()
endstring = ""
endstring += name+"\n"
endstring += "LBP"+str(game+1)+" level by "+npHandle+"\n"
endstring += "---------------"+"\n"
if(description == None):
    endstring += "No description provided"+"\n"
else:
    endstring += description+"\n"
endstring += "HASH: "+str.lower(rootLevel)+"\n"

if(WriteToFile):
    file = open("randomlevelsel.txt","w")
    file.write(endstring)
    file.close()
print(endstring)