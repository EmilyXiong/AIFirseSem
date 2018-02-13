from tkinter import Tk, Canvas, Frame, BOTH, BOTTOM,TOP
import time

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
        
    def initUI(self):
        self.master.title("Lines")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(15, 25, 200, 25)
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        
        
        canvas.create_rectangle(30, 10, 120, 80, 
            outline="#fb0", fill="#fb0")
        canvas.create_rectangle(150, 10, 240, 80, 
            outline="#f50", fill="#f50")
        canvas.create_rectangle(270, 10, 370, 80, 
            outline="#05f", fill="#05f")            
        canvas.pack(fill=BOTH, expand=1)
        


def main():
  
    root = Tk()
    frame = Frame(root)
    frame.master.title("Lines")  
    frame.pack(fill=BOTH, expand=1)
    canvas = Canvas(frame)
    root.geometry("600x500+0+1000")
    canvas.pack(side=TOP, fill=BOTH, expand=1)
    canvas.create_line( 0,100,100,0)
    canvas.create_line(15, 25, 200, 25)
#     canvas.create_line(300, 35, 300, 200, dash=(4, 2))
#     canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
    #root.update_idletasks()
    #root.update()
    
    root.mainloop()  
    print("The total distance of the path is:" )
    time.sleep(3)
if __name__ == '__main__':
    main()  
