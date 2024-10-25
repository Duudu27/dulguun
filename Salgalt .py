#Test ni:
#1. b)
#2. c)
#3. c) 
#4. a)
#5. c) 
#6. a)  
#7. c)
#7(1). d)
#8. c)
#9. a)
#10. b
#11. b)
#12. b
#13. Массив:Бүх элементүүийг дараалсан санах ойд хадгалдаг
# Өгөгдлийг хадгалах арга:
# Массив: Бүх элементүүдийг дараалсан санах ойд хадгалдаг.
# Холбоослогдсон жагсаалт: Элементүүдийг тусдаа санах ойд хадгалж, холбоосоор холбосон байдаг.
# санах ой:
# Санах ой:
# Массив: Нэг хэмжээст массивд бүх элементүүдийг олоход хурдан (O(1)).
# Холбоослогдсон жагсаалт: Элемент олохын тулд нэгдүгээрээс нь эхэлж (O(n)) явна.
# Мэдээллийг боловсруулах хурд:
# Мэдээллийг боловсруулах хурд:
# Массив: Хурдан бөгөөд уян хатан. Гэсэн хэдий ч, хэмжээ нэмэгдэхэд дахин тохируулах шаардлагатай.
# Холбоослогдсон жагсаалт: Олон үйлдлийг гүйцэтгэхэд хялбар, гэхдээ элемент олох, дахин давталт хийхэд удаан.
#14. Стек:
# Хэрхэн ажилладаг: LIFO (Last In, First Out) зарчмаар ажилладаг. Сүүлийн оруулсан элемент хамгийн түрүүнд гарч ирнэ.
# Жишээ: Сайтын "Undo" функцийг ажиллуулахад ашиглагддаг.
# Давуу тал: Саруулж ойлгоход хялбар, хурдан (O(1)) үйлдлүүд.
# Сул тал: Зөвхөн дээд хэсэгт ажилладаг, бусад элементүүдийг шууд олох боломжгүй.
# Мод:
# Хэрхэн ажилладаг: Тодорхой бүтэцтэй, ихэвчлэн олон давхарга, олон салбартай.
# Жишээ: Хайлт хийхэд (жишээ нь, хоёртын хайлтын мод).
# Давуу тал: Мэдээллийг зохион байгуулах, хялбархан хайлт хийх боломжтой.
# Сул тал: Зэрэгцээгээ алдахад үйлдлүүд удаан болох боломжтой.
#15. c
#16. a
#17. b 
#18. c
#19. (uzeegui)
#20. (uzeegui)
#21. (uzeegui)
#22. (uzeegui)


#1. Грэйди алгоритм - Минимум зоосны тоо.

def greedy_coin_change(amount):
    coins = [25, 10, 5, 1]
    coin_count = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            coin_count[coin] = count
            amount -= count * coin

    return coin_count

amount = 83
result = greedy_coin_change(amount)

for coin, count in result.items():
    print(f"{count}x{coin} төгрөг")

#Асуулт (1): Грэйди алгоритмын дагуу хамгийн бага зоосны тоог хэрхэн сонгох вэ?      хариултгүй
#Асуулт (2): Аль алгоритм нь Грэйди алгоритмын зарчмыг ашиглан шийдэгддЭг вэ?        (b)



#2. Хаффман кодчилол. 
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
    priority_queue = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    root = priority_queue[0]

    huffman_codes = {}
    
    def generate_codes(node, current_code):
        if node:
            if node.char is not None:
                huffman_codes[node.char] = current_code
            generate_codes(node.left, current_code + "0")
            generate_codes(node.right, current_code + "1")

    generate_codes(root, "")

    return huffman_codes

frequencies = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
huffman_codes = huffman_code(frequencies)
print("Huffman Codes:", huffman_codes)


#3. Bubble Sort болон Insertion Sort Хэрэгжуулэлт ба Харьцуулалт.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)


#3. Алгоритмын гуйцэтгэлийн ШИНЖИЛГЭЭ
#AcyynT1:0(n) rax r yr илэрхийлдэг вэ?     (c)


#4. Бинар мод уусгэх ба хайлтын мод
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursively(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursively(node.right, key)

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_recursively(node.left, key)
        return self._search_recursively(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursively(self.root, key)

    def _delete_recursively(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self._delete_recursively(node.left, key)
        elif key > node.val:
            node.right = self._delete_recursively(node.right, key)
        else:

            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete_recursively(node.right, temp.val)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=' ')
            self.inorder(node.right)

if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [20, 9, 25, 5, 12, 15, 30]
    for val in values:
        bst.insert(val)
    print("Inorder Traversal:")
    bst.inorder(bst.root) 
    search_key = 40
    found_node = bst.search(search_key)
    if found_node:
        print(f"\nFound: {found_node.val}")
    else:
        print(f"\n{search_key} not found in the BST.")
    bst.delete(20)
    print("Inorder Traversal after deleting 20:")
    bst.inorder(bst.root)

#Функц ба буцаах утга
#Асуулт 1: Дараах функц ямар утга буцаах вэ?   b) 7