class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        queue =deque([(startGene,0)]) #curr gene seq and number of mutations
        visited =set([startGene])
        chars =['A', 'C', 'G','T']
        while queue:
            curr_gene, Mutations = queue.popleft()
            for i in range(len(curr_gene)):
                for char in chars:
                    if char != curr_gene[i]:
                        mutated_gene = curr_gene[:i]+char+curr_gene[i+1:]
                        if mutated_gene ==endGene:
                            return Mutations+1
                        if mutated_gene in bank_set and mutated_gene not in visited:
                            visited.add(mutated_gene)
                            queue.append((mutated_gene,Mutations+1))
        return -1