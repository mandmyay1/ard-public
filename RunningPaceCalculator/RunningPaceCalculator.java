import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;


public class RunningPaceCalculator implements ActionListener {
	JPanel _panel;
	JFrame _frame;
	ButtonGroup group;
	JTextField minuteField;
	JTextField hourField;
	JTextField secondsField;
	JTextField distanceField;
	JLabel resultsLabel;
	JRadioButton milesButton;
	JRadioButton kmButton;
	
	public RunningPaceCalculator(){
		_panel = new JPanel();
		_panel.setLayout(new GridBagLayout());
		//_panel.setBorder(BorderFactory.createEmptyBorder(5,5,5,5));
		
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
		_panel.add(distanceField, c);
		
		/*JLabel mileLabel = new JLabel("miles");
		c = new GridBagConstraints();
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 2;
		c.gridy = 0;
		_panel.add(mileLabel, c);
		*/
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
		hourField = new JTextField("",2);
		_panel.add(hourField, c);
		
		c = new GridBagConstraints();
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 2;
		c.gridy = 1;
		_panel.add(new JLabel("h"), c);
		
		c = new GridBagConstraints();
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 3;
		c.gridy = 1;
		minuteField = new JTextField("",2);
		_panel.add(minuteField, c);
		
		c = new GridBagConstraints();
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 4;
		c.gridy = 1;
		_panel.add(new JLabel("m"), c);
		
		c = new GridBagConstraints();
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 5;
		c.gridy = 1;
		secondsField = new JTextField("",2);
		_panel.add(secondsField, c);
		
		c = new GridBagConstraints();
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 6;
		c.gridy = 1;
		_panel.add(new JLabel("s"), c);
		
		JButton goButton = new JButton("Calculate");
		c = new GridBagConstraints();
		//c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 0;
		c.gridy = 2;
		_panel.add(goButton, c);
		goButton.addActionListener(this);
		
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

	@Override
	public void actionPerformed(ActionEvent arg0) {
		// TODO Auto-generated method stub
		String hStr = hourField.getText();
		String mStr = minuteField.getText();
		String sStr = secondsField.getText();
		double hours = ( hStr.isEmpty() ) ? 0 : Double.parseDouble( hStr );
		double minutes = ( mStr.isEmpty() ) ? 0 : Double.parseDouble( mStr );
		double seconds =  ( sStr.isEmpty() ) ? 0 : Double.parseDouble( sStr );
		
		String dStr = distanceField.getText();
		if( dStr.isEmpty() ){ return; }
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
