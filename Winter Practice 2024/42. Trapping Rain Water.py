class Solution:
    def trap(self, height: List[int]) -> int:
        sh = 0
        gap = False
        water_total = 0
        water = 0
        for h in height:
            if h >= sh and not gap:
                print("increasing height")
                print("1: h: ", h)
                sh = h
            elif h >= sh and gap:
                print("end of gap")
                print("2: h: ", h)
                water_total += water
                gap = False
                sh = h
                water = 0
                print("wt: ", water_total)
            elif h < sh:
                print("going down")
                print("3: h: ", h)
                print("sh: ", sh)
                gap = True
                water += sh-h
        print(water_total)
        sh = 0
        gap = False
        water = 0
        for h in reversed(height):
            if h >= sh and not gap:
                print("increasing height")
                print("1: h: ", h)
                sh = h
            elif h >= sh and gap:
                print("end of gap")
                print("2: h: ", h)
                water_total += water
                gap = False
                sh = h
                water = 0
                print("wt: ", water_total)
            elif h < sh:
                print("going down")
                print("3: h: ", h)
                print("sh: ", sh)
                gap = True
                water += sh-h
        print(water_total)
        
        return water_total
        