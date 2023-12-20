import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(219, 32)
		self._label1.TabIndex = 0
		self._label1.Text = "Pounds:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 82)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(219, 32)
		self._label2.TabIndex = 1
		self._label2.Text = "Shillings:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 152)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(219, 32)
		self._label3.TabIndex = 2
		self._label3.Text = "Pence:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 338)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(219, 32)
		self._label4.TabIndex = 3
		self._label4.Text = "Decimal Pounds:"
		self._label4.Click += self.Label4Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(294, 21)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(294, 94)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(294, 164)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 6
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(294, 338)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(219, 32)
		self._label5.TabIndex = 7
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 391)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(219, 93)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(294, 391)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(219, 93)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(576, 391)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(219, 93)
		self._button3.TabIndex = 10
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self.ClientSize = System.Drawing.Size(812, 496)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog65h"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label4Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		Pounds = float(self._textBox1.Text)
		Shillings = float(self._textBox2.Text)
		Pence = float(self._textBox3.Text)
		# 1 pound = 20 shillings = 240 pence
		# 1 pound = 20 pence
		Total = (((Pounds * 240) + (Shillings * 12) + Pence) / 100) / 2.4
		Total = round(Total, 2)
		# Another = Total * 100
		# Bnother = Another // 1
		# Cnother = Bnother / 100
		# Dnother = Total - Cnother
		# Enother = Cnother + Dnother
		self._label5.Text = "£" + str(Total)


	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()