import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(29, 117)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(217, 91)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(29, 240)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(217, 91)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(29, 361)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(217, 91)
		self._button3.TabIndex = 2
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(29, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(118, 91)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter Kilowatts used:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(146, 68)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(270, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(473, 443)
		self._label2.TabIndex = 5
		self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(767, 473)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		x = float(self._textBox1.Text)
		money1 = x * 0.0475
		tax = money1 * 0.03
		sur = money1 * 0.10
		MONEY2 = money1 + tax + sur
		maybe = MONEY2 * 0.04
		MONEY21 = MONEY2 + maybe
		
		money1 = round(money1, 2)
		tax = round(tax, 2)
		sur = round(sur, 2)
		MONEY2 = round(MONEY2, 2)
		maybe = round(maybe, 2)
		MONEY21 = round(MONEY21, 2)
		
		
		
		self._label2.Text = "C O M P S C I Electric\t___________________________________________\tKilowatts used: " \
		+ str(self._textBox1.Text) + "\t___________________________________________\tBase Rate  -  " \
		+ str(self._textBox1.Text) + "                              $0.0475  $ " + str(money1) + \
		"\tSurcharge                                                          $ " + str(sur) \
		+ "\tCitytax                                                                $ " \
		+ str(tax) + "\t\t\t\t\t\t\t Pay this amount:                                                  $ " \
		+ str(MONEY2) + " Pay after May 20th:                                           $ " + str(MONEY21)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()