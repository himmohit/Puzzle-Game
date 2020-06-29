print("Welcome to Puzzle Game!")
name = input("What is your name? ")
age = int(input("How old are you? "))
print('Hi',name, 'You are',age,' years old.')
health = 10

if age >= 18:
  print("You are enough to play.")
  want_to_play = input("Do you want to Play (yes/no)? ").lower()

  if want_to_play == "yes":
    print("Good to hear that! Let's Play the Game.")
    swim = input("Do you know how to Swim (yes/no)? ").lower()
    
    if swim == "yes":
      print("Sounds good!") 
      print("You got '10' Health.")
      swim_in_lake = input("Okay! So, There's two way you want to swim in a lake or river (lake/river)? ").lower()

      if swim_in_lake == "lake":
        print("It seems you are brave heart! Well! you swim in the lake and you got caught by fish and you lost '5 health'.")
        print("Your remaining Health is '5' ")

        ans = input("Alright! So, Do you want to go across or around the lake (across/around)? ").lower()
        if ans == "around":
          print("Congratulations! You won.")

        else: 
          print("As you decided to swim across the lake somehow bit by 'aquatic animal' and you lose your remaining health.")
          print("Your Health is '0' and you lost this Game.")

      elif swim_in_lake == "river":
        print("It seems you are brave heart! But somehow you faced a crocodile and you losted your Health")
        print("Your Health is '0'. Best of luck for the next time.")

      else:
        print("Ahh! You made wrong choice. You can try later.")

    else:
      print("Sorry! You Losted.")

  else:
    print("Thanks! You can try again.")

else:
  print("Thank you for your time! You should be atleast 18 years old.")

