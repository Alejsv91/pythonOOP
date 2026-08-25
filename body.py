class Head:
	pass

class Torso:
    head: Head
    left_arm: Arm
    right_arm: Arm
    left_leg: Leg
    right_let: Leg
    
    def __init__(self, head: Head, left_arm: Arm, right_arm: Arm, left_leg: Leg, right_leg: Leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_let = right_leg
    
    pass

class Arm:
    def __init__(self, hand: Hand):
        self.hand = hand
    
class Hand:
    pass
    
class Leg:
    def __init__(self, feet: Feet):
        self.feet = feet
    pass

class Feet:
    pass

head = Head()
right_hand = Hand()
left_hand = Hand()
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)
right_feet = Feet()
left_feet = Feet()
right_leg = Leg(right_feet)
left_leg = Leg(left_feet)

torso = Torso(head, left_arm,right_arm, left_leg, right_leg)




