require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

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

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox4 = System::Windows::Forms::TextBox.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 27.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label1.Location = System::Drawing::Point.new(200, 139)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(314, 55)
		@label1.TabIndex = 0
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 27.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label2.Location = System::Drawing::Point.new(200, 244)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(314, 55)
		@label2.TabIndex = 1
		@label2.Click { |sender, e| self.Label2Click(sender, e) }
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 36, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label3.Location = System::Drawing::Point.new(16, 129)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(136, 56)
		@label3.TabIndex = 2
		@label3.Text = "Sum:"
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 36, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label4.Location = System::Drawing::Point.new(16, 235)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(136, 56)
		@label4.TabIndex = 3
		@label4.Text = "Avg:"
		# 
		# textBox1
		# 
		@textBox1.BackColor = System::Drawing::SystemColors.InactiveCaption
		@textBox1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(143, 15)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(100, 31)
		@textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		@textBox2.BackColor = System::Drawing::SystemColors.InactiveCaption
		@textBox2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox2.Location = System::Drawing::Point.new(277, 15)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(100, 31)
		@textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		@textBox3.BackColor = System::Drawing::SystemColors.InactiveCaption
		@textBox3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox3.Location = System::Drawing::Point.new(16, 15)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(100, 31)
		@textBox3.TabIndex = 6
		# 
		# textBox4
		# 
		@textBox4.BackColor = System::Drawing::SystemColors.InactiveCaption
		@textBox4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox4.Location = System::Drawing::Point.new(414, 15)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(100, 31)
		@textBox4.TabIndex = 7
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ControlDarkDark
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@button1.Location = System::Drawing::Point.new(16, 74)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(131, 38)
		@button1.TabIndex = 8
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ControlDarkDark
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@button2.Location = System::Drawing::Point.new(191, 74)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(131, 38)
		@button2.TabIndex = 10
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::SystemColors.ControlDarkDark
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@button3.Location = System::Drawing::Point.new(383, 74)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(131, 38)
		@button3.TabIndex = 11
		@button3.Text = "Close"
		@button3.UseVisualStyleBackColor = false
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		self.ClientSize = System::Drawing::Size.new(532, 319)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Prog52b"
		self.Load { |sender, e| self.MainFormLoad(sender, e) }
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Label1Click(sender, e)
		
	end

	def MainFormLoad(sender, e)
		
	end

	def Button1Click(sender, e)
		S = int(@textBox1.Text) + int(@textBox2.Text) + int(@textBox3.Text) + int(@textBox4.Text)
		Avg = S / 4.0
		@label1.Text = "" + str(S)
		@label2.Text = "" + str(Avg)
	end
end

