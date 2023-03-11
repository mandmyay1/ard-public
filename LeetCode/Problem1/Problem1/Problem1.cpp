// Problem1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
using namespace std;
#include <iostream>
#include <vector>
#include <unordered_map>

// https://leetcode.com/problems/two-sum/
/**
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
 */

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        std::unordered_map<int, int> kvps;
        for (int i = 0; i < nums.size(); i++) {
            kvps[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++) {
            int numA = nums[i];
            int numB = target - numA;
            if (kvps.find(numB) != kvps.end() && i != kvps[numB]) {
                ret.push_back(i);
                ret.push_back(kvps[numB]);
                return ret;
            }
        }
        return ret;
    }
    int main()
    {
        vector<int> input1{ 2, 7, 11, 15 };
        vector<int> var1 = twoSum(input1, 9);
        std::cout << var1[0] << " " << var1[1] << endl;
    }
};
// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
