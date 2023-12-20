require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"
def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox
class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@button3 = System::Windows::Forms::Button.new()
		@label3 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ActiveCaption
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(31, 427)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(189, 76)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ActiveCaption
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(305, 427)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(189, 76)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.GradientInactiveCaption
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(31, 142)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(221, 76)
		@label1.TabIndex = 3
		@label1.Text = "Circumference:"
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::SystemColors.GradientInactiveCaption
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(31, 47)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(221, 76)
		@label2.TabIndex = 4
		@label2.Text = "Radius:"
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		@textBox1.BackColor = System::Drawing::SystemColors.ControlDarkDark
		@textBox1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@textBox1.Location = System::Drawing::Point.new(400, 66)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(214, 31)
		@textBox1.TabIndex = 5
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::SystemColors.ActiveCaption
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(575, 427)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(189, 76)
		@button3.TabIndex = 6
		@button3.Text = "Close"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::SystemColors.GradientInactiveCaption
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(31, 236)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(221, 76)
		@label3.TabIndex = 7
		@label3.Text = "Area:"
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::SystemColors.ControlDarkDark
		@label5.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label5.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label5.Location = System::Drawing::Point.new(400, 253)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(214, 40)
		@label5.TabIndex = 9
		@label5.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::SystemColors.ControlDarkDark
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label4.Location = System::Drawing::Point.new(400, 162)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(214, 40)
		@label4.TabIndex = 8
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.AppWorkspace
		self.ClientSize = System::Drawing::Size.new(822, 515)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@button3)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button3Click(sender, e)
		Application.Exit()
	end

	def Button1Click(sender, e)
		radius = float(@textBox1.Text)
		pi = 3.14159
		area = pi * radius**2
		circumference = (radius + radius) * pi
		@label4.Text = "Circumference: " + str(circumference)
		@label5.Text = "Area: " + str(area)
	end

	def Button2Click(sender, e)
		@label4.Text = ""
		@label5.Text = ""
		@textBox1.Text = ""
	end
end

