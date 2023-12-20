import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["1970 VW Bug",
			"1979 Firebird",
			"1980 Subaru",
			"1975 Cutlass"]))
		self._comboBox1.Location = System.Drawing.Point(307, 21)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(328, 21)
		self._comboBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(44, 21)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(147, 33)
		self._label1.TabIndex = 1
		self._label1.Text = "Pick a car:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(44, 377)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(161, 70)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(343, 377)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(156, 70)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(645, 377)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(156, 70)
		self._button3.TabIndex = 4
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Lime
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(44, 91)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(147, 33)
		self._label2.TabIndex = 5
		self._label2.Text = "Miles:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Lime
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(44, 160)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(147, 33)
		self._label3.TabIndex = 6
		self._label3.Text = "Gallons:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Lime
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(44, 237)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(147, 33)
		self._label4.TabIndex = 7
		self._label4.Text = "MPG:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(250, 91)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(523, 33)
		self._label5.TabIndex = 10
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(250, 160)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(523, 33)
		self._label6.TabIndex = 9
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Yellow
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(250, 237)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(523, 33)
		self._label7.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Blue
		self.ClientSize = System.Drawing.Size(885, 495)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._comboBox1)
		self.Name = "MainForm"
		self.Text = "Prog54a"
		self.ResumeLayout(False)

	def Button1Click(self, sender, e):
		miles = 0
		gallons = 0
		mpg = 0
		car = self._comboBox1.Text
		
		if car == "1970 VW Bug":
			miles = 286
			gallons = 9
		if car == "1979 Firebird":
			miles = 412
			gallons = 40
		if car == "1980 Subaru":
			miles = 361
			gallons = 18
		if car == "1975 Cutlass":
			miles = 161
			gallons = 11
			
		# Cast one or both as float to do real division instead of integer division.
		mpg = miles / float(gallons)
		mpg = round(mpg, 10)
		
		self._label5.Text = str(miles)
		self._label6.Text = str(gallons)
		self._label7.Text = str(mpg)

	def Button2Click(self, sender, e):
		self._label5.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""
		self._comboBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()