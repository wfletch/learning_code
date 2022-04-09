class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Silly way.
        # We can do string matching for each iteration
        upper_index = 0
        word = ""
        results = []
        products.sort()
        
        for a in searchWord:
            upper_index += 1
            word += a
            count = 0
            iteration_results = []
            for product in products:
                if product[0:upper_index] == word:
                    count+=1
                    iteration_results.append(product)
                    if count == 3:
                        break
            results.append(iteration_results)
        return results
        # LC 1268
        # This is not efficient.
        # A trie would be better
        # # Complexity
        # # O(nlogn) for the sort
        # # O(n^2) for the search
        # # O(n^2) Time
        # # O(n) Space

# Turns out, a trie is not really neccessery. We can sort and bisect on the prefix then return the values
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        i = 0
        results = []
        prefix = ""
        products.sort()
        for a in searchWord:
            prefix += a
            i = bisect.bisect_left(products, prefix, i)
            results.append(w for w in products[i:i + 3] if w.startswith(prefix))
        return results