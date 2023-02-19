private void initialize() {
		this.setCursor(new java.awt.Cursor(java.awt.Cursor.WAIT_CURSOR));
		this.setResizable(false);
		this.setContentPane(getAboutPanel());
		this.pack();
		centerFrame();
	}