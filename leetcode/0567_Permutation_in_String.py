#You are given two strings s1 and s2.
#Return True if s2 contains a permutation of s1, otherwise return False.
s1 = "ab"
s2 = "eidbaooo"

need = {}
window = {}

# build need
for ch in s1:
    if ch in need:
        need[ch] += 1
    else:
        need[ch] = 1

left = 0

for right in range(len(s2)):
    ch = s2[right]

    # add current char into window
    if ch in window:
        window[ch] += 1
    else:
        window[ch] = 1
    print(window) #這瞬間 windows size 可能會超過，下面處理
    # keep window size = len(s1)
    if right - left + 1 > len(s1):#超過window size的處理
        left_char = s2[left]
        window[left_char] -= 1  #最左邊的字元 -1

        if window[left_char] == 0:
            del window[left_char] # - 1 後 ＝ 0 就直接刪了 保持windows 裡面的數量合法

        left += 1   # right 往右移到大於window size 了 所以left +1 保持windows size
    print(window)
    # compare
    if window == need:
        
        print(True)
        break
else:
    print(False)