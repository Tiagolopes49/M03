def MDC(n1,n2):
    if n1<n2:
        menor=n1
    else:
        menor=n2
    for i in range(menor,0,-1):
        if n1%i==0 and n2%i==0:
            print(i)
            return
        
def main():
    MDC(10,5)
    MDC(10,3)

if __name__=="__main__":
    main()