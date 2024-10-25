#1b
#2b
#3c
#4a
#5c
# 6a
# 7c
# 7-1c
# 8c
# 9a
# 10d
# 11b
# 12b



# 13 **Массив vs. Холбоослогдсон жагсаалт:**

# 1. **Элементийн хадгалах арга**:
#    - **Массив**: Элементүүд нь үргэлжилсэн хаягт хадгалагддаг (индексээр хандана).
#    - **Холбоослогдсон жагсаалт**: Элементүүд нь бие биетэйгээ холбоосоор холбогдсон, тус тусад нь хаягдаж хадгалагддаг.

# 2. **Санах ой**:
#    - **Массив**: Урьдчилан тодорхойлсон хэмжээгээр, тогтмол хаягт. Динамик биш.
#    - **Холбоослогдсон жагсаалт**: Динамик, шаардлагатай үед санах ойг зүгээр л хуваарилах боломжтой.

# 3. **Мэдээллийг боловсруулах хурд**:
#    - **Массив**: Элементэд хандах хугацаа O(1), нэмэх/устгах O(n).
#    - **Холбоослогдсон жагсаалт**: Нэмэх/устгах O(1) (хэрэв хандаж чадвал), хандах O(n).

# 4. **Согтуу хаягдлын аюул**:
#    - **Массив**: Хэмжээний хязгаарлалт, томруулахад асуудал үүсэх.
#    - **Холбоослогдсон жагсаалт**: Динамик, хязгаарлагдмал биш, гэхдээ хаягдлын асуудалгүй.




# 14
#stack: LIFO buyu etssiin element hamgiin turuund garc irne, 
# function-ii dotood unalt algorithm, 
# ashiglahad hylbar bas hurdan baidag bol sul tal n zarim medeellig aldaj boldg


#Tree: esteg huuhd esvel uuruur undes navchtai,
# data hadaglah hailt hiihed ashigladag,
# medeellig zohion baiguulj turuljuuldeg davuu talai bol sul tal ni iluu ih sanah oi shaarddag bas hetsuu







# 15c
# 16a
# 17b
# 18c



#asuult_1-a
#min_coins(daalgavar_1)

def greedy_coin_change(amount):
    coins = [25, 10, 5, 1]  
    result = []  

    for coin in coins:
        if amount >= coin:
            count = amount // coin 
            amount -= count * coin  
            result.append(f"{count}x{coin} төгрөг")

    return ', '.join(result)

amount = 83
print(greedy_coin_change(amount))

#asuult_2 -b
#haffman(daalgavar_2)
import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_code(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)


    root = heap[0]
    codes = {}
    
    def generate_codes(node, current_code):
        if node is not None:
            if node.char is not None:
                codes[node.char] = current_code
            generate_codes(node.left, current_code + "0")
            generate_codes(node.right, current_code + "1")

    generate_codes(root, "")
    return codes


frequencies = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
codes = huffman_code(frequencies)

for char, code in codes.items():
    print(f"{char}: {code}")




#asuult_3 -b
#daalgavar-3

import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


input_data = [64, 34, 25, 12, 22, 11, 90]

start_time = time.time()
sorted_bubble = bubble_sort(input_data.copy())
bubble_sort_time = time.time() - start_time

#asuult_4-b









