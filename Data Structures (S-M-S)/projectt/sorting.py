class sorting():
    def bubble_sort(self,list):
        n=len(list)
        for i in range(n):
            for j in range(0, n-i-1):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]

    def partition(self,arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot
        for j in range(low, high):
            # If current element is smaller than the pivot
            if arr[j] < pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)
    def quickSort(self,arr, low, high):
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high)
            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)