class Solution
{
public:
    bool increasingTriplet(vector<int> &nums)
    {
        if (nums.size() < 3)
            return false;

        int smallestFirstNum = INT_MAX;
        int smallestSecondNum = INT_MAX;

        for (int i = 0; i < nums.size(); i++)
        {
            if (smallestSecondNum < nums[i])
            {
                return true;
            }
            else if (smallestFirstNum < nums[i] && smallestSecondNum > nums[i])
            {
                smallestSecondNum = nums[i];
            }
            else if (smallestFirstNum > nums[i])
            {
                smallestFirstNum = nums[i];
            }
        }

        return false;
    }
};