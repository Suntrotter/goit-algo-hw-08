import heapq

def merge_k_lists(lists):    
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    merged = [] 
    
    while heap:
        val, lst_index, idx = heapq.heappop(heap)
        merged.append(val)         
        if idx + 1 < len(lists[lst_index]):
            next_val = lists[lst_index][idx + 1]
            heapq.heappush(heap, (next_val, lst_index, idx + 1))
    
    return merged

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
