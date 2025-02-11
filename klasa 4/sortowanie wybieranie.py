class Sorting:
    def __init__(self) -> None:
        #self.tab_numbers = []
        self.tab_numbers = [12,-5,123,721,1,65427,1,753,93,-120]
        

    def Select_Sort(self):
        for i in range(10):
            temp_index = i
            for j in range(i+1, 10):
                if self.tab_numbers[j] > self.tab_numbers[temp_index]:
                    temp_index = j

            self.tab_numbers[i], self.tab_numbers[temp_index] = self.tab_numbers[temp_index], self.tab_numbers[i]

        return self.tab_numbers

    def Max_Search(self):
        temp_tab = self.Select_Sort()
        return temp_tab[0]


sort = Sorting()
print(sort.Select_Sort())
print(sort.Max_Search())
