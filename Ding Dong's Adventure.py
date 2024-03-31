#                         ;\ 
#                            |' \ 
#        _                  ; : ; 
#       / `-.              /: : | 
#       |  ,-.`-.          ,': : | 
#       \  :  `. `.       ,'-. : | 
#        \ ;    ;  `-.__,'    `-.| 
#         \ ;   ;  :::  ,::'`:.  `. 
#          \ `-. :  `    :.    `.  \ 
#           \   \    ,   ;   ,:    (\ 
#            \   :., :.    ,'o)): ` `-. 
#           ,/,' ;' ,::"'`.`---'   `.  `-._ 
#         ,/  :  ; '"      `;'          ,--`. 
#        ;/   :; ;             ,:'     (   ,:) 
#          ,.,:.    ; ,:.,  ,-._ `.     \""'/ 
#          '::'     `:'`  ,'(  \`._____.-'"' 
#             ;,   ;  `.  `. `._`-.  \\ 
#             ;:.  ;:       `-._`-.\  \`. 
#              '`:. :        |' `. `\  ) \ 
#           ` ;:       |    `--\__,' 
#                   '`      ,' 
#                        ,-' 
print("You have travelled a long and storied path only to find that you have ended up in the worst place you can imagine: Ding Dong's bedroom.")
panic = input("Do you panic? Yes or No?")
if panic.lower() == " yes":
    print("You made a mistake. It's over.")
else:
    print("Of course not. You don't panic. You never panic. Even when Ding Dong's involved.")
    tool = input("You check your pockets for anything of use. In them, you find a key, a toothbone, and some fluff. Which do you take?")
    if tool.lower() == " key":
        print("There are no doors here. You lose.")
    elif tool.lower() == " toothbone":
        print("This only hastens your demise. It was chicken flavored. Game over.")
    else:
        print("You can use this to negotiate with Sleepytime Bear! He always needs more fluff!")
        namepass = input("You approach Sleepytime Bear and proceed to negotiate. He wants to know your name.")
        if namepass.lower() == " ding dong":
            print("Sleeptime Bear can see through your lies. You lose.")
        elif namepass.lower() == " nick":
            print("Nuh uh. You lose.")
        elif namepass.lower() == " katie rose":
            print("Sleepytime Bear was testing you. He knew your name, but he was just being sassy. He takes the fluff from you and agrees to show you the way out.")
        else:
            print("Sleepytime Bear doesn't know who you are. He tells on you and you lose.")
