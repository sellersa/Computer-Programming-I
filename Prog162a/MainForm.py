import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 40)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(225, 33)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter a number:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(243, 47)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(328, 20)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 167)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(182, 95)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(200, 167)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(182, 95)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(388, 167)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(183, 95)
		self._button3.TabIndex = 4
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._label2.Location = System.Drawing.Point(12, 85)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(555, 79)
		self._label2.TabIndex = 5
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self.ClientSize = System.Drawing.Size(583, 268)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog162a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		i = self._textBox1.Text
		i = int(i)
		l = 1
		if i > 0:
			for num in range(1, i+1):
				l = num * l
			self._label2.Text = "The value of " + str(i) + "! is " + str(l)
		else:
			self._label2.Text = ">:("

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()