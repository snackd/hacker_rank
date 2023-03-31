class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n or not k:
            return None

        elements = [i for i in range(1, n + 1)]
        result = []
        self.dfs(elements, k, [], result)

        return result

    def dfs(self, elements, k, combinations, result):
        if not k:
            # deepcopy
            result.append(combinations[:])
            return
        if not elements:
            return

        for idx, element in enumerate(elements):
            combinations.append(element)
            self.dfs(elements[idx + 1:], k - 1, combinations, result)
            combinations.pop()
