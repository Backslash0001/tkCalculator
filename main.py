import tkinter as tk 


class Calculator(tk.Tk):
	def __init__(self):
		super().__init__()

		self.calcul = tk.StringVar(value="0")
		self.value = tk.StringVar()
		self.memory = tk.DoubleVar(value=0)


		self.set_window()
		self.add_widgets()
		self.display()


	def set_window(self):
		self.title("Calculatrice")
		self.config(bg="#f3f3f3")
		self.resizable(False, True)
		self.minsize(width=0, height=522)
		self.maxsize(width=900, height=580)

	def add_widgets(self):
		self.output = tk.Frame(self, bg="#fff", height=150, padx=10)
		self.output.pack_propagate(False)
		self.output.pack(fill="both", expand=True)

		calcul = tk.Label(self.output, bg="#fff", height=2, anchor="se", font="Helvetica 25", textvariable=self.calcul)
		calcul.pack(fill="x", side="bottom")

		message = tk.Label(self.output, anchor="se", bg="#fff", font="Arial 12", textvariable=self.value)
		message.pack(fill="x", side="bottom", before=calcul)

		keyboard = tk.Frame(self, padx=3, pady=3)
		keyboard.pack(fill="both")

		simple_keys = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "", "0", ","]
		for i in range(4):
			for j in range(3):
				key = simple_keys[i*3+j]
				btn = tk.Button(keyboard, text=key, width=4, font="Arial 25", bg="#fff", activebackground="#fff", relief="flat")
				btn.text=key
				btn.config(command=lambda button=btn:self.affect(button.text))
				btn.grid(row=i+1, column=j, padx=3, pady=3)
		

		self.signs=["/","x", "-", "+"]
		for i in range(4):
			btn = tk.Button(keyboard, text=self.signs[i], width=4, font="Arial 25", bg="#f9f9f9", activebackground="#f9f9f9", relief="flat")
			btn.text = self.signs[i]
			btn.config(command=lambda button=btn:self.affect(button.text))
			btn.grid(row=i, column=3, padx=3, pady=3)

		mem = tk.Button(keyboard, text="M+", width=4, font="Arial 14", bg="#f9f9f9")
		mem.config(activebackground="#f9f9f9", relief="flat", command=self.memorize)
		mem.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)

		c = tk.Button(keyboard, text="C", width=4, font="Arial 14", bg="#f9f9f9", activebackground="#f9f9f9", relief="flat")
		c.config(command=self.clear)
		c.grid(row=0, column=1, sticky="nsew", padx=3, pady=3)

		ce = tk.Button(keyboard, text="CE", width=4, font="Arial 14", bg="#f9f9f9", activebackground="#f9f9f9", relief="flat")
		ce.config(command=self.erase)
		ce.grid(row=0, column=2, sticky="nsew", padx=3, pady=3)

		release = tk.Button(keyboard, text="M-", width=4, font="Arial 14", bg="#f9f9f9")
		release.config(activebackground="#f9f9f9", relief="flat", command=self.release)
		release.grid(row=4, column=0, sticky="nsew", padx=3, pady=3)

		equal = tk.Button(keyboard, text="=", width=4, font="Arial 25", bg="#005a9e", activebackground="#004b8a")
		equal.config(activeforeground="#fff", fg="#fff", relief="flat", command=self.show)
		equal.grid(row=4, column=3)

	def memorize(self):
		# garder la valeur actuelle en memoire
		if self.value.get() == "  ":
			self.memory.set(self.calcul.get())
		elif self.value.get() not in ("", " "):
			self.memory.set(self.value.get()[2:])


	def release(self):
		if self.memory.get().is_integer():
			self.affect(str(int(self.memory.get())))
		else:
			self.affect(str(self.memory.get()))

	def clear(self):
		self.calcul.set("0")
		self.calculate()

	def erase(self):
		if len(self.calcul.get()) != 1 and self.calcul.get() != "SyntaxError":
			self.calcul.set(self.calcul.get()[:-1])
		else:
			self.calcul.set("0")

		self.calculate()
	

	def affect(self, char):
		# ajout du caracter actuel a la chaine de calcul

		if self.value.get() == "  " and char not in self.signs:
			self.calcul.set(char)
		elif self.calcul.get() != "0" and self.calcul.get() != "SyntaxError":
			self.calcul.set(self.calcul.get() + char)
		else:
			self.calcul.set(char)

		self.calculate()

	def calculate(self):
		try:
			self.value.set("= " + str(eval(self.calcul.get().replace(',', ".").replace("x", "*"))))
		except SyntaxError:
			self.value.set(" ")

	def show(self):
		if self.value.get() == " " and self.calcul.get() != "0":
			self.calcul.set("SyntaxError")
		else:
			self.calcul.set(self.value.get()[2:])
			self.value.set("  ")

	def display(self):
		self.mainloop()

Calculator()