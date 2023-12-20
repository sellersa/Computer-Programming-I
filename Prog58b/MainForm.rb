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
		@button3 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.AppWorkspace
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 36, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(27, 330)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(237, 121)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.AppWorkspace
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 36, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(337, 330)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(237, 121)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::SystemColors.AppWorkspace
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 36, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(627, 330)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(237, 121)
		@button3.TabIndex = 2
		@button3.Text = "Close"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaption
		self.ClientSize = System::Drawing::Size.new(892, 504)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Prog58b"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
	end

	def Button2Click(sender, e)
		
	end

	def Button3Click(sender, e)
		Application.Exit()
	end
end

