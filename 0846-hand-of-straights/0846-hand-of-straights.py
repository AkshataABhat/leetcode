class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if not hand or len(hand)%groupSize!=0:
            return False
        
        hand.sort()
        
        while hand:
            current=hand[0]
            for i in range(groupSize):
                if current+i not in hand:
                    return False 
                hand.remove(current+i)
                
        return True 
            
                
        