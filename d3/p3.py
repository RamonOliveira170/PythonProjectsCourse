print("""
                                         .- ._          *
                 .       (   ) `) ._,--.
          _.-.          (      .' | af }      ._    +
        .'     )         `(_'-'   |--'"        ))        |
       (   _.   )                 |           '"       - * -
      .-.-'  )  _)  .        ["I"I"I"I"}   .             .
     (  `   .)`'              I_I_I_I_I
      `-. (   )          [UUUUI_I_I_I_I
         `-..'            |[__I_I_[#]_I .        .
                   +      |__[I_I_I=I_I
         .       ._    +  |]_ I_[#]-I_I    ._          ;
                 |~       |_[ I_I=I_I_[,   |~
               uuuuu      |__ I_I_I%I_I  uuuuu
               | #_|      |[ _$_I_I%%_I  | _ |
               |-  [      | [ %%I_g%%_I  |  -|         __a:f
          ---..|_  |.--,,'|]_ %_Ia%%I_I -|_- |.------""
               |_-#|  ((  |_[ $%I%%_!^!  | _ |      +
               |   |   )) |[_ |%.%I_|"|  |_  |    n Am   n
             .-[_A_]_ '/  |_ / _Y_)_|`| -[N__]_        n
         ._.'        `- _.--'`'  ' "|\=\ ''    `-.
                      .'             |\=\`-._     `
                   .-'                  `:.  `---....__
""")
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
user = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ").lower()

if user == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    user = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.: ").lower()
    if user == "wait":
        print("You arrive at the island. There is 3 towers. One red, one yellow and one blue.")
        user = input("Which colour do you choose?: ").lower()
        if user == "yellow":
            print("You found the treasure! You win!")
        elif user == "blue":
            print("You enter a room of beasts. Game over")
        else:
            print("You fell into a hole. Game Over")
    else:
        print("Game Over.")
else:
    print("Game Over.")
