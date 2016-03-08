# Characters
define whitlock = Character('Whitlock', color="#c8ffc8")
image whitlock = Placeholder("girl")

define mc = Character('Mikeadita', color="#FF8000")
image mc = Placeholder("boy")

define nish = Character('Nishnha', color="#008080")
image nish = Placeholder("boy")

define sean = Character('Sean AKA MemeMachine2016', color="#000000")

define girl0 = Character('Nasufiaw', color="#C0C0C0")
image girl0 = Placeholder("girl")

define girl1 = Character('Nabeel', color="#805000")

define obama = Character('Obama', color="#202020")

define onenugget = Character('One-Nugget', color="#0000FF")


# Scenes
image bike = "092.JPG"
image wheel = "022.JPG"

#################################################################################

label start:
    scene bike
    show whitlock with dissolve

    whitlock "Hello this is a tale of one of my legendary student that went out and found his girl of his dreams from my lesson on polymorphism"
    whitlock "Please do not copy this project it is completely reserved by the NTG Foundation"
    
    jump opening

label opening:
    scene wheel with fade
    show mc with dissolve

    mc "Im so jealous of Sean getting all the girls with his memes"
    "I realized I said that out loud. Everyone turned to me and I tried to pretend I wasn't alive"

    with dissolve

    show mc at right with dissolve
    show nish at left with dissolve
    
    sean "You wot m8?"
    "Ahhh he heard me"
    sean "Look, you just have to be polymorphic"
    mc "..."
    nish "What does that even mean?"
    sean "If you paid attention in computer scienece you would know!"
    mc "I guess we'd better go to class."

    jump inClass

label inClass:
    scene bike
    show whitlock with dissolve

    whitlock "Today we're going to learn about polymorphism."
    whitlock "I'm about to blow your minds."
    whitlock "We're making polymorphic sandwiches."
    
    show nish at right with moveinright
    nish "Can we eat them afterwards?"

    whitlock "I don't think you'll want to."

    show sean at left with moveinleft
    sean "Yeah, instead of jelly we're using the darkness of my soul."
    
    hide nish with moveoutright
    hide sean with moveoutleft

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
