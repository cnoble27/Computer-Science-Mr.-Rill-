import pyautogui as pg
import webbrowser as wb
points = 0
show = pg.prompt("What is your favorite show")
if show == "Parks and Rec":
    pg.alert("That is a really good show!")
    wb.open("https://www.youtube.com/watch?v=hPkf4yoU9J0")
    points += 5
elif show == "The Office":
    pg.alert("I love Dwight!")
    wb.open("https://www.youtube.com/watch?v=1oySHDwXTWw")
    points += 5
elif show == "Meat Eater":
    pg.alert("I love to hunt!")
    wb.open("https://www.youtube.com/watch?v=1G8Xlx7dfT8")
    points +=5
elif show == "Seal Team":
    pg.alert("Action shows are great!")
    wb.open("https://www.youtube.com/watch?v=Ebcs17KOZ5M")
    points +=5
elif show == "Riverdale":
    pg.alert("Yeah, no.")
    wb.open("https://www.youtube.com/watch?v=t-JzvCzj5a0")
    points -=1000
elif show == "Family Guy":
    pg.alert("I strongly dislike that show.")
    wb.open("https://www.youtube.com/watch?v=H46FRRvb-9o")
    points -=1000
else:
    pg.alert("Your favorite show is " + show)
fish = pg.prompt("What is your favorite fish")
if fish == "Red Snapper":
    pg.alert("That is one tasty fish!")
elif fish == "Goliath Grouper":
    pg.alert("That is one big fish!")
elif fish == "Salmon":
    pg.alert("I see that you are a fly fisherman!")
elif fish == "Rainbow Trout":
    pg.alert("They are so much fun to catch!")
elif fish == "Pufferfish":
    pg.alert("Puffer fish are funny looking.")
elif fish == "Swordfish":
    pg.alert("Swordfish are dangerous.")
else:
    pg.alert("Your favorite fish is " + fish)
game = pg.prompt("What is your favorite game?")
if game == "Fortnite":
    pg.alert("Fortnite is my favorite game as well!")
elif game == "Mario Cart":
    pg.alert("Ok, you are an old timer")
elif game == "PUBG":
    pg.alert("That is one fun game!")
elif game == "Overwatch":
    pg.alert("Overwatch was cool before Fortnite.")
elif game == "World of Warcraft":
    pg.alert("Mr. Rill is a huge fan as well!")
elif game == "NHL 19":
    pg.alert("I play real hockey, so naturally I like the game.")
else:
    pg.alert("Your favorite game is " + game)
brand = pg.prompt("What is your favorite brand?")
if brand == "Asics":
    pg.alert("Don't let anybody bully you!")
elif brand == "Nike":
    pg.alert("I used to like you.")
elif brand == "Adidas":
    pg.alert("They make some good soccer cleats!")
elif brand == "Sketchers":
    pg.alert("I have no words.")
elif brand == "Supreme":
    pg.alert("You think that you are cool, don't you!")
elif brand == "Vineyard Vines":
    pg.alert("Is that so.")
else:
    pg.alert("Your favorite brand is " + brand)
name = pg.prompt("What is your favorite name?")
if name == "Santos":
    pg.alert("I really like that name.")
elif name == "Charlie":
    pg.alert("That is by far the best name!")
elif name == "Jay":
    pg.alert("I am so sorry for you.")
elif name == "Teddy":
    pg.alert("It's a common name but what can you do?")
elif name == "Christian":
    pg.alert(" I like the flow of that!")
elif name == "Andrew":
    pg.alert("Please close the program.")
else:
    pg.alert("Your favorite name is " + name)
pg.alert(points)
