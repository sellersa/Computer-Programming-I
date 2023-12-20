import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 310)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(165, 87)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 75)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(503, 134)
		self._listBox1.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Lime
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 22)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(165, 38)
		self._label1.TabIndex = 2
		self._label1.Text = "Enter Number:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(216, 32)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(264, 20)
		self._textBox1.TabIndex = 3
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(183, 310)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(165, 87)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(354, 310)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(165, 87)
		self._button3.TabIndex = 5
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 212)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(503, 95)
		self._label2.TabIndex = 6
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self.ClientSize = System.Drawing.Size(527, 409)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog152b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()
		t = self._textBox1.Text
		t = int(t)
		l = 0
		self._label2.Text = "The sum of the even integers"
		heading = "Even Integer     Sum"
		self._listBox1.Items.Add(heading)
		
		for num in range(2, t+2, 2):
			if l <= t:

				l = num + l

				closing2 = ", " + str(num)
				self._label2.Text = self._label2.Text + closing2

				f = str(num) + "   ----------->   " + str(l)
				self._listBox1.Items.Add(f)
			else:
				pass
			

		self._label2.Text = self._label2.Text + " is >= to " + str(t) + "."
		

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()