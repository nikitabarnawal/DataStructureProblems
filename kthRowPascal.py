#get the kth row for a pascals triangle
def getRow(rowIndex):
    
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    preRow = getRow(rowIndex - 1)
    curRow = [1]
    for i in range(len(preRow)-1):
        #print(preRow)
        curRow.append(preRow[i]+preRow[i+1])
    
    curRow.append(1)

    return curRow


print(getRow(4))
