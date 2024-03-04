#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 10 sayısı dizimizde bulunuyor mu? sorusunu binary search tree arama algoritması ile çözdüm.
# Verilen dizide x'in konumunu döndürür
def binarySearch(arr, l, r, x):
 
    while l <= r:
 
        mid = l + (r - l) // 2
 
        # x'in ortada olup olmadığını kontrol et
        if arr[mid] == x:
            return mid
 
        # x ortalamadan büyükse, sol yarısını yok say
        elif arr[mid] < x:
            l = mid + 1
 
        # x ortalamadan küçükse, sağ yarısını yok say
        else:
            r = mid - 1
 
    # Eğer buraya ulaşırsak, eleman bulunamadı demektir
    return -1
 
 
#Ana Kod
if __name__ == '__main__':
    arr = [7,5,1,8,3,6,0,9,4,2]
    x = 10
 
   #Fonksiyon çağrısı
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element indexte bulunuyor", result)
    else:
        print("Element dizi de bulunmuyor.")#Big-O:O(logN)
#Big-O:O(logN)


# In[ ]:




