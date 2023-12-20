import math
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
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 150)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(153, 40)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(204, 150)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(151, 40)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(-8, 439)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(668, 46)
		self._button3.TabIndex = 2
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(379, 37)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(260, 49)
		self._label1.TabIndex = 3
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(273, 49)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(273, 93)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 5
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(13, 37)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(243, 37)
		self._label2.TabIndex = 6
		self._label2.Text = "Enter Purchace Price:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 93)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(244, 38)
		self._label3.TabIndex = 7
		self._label3.Text = "Enter Amount Received:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(379, 104)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(260, 49)
		self._label4.TabIndex = 8
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(379, 172)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(260, 49)
		self._label5.TabIndex = 9
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(379, 233)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(260, 49)
		self._label6.TabIndex = 10
		self._label6.Click += self.Label6Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(374, 297)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(265, 49)
		self._label7.TabIndex = 11
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(38, 375)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(287, 42)
		self._label8.TabIndex = 12
		self._label8.Text = "Money Due: ------>"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.FromArgb(0, 192, 0)
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(374, 365)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(265, 61)
		self._label9.TabIndex = 13
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(656, 497)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog58t"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label3Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		Price = float(self._textBox1.Text)
		Money = float(self._textBox2.Text)
		Change = Money - Price
		Do = Change // 1
		Q = (Change - Do) // 0.25
		Di = (Change - Do - (Q / 4)) //  0.10
		N = (Change - Do - (Q / 4) - (Di / 10)) // 0.05
		P = (Change - Do - (Q / 4) - (Di / 10) - (N / 20)) / 0.01
		all = Do + (Q * 0.25) + (Di * 0.1) + (N * 0.05) + (P * 0.01)
		self._label1.Text = "Dollars: " + str(Do)
		self._label4.Text = "Quarters: " + str(Q)
		self._label5.Text = "Dimes: " + str(Di)
		self._label6.Text = "Nickles: " + str(N)
		self._label7.Text = "Pennies: " + str(P)
		self._label9.Text = "=___________________\n" + str(all)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label1.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""
		self._label9.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def Label6Click(self, sender, e):
		pass