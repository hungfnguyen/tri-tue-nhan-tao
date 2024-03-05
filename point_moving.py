import tkinter as tk
import numpy as np
import time
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Point Moving')
        self.cvs_map = tk.Canvas(self, width=300, height=300, relief = tk.SUNKEN, border=1)

        btn_start = tk.Button(self, text = 'Start', width=6, command=self.btn_start_click)
        # toa do cac diem cua duong
        self.mypath = [(10, 10), (250, 60), (150, 150), (200, 250)]

        # duong di
        self.cvs_map.create_line(self.mypath, fill = 'blue', width=3)
        x0 = self.mypath[0][0]
        y0 = self.mypath[0][1]
        # x1 = mypath[1][0]
        # y1 = mypath[1][1]
        # x2 = mypath[2][0]
        # y2 = mypath[2][1]
        # x3 = mypath[3][0]
        # y3 = mypath[3][1]
        # cvs_map.create_text(x0, y0+10, text='A')
        # cvs_map.create_text(x1+10, y1, text='B')
        # cvs_map.create_text(x2-10, y2, text='C')
        # cvs_map.create_text(x3, y3+10, text='D')
        self.cvs_map.create_oval(x0-5, y0-5, x0+5, y0+5, fill='red', outline='red')
        text = 'A'
        for point in self.mypath:
            x = point[0]
            y = point[1]
            print(x, y)
            self.cvs_map.create_text(x, y+10, text=text)
            text = chr(ord(text) + 1)
            
        

        self.cvs_map.grid(row=0, column=0, padx=5, pady=5)
        btn_start.grid(row=0, column=1, padx=5, pady=6, sticky=tk.NW)

    def btn_start_click(self):
        cvs_map_bg = self.cvs_map["background"]
        N=21
        d = 245
        L = len(self.mypath)
        for k in range(0, L-1):
            x0 = self.mypath[k][0]
            y0 = self.mypath[k][1]
            x1 = self.mypath[k+1][0]
            y1 = self.mypath[k+1][1]
            d1 = np.sqrt((x1-x0)**2 + (y1-y0)**2)
            N1 = int(N*d1/d)
            dt = 1.0/(N1-1)
            for i in range(0, N1):
                t = i*dt
                x = x0 + (x1-x0)*t
                y = y0 + (y1-y0)*t
                self.cvs_map.create_line(self.mypath, fill = 'blue', width=3)
                self.cvs_map.create_oval(x-5, y-5, x+5, y+5, fill='red', outline='red')
                time.sleep(0.2)
                self.cvs_map.update()
                if i < N1-1:
                    self.cvs_map.create_oval(x-5, y-5, x+5, y+5, fill=cvs_map_bg, outline=cvs_map_bg)
        # #khoang cach diem dau tien
        # x0 = self.mypath[0][0]
        # y0 = self.mypath[0][1]
        # x1 = self.mypath[1][0]
        # y1 = self.mypath[1][1]
        # d0 = np.sqrt((x1-x0)**2 + (y1-y0)**2)
        # N0 = 21
        # dt = 1.0/(N0-1)
        # for i in range(0, N0):
        #     t = i*dt
        #     x = x0 + (x1-x0)*t
        #     y = y0 + (y1-y0)*t
        #     self.cvs_map.create_line(self.mypath, fill = 'blue', width=3)
        #     self.cvs_map.create_oval(x-5, y-5, x+5, y+5, fill='red', outline='red')
        #     time.sleep(0.2)
        #     self.cvs_map.update()
        #     if i < N0-1:
        #         self.cvs_map.create_oval(x-5, y-5, x+5, y+5, fill=cvs_map_bg, outline=cvs_map_bg)
        
        # for i in range(len(self.mypath) - 1):
        #     x0 = self.mypath[0][0]
        #     y0 = self.mypath[0][1]
        #     x1 = self.mypath[i+1][0]
        #     y1 = self.mypath[i+1][1]
        #     d = np.sqrt((x1-x0)**2 + (y1-y0)**2)
        #     N0 = 21
        # dt = 1.0/(N0-1)
        # for i in range(0, N0):
        #     t = i*dt
        #     x = x0 + (x1-x0)*t
        #     y = y0 + (y1-y0)*t
        #     self.cvs_map.create_line(self.mypath, fill = 'blue', width=3)
        #     self.cvs_map.create_oval(x-5, y-5, x+5, y+5, fill='red', outline='red')
        #     time.sleep(0.2)
        #     self.cvs_map.update()
        #     if i < N0-1:
        #         self.cvs_map.create_oval(x-5, y-5, x+5, y+5, fill=cvs_map_bg, outline=cvs_map_bg)
        
        #     #BFS: tim kiem theo be rong
        #     #GUI: lam giao dien

if __name__ == '__main__':
    app = App()
    app.mainloop()