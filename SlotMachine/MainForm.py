import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.num1 = 0
		self.num2 = 0
		self.num3 = 0
		
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		resources = System.Resources.ResourceManager("SlotMachine.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._pictureBox2 = System.Windows.Forms.PictureBox()
		self._pictureBox3 = System.Windows.Forms.PictureBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._pictureBox4 = System.Windows.Forms.PictureBox()
		self._label1 = System.Windows.Forms.Label()
		self._timer1 = System.Windows.Forms.Timer(self._components)
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._pictureBox5 = System.Windows.Forms.PictureBox()
		self._pictureBox6 = System.Windows.Forms.PictureBox()
		self._pictureBox7 = System.Windows.Forms.PictureBox()
		self._pictureBox8 = System.Windows.Forms.PictureBox()
		self._pictureBox9 = System.Windows.Forms.PictureBox()
		self._pictureBox10 = System.Windows.Forms.PictureBox()
		self._pictureBox11 = System.Windows.Forms.PictureBox()
		self._pictureBox1.BeginInit()
		self._pictureBox2.BeginInit()
		self._pictureBox3.BeginInit()
		self._pictureBox4.BeginInit()
		self._pictureBox5.BeginInit()
		self._pictureBox6.BeginInit()
		self._pictureBox7.BeginInit()
		self._pictureBox8.BeginInit()
		self._pictureBox9.BeginInit()
		self._pictureBox10.BeginInit()
		self._pictureBox11.BeginInit()
		self.SuspendLayout()
		# 
		# pictureBox1
		# 
		self._pictureBox1.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._pictureBox1.Location = System.Drawing.Point(12, 12)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(121, 180)
		self._pictureBox1.TabIndex = 0
		self._pictureBox1.TabStop = False
		# 
		# pictureBox2
		# 
		self._pictureBox2.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._pictureBox2.Location = System.Drawing.Point(139, 12)
		self._pictureBox2.Name = "pictureBox2"
		self._pictureBox2.Size = System.Drawing.Size(121, 180)
		self._pictureBox2.TabIndex = 1
		self._pictureBox2.TabStop = False
		# 
		# pictureBox3
		# 
		self._pictureBox3.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._pictureBox3.Location = System.Drawing.Point(266, 12)
		self._pictureBox3.Name = "pictureBox3"
		self._pictureBox3.Size = System.Drawing.Size(121, 180)
		self._pictureBox3.TabIndex = 2
		self._pictureBox3.TabStop = False
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(393, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(219, 283)
		self._button1.TabIndex = 3
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(393, 302)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(218, 67)
		self._button2.TabIndex = 4
		self._button2.Text = "Pickpocket"
		self._button2.UseVisualStyleBackColor = True
		# 
		# pictureBox4
		# 
		self._pictureBox4.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._pictureBox4.BackgroundImage = resources.GetObject("pictureBox4.BackgroundImage")
		self._pictureBox4.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox4.Location = System.Drawing.Point(12, 198)
		self._pictureBox4.Name = "pictureBox4"
		self._pictureBox4.Size = System.Drawing.Size(375, 230)
		self._pictureBox4.TabIndex = 5
		self._pictureBox4.TabStop = False
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(394, 372)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 6
		self._label1.Text = "Bet:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(500, 398)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 7
		self._label2.Text = "100"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(394, 398)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 8
		self._label3.Text = "Money:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(500, 375)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 9
		# 
		# pictureBox5
		# 
		self._pictureBox5.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._pictureBox5.Image = resources.GetObject("pictureBox5.Image")
		self._pictureBox5.Location = System.Drawing.Point(12, 198)
		self._pictureBox5.Name = "pictureBox5"
		self._pictureBox5.Size = System.Drawing.Size(70, 63)
		self._pictureBox5.TabIndex = 10
		self._pictureBox5.TabStop = False
		# 
		# pictureBox6
		# 
		self._pictureBox6.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._pictureBox6.Location = System.Drawing.Point(88, 198)
		self._pictureBox6.Name = "pictureBox6"
		self._pictureBox6.Size = System.Drawing.Size(70, 63)
		self._pictureBox6.TabIndex = 11
		self._pictureBox6.TabStop = False
		# 
		# pictureBox7
		# 
		self._pictureBox7.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._pictureBox7.Location = System.Drawing.Point(165, 198)
		self._pictureBox7.Name = "pictureBox7"
		self._pictureBox7.Size = System.Drawing.Size(70, 63)
		self._pictureBox7.TabIndex = 12
		self._pictureBox7.TabStop = False
		# 
		# pictureBox8
		# 
		self._pictureBox8.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._pictureBox8.Location = System.Drawing.Point(241, 198)
		self._pictureBox8.Name = "pictureBox8"
		self._pictureBox8.Size = System.Drawing.Size(70, 63)
		self._pictureBox8.TabIndex = 13
		self._pictureBox8.TabStop = False
		# 
		# pictureBox9
		# 
		self._pictureBox9.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._pictureBox9.Location = System.Drawing.Point(317, 198)
		self._pictureBox9.Name = "pictureBox9"
		self._pictureBox9.Size = System.Drawing.Size(70, 63)
		self._pictureBox9.TabIndex = 14
		self._pictureBox9.TabStop = False
		# 
		# pictureBox10
		# 
		self._pictureBox10.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._pictureBox10.Location = System.Drawing.Point(12, 365)
		self._pictureBox10.Name = "pictureBox10"
		self._pictureBox10.Size = System.Drawing.Size(70, 63)
		self._pictureBox10.TabIndex = 15
		self._pictureBox10.TabStop = False
		# 
		# pictureBox11
		# 
		self._pictureBox11.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._pictureBox11.Location = System.Drawing.Point(88, 365)
		self._pictureBox11.Name = "pictureBox11"
		self._pictureBox11.Size = System.Drawing.Size(70, 63)
		self._pictureBox11.TabIndex = 16
		self._pictureBox11.TabStop = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self.ClientSize = System.Drawing.Size(623, 430)
		self.Controls.Add(self._pictureBox11)
		self.Controls.Add(self._pictureBox10)
		self.Controls.Add(self._pictureBox9)
		self.Controls.Add(self._pictureBox8)
		self.Controls.Add(self._pictureBox7)
		self.Controls.Add(self._pictureBox6)
		self.Controls.Add(self._pictureBox5)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._pictureBox4)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._pictureBox3)
		self.Controls.Add(self._pictureBox2)
		self.Controls.Add(self._pictureBox1)
		self.Name = "MainForm"
		self.Load += self.MainFormLoad
		self._pictureBox1.EndInit()
		self._pictureBox2.EndInit()
		self._pictureBox3.EndInit()
		self._pictureBox4.EndInit()
		self._pictureBox5.EndInit()
		self._pictureBox6.EndInit()
		self._pictureBox7.EndInit()
		self._pictureBox8.EndInit()
		self._pictureBox9.EndInit()
		self._pictureBox10.EndInit()
		self._pictureBox11.EndInit()
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		rnd = System.Random()
		money = rnd,Next(1, 51)
		if money > 25:
			MessageBox.Show("You failed to steal money!")
		else:
			cmoney = float(self._label2.Text)
			self.label2.Text = str(round(cmoney + money, 2))

	def Button1Click(self, sender, e):
		img1 = self._pictureBox5.BackroundImage
		img2 = self._pictureBox6.BackroundImage
		img3 = self._pictureBox7.BackroundImage
		img4 = self._pictureBox8.BackroundImage
		img5 = self._pictureBox9.BackroundImage
		img6 = self._pictureBox10.BackroundImage
		img7 = self._pictureBox11.BackroundImage
		rnd = System.Random()
		num1 = 0
		num2 = 0
		num3 = 0
		
		if self._textBox1.Text == "":
			MessageBox.Show ("You must enter an amount to bet first!")
			return
		money = float(self._label2.Text)
		bet = float(self._textBox1.Text)
		moneytwo = money - bet
		
		if money == 0:
			MessageBox.Show("You have no money!")
		elif bet < 1:
			MessageBox.Show("You must bet at least 1 dollar!")
		elif bet > money and bet > moneytwo:
			MessageBox.Show("You don't have enough money!")
		else:
			self._button1.BackgroundImage = levOn
			self._pictureBox4.Visible = True
			self._timer1.Enabled = True
			self._label2.Text = str(round(money2, 2))
			self._progressBar1.Value = 0
			
			num1 = self.num1
			num2 = self.num2
			num3 = self.num3
			
			if num1 == 1 and num2 == 1 and num3 == 1:
				money2 += bet * 2
				
			if num1 == 2 and num2 == 2 and num3 == 2:
				money2 += bet * 2
			
			# Check if num1, num2, and num3 = 3, 4, and 5
			# and multiply bet by whatever you want
			
			if num1 == 5 and num2 == 5 and num3 == 5:
				money2 += bet * 100
			
			self.num1 = 0
			self.num2 = 0
			self.num3 = 0
			self._label2.Text = str(round(money2, 2))
			
			if money2 == 0:
				MessageBox.Show("You ran out of cash!")
		pass

	def MainFormLoad(self, sender, e):
		pass