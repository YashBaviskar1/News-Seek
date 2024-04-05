import tkinter as tk
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Per Captia GDP of India (1960-2022)')
        self.list_x= ["1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022"]
        self.list_y = ["83.0351018240893","85.9697041851008","90.2768689288905","101.31516498136","115.487608356699","119.082475942029","89.7575826115815","96.0463298450023","99.5168361228774","107.182143141928","111.968318177372","118.160528911908","122.612453445976","143.456124984427","163.231615579564","157.929385028241","161.137236080759","186.419089544981","206.073749258556","224.575437698719","267.390578652535","271.426149209154","275.266085855139","292.644647182024","278.095415220662","297.999248705447","312.059843942513","342.071923724964","355.738409768732","347.462029998068","368.749759408129","303.850437957407","317.558738700794","301.50079120851","346.227393115934","373.628235651141","399.577312178982","414.898679748919","412.509354123275","440.961454614021","442.034778911498","449.911124933268","468.844428308942","543.843798895899","624.105094381691","710.509344848758","802.013742049265","1022.73246704551","993.503405266506","1096.63613605519","1350.63447029491","1449.60330101563","1434.01798721629","1438.05700508042","1559.86377870535","1590.17433135955","1714.27953740039","1957.96981329558","1974.3777314935","2050.1638002619","1913.21973278751","2238.12714218765","2410.88802070689"]

        self.plot_types = ['Line Plot', 'Bar Plot', 'Scatter Plot']
        self.plot_type_var = tk.StringVar(value=self.plot_types[0])
        self.plot_menu = tk.OptionMenu(self, self.plot_type_var, *self.plot_types, command=self.plot_type_select)
        self.plot_menu.pack(padx=10, pady=10)

        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.axes = self.figure.add_subplot()

        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)
        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.load_button = tk.Button(self, text='Load Graph', command=self.load_data)
        self.load_button.pack(padx=5, pady=5)


        NavigationToolbar2Tk(self.figure_canvas, self)

    def load_data(self):
        self.x_values = [int(i) for i in self.list_x]
        self.y_values = [float(i) for i in self.list_y]
        self.plot_type_select()

    def plot_type_select(self):
        self.axes.clear()  
        plot_type = self.plot_type_var.get()
        if plot_type == 'Line Plot':
            self.axes.plot(self.x_values, self.y_values)
        elif plot_type == 'Bar Plot':
            self.axes.bar(self.x_values, self.y_values)
        elif plot_type == 'Scatter Plot':
            self.axes.scatter(self.x_values, self.y_values)
        self.axes.set_title('Per Capita GDP of India')
        self.axes.set_ylabel('GDP (in Dollars $)')
        self.axes.set_xlabel('Years')
  
        self.figure_canvas.draw()


if __name__ == '__main__':
    app = App()
    app.mainloop()
