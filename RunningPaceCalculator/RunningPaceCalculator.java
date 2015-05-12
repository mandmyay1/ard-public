import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.ButtonGroup;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;


public class RunningPaceCalculator {
	JPanel _panel;
	JFrame _frame;
	ButtonGroup group;
	JTextField timeField;
	JTextField distanceField;
	JLabel resultsLabel;
	JRadioButton milesButton;
	JRadioButton kmButton;
	
	class MyKeyListener implements KeyListener{
		@Override
		public void keyTyped(KeyEvent arg0) {
		}
		
		@Override
		public void keyReleased(KeyEvent event) {
			if( event.getKeyChar() == KeyEvent.VK_ENTER ){
				if( distanceField.isFocusOwner() ){
					timeField.requestFocus();
				}
				else if( timeField.isFocusOwner() ){
					distanceField.requestFocus();
				}
			}
			try{
				calculate();
			} catch(NumberFormatException e){
				resultsLabel.setText("ERR");
			}
		}
		
		@Override
		public void keyPressed(KeyEvent arg0) {
		}
	}
	
	public RunningPaceCalculator(){
		_panel = new JPanel();
		_panel.setLayout(new GridBagLayout());
		
		GridBagConstraints c = new GridBagConstraints();
		JLabel distLabel = new JLabel("Enter Distance: ");
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 0;
		c.gridy = 0;
		_panel.add(distLabel, c);
		
		distanceField = new JTextField("",5);
		c = new GridBagConstraints();
		c.gridx = 1;
		c.gridy = 0;
		c.gridwidth = 3;
		c.fill = GridBagConstraints.HORIZONTAL;
		c.anchor = GridBagConstraints.FIRST_LINE_START;
		distanceField.addKeyListener(new MyKeyListener());
		_panel.add(distanceField, c);

		milesButton = new JRadioButton("miles");
		kmButton = new JRadioButton("km");
		group = new ButtonGroup();
		group.add(milesButton);
		group.add(kmButton);
		
		c = new GridBagConstraints();
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 5;
		c.gridy = 0;
		c.gridwidth = 2;
		milesButton.setSelected(true);
		_panel.add(milesButton, c);
		
		c = new GridBagConstraints();
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 7;
		c.gridy = 0;
		_panel.add(kmButton, c);
		
		c = new GridBagConstraints();
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 0;
		c.gridy = 1;
		_panel.add(new JLabel("Enter Time: "), c);
		
		c = new GridBagConstraints();
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 1;
		c.gridy = 1;
		timeField = new JTextField("",5);
		timeField.addKeyListener(new MyKeyListener());
		_panel.add(timeField, c);
		
		resultsLabel = new JLabel();
		c = new GridBagConstraints();
		//c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 1;
		c.gridy = 2;
		c.gridwidth = 6;
		_panel.add(resultsLabel, c);
		
		_frame = new JFrame("Running Pace Calculator");
		_frame.setPreferredSize(new Dimension(500,500));
		//_frame.setSize(new Dimension(500,500));
		_frame.pack();
		_frame.setVisible(true);
		_frame.setContentPane(_panel);

		
	}
	
	public static void main(String[] args){
		new RunningPaceCalculator();
	}
	
	double round(double value, int places){
		if (places < 0) throw new IllegalArgumentException();
		
		long factor = (long) Math.pow(10, places);
		value = value * factor;
		long tmp = Math.round(value);
		return (double) tmp / factor;
	}
	
	public void calculate(){
		String hStr = timeField.getText();
		String[] timeSplit = hStr.split("\\.| |:");
		/*System.out.print(hStr);
		System.out.print(" ");
		System.out.print(timeSplit.length);
		System.out.print(" ");
		for( String time : timeSplit ){
			System.out.print(time);
			System.out.print(" ");
		}
		System.out.println();*/
		double seconds = 0;
		double minutes = 0;
		double hours = 0;
		int numTimes = timeSplit.length;
		if( 1 == numTimes ){
			seconds = Double.parseDouble(timeSplit[0]);
		}
		else if( 2 == numTimes ){
			minutes = Double.parseDouble(timeSplit[0]);
			seconds = Double.parseDouble(timeSplit[1]);
		}
		else if( 3 == numTimes ){
			hours =  Double.parseDouble(timeSplit[0]);
			minutes = Double.parseDouble(timeSplit[1]);
			seconds = Double.parseDouble(timeSplit[2]);
		}
		
		
		String dStr = distanceField.getText();
		//if( dStr.isEmpty() ){ return; }
		double distance = Double.parseDouble( dStr );
		
		double timeInMinutes = 60 * hours + minutes + seconds / 60;
		
		double pace = timeInMinutes / distance;
		int minutePace = (int)pace;
		double secondPace = (pace - minutePace) * 60;
		
		String strPace = Integer.toString(minutePace) + ":";
		if( secondPace < 10 ){ strPace += "0"; }
		strPace += Double.toString( round( secondPace, 2 ) );
		
		if(milesButton.isSelected()){ strPace += " minutes/mile"; }
		else if(kmButton.isSelected()){ strPace += " minutes/km"; }
		resultsLabel.setText(strPace);
		
	}
}
