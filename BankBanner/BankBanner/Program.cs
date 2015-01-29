using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace BankBanner
{
    class Character
    {
        private int numberThisRepresents;
        public int number
        {
            get
            {
                return numberThisRepresents;
            }
            set
            {
                numberThisRepresents = value;
            }
        }
        public string top;
        public string middle;
        public string bottom;
        public Character(int representation, string t, string m, string b)
        {
            number = representation;
            top = t;
            middle = m;
            bottom = b;
        }
        public override bool Equals(object obj)
        {
            Character other = obj as Character;
            if (null == other) { return false; }
            if (other.top == this.top && other.middle == this.middle && other.bottom == this.bottom) { return true; }
            return false;
        }
    }
    class Program
    {
        Character[] characters = 
        {
            new Character(0," _ ", "| |", "|_|"),//0
            new Character(1, "   ", "  |", "  |"),//1
            new Character(2, " _ ", " _|", "|_ "),//2
            new Character(3, " _ ", " _|", " _|"),//3
            new Character(4, "   ", "|_|", "  |"),//4
            new Character(5, " _ ", "|_ ", " _|"),//5
            new Character(6, " _ ", "|_ ", "|_|"),//6
            new Character(7, " _ ", "  |", "  |"),//7
            new Character(8, " _ ", "|_|", "|_|"),//8
            new Character(9, " _ ", "|_|", " _|"),//9
        };
        static void Main(string[] args)
        {
            Program newProgram = new Program();
            List<string> strs = new List<string>();
            strs.Add(newProgram.printCharacters("000000000"));
            strs.Add(newProgram.printCharacters("111111111"));
            strs.Add(newProgram.printCharacters("490067715"));
            strs.Add(newProgram.printCharacters("123456789"));

            foreach (string str in strs)
            {
                Console.Out.Write(str);
                Console.Out.WriteLine(newProgram.parseBack(str));
            }
            Console.Out.WriteLine("------------------------------");

            Console.Out.WriteLine( newProgram.parseBack(" _  _  _  _  _  _  _  _  _ \n"+
                                 "| || || || || || || || || |\n"+
                                 "|_||_||_||_||_||_||_||_||_|\n"
                                 ) );
            Console.Out.WriteLine( newProgram.parseBack("\n" +
                                 "  |  |  |  |  |  |  |  |  |\n"+
                                 "  |  |  |  |  |  |  |  |  |\n"
                                 ) );
            Console.Out.WriteLine( newProgram.parseBack("    _  _  _  _  _  _     _ \n" +
                                 "|_||_|| || ||_   |  |  ||_ \n" +
                                 "  | _||_||_||_|  |  |  | _|"
                                 ) );
        }

        public string printCharacters(string sequence)
        {
            StringBuilder sb = new StringBuilder();
            foreach( char c in sequence )
            {
                int i = (int)Char.GetNumericValue(c);
                sb.Append(characters[i].top);
            }
            sb.Append("\n");
            foreach (char c in sequence)
            {
                int i = (int)Char.GetNumericValue(c);
                sb.Append(characters[i].middle);
            }
            sb.Append("\n");
            foreach (char c in sequence)
            {
                int i = (int)Char.GetNumericValue(c);
                sb.Append(characters[i].bottom);
            }
            sb.Append("\n");
            return sb.ToString();
        }

        public string parseBack(string entireString)
        {
            StringBuilder returnSB = new StringBuilder();
            string[] splits = entireString.Split(new char[]{'\r','\n'}, StringSplitOptions.RemoveEmptyEntries);
            string top, middle, bottom;
            if (splits.Length == 2)
            {
                //No Top Level
                middle = splits[0];
                bottom = splits[1];
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < Math.Max(middle.Length, bottom.Length); i++){ sb.Append(" "); }
                top = sb.ToString();
            }
            else if (splits.Length == 3)
            {
                top = splits[0];
                middle = splits[1];
                bottom = splits[2];
            }
            else { return null; }    //Improperly formatted

            while (top != "" && middle != "" && bottom != "")
            {
                string topC = new String(top.Take(3).ToArray());
                top = top.Substring(3);
                string midC = new String(middle.Take(3).ToArray());
                middle = middle.Substring(3);
                string botC = new String(bottom.Take(3).ToArray());
                bottom = bottom.Substring(3);

                Character oneChar = new Character(0, topC, midC, botC);
                returnSB.Append(matchOneChar(oneChar));
            }
            return returnSB.ToString();
        }
        public int matchOneChar(Character oneChar)
        {
            foreach (Character c in characters)
            {
                if (c.Equals(oneChar))
                {
                    return c.number;
                }
            }
            return -1;
        }
    }
}
