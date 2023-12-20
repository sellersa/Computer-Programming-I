import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 222)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(118, 76)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(119, 58)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(156, 26)
		self._label1.TabIndex = 2
		self._label1.Text = "Enter tickets sold:"
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._label2.Location = System.Drawing.Point(13, 58)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Class A Tickets:"
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(167, 224)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(118, 76)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(313, 224)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(118, 75)
		self._button3.TabIndex = 10
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Cyan
		self._label3.Location = System.Drawing.Point(13, 103)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 11
		self._label3.Text = "Class B Tickets:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self._label4.Location = System.Drawing.Point(13, 148)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 12
		self._label4.Text = "Class C Tickets:"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(119, 106)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 13
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(119, 149)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 14
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Yellow
		self._label5.Location = System.Drawing.Point(225, 149)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 17
		self._label5.Text = "Class C Tickets:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.FromArgb(0, 192, 0)
		self._label6.Location = System.Drawing.Point(225, 101)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 16
		self._label6.Text = "Class B Tickets:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Red
		self._label7.Location = System.Drawing.Point(225, 58)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 15
		self._label7.Text = "Class A Tickets:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label8.Location = System.Drawing.Point(331, 58)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 18
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label9.Location = System.Drawing.Point(331, 101)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 19
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label10.Location = System.Drawing.Point(331, 149)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 20
		# 
		# label11
		# 
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(225, 16)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(156, 26)
		self._label11.TabIndex = 21
		self._label11.Text = "Money obtained:"
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.Brown
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(83, 196)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 23)
		self._label12.TabIndex = 22
		self._label12.Text = "Total money:"
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label13.Location = System.Drawing.Point(200, 196)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 23)
		self._label13.TabIndex = 23
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(442, 337)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg186"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		A = self._textBox1.Text
		B = self._textBox2.Text
		C = self._textBox3.Text
		
		A = int(A)
		B = int(B)
		C = int(C)
		
		a = A * 15
		b = B * 12                                  
		c = C * 9
		spookyscaryskeletonsspeakwithsuchascreechyoullshakeandshudderinsurprisewhenyouhearthesezombiesshriekweresosorryskeletonsyoursoulmisunderstoodweonlywanttosocialzebutIdontthinkweshould = (a) + (b) + (c)
		
		self._label8.Text = str(a)
		self._label9.Text = str(b)
		self._label10.Text = str(c)
		self._label13.Text = str(spookyscaryskeletonsspeakwithsuchascreechyoullshakeandshudderinsurprisewhenyouhearthesezombiesshriekweresosorryskeletonsyoursoulmisunderstoodweonlywanttosocialzebutIdontthinkweshould)


	def Button2Click(self, sender, e):
		self._label8.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""
		self._label13.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()