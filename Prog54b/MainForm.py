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
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.Control
		self._button1.Location = System.Drawing.Point(67, 168)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(157, 53)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.SystemColors.Control
		self._button2.Location = System.Drawing.Point(326, 168)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(157, 53)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.Control
		self._button3.Location = System.Drawing.Point(589, 168)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(157, 53)
		self._button3.TabIndex = 2
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(279, 73)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 38)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(136, 73)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 38)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(575, 73)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 38)
		self._textBox3.TabIndex = 5
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(433, 73)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 38)
		self._textBox4.TabIndex = 6
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(131, 234)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(544, 124)
		self._label1.TabIndex = 7
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(131, 358)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(544, 124)
		self._label2.TabIndex = 8
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 234)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 124)
		self._label3.TabIndex = 9
		self._label3.Text = "Sum:"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 358)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 124)
		self._label4.TabIndex = 10
		self._label4.Text = "Avg:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(881, 491)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		num4 = int(self._textBox4.Text)
		
		Sum = num1 + num2 + num3 + num4
		Avg = Sum / 4.0
		
		self._label1.Text = "Sum: " + str(Sum)
		self._label2.Text = "Average: " + str(Avg)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._label1.Text = ""
		self._label2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()
		
		
		
		
		
		#wompwomp