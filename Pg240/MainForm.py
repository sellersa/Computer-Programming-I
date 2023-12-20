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
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Lime
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(2, 218)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(336, 77)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Lime
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(2, 312)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(165, 77)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Lime
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(183, 312)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(165, 77)
		self._button3.TabIndex = 2
		self._button3.Text = "Close"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Red
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(2, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(208, 31)
		self._label1.TabIndex = 3
		self._label1.Text = "Sales for the month:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(2, 52)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(208, 31)
		self._label2.TabIndex = 4
		self._label2.Text = "Advance pay Awarded:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Red
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(2, 95)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(208, 31)
		self._label3.TabIndex = 5
		self._label3.Text = "Commission Rate:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(2, 138)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(208, 31)
		self._label4.TabIndex = 6
		self._label4.Text = "Commission:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Red
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(2, 184)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(208, 31)
		self._label5.TabIndex = 7
		self._label5.Text = "Net Pay:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Red
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(219, 100)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(119, 23)
		self._label6.TabIndex = 8
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.White
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(219, 143)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(119, 23)
		self._label7.TabIndex = 9
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Red
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(219, 188)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(119, 23)
		self._label8.TabIndex = 10
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Red
		self._textBox1.Location = System.Drawing.Point(219, 14)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(119, 20)
		self._textBox1.TabIndex = 11
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(219, 57)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(119, 20)
		self._textBox2.TabIndex = 12
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Cyan
		self.ClientSize = System.Drawing.Size(350, 401)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg240"
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox2TextChanged(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		
		
		
		
		
		
		
		
		"""decSalesAmount = 0.0
		decAdvancedPayAmount = 0.0
		decCommissionRate = 0.0
		decCommissionAmount = 0.0
		decNetPay = 0.0
		
		try:
			decSalesAmount = float(self._txtSalesAmount.Text)
		except:
			self._lblErrorMessage.Text = "Sales amount must be numeric"
			self._lblErroMessage.Visible = True
			return
		
		try:
			decAdvancePayAmount = float(self._txtAdvancePayAmount.Text)
		except:
			self._lblErrorMessage.Text = "Advance pay amount must be numeric"
			self._lblErroMessage.Visible = True
			return
		
		self._lblErrorMessageVisible = False
		
		if decSalesAmount < 10000:
			decCommissionRate = 0.05
		elif decSalesAmount >= 10000 and decSalesAmount < 15000:
			decCommissionRate = 0.1
		elif decSalesAmount < 10000 and decSalesAmount < 15000:
			decCommissionRate = 0.12
		elif decSalesAmount < 10000 and decSalesAmount < 18000:
			decCommissionRate = 0.14
		elif decSalesAmount < 10000 and decSalesAmount < 22000:
			decCommissionRate = 0.15"""
			
		MonthSales = int(self._textBox1.Text)
		AdvancePay = int(self._textBox2.Text)
		
		if MonthSales < 10000:
			Percent = 5
			Number = 0.05
		elif MonthSales >= 10000 and MonthSales <= 14999:
			Percent = 10
			Number = 0.1
		elif MonthSales >= 15000 and MonthSales <= 17999:
			Percent = 12
			Number = 0.12
		elif MonthSales >= 18000 and MonthSales <= 21999:
			Percent = 14
			Number = 0.14
		elif MonthSales >= 22000:
			Percent = 16
			Number = 0.15
		else:
			Percent = 63
			Number = 63
		self._label6.Text = str(Percent) + "%"
		
		
		
		Monayee = float(self._textBox1.Text) * Number
		self._label7.Text = "$" + str(Monayee)
		
		NetPay = Monayee - float(self._textBox2.Text)
		self._label8.Text = "$" + str(NetPay)
	

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()
		
		