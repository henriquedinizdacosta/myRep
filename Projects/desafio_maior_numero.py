def greaterNum(): 

    def getArr():
        try:
            array = [int(i) for i in input('Input your numbers separated by spaces:\n').split()]
        except ValueError:
            print('You must input only integer numbers!')
            return getArr()
        if len(array) <= 1: 
            print('You must imput more than 1 number!')
            return getArr()
        return array
    
    def sorting(array):
        for i in range(len(array)):
            if array[i] > array[-1]:
                array[i], array[-1] = array[-1], array[i]
        return array[-1]  
    return print('the greatest number is ', sorting(getArr()))

greaterNum()
