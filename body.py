class Head:
	pass
        
class Feet:
    pass

class Leg:
    def __init__(self, feet: Feet):
        self.feet = feet

class Hand:
    pass

class Arm:
    def __init__(self, hand: Hand):
        self.hand = hand

class Torso:
    head: Head
    left_arm: Arm
    right_arm: Arm
    
    def __init__(self, head: Head, left_arm: Arm, right_arm: Arm):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm

class Human:
    torso: Torso
    left_leg: Leg
    right_leg: Leg
    
    def __init__(self, torso: Torso, left_leg: Leg, right_leg: Leg):
        self.torso = torso
        self.left_leg = left_leg
        self.right_leg = right_leg

head = Head()
right_hand = Hand()
left_hand = Hand()
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)
right_feet = Feet()
left_feet = Feet()
right_leg = Leg(right_feet)
left_leg = Leg(left_feet)
torso = Torso(head, left_arm,right_arm)
human = Human(torso, left_leg, right_leg)




