require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.HotTrack
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::SystemColors.ButtonFace
		@button1.Location = System::Drawing::Point.new(212, 282)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(138, 80)
		@button1.TabIndex = 0
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.HotTrack
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 26.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::SystemColors.ButtonFace
		@button2.Location = System::Drawing::Point.new(516, 282)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(138, 80)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.HotTrack
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::SystemColors.ButtonFace
		@label1.Location = System::Drawing::Point.new(212, 39)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(442, 202)
		@label1.TabIndex = 2
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.AppWorkspace
		self.ClientSize = System::Drawing::Size.new(815, 485)
		self.Controls.Add(@label1)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "PhoneNumbers"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "1.(608) 754-2226\n2.(888) 280-4331 \n3.(608) 743-5200  \n4.(608) 752-0100  \n5.(608) 754-7090"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

