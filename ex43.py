from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and hit enter().")
        exit(1)

class Engine(object):

    # scene_map = central_corridor
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # ???How method opening_scene() be called as method from Map???
        # current_scene = CentralCorridor()?
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died.  You kinda suck at this.",
        "Your mom would be proud...id she was smarter.",
        "Such a luser.",
        "I have a small puppy that's  better at this.",
        "You're worse than my Dad's jokes",
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last survuving
            member and your last mission is to get the neutron destuct bomb
            from the Weapons Armory, put it on the Bridge, and blow the ship up
            after getting into an escape pod.

            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scally skin, dark grimy
            teeth, and evil clown costume flowing around his hate filled body.
            He's blocking the door to the Weapons Armory and about to pull
            a weapon to blast you.
        """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire
                it at the Gothon. His clown cosume is flowing and moving
                around his body, which throws off your aim.
                Your laser hits his costume but misses him entirely.
                This completely ruins his brand new costume his mother bought
                him, which makes him fly into insane rage and blasts you
                repeadedly in the face until you are dead. The he eats you.
            """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                Like a world class boxer you dodhe, weave, slip and slide
                right as the Gothon's blaster cranks a laser past you head.
                In the middle of your artfull dodge your foor slips and you
                bang your head at the metal wall and pass out. You wake up
                shortly after only to die as the Gothon's stomps on your head
                and eats you.
            """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                Lucky for you they made you learn Gothon insults in the
                acadamy. You tell the one Gothon joke you know:
                mdkfmdlskm skmsdlfkm fdskdfmlkmsdff fdsmdslmdsflsdlkmfd.
                The Gothon stops, tries not to laugh, then busts out of laughing
                and can't move. While he laughing you run up and shoot him
                square in the hed putting him down, the jump through the Weapon
                Armory door.
            """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You do a dive roll into the Weapon Armory crouch and scan
            the room for more Gothons that might be hiding. It's dead
            quiet, too quiet. You stand up and run to the far side of
            room and find the neatron bomb in its cointainer.
            There's a keyboard lock ont he box and you need the code
            to get the bomb ou. If you het the code wrong 10 times then
            the lock closes forever and you can't get the bomb. The code
            is 3 digits.
        """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses <9:
            print("BZZZZED!")
            guesses += 1
            guess = input("[keypad]")

        if guess == code:
            print(dedent("""
                The cointainer clicks open and the seal breaks. letting gas
                out. You grab the neutron bomb and runs as fast as you can
                to the bridge where you must plaste it in the right spot.
                {code}
            """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock busses ont last time and then you hear a sickening
                melting sound at the mechanism is fused together. You decide
                to sit there, and finally the Gothons blow up the ship from
                their ship and you die.
            """))
            return 'dead'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You bust onto tje Bridge with the neutron bomb under your
            arm an suprose 5 Gothons who are trying to take control
            of the ship. Each of them has a even uglier clown costume
            than the last. They havent pulled their weapons out yet, as
            they see the active bomb under your arm and dont't want
            to set it off.
        """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                In the panic you throw the bomb at the group of Gothons
                and make a leap for the door. Right as you drop it a
                Gothon shoots you right in tje back killing you. As you
                die you see another Gorhon frantically try to disarm
                the bomb. You die knowing they will probably blow up
                when it goes off.
            """))
            return 'death'

        elif action == 'slowly place the bomb':
            print(dedent("""
                You point your blaster at the bomb under your arm and the
                Gothonsput their hands up and start to sweat. You inch
                backward to the door, open it, and the carefully place
                the bomb on the floor, pointing your blaster at it. You
                then jump back through the door, punch the close button
                and blast the lock so the gothons can't get out. Now
                that the bomb is placed you run to the escape pod to get
                off this tin can.
            """))
            return 'escape_pod'

        else:
            print("CANNOT COMPUTE!")
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes. It seems
            like hardly any Gothons are ont he ship, so you run is clear
            of inteference. You het to the chamber  with the escape
            pods, and now you need to pick one to take. Some of them
            could be damaged but you don't have time to look.
            There's 5 pods, wich on tod you take?
        """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                You jump into pod {guess} and hit the eject button. The
                pod escaped out into the coid of space, then implodes as
                the hull ruptures, crushing your body into jam jelly.
                {good_pod}
            """))
            return 'death'
        else:
            print(dedent("""
                You jump into the pod {guess} and hit the eject button.
                the pod easilly slides out into space heading to the
                planet below. As it flies to the planet, you look back
                and see your ship implode then explode like a bright star
                taking out the Gothon ship at the same time. You won!
            """))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You've won! Good job.")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory' : LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'death' : Death(),
        'finished' : Finished,
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    # ??? this get value van the key ??? But is not next but current?
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    # Get start_scene == central_corridor -> method next scene which gets value from key central_corridor == CentralCorridor()
    def opening_scene(self):
        return self.next_scene(self.start_scene)

#Isntantiate Map Class with argument 'central_corridor' -> Class sets central_corridor to variable start_scene
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
