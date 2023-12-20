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
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(25, 331)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(152, 69)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(181, 331)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(152, 69)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(339, 331)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(152, 69)
		self._button3.TabIndex = 2
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(350, 65)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(350, 141)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Beige
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(301, 208)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(190, 85)
		self._label1.TabIndex = 5
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(25, 141)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(133, 35)
		self._label2.TabIndex = 6
		self._label2.Text = "Speed:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(25, 228)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(133, 35)
		self._label3.TabIndex = 7
		self._label3.Text = "Ticket Price:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(25, 54)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(133, 35)
		self._label4.TabIndex = 8
		self._label4.Text = "Speed Limit:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Yellow
		self.ClientSize = System.Drawing.Size(510, 411)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog82a"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		L = int(self._textBox1.Text)
		S = int(self._textBox2.Text)
		
		Amount = S - L
		Money = 20 + (Amount * 5.0)
		
		self._label1.Text = "$" + str(Money)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()