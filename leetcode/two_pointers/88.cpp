class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {

        int i = m-1;
        int j = n-1;

        if (i < 0) {
            while (j >= 0) {
                nums1[j] = nums2[j];
                j--;
            }
        } else {
            while (i >= 0 && j >= 0) {
                if (nums1[i] >= nums2[j]) {
                    nums1[i+j+1] = nums1[i];
                    nums1[i] = 0;
                    i--;
                } else {
                    nums1[i+j+1] = nums2[j];
                    j--;
                }
            }

            if (i == -1) {
                while (j >= 0) {
                    nums1[j] = nums2[j];
                    j--;
                }
            }
        }
    }
};