def count_positives_sum_negatives(arr):
    positive = 0
    negative = 0
    if arr ==[]:
        return []
    else:
        for i in range(len(arr)):
            if arr[i]>0:
                positive+=1
            else: negative+=arr[i]
        return [positive,negative]