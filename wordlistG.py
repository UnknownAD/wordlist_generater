print("""
 █     █░ ▒█████   ██▀███  ▓█████▄  ██▓     ██▓  ██████ ▄▄▄█████▓  ▄████ 
▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌▓██▒    ▓██▒▒██    ▒ ▓  ██▒ ▓▒ ██▒ ▀█▒
▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌▒██░    ▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒██░▄▄▄░
░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌▒██░    ░██░  ▒   ██▒░ ▓██▓ ░ ░▓█  ██▓
░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓ ░██████▒░██░▒██████▒▒  ▒██▒ ░ ░▒▓███▀▒
░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░    ░▒   ▒ 
  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ ░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░    ░      ░   ░ 
  ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░   ░ ░    ▒ ░░  ░  ░    ░      ░ ░   ░ 
    ░        ░ ░     ░        ░        ░  ░ ░        ░                 ░ 
                            ░                                   by:UnknownAD -_-
""")
stdin=[]
result=[]
config=__import__('sys').argv
while True:
    userinput=input("\033[1;31;40m$ Type a keyword: \033[0m")
    if userinput!="exit":stdin.append(userinput)
    else:break
print(stdin)
def generation(ll):
   for p1 in ll:
       for p2 in ll:
           result.append(p2+"\n")
           result.append(p1+p2+"\n")
           result.append(p1+p2+"\n")
   return list(dict.fromkeys(result))
stdout=generation(stdin)
file=open(config[1],'w')
for x in stdout:
    file.write(x)
file.close()
