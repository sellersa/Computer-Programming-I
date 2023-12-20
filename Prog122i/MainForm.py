import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("Prog122i.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._button1 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Red
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 261)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(205, 187)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(434, 261)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(205, 187)
		self._button3.TabIndex = 2
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(209, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(237, 186)
		self._listBox1.TabIndex = 3
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Red
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(223, 261)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(205, 187)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Red
		self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
		self.ClientSize = System.Drawing.Size(650, 460)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122i"
		self.ResumeLayout(False)


#	def Button1Click(self, sender, e):
		#heading = "Number\tCube Root\tCube"
		#self._listBox1.Items.Add(heading)
		
	#	for num in range(-25, 25 + 1):
		#	cr = math.sqrt(math.sqrt(num))
		#	c = num**3
			
		#	cr = round(cr, 4)
			
			#all = cr + "\t" + c
		#	self._listBox1.Items.Add(all)
#
	#def Button2Click(self, sender, e):
	#	self._listBox1.Items.Clear()

#	def Button3Click(self, sender, e):
		##Application.Exit()