class Graf:
    def __init__(self,matrix,num_ver):
        self.num_ver=num_ver
        self.matrix=matrix

    def print_num_ver(self):
        return print(self.num_ver)


    def num_line(self):
        s=0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]==1:
                    s+=1
        return print(s)

    def new_line(self,row,el):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[row][el]=1
        return print(self.matrix)


    def none_line(self,row,el):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[row][el]=0
        return print(self.matrix)

a=Graf(3,[[1,0,0],[0,0,1],[0,1,0]])
a.new_line(1,1)


