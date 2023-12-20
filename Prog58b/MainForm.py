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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(52, 353)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(171, 76)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(306, 353)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(171, 76)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(566, 353)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(171, 76)
		self._button3.TabIndex = 2
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(52, 39)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 44)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(52, 112)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 44)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(52, 177)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 44)
		self._textBox3.TabIndex = 5
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label1.Location = System.Drawing.Point(189, 251)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(228, 42)
		self._label1.TabIndex = 6
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label2.Location = System.Drawing.Point(52, 251)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(143, 42)
		self._label2.TabIndex = 7
		self._label2.Text = "Roots:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label3.Location = System.Drawing.Point(414, 251)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(38, 42)
		self._label3.TabIndex = 8
		self._label3.Text = ","
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label4.Location = System.Drawing.Point(444, 251)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(278, 42)
		self._label4.TabIndex = 9
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(825, 441)
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
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "Prog58b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		a = float(self._textBox1.Text)
		b = float(self._textBox2.Text)
		c = float(self._textBox3.Text)
		root = math.sqrt(b ** 2 - (a * 4 * c))
		this = (-b + (root)) / (a * 2)
		that = (-b - (root)) / (a * 2)
		self._label1.Text = "" + str(this)
		self._label4.Text = "" + str(that)
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label1.Text = ""
		self._label4.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()