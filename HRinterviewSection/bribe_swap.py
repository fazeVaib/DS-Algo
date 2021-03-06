# Problem Statement:
# It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by  from  at the front of the line to  at the back.

# Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. 

# Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!

arr = list(map(int, input().strip().split()))

def numofbribe(arr):
    i = len(arr)-1
    count = 0

    while i>=0:
        if (arr[i] - (i+1) > 2):
            print("Too chaotic")
            return

        j = max(0, arr[i]-2)
        while j<i:
            if arr[j] > arr[i]:
                count+=1
            j+=1
        i-=1

    print(count)

numofbribe(arr)