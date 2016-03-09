# Main characters used by this game.
define whitlock = Character('Whitlock', color="#c8ffc8")
define mc = Character('Lucky', color="#FF8000")
image mc = "mc.png"
define star = Character('Star', color="FF8000")
image star = "star.png"
define sean = Character('Meme Slangar', color="#D941B0")
define nish = Character('Nishnha', color="#008080")
image nish = ""
define obama = Character('Obama', color="#8DD941")
image obama = "obama.jpg"

# Placeholder Characters
define fangirl = Character('Fangirl', color="#FFFFFF")
image fangirl = Placeholder("girl")

# Scenes
image classroom = "classroom.jpg"
image hallway = "hallway.jpg"
image outside = "outside.jpg"

#################################################################################

# The game starts here.
label start:
    scene classroom
    show whitlock with dissolve

    whitlock "Hello this is a tale of one of my legendary students that was enlightened by polymorphism."
    whitlock "Please do not copy this project it is completely reserved by the NTG Foundation."
    
    jump opening

label opening:
    scene classroom with fade

    show sean at center with dissolve
    show fangirl at left

    show mc at right with dissolve

    mc "{i}Im so jealous of Sean getting all the girls with his memes!{/i}"
    mc "{i}Its not that I don't like my relationship now its just too plain and uneventful.{/i}" 
    mc "{i}Simply put I just want to date someone that is interesting and unpredictable!{/i}"
    mc "{i}Maybe I'll ask Sean for some advice.{/i}"
    mc "Hey Sean ...."
    "bell rings and Sean leaves with his crowd of girls."

    hide sean
    hide fangirl

    mc "{i}Sigh better get to class, and hopefully I can squeeze my way into talking with him. {/i}"

    with dissolve

    jump inClass

label inClass:
    scene classroom
 
    show mc at right
    show star at left with moveinleft

    star "Hello"
    mc "Hello"
    mc "{i}Same small talk again{/i}"

    "bell rings"

    hide star
    show whitlock at center

    whitlock "Today we're going to learn about polymorphism."
    whitlock "I'm about to blow your minds."
    mc "{i}Oh boy is this going to be as mind blowing as 2-D arrays{/i}"
    whitlock "We're making polymorphic sandwiches."
    mc "{i}W-what?!{/i}" 

    show nish at left with moveinleft
    nish "Can we eat them afterwards?"
    whitlock "I don't think you'll want to."
    
    hide nish with moveoutleft

    sean "Yeah, instead of jelly we're using the darkness of my soul."

    show sean with moveinleft

    fangirl "Sean's so cool"

    hide sean with moveoutleft

    mc "{i}Darn it Sean, back at it again with those dank memes!{/i}"
    whitlock "Polymorphism is when a variable's type is a super class with multiple sub classes."

    scene code1

    whitlock "The variable can refer to different objects at different times as long as they all extend the super class!"

    scene code2

    whitlock "This way, your code doesn't have to care or know about which subclass it's using. It'll all work the same."

    scene code3

    pause

    show nish at left with  moveinleft
    nish "Can we eat the sandwiches yet?"
    whitlock "We haven't even made them!"
    mc "{i}I'm so confused about this...{/i}"
    nish "..."
    nish "What? I'm hungry!"
    hide nish with moveoutleft

    whitlock "Let me pick two volunteers to demonstrate this"
    mc "{i}Ugh I hope its not me{/i}"
    whitlock "I pick Lucky and Star for my demonstration"
    mc "{i}Ugh{/i}"
    whitlock "Please pick a recipe to follow"
    
    menu: 
        "Pick Left Card":
            $ card = "left"
            jump sandwich
        "Pick Right Card":
            $ card = "right"
            jump sandwich

label sandwich:
    scene classroom

    show whitlock with dissolve
    whitlock "Read your instructions and proceed to make your sandwiches"

    if card == "left":
        mc "{i}What is this? Just flatbread, pepperjack cheese, and ham? Lets see what Star is doing. Only wheat and ham? What's going on here?!{/i}"

    if card == "right":
        mc "{i}Why is this only wheat and ham? Lets see what Star is doing.{/i}"
    if card == "right":
        mc "{i}She's using flatbread, pepperjack cheese, and ham? Just what's going on here.{/i}"

    whitlock "As you can see lucky and star have made two sandwiches following the instructions on the card"
    whitlock "If you think of the idea of the sandwich as the variable, and the cards being classes changing the variable in it then you understand polymorphism!"
    "{i}Class crickets{/i}"

    show nish at left with moveinleft
    nish "So now can we just eat the sandwiches"
    whitlock "..."
    whitlock "sure"
    hide nish with moveoutleft

    mc "{i} Huh so that was polymorphism. I wish Star would be more polymorphic{/i}"
    mc "{i} Maybe while everyone is eatting I should go talk to her about this{/i}"
    
    menu:
        "Go talk to Star":
            jump Star
        "Sit idly":
            if card == "left":
                jump obamaScene1
            if card == "right":
                jump obamaScene2

label Star:
    scene classroom

    mc "Hey Star I have something that I want to talk to you about"
    star "???"
    menu:
        "Its about us":
            jump deepConversation1
        "Nevermind lets talk about it in the hall":
            jump Hallway

label obamaScene1:
    scene classroom
    
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
    
    "{i}bell rings{/i}"
    
    jump Hallway

label obamaScene2:
    scene classroom
    
    mc "Sigh I wish Star could just be more polymorphic!"
    mc "Just what am I going to do Obama?"
    obama "..."
    mc "I need to tell her how I feel but I don't know how!"
    obama "..."
    mc "What would you do if you were in my position?"
    obama "Don't just play on your phone, program it."
    mc "..."
    mc "Thanks Obama."
    
    "{i}bell rings{/i}"

    jump Hallway

label deepConversation1:
    scene classroom

    mc "its just that "

    menu:
        "I don't get polymorphism, I'm totally lost! Tutor me please!":
            jump Hallay
        "I think this thing between you and me won't work out":
            jump deepConversation2

label deepConversation2:
    scene classroom

    star "!!!!!!!!!!"
    star " Why is that!"

    mc "{i} I'm shocked at how much she's reacting to this{/i}"
    
    menu: 
        "Tell her its a joke and it was fun seeing her reaction":
            jump badEnding
        "Tell her that you didn't know she cared so much":
            jump conclusion

label Hallway:
    scene hallway

    mc "Hey Star has life been bland"
    star "No"
    mc "I've been thinking if there should be a change between you and me"
    star "...."
    mc "It's just that I think you and I won't work out"
    star "!!!!!!!!!!"
    star "Why is that!"
    
    mc "{i}I'm shocked at how much she's reacting to this{/i}"
    menu: 
        "Tell her its a joke and it was fun seeing her reaction":
            jump badEnding
        "Tell her that you didn't know she cared so much":
            jump conclusion
    
label conclusion:
    scene outside

    star "!!!!!!!!!!!!!"
    mc "I didn't know she liked me this much and he accidently said it outloud"
    star "Of course, but I didn't know how to talk to you"
    mc "......"
    mc "We're both dumb"
    mc "I guess we can both use some polymorphism on us in ourselves"


label badEnding:
    scene outside
    
    mc "The boring relationship carried out until until graduation"
    mc "{i}Only if she could be changed{/i}"

return #ends game
