require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ActiveCaption
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 24, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(209, 270)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(164, 89)
		@button1.TabIndex = 0
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.ActiveCaption
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(209, 40)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(447, 201)
		@label1.TabIndex = 1
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ActiveCaption
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 24, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(492, 270)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(164, 89)
		@button2.TabIndex = 2
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.AppWorkspace
		self.ClientSize = System::Drawing::Size.new(841, 505)
		self.Controls.Add(@button2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Schedule"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "1. Geometry\n2. Spanish\n3. Computer Programming\n4. Global Studies\n5. Biology\n6. English\n7. Band\n8. Freshmen Seminar"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

