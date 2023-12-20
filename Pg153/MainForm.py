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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(130, 31)
		self._label1.TabIndex = 0
		self._label1.Text = "Annual Salary:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 66)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(130, 31)
		self._label2.TabIndex = 1
		self._label2.Text = "Pay periods per year:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 123)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(130, 31)
		self._label3.TabIndex = 2
		self._label3.Text = "Salary per pay period:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(12, 158)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(130, 20)
		self._label4.TabIndex = 3
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(12, 43)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(130, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(12, 100)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(130, 20)
		self._textBox2.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkSlateBlue
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 181)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(130, 35)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkSlateBlue
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(12, 222)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(130, 35)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkSlateBlue
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(11, 263)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(130, 35)
		self._button3.TabIndex = 8
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Purple
		self.ClientSize = System.Drawing.Size(153, 304)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg153"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		money = self._textBox1.Text
		time = self._textBox2.Text
		fgsdjgsdfk = int(money) / int(time)
		self._label4.Text = str(round(fgsdjgsdfk, 3))

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()