// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>

using namespace std;

void printArr(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

void printArrByPointer(int* arr, int n) {
    for (int i = 0; i < n; i++) {
        std::cout << *(arr + i) << " ";
    }
    std::cout << std::endl;
}

void printVector(vector<int>& v) {
    for (int i = 0; i < v.size(); i++) {
        std::cout << v[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    // Write C++ code here
    std::cout << "Nhap n: ";
    int n;
    std::cin >> n;

    int nums[n];
    for (int i = 0; i < n; i++) {
        nums[i] = i * i;
    }

    printArr(nums, n);
    printArrByPointer(nums, n);

    vector<int> v1 = {0};
    for (int i = 1; i < n; i++) {
        v1.push_back(i);
    }
    printVector(v1);

    vector<int> v2(n);
    v2[0] = 0;
    for (int i = 1; i < v2.size(); i++) {
        v2[i] = i;
    }
    printVector(v2);

    return 0;
}