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
		self._listBox1 = System.Windows.Forms.ListBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 198)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(81, 28)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(99, 198)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(53, 27)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(164, 198)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(56, 27)
		self._button3.TabIndex = 2
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Purple
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(201, 95)
		self._listBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 115)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 4
		self._label1.Text = "Guests:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Red
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 160)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Chairs:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(120, 115)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(120, 160)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 7
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(225, 230)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog162h"
		self.ResumeLayout(False)
		self.PerformLayout()



	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()
		Guests = self._textBox1.Text
		Guests = int(Guests)
		
		Chairs = self._textBox2.Text
		Chairs = int(Chairs)
		
		Losers = Guests - Chairs

		Outcomes = 1
		
		for num in range(Guests, Chairs-2, -1):
			Outcomes = num * Outcomes
		
		
		One = "Guests: " + str(Guests)
		Two = "Chairs: " + str(Chairs)
		Three = "Permutations: " + str(Outcomes)
		Four = "Guests Standing: " + str(Losers)
		self._listBox1.Items.Add(One)
		self._listBox1.Items.Add(Two)
		self._listBox1.Items.Add(Three)
		self._listBox1.Items.Add(Four)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()