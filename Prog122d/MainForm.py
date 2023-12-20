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
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Cyan
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 371)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(174, 91)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Fuchsia
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 24
		self._listBox1.Location = System.Drawing.Point(184, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(294, 340)
		self._listBox1.TabIndex = 1
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Cyan
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(242, 371)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(174, 91)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Cyan
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(478, 371)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(174, 91)
		self._button3.TabIndex = 3
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self.ClientSize = System.Drawing.Size(676, 474)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122d"
		self.ResumeLayout(False)

# y = x^6 -3x^5 -93x^4 + 87x^3 + 1596x^2 - 1380x - 2800

	def Button1Click(self, sender, e):
		for num in range(-12, 16 + 1):
			y = (num**6) + (-3 * num**5) + (-93 * num**4) + (87 * num**3) + (1596 * num**2) - (1380 * num) - (2800)
			z = str(num) + "      -      " + str(y)
			self._listBox1.Items.Add(z)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()