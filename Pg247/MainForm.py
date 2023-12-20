import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# checkBox1
		# 
		self._checkBox1.BackColor = System.Drawing.Color.Lime
		self._checkBox1.Location = System.Drawing.Point(0, 1)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Choice 1"
		self._checkBox1.UseVisualStyleBackColor = False
		# 
		# checkBox2
		# 
		self._checkBox2.BackColor = System.Drawing.Color.Red
		self._checkBox2.Location = System.Drawing.Point(0, 62)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "Choice 2"
		self._checkBox2.UseVisualStyleBackColor = False
		# 
		# checkBox3
		# 
		self._checkBox3.BackColor = System.Drawing.Color.Lime
		self._checkBox3.Location = System.Drawing.Point(0, 122)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(104, 24)
		self._checkBox3.TabIndex = 2
		self._checkBox3.Text = "Choice 3"
		self._checkBox3.UseVisualStyleBackColor = False
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.Red
		self._radioButton1.Location = System.Drawing.Point(132, 1)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 3
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Choice 4"
		self._radioButton1.UseVisualStyleBackColor = False
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.Lime
		self._radioButton2.Location = System.Drawing.Point(132, 61)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 4
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Choice 5"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.Red
		self._radioButton3.Location = System.Drawing.Point(132, 121)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 5
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Choice 6"
		self._radioButton3.UseVisualStyleBackColor = False
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# label1
		# 
		self._label1.ForeColor = System.Drawing.Color.Fuchsia
		self._label1.Location = System.Drawing.Point(13, 153)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(211, 75)
		self._label1.TabIndex = 6
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(-1, 232)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(237, 34)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(-1, 265)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(237, 34)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(-1, 298)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(237, 34)
		self._button3.TabIndex = 9
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self.ClientSize = System.Drawing.Size(236, 332)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Name = "MainForm"
		self.Text = "Pg247"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		
		one = self._checkBox1.Checked
		two = self._checkBox2.Checked
		three = self._checkBox3.Checked
		four = self._radioButton1.Checked
		five = self._radioButton2.Checked
		six = self._radioButton3.Checked
		message = ""
		
		if one == True:
			message = "Choice 1"
		
		if two == True and one == True:
			message += " and Choice 2"
		elif two == True:
			message = "Choice 2"
		else:
			pass
		
		
		if three == True and one == True:
			message += " and Choice 3"
		elif two == True:
			message += " and Choice 3"
		else:
			message = "Choice 3"
		
			
			
			
		if four == True:
			message += " and Choice 4 were chosen"
		elif five == True:
			message += " and Choice 5 were chosen"
		elif six == True:
			message += " and Choice 6 were chosen"
		else:
			message += " were chosen"
		
		self._label1.Text = message
		
		
		
		
		"""
		
		if one == True:
			message = "Choice 1"
			if two == True:
				message += "and Choice 2"
				if three == True:
					message += "and Choice 3"
					if four == True:
						message += "and Choice 4 were chosen"
						if five == True:
							message += "and Choice 5 were chosen"
							if six == True:
								message += "and Choice 6 were chosen"
		elif two == True:
			message = "Choice 2"
			if three == True:
					message += "and Choice 3"
					if four == True:
						message += "and Choice 4 were chosen"
						if five == True:
							message += "and Choice 5 were chosen"
							if six == True:
								message += "and Choice 6 were chosen"
		elif three == True:
			message = "Choice 3"
			if four == True:
				message += "and Choice 4 were chosen"
				if five == True:
					message += "and Choice 5 were chosen"
					if six == True:
						message += "and Choice 6 were chosen"
		elif four == True:
			message = "and Choice 4 was chosen."
		elif five == True:
			message = "and Choice 5 was chosen."
		elif six == True:
			message = "and Choice 6 was chosen."
		else:
			message = "was chosen."

			"""
		
	
			
			
			

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def RadioButton3CheckedChanged(self, sender, e):
		pass