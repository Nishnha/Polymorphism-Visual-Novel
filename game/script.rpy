# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Main characters used by this game.
define whitlock = Character('Whitlock', color="#c8ffc8")
define mc = Character('Mikeadita', color="#FF8000")
define nish = Character('Nishnha', color="#008080")
define sean = Character('Sean AKA MemeMachine2016', color="#000000")

# Side characters
define girl0 = Character('Nasufiaw', color="#C0C0C0")
define girl1 = Character('Nabeel', color="#805000")
define obama = Character('Obama', color="#202020")
define onenugget = Character('One-Nugget', color="#0000FF")

image mc = Placeholder("boy")
image girl0 = Placeholder("girl")
image nish = Placeholder("boy")

# Scenes
image bike = "092.JPG"
image wheel = "022.JPG"

#################################################################################

# The game starts here.
label start:
    scene bike
    show whitlock with dissolve

    whitlock "Hello this is a tale of one of my legendary student that went out and found his girl of his dreams from my lesson on polymorphism"
    whitlock "Please do not copy this project it is completely reserved by the NTG Foundation"
    
    jump opening

label opening:
    scene wheel with fade
    show mc with dissolve

    "Im so jealous of Sean getting all the girls with his memes"
    mc "I need to date someone and I want them to be super polymorphic!"
    "I realized I said that out loud. Everyone turned to me and I tried to pretend
    I wasn't alive"

    with dissolve

    show mc at right with dissolve
    show nish at left with dissolve
    
    nish "You wot m8?"
    mc "Ahhhn I want a girl that can be anything of my dreams"
    mc "I don't know what polymorphism is though!!!"
    mc "..."
    nish "Same."
    mc "I guess we'd better go to class."

    jump inClass

label inClass:
    
    whitlock "Today we're going to learn about polymorphism."
    whitlock "I'm about to blow your minds."
    whitlock "We're making polymorphic sandwiches."
    nish "Can we eat them afterwards?"
    whitlock "I don't think you'll want to."
    sean "Yeah, instead of jelly we're using the darkness of my soul."
    whitlock "Polymorphism is when a variable's type is a super class with multiple sub classes."
    whitlock "The variable can refer to different objects at different times as long as they all extend the super class!"
    whitlock "This way, your code doesn't have to care or know about which subclass it's using. It'll all work the same."
    nish "Can we eat the sandwiches yet?"
    whitlock "We haven't even made them!"
    mc "I'm so confused..."
    mc "If that's what polymorphism is, how can a person be polymorphic?"
    nish "..."
    nish "What?"
    whitlock "I need a volunteer for making these sandwiches."
    
    menu: 
        "volunteer yourself":
            jump volunteerSelf
        "Point at Galen and volunteer him":
            jump volunteerGalen

label hallway:
    

label obamascene:
    
    mc "It's halfway through the day and I still don't understand how someone can be polymorphic!"
    mc "What am I going to do Obama?"
    obama "Don't just play on your phone, program it."
    mc "..."
    mc "I mean about learning about polymorphism!"
    obama "Don't just play on your phone, program it."
    mc "But how is programming my phone going to solve my relationship problems?"
    obama "Don't just play on your phone, program it."
    mc "..."
    mc "Thanks Obama."
    
label conclusion:
    mc "I don't care how you brush your teeth, or how you eat your sandwiches."
    mc "I just care that..."

    menu: 
        "You have good hygiene":
            jump hygiene
        "You're happy":
            jump happy

return #ends game
