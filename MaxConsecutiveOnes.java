//Finds maximum no. of consecutive ones in an array with only elements(0/1)
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount=0;
        int curCount = 0;
        for(int num: nums){
            if(num == 1)
                curCount++;
            else
                curCount=0;
            if(curCount > maxCount)
                maxCount = curCount;
            
        }
        return maxCount;
    }
}
