# Main characters used by this game.
define whitlock = Character('Whitlock', color="#c8ffc8")
define mc = Character('Lucky', color="#FF8000")
image mc = Placeholder("boy")
define maingirl = Character('Star', color="FF8000")
define sean = Character('Sean AKA MemeMachine2016', color="#000000")
define nish = Character('Nishnha', color="#008080")
image nish = Placeholder("boy")

# Placeholder Characters
define girl0 = Character('', color="#FFFFFF")
image girl0 = Placeholder("girl")

int num = 0;


# Scenes
image bike = "092.JPG"
image wheel = "022.JPG"

#################################################################################

# The game starts here.
label start:
    scene bike
    show whitlock with dissolve

    whitlock "Hello this is a tale of one of my legendary students that was enlightened by polymorphism."
    whitlock "Please do not copy this project it is completely reserved by the NTG Foundation."
    
    jump opening

label opening:
    scene wheel with fade

    show sean at center with dissolve
    show girl0 at left

    show mc at right with dissolve

    mc "{i}Im so jealous of Sean getting all the girls with his memes!{/i}"
    mc "{i}Its not that I don't like my relationship now its just too plain and uneventful.{/i}" 
    mc "{i}Simply put I just want to date someone that is interesting and unpredictable!{/i}"
    mc "{i}Maybe I'll ask Sean for some advice.{/i}"
    mc "Hey Sean ...."
    "bell rings and Sean leaves with his crowd of girls."

    hide sean
    hide girl0

    mc "{i}Sigh better get to class, and hopefully I can squeeze my way into talking with him. {/i}"

    with dissolve

    jump inClass

label inClass:
    
    maingirl "Hello"
    mc "Hello"
    mc "{i}Same small talk again{/i}"
    whitlock"{i}Bell rings{/i} Today we're going to learn about polymorphism."
    whitlock "I'm about to blow your minds."
    mc "{i}Oh boy is this going to be as mind blowing as 2-D arrays{/i}"
    whitlock "We're making polymorphic sandwiches."
    mc "{i} Just what?!{/i}" 
    nish "Can we eat them afterwards?"
    whitlock "I don't think you'll want to."
    sean "Yeah, instead of jelly we're using the darkness of my soul."
    randomfangirl "Sean's so cool"
    mc "{i} Darn it Sean {/i}"
    whitlock "Polymorphism is when a variable's type is a super class with multiple sub classes."
    whitlock "The variable can refer to different objects at different times as long as they all extend the super class!"
    whitlock "This way, your code doesn't have to care or know about which subclass it's using. It'll all work the same."
    nish "Can we eat the sandwiches yet?"
    whitlock "We haven't even made them!"
    mc "{i}I'm so confused about this...{/i}"
    nish "..."
    nish "What?"
    whitlock "Let me pick two volunteers to demonstrate this"
    mc "{i}Ugh I hope its not me{/i}"
    whitlock "I pick Lucky and Star for my demonstration"
    mc "{i}Ugh{/i}"
    whitlock "Please pick a card for a recipe to follow"
    
    
    menu: 
        "Pick Left Card":
            jump leftCard
        "Pick Right Card":
            jump rightCard

label leftCard:
    num++;
    whitlock "Read your instructions and proceed to make your sandwiches"
    mc "{i}What is this just flatbread,pepperjack cheese, and ham? Lets see what Star is doing. Only wheat and ham just what's going on here?!{/i}"
    whitlock "As you can see lucky and star has made two sandwiches following the instructions on the card"
    whitlock "If you think of the idea of the sandwich as the variable, and the cards being classes changing the variable in it then you understand polymorphism!"
    idle "{i}Class crickets{/i}"
    nish "So now can we just eat the sandwiches"
    whitlock "........ sure"
    mc "{i} Huh so that was polymorphism I wish Star would be more polymorphic{/i}"
    mc "{i} Maybe while everyone is eatting I should go talk to star about this{/i}"
    menu:
        "Go talk to Star"
        jump Star
        "Sit idly"
        if(num = 1)
        jump obamaScene1
        if(num = 0)
        jump obamaScene2
label rightCard:
    whitlock "Read your instructions and proceed to make your sandwiches"
    mc "{i}What is this just only wheat and ham ? Lets see what star is doing. She's using flatbread,pepperjack cheese, and ham? Just what's going on here.{/i}"
    whitlock "As you can see lucky and star has made two sandwiches following the instructions on the card."
    whitlock "If you think of the idea of the sandwich as the variable, and the cards being classes changing the variable in it then you understand polymorphism!"
    idle "{i}Class crickets{/i}"
    nish "So now can we just eat the sandwiches"
    whitlock "........ sure"
    mc "{i} Huh so that was polymorphism. I wish Star would be more polymorphic.{/i}"
    mc "{i} Maybe while everyone is eatting I should go talk to star about this.{/i}"
    menu:
        "Go talk to Star"
        jump Star
        "Sit idly"
        jump obamaScene

label Star:
    mc "Hey Star I have something that I want to talk to you about"
    maingirl "???"
    menu:
        "Its about us"
        jump deepConversation1
        "Nevermind lets talk about it in the hall"
        jump hallWay
    maingirl "???"
label deepConversation1
    mc "its just that 
    menu:
        "I need private tutoring for polymorphism, because I'm totally lost"
        jump hallWay
        "I think this thing between you and me won't work out"
        jump deepConversation2
label deepConversation2
    maingirl "!!!!!!!!!! Why is that!"
    mc "{i} I'm shocked at how much she's reacting to this{/i}"
    menu: 
        "Tell her its a joke and it was fun seeing her reaction"
        jump badEnding
        "Tell her that you didn't know she cared so much"
    jump conclusion
label hallWay:
    mc "Hey Star has life been bland"
    maingirl "No"
    mc "I've been thinking if there should be a change between you and me"
    maingirl "...."
    mc "It's just that I think you and I won't work out"
    maingirl "!!!!!!!!!! Why is that!"
    mc "{i} I'm shocked at how much she's reacting to this{/i}"
    menu: 
        "Tell her its a joke and it was fun seeing her reaction"
        jump badEnding
        "Tell her that you didn't know she cared so much"
    jump conclusion
    
    
label obamascene1:
    
    mc "Sigh I wish Star could just be more polymorphic!"
    mc "Just what am I going to do Obama?"
    obama "Don't just play on your phone, program it."
    mc "..."
    mc "That doesn't help!"
    obama "Don't just play on your phone, program it."
    mc "But how is programming my phone going to solve my relationship problems?"
    obama "Don't just play on your phone, program it."
    mc "..."
    mc "Thanks Obama."
    idle "{i}bell rings{/i}
    jump hallway

label obamascene2:
    
    mc "Sigh I wish Star could just be more polymorphic!"
    mc "Just what am I going to do Obama?"
    obama "..."
    mc "I need to tell her how I feel but I don't know how!"
    obama "..."
    mc "What would you do if you were in my position?"
    obama "Don't just play on your phone, program it."
    mc "..."
    mc "Thanks Obama."
    idle "{i}bell rings{/i}
    jump hallway
    
label conclusion:
    maingirl "!!!!!!!!!!!!!"
    mc "I didn't know she liked me this much and he accidently said it outloud"
    maingirl "Of course, but I didn't know how to talk to you"
    mc "......"
    mc "We're both dumb"
    mc "I guess we can both use some polymorphism on us in our self class"

return #ends game
label badEnding:
    mc "The boring relationship carried out until until graduation"
    mc "{i}Only if she could be changed{/i}"

return #ends game
