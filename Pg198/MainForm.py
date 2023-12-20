﻿import math
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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(-3, 279)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(125, 62)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate Average"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(-3, 347)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(125, 39)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(-3, 392)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(125, 40)
		self._button3.TabIndex = 2
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(-3, 97)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(125, 20)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.White
		self._textBox2.Location = System.Drawing.Point(-3, 171)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(125, 20)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.White
		self._textBox3.Location = System.Drawing.Point(-3, 229)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(125, 20)
		self._textBox3.TabIndex = 5
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._label1.Location = System.Drawing.Point(-3, 71)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(125, 23)
		self._label1.TabIndex = 6
		self._label1.Text = "Score 1:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._label2.Location = System.Drawing.Point(-3, 203)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(125, 23)
		self._label2.TabIndex = 7
		self._label2.Text = "Score 3:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._label3.Location = System.Drawing.Point(-3, 130)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(125, 23)
		self._label3.TabIndex = 8
		self._label3.Text = "Score 2:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Red
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(-3, 0)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(125, 71)
		self._label4.TabIndex = 9
		self._label4.Text = "Enter your test scores"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Lime
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(-3, 253)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(125, 23)
		self._label5.TabIndex = 10
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self.ClientSize = System.Drawing.Size(120, 430)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg198"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		a = float(self._textBox1.Text)
		b = float(self._textBox2.Text)
		c = float(self._textBox3.Text)
		
		sfjl = a + b + c
		sfjl = sfjl / 3
		sfjl = round(sfjl, 3)
		self._label5.Text = str(sfjl)
		
		if sfjl >= 95:
			self._label4.Text = "Congratulations! Great Job!"
		
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label4.Text = "Enter your test scores"

	def Button3Click(self, sender, e):
		Application.Exit()

	def Label4Click(self, sender, e):
		pass