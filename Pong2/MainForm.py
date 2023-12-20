import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.R = System.Random()
		self.ballup = 0
		self.balld = 0
		self.flagleft = False
		self.flagright = False	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._lbltitle = System.Windows.Forms.Label()
		self._leftscore = System.Windows.Forms.Label()
		self._lblleft = System.Windows.Forms.Label()
		self._lblball = System.Windows.Forms.Label()
		self._rightscore = System.Windows.Forms.Label()
		self._lblright = System.Windows.Forms.Label()
		self._timerright = System.Windows.Forms.Timer(self._components)
		self._timerleft = System.Windows.Forms.Timer(self._components)
		self._timerball = System.Windows.Forms.Timer(self._components)
		self._timermulti = System.Windows.Forms.Timer(self._components)
		self._timerdummy = System.Windows.Forms.Timer(self._components)
		self._timerboolean = System.Windows.Forms.Timer(self._components)
		self.SuspendLayout()
		# 
		# lbltitle
		# 
		self._lbltitle.Font = System.Drawing.Font("Sans Serif Collection", 23.9999981, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lbltitle.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._lbltitle.Location = System.Drawing.Point(12, 25)
		self._lbltitle.Name = "lbltitle"
		self._lbltitle.Size = System.Drawing.Size(964, 345)
		self._lbltitle.TabIndex = 0
		self._lbltitle.Text = "Press Enter to Start or M to start Multiplayer"
		self._lbltitle.TextAlign = System.Drawing.ContentAlignment.TopCenter
		self._lbltitle.Click += self.LbltitleClick
		# 
		# leftscore
		# 
		self._leftscore.BackColor = System.Drawing.Color.Transparent
		self._leftscore.Font = System.Drawing.Font("Sans Serif Collection", 23.9999981, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._leftscore.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._leftscore.Location = System.Drawing.Point(121, 96)
		self._leftscore.Name = "leftscore"
		self._leftscore.Size = System.Drawing.Size(95, 64)
		self._leftscore.TabIndex = 2
		self._leftscore.Text = "0"
		self._leftscore.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# lblleft
		# 
		self._lblleft.BackColor = System.Drawing.SystemColors.Control
		self._lblleft.Font = System.Drawing.Font("Sans Serif Collection", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lblleft.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._lblleft.Location = System.Drawing.Point(12, 246)
		self._lblleft.Name = "lblleft"
		self._lblleft.Size = System.Drawing.Size(20, 100)
		self._lblleft.TabIndex = 3
		self._lblleft.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# lblball
		# 
		self._lblball.BackColor = System.Drawing.Color.White
		self._lblball.Font = System.Drawing.Font("Sans Serif Collection", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lblball.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._lblball.Location = System.Drawing.Point(479, 404)
		self._lblball.Name = "lblball"
		self._lblball.Size = System.Drawing.Size(20, 20)
		self._lblball.TabIndex = 5
		self._lblball.TextAlign = System.Drawing.ContentAlignment.TopCenter
		self._lblball.Click += self.LblballClick
		# 
		# rightscore
		# 
		self._rightscore.BackColor = System.Drawing.Color.Transparent
		self._rightscore.Font = System.Drawing.Font("Sans Serif Collection", 23.9999981, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._rightscore.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._rightscore.Location = System.Drawing.Point(765, 96)
		self._rightscore.Name = "rightscore"
		self._rightscore.Size = System.Drawing.Size(112, 64)
		self._rightscore.TabIndex = 6
		self._rightscore.Text = "0"
		self._rightscore.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# lblright
		# 
		self._lblright.BackColor = System.Drawing.Color.White
		self._lblright.Font = System.Drawing.Font("Sans Serif Collection", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lblright.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._lblright.Location = System.Drawing.Point(950, 246)
		self._lblright.Name = "lblright"
		self._lblright.Size = System.Drawing.Size(20, 100)
		self._lblright.TabIndex = 7
		self._lblright.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# timerright
		# 
		self._timerright.Interval = 20
		self._timerright.Tick += self.TimerrightTick
		# 
		# timerleft
		# 
		self._timerleft.Interval = 20
		self._timerleft.Tick += self.TimerleftTick
		# 
		# timerball
		# 
		self._timerball.Interval = 20
		self._timerball.Tick += self.TimerballTick
		# 
		# timermulti
		# 
		self._timermulti.Interval = 20
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(988, 607)
		self.Controls.Add(self._lblright)
		self.Controls.Add(self._rightscore)
		self.Controls.Add(self._lblball)
		self.Controls.Add(self._lblleft)
		self.Controls.Add(self._leftscore)
		self.Controls.Add(self._lbltitle)
		self.Name = "MainForm"
		self.Text = "Pong2"
		self.Load += self.MainFormLoad
		self.SizeChanged += self.MainFormSizeChanged
		self.KeyDown += self.MainFormKeyDown
		self.ResumeLayout(False)

	def TimerballTick(self, sender, e):
		ball = self._lblball
		lpdl = self._lblleft
		rpdl = self._lblright
		rscore = int(self._rightscore.Text)
		lscore = int(self._leftscore.Text)
		ball.Top += self.ballup
		ball.Left += 8 * self.balld
		
		if ball.Right >= rpdl.Left and ball.Bottom >= rpdl.Top and ball.Top <= rpdl.Bottom:
			self.balld = -1
			self.ballup = self.R.Next(-4, 5)
			if ball.BackColor == Color.Orange:
				rpdl.BackColor = Color.Orange
		elif ball.Left <= lpdl.Right and ball.Bottom >= lpdl.Top and ball.Top <= lpdl.Bottom:
			self.balld = 1
			self.ballup = self.R.Next(-4, 5)
			if ball.BackColor == Color.Orange:
				lpdl.BackColor = Color.Orange
				
		if ball.Top <= 0:
			self.balld = -1
			ball.Top += 5 * self.balld
		
		if ball.Bottom >= self.Height:
			self.balld = 1
			ball.Top += 5 * self.balld
		
		if ball.Location.X <= 0 or \
		   (ball.Location.X < lpdl.Left + 20 and ball.Location.Y < lpdl.Top):
		   	rscore += 1
		   	ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self._rightscore.Text = str(rscore)
			if ball.BackColor == Color.Orange:
				ball.BackColor = Color.White
				lpdl.BackColor = Color.White
				rpdl.BackColor = Color.White
				self.balld = 1
				self.ballup = 1

	
		if ball.Location.X >= self.Width or \
		   (ball.Location.X > rpdl.Right + 20 and ball.Location.Y > rpdl.Top):
		   	lscore += 1
		   	ball.Left = self.Width // 2
		   	ball.Top = self.Height // 2
		   	self._leftscore.Text = str(lscore)
		   	if ball.BackColor == Color.Orange:
				ball.BackColor = Color.White
				lpdl.BackColor = Color.White
				rpdl.BackColor = Color.White
				self.balld = 1
				self.ballup = 1
		
		if lscore == 10:
			self._timerball.Enabled = False
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self.ballup = 0
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Left Player Wins! Press R to restart"
		
		if rscore == 10:
			self._timerball.Enabled = False
  			ball.Left = self.Width // 2
  			ball.Top = self.Height // 2
          	self._ballup = 0
       		self._lbltitle.Text = "Right victory! R to restart"
       		self._lbltitle.Visible = True
		
		
		if ball.Top <= 0:
			self.ballup *= -1
		elif ball.Bottom >= self.Height - 50:
			self.ballup *= -1
		
		if ball.Top <= self.Top + 10:
			self.ballup = 1
		elif ball.Top >= self.Height - 50:
			self.ballup = -1
		
		if self._timerboolean.Enabled == True:
			#lpdl.Top += ball.Top - lpdl.Top
			#lpdl.Top = lpdl.Top + ball.Top - lpdl.Top ** 1.1
			if ball.Top > lpdl.Top:
				lpdl.Top = lpdl.Top + 3
			else:
				lpdl.Top = lpdl.Top - 3
			
			


	def MainFormKeyDown(self, sender, e):
		tball = self._timerball
		tdum = self._timerdummy
		tbool = self._timerboolean
		tmult = self._timermulti
		tleft = self._timerleft
		tright = self._timerright
		bl = self._lblball
		lblf = self._lblleft
		lblrt = self._lblright
		
		def reset():
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Press Enter to Start or M to start Multiplayer"
			self._leftscore.Text = "0"
			self._rightscore.Text = "0"
			tball.Enabled = False
			tdum.Enabled = False
			tbool.Enabled = False
			tmult.Enabled = False
			tleft.Enabled = False
			tright.Enabled = False
			bl.Left = self.Width // 2
			bl.Top = self.Height // 2
			self._lblleft.Top = (self.Height // 2) - 100 + self._lblleft.Height
			self._lblright.Top = (self.Height // 2) - 100 + self._lblright.Height
			self.BackColor = Color.Black
			bl.BackColor = Color.White
			self._lblleft = Color.White
			self._lblright = Color.White
		
		if e.KeyCode == Keys.R:
			reset()
		
		if e.KeyCode == Keys.Enter:
			tball.Enabled = True
			tdum.Enabled = True
			tbool.Enabled = True
			self._lbltitle.Visible = False
		
		if e.KeyCode == Keys.M:
			reset()
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Use W and S to move the left paddle; " \
								  "hit Enter to begin"
			tmult.Enabled = True
			if e.KeyCode == Keys.Enter:
				self._lbltitle.Visible = False
				tbool.Enabled = False
				tmult.Enabled = True
				tdum.Enabled = True
				tball.Enabled = True
		
		if tdum.Enabled:
			if e.KeyCode == Keys.Up:
				self.flagright = False
				tright.Enabled = True
			elif e.KeyCode == Keys.Down:
				self.flagright = True
				tright.Enabled = True
			elif tright.Enabled and self.flagright == False:
				tright.Enabled = False
			elif e.KeyCode == Keys.F:
				self._lblball.BackColor = Color.Orange
				self.balld = self.balld * 2
				self.ballup = self.ballup * 2
			
		

		if tmult.Enabled and tball.Enabled:
			if e.KeyCode == Keys.W:
				self.flagleft = False
        		tleft.Enabled = True
        		tbool.Enabled = False
			if e.KeyCode == Keys.S:
				self.flagleft = False
        		tleft.Enabled = True
        		tbool.Enabled = False
        	if tleft.Enabled and self.flagleft == False:
        		tleft.Enabled = False


	def LbltitleClick(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		self.balld = 1
		self.ballup = self.R.Next(-4, 5)
		self._timerball.Enabled = False
		self._timerdummy.Enabled = False
		self._timermulti.Enabled = False
		
	def pdlTick(self, pdl, flagd, tmr):
		if flagd == True and self._lblright.BackColor == Color.White:
			pdl.Top += 5
		if flagd == False and self._lblright.BackColor == Color.White:
			pdl.Top -= 5
		if pdl.Top <= 10:
			tmr.Enabled = False
		if pdl.Bottom >= self.Height - 50:
			tmr.Enabled = False

	def TimerrightTick(self, sender, e):
			self.pdlTick(self._lblright, self.flagright, self._timerright)


	def TimerleftTick(self, sender, e):
			self.pdlTick(self._lblleft, self.flagleft, self._timerleft)

	def MainFormSizeChanged(self, sender, e):
		self._lblright.Left = self.Width - 25 - self._lblright.Width
		self._lblball.Left = self.Width // 2
		self._lblball.Top = self.Height // 2
		self._lbltitle.Width = self.Width - 25
		self._rightscore.Left = self.Width - 75 - self._rightscore.Width

	def LblballClick(self, sender, e):
		self._lblball.BackColor = Color.Red
		""" TODO: PUT MORE EASTER EGGS LATER """
		self.BackColor = Color.Green