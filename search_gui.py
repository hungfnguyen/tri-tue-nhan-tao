import tkinter as tk
import numpy as np
import time
from search import *
import tkinter.ttk as ttk



romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))

romania_map.locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))

name_city = dict(Arad=(-35, 0), Bucharest=(0, 15), Craiova=(15, 0),
    Drobeta=(0, 15), Eforie=(15, 0), Fagaras=(15, 0),
    Giurgiu=(15, 0), Hirsova=(15, 0), Iasi=(15, 0),
    Lugoj=(10, 0), Mehadia=(10, 0), Neamt=(15, 0),
    Oradea=(15, 0), Pitesti=(15, 0), Rimnicu=(15, 0),
    Sibiu=(0, -15), Timisoara=(10, 0), Urziceni=(0, 15),
    Vaslui=(0, 15), Zerind=(-45, 0 ))

dict_neighbors =  romania_map.graph_dict




class App(tk.Tk):
    def __init__(self):
        self.start = 'Arad'
        self.dest = 'Arad'
        ##
        #self.lst_path = None

        super().__init__()
        self.title('Search GUI')
        self.cvs_map = tk.Canvas(self, width=620, height=460, relief = tk.SUNKEN, border=1)

        self.ve_ban_do()
        lbl_frm_menu = tk.LabelFrame(self)


        lst_city = []
        for city in romania_map.locations:
            lst_city.append(city)
        
        lbl_start = ttk.Label(lbl_frm_menu, text='Start')
        self.cbo_start = ttk.Combobox(lbl_frm_menu, values=lst_city)
        self.cbo_start.set('Arad')
        self.cbo_start.bind("<<ComboboxSelected>>", self.cbo_start_click)

        lbl_dest = ttk.Label(lbl_frm_menu, text='Dest')
        self.cbo_dest = ttk.Combobox(lbl_frm_menu, values=lst_city)
        self.cbo_dest.set('Arad')
        self.cbo_dest.bind("<<ComboboxSelected>>", self.cbo_dest_click)

        btn_direction = ttk.Button(lbl_frm_menu, text = 'Direction', command= self.btn_direction_click)
        
        btn_run = ttk.Button(lbl_frm_menu, text = 'Run', command= self.btn_run_click)


        lbl_start.grid(row=0, column=0, padx=5, pady=0, sticky=tk.W)
        self.cbo_start.grid(row=1, column=0, padx=5, pady=5)

        lbl_dest.grid(row=2, column=0, padx=5, pady=0, sticky=tk.W)
        self.cbo_dest.grid(row=3, column=0, padx=5, pady=5)

        btn_direction.grid(row=4, column=0, padx=5, pady=5, sticky = tk.EW)

        btn_run.grid(row=5, column=0, padx=5, pady=5, sticky = tk.EW)

        self.cvs_map.grid(row=0, column=0, padx=5, pady=5)
        lbl_frm_menu.grid(row=0, column=1, padx=5, pady=7, sticky=tk.N)

    #ham ve ban do
    def ve_ban_do(self):
        for key in dict_neighbors:
            dict_child = dict_neighbors[key]
            print(romania_map.locations[key])
            p0 = romania_map.locations[key]

            x0 = p0[0]
            y0 = 620 - p0[1]
            self.cvs_map.create_rectangle(x0-4, y0-4, x0+4, y0+4, fill = 'blue', outline='blue')

            dx = name_city[key][0]
            dy = name_city[key][1]
            self.cvs_map.create_text(x0+dx,y0+dy,text=key, anchor = tk.W)

            for key in dict_child:

                print(key, romania_map.locations[key])
                p1 = romania_map.locations[key]
                x1 = p1[0]
                y1 = 620 - p1[1]
                self.cvs_map.create_line(x0, y0, x1, y1)

    def cbo_start_click(self, *args):
        self.start = self.cbo_start.get()
        print("Thanh pho bat dau la", self.start)

    def cbo_dest_click(self, *args):
        self.dest = self.cbo_dest.get()
        print("Thanh pho dich la", self.dest)

    def btn_direction_click(self):
        self.cvs_map.delete(tk.ALL)
        self.ve_ban_do()

        romania_problem = GraphProblem(self.start, self.dest, romania_map)
        c = astar_search(romania_problem)

        self.lst_path = c.path()
        for data in self.lst_path:
            print(data.state, end=' ')
        print()
        L = len(self.lst_path)
        
        for i in range(0, L-1):
            city = self.lst_path[i].state
            p0 = romania_map.locations[city]
            x0 = p0[0]
            y0 = 620 - p0[1]
            for neighbor in dict_neighbors[city]:
                if neighbor == self.lst_path[i+1].state:
                    p1 = romania_map.locations[neighbor]
                    x1 = p1[0]
                    y1 = 620 - p1[1]
                    self.cvs_map.create_line(x0, y0, x1, y1, fill = 'red')
            
    def btn_run_click(self):
        mypath = []
        
        L = len(self.lst_path)
        
        for i in range(0, L-1):
            city = self.lst_path[i].state
            p0 = romania_map.locations[city]
            x0 = p0[0]
            y0 = 620 - p0[1]
            if(x0,y0) not in mypath:
                mypath.append((x0, y0))

            for neighbor in dict_neighbors[city]:
                if neighbor == self.lst_path[i+1].state:
                    p1 = romania_map.locations[neighbor]
                    x1 = p1[0]
                    y1 = 620 - p1[1]
                    if(x1,y1) not in mypath:
                        mypath.append((x1, y1))
        print(mypath)
        cvs_map_bg = self.cvs_map["background"]
        N=21
        d = 245
        L = len(mypath)
        for k in range(0, L-1):
            x0 = mypath[k][0]
            y0 = mypath[k][1]
            x1 = mypath[k+1][0]
            y1 = mypath[k+1][1]
            d1 = np.sqrt((x1-x0)**2 + (y1-y0)**2)
            N1 = int(N*d1/d)
            dt = 1.0/(N1-1)
            for i in range(0, N1):
                t = i*dt
                x = x0 + (x1-x0)*t
                y = y0 + (y1-y0)*t
                self.cvs_map.create_line(mypath, fill = 'red', width=3)
                self.cvs_map.create_oval(x-5, y-5, x+5, y+5, fill='blue', outline='blue')
                time.sleep(0.2)
                self.cvs_map.update()
                if i < N1-1:
                    self.cvs_map.create_oval(x-5, y-5, x+5, y+5, fill=cvs_map_bg, outline=cvs_map_bg)
if __name__ == '__main__':
    app = App()
    app.mainloop()