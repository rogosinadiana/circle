def circle(X,X0,Y,Y0,R,mas):
    for i in range(Y):
        for j in range(X):
            if abs((i-X0)**2+(j-Y0)**2)<=R**2 and abs((i-X0)**2+(j-Y0)**2)>=(R-1)**2:
                mas[i][j]=1
def display(X,Y,mas):

    for i in range(0,len(mas)):
        for j in range(0,len(mas[i])):
            print(mas[i][j],end=' ')
        print()

def main():
    X=int(input('ЧИСЛО СТРОК (X):'))
    Y=int(input('ЧИСЛО СТОЛБЦОВ (Y):'))
    X0=int(input('КООРДИНАТА ЦЕНТРА по X (X0):'))-1
    Y0=int(input('КООРДИНАТА ЦЕНТРА по Y (Y0):'))-1
    R=int(input('РАДИУС:'))
    if R>(X-X0-1) or R>(X0) or R>(Y-Y0-1) or R>(Y0):
        print("ОКРУЖНОСТЬ ВЫХОДИТ ЗА ГРАНИЦЫ ПОЛЯ!!!")
    else:
        mas=[[0]*Y for i in range(X)]
        circle(X,X0,Y,Y0,R,mas)
        display(X,Y,mas)
main()
