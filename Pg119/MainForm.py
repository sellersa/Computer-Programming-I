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
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(-2, 240)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(177, 108)
		self._button1.TabIndex = 0
		self._button1.Text = "Combine"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(171, 240)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(177, 108)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(341, 240)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(177, 108)
		self._button3.TabIndex = 2
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(19, 36)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(156, 28)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter First Name:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(19, 104)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(156, 28)
		self._label2.TabIndex = 4
		self._label2.Text = "Enter Last Name:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(290, 36)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(290, 104)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 6
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(19, 170)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(156, 28)
		self._label3.TabIndex = 7
		self._label3.Text = "Your Full Name:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(265, 170)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(155, 28)
		self._label4.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self.ClientSize = System.Drawing.Size(517, 369)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg119"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label4.Text = self._textBox1.Text + " " + self._textBox2.Text

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()