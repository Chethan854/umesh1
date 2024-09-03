class date:
    def __init__(self,a,b,c):
        self.d=a
        self.m=b
        self.y=c
    def day(self):
        print("date=",self.d)
    def month(self):
        print("month=",self.m)
    def year(self):
        print("year=",self.y)
    def monthname(self):
        months=["jan","feb","mar","apr","may",'jun',"jul","aug","sep","oct","nov","dec"]
        print("monthname=",months[self.m])
        def isleapyear (self):
            if(self.y%400==0)and(self.y%100!=0):
                print("it isleapyear")
            elif(self.y%4==0)and(self.y%100!=0):
                print("it isleapyear")
            else:
                print("it is not leap year")
d1=date(18,2,2024)
d1.day()
d1.month()
d1.year()
d1.monthname()
d1.isleapyear()

                    
            