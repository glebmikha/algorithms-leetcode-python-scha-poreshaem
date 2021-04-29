class SparseVector:
    def __init__(self, nums):
        self.length = len(nums)
        self.sparse_dict = {}
        for i, el in enumerate(nums):
            if el:
                self.sparse_dict[i] = el

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        if self.length != vec.length:
            raise ValueError('Vectors should have equal length')

        s = 0
        for key in self.sparse_dict:
            if key in vec.sparse_dict:
                s += self.sparse_dict[key] * vec.sparse_dict[key]
        return s


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

if __name__ == '__main__':
    nums1 = [1, 0, 2]
    nums2 = [0, 2, 3]

    sv1 = SparseVector(nums1)
    sv2 = SparseVector(nums2)
    # print(sv1.sparse_dict)
    # print(sv2.sparse_dict)
    print(sv1.dotProduct(sv2))
