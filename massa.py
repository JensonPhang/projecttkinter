import tkinter
from tkinter import messagebox

# dataset elemen
ElementList = [
    ("H", 1.008), ("He", 4.0026), ("Li", 6.94), ("Be", 9.0122), ("B", 10.81), ("C", 12.011),
    ("N", 14.007), ("O", 15.999), ("F", 18.998), ("Ne", 20.180), ("Na", 22.990), ("Mg", 24.305),
    ("Al", 26.982), ("Si", 28.085), ("P", 30.974), ("S", 32.06), ("Cl", 35.45), ("Ar", 39.948),
    ("K", 39.098), ("Ca", 40.078), ("Sc", 44.956), ("Ti", 47.867), ("V", 50.942), ("Cr", 51.996),
    ("Mn", 54.938), ("Fe", 55.845), ("Co", 58.933), ("Ni", 58.693), ("Cu", 63.546), ("Zn", 65.38),
    ("Ga", 69.723), ("Ge", 72.630), ("As", 74.922), ("Se", 78.971), ("Br", 79.904), ("Kr", 83.798),
    ("Rb", 85.468), ("Sr", 87.62), ("Y", 88.906), ("Zr", 91.224), ("Nb", 92.906), ("Mo", 95.95),
    ("Tc", 98.0), ("Ru", 101.07), ("Rh", 102.91), ("Pd", 106.42), ("Ag", 107.87), ("Cd", 112.41),
    ("In", 114.82), ("Sn", 118.71), ("Sb", 121.76), ("Te", 127.60), ("I", 126.90), ("Xe", 131.29),
    ("Cs", 132.91), ("Ba", 137.33), ("La", 138.91), ("Ce", 140.12), ("Pr", 140.91), ("Nd", 144.24),
    ("Pm", 145.0), ("Sm", 150.36), ("Eu", 151.96), ("Gd", 157.25), ("Tb", 158.93), ("Dy", 162.50),
    ("Ho", 164.93), ("Er", 167.26), ("Tm", 168.93), ("Yb", 173.05), ("Lu", 174.97), ("Hf", 178.49),
    ("Ta", 180.95), ("W", 183.84), ("Re", 186.21), ("Os", 190.23), ("Ir", 192.22), ("Pt", 195.08),
    ("Au", 196.97), ("Hg", 200.59), ("Tl", 204.38), ("Pb", 207.2), ("Bi", 208.98), ("Po", 209.0),
    ("At", 210.0), ("Rn", 222.0), ("Fr", 223.0), ("Ra", 226.0), ("Ac", 227.0), ("Th", 232.04),
    ("Pa", 231.04), ("U", 238.03), ("Np", 237.0), ("Pu", 244.0), ("Am", 243.0), ("Cm", 247.0),
    ("Bk", 247.0), ("Cf", 251.0), ("Es", 252.0), ("Fm", 257.0), ("Md", 258.0), ("No", 259.0),
    ("Lr", 262.0), ("Rf", 267.0), ("Db", 270.0), ("Sg", 271.0), ("Bh", 270.0), ("Hs", 277.0),
    ("Mt", 278.0), ("Ds", 281.0), ("Rg", 282.0), ("Cn", 285.0), ("Nh", 286.0), ("Fl", 289.0),
    ("Mc", 290.0), ("Lv", 293.0), ("Ts", 294.0), ("Og", 294.0)
]

# separate elements and masses
elements = [symbol for symbol, mass in ElementList]
element_mass = [mass for symbol, mass in ElementList]

class mainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Massa Molar")
        self.dataList = []

        frame = tkinter.Frame(self.root)
        frame.pack()

        userInfoFrame = tkinter.LabelFrame(frame, text="Rumus Kimia")
        userInfoFrame.grid(row=0, column=0, padx=30, pady=10)

        tkinter.Label(userInfoFrame, text="Molekul:").grid(row=0, column=0)

        self.strEntry = tkinter.Entry(userInfoFrame, width=200)
        self.strEntry.grid(row=1, column=0, padx=10, pady=5)

        button = tkinter.Button(frame, text="Hitung", command=self.enterData)
        button.grid(row=3, column=0, padx=20, pady=10)

    def enterData(self):
        ansStr = self.strEntry.get()
        hasil = 0
        i = 0
        while i < len(ansStr):
            current = ansStr[i]
            if current.isupper():
                if i + 1 < len(ansStr) and ansStr[i+1].islower():
                    current += ansStr[i+1]
                    i += 1

                num = ''
                n = i + 1
                while n < len(ansStr) and ansStr[n].isdigit():
                    num += ansStr[n]
                    n += 1

                num = int(num) if num else 1
                if current in elements:
                    hasil += element_mass[elements.index(current)] * num
                else:
                    messagebox.showerror("Error", f"Elemen {current} tidak ditemukan.")
                    return
                i = n
            elif current == "(":
                i += 1
                temp = 0
                while i < len(ansStr) and ansStr[i] != ")":
                    current = ansStr[i]
                    if current.isupper():
                        if i + 1 < len(ansStr) and ansStr[i+1].islower():
                            current += ansStr[i+1]
                            i += 1

                        num = ''
                        n = i + 1
                        while n < len(ansStr) and ansStr[n].isdigit():
                            num += ansStr[n]
                            n += 1

                        num = int(num) if num else 1
                        if current in elements:
                            temp += element_mass[elements.index(current)] * num
                        else:
                            messagebox.showerror("Error", f"Elemen {current} tidak ditemukan.")
                            return
                        i = n
                    else:
                        messagebox.showerror(title="Error", message=f"Rumus molekul salah atau tidak ditemukan!")
                        return
                if i >= len(ansStr) or ansStr[i] != ")":
                    messagebox.showerror(title="Error", message="Tanda ')' tidak ditemukan.")
                    return
                i += 1

                num = ''
                n = i
                while n < len(ansStr) and ansStr[n].isdigit():
                    num += ansStr[n]
                    n += 1
                num = int(num) if num else 1
                hasil += temp * num
                i = n
            else:
                messagebox.showerror(title="Error", message=f"Rumus molekul salah atau tidak ditemukan!")
                return

        messagebox.showinfo(title="Hasil", message=f"Massa molar dari {ansStr} adalah {hasil}g/mol")
# Run the app
root = tkinter.Tk()
mainApp(root)
root.mainloop()
